#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

import lib.calendario as cal

from lib.estoques import *
from lib.eventos import *
from lib.medicacao import *
from lib.medicamentos import *

def exporta_calendario():
    
    trimestre_label = [ '',
        'primeiro trimestre',
        'segundo trimestre',
        'terceiro trimestre',
    ]
    
    with codecs.open('agenda_calendario.html', 'w', 'utf-8') as fout:
    
        fout.write( 'data do beta: %s<br>' % str(cal.BETA_HCG)[:10] )
        fout.write( 'data do DUM: %s<br>' % str(cal.DUM)[:10] )
        
        data_parto = cal.semana_gestacao( 40 ).fim
        
        fout.write( 'data do parto: %s<br>' % str( data_parto )[:10] )
        fout.write( u'Retorno licença Mamãe: %s<br>' % str( data_parto + 180 * cal.UM_DIA )[:10] )
        fout.write( u'Retorno licença Papai: %s<br>' % str( data_parto +  20 * cal.UM_DIA )[:10] )
    
        for i in range(1, 41):
            sg = cal.semana_gestacao(i)
            itg = cal.qual_trimestre_gestacao( sg.fim )
            tgl = trimestre_label[itg]
            fout.write(  u'<p>semana %02s [%s]: de %s até %s</p>'%( i, tgl, str(sg.inicio)[:10], str(sg.fim)[:10] ) )
    
        hoje = cal.hoje()
    
        select_list = set( [ Smorfolipide, Utrogestan ] )
    
        for medicacao in Posologias.values():
            medicamento = medicacao.medicamento()
            if medicamento not in select_list:
                continue
            fout.write( u'<ul>')
            fout.write( u'<li>%s</li>' % medicamento.nome() )
            fout.write( u'<ul>')
            agendamentos = medicacao.agendamentos()
            lagendamentos = len( agendamentos )
            for i in range( lagendamentos ):
                agendamento = agendamentos[i]
                if agendamento.datahora < hoje:
                    continue
                fout.write( u'<li>Em: %s, %s unidade</li>' % ( str(agendamento.datahora)[:16], agendamento.quantidade ))
            fout.write( u'</ul>')
            fout.write( u'</ul>')


def datahora_split( x ):
    # semana gestacao
    sg = cal.qual_semana_gestacao(x)
    # delta dias
    dd = ( x - cal.semana_gestacao( sg ).inicio) .days + 1
    if dd == 7: wg = u'[aniversário %(semana)d semana(s) ]'%{'semana':sg }
    else: wg = '[ %(semana)d semana(s) e %(dia)d dia(s) ]'%{ 'dia':dd, 'semana':sg - 1 }
    sx = str(x)
    return sx[0:10] + ', ' + cal.dia_da_semana( x ) + ' ' + wg, sx[10:16]


def exporta_expectativa_consumo():
    sga = cal.qual_semana_gestacao( cal.hoje() )
    sgf = min( sga + 7, cal.SEMANAS_GESTACAO_TOTAL - sga + 1)
    data = {}
    for i in range( sga, sgf ):
        sg = cal.semana_gestacao(i)
        sgkey = str(sg.inicio)[2:10] + u' até ' + str(sg.fim)[2:10]
        data[  sgkey ] = {}
        for medicamento in Medicamentos:
            quantidade_acumulada = 0
            posologia = obter_posologia( medicamento )
            for agendamento in posologia.agendamentos():
                if sg.inicio <= agendamento.datahora <= sg.fim:
                    quantidade_acumulada += agendamento.quantidade
            data[ sgkey ][ medicamento.nome() ] = quantidade_acumulada
    
    
    sg = cal.semana_gestacao( sga )
    table = []
    
    header1 = [ '', '']
    for x in range( sga, sgf ):
        header1.append(str(x) )
        header1.append( '' )
    table.append( '\t'.join(header1) )
    
    header2 = [ 'Medicamento', 'Estoque']
    for x in sorted(data.keys()):
        header2.append( x )
        header2.append( 'Estoque' )
    table.append( '\t'.join(header2) )
    
    
    ref = data[ header2[ 2 ] ]
    for med in sorted(ref.keys()):
        medicamento = obter_medicamento( med )
        estoque = obter_estoque( medicamento )
        saldo = estoque.saldo( sg.inicio )
        
        i = 1
        row = [ med, str(saldo) ]
        for x in sorted(data.keys()):
            consumo_na_semana = data[x][med]
            row.append( str(consumo_na_semana) ) # consuma na semana 'x'
            saldo -= consumo_na_semana
            
            # ajuste do saldo, com adições ou subtrações em estoque!
            sgai = cal.semana_gestacao( sga + i  )
            saldo_em_estoque = estoque.saldo( sgai.inicio )
            if saldo_em_estoque != saldo and saldo_em_estoque > 0:
                saldo = saldo_em_estoque
            
            row.append( str(saldo)  )
            i += 1
        
        table.append( '\t'.join(row) )
    
    
    with codecs.open( 'consumo.txt', 'w', 'utf-8') as fout:
        fout.write( '\n'.join(table) )


def exporta_dados_planilha():
    
    hoje = cal.hoje() - cal.UM_DIA
    ultdia = hoje + 45 * cal.UM_DIA
    sultdia = str(ultdia)[:10]
    
    grafico_data = {}
    for medicamento in Medicamentos:
        
        if medicamento == Smorfolipide:
            continue
        
        estoque = obter_estoque( medicamento )
        posologia = obter_posologia( medicamento )
        
        #if not estah_tratando:
        #    continue
        
        grafico_data[ medicamento.nome() ] = {}
        i = 1
        for dia in cal.dias_entre( hoje, ultdia ):
            fdia = cal.agendamento( dia, 0, 0 )
            sdia = str(fdia)[:10]
            if not posologia.estah_tratando( dia ):
                grafico_data[ medicamento.nome() ][ sdia ] = ''
            else:
                saldo = estoque.saldo(fdia)
                grafico_data[ medicamento.nome() ][ sdia ] = saldo
            i+=1
        
        #if  ( grafico_data[medicamento.nome()][sultdia] > 50) :
        #    del grafico_data[ medicamento.nome() ]
    
    table = []
    header = [ 'data' ] + [ x for x in sorted(grafico_data.keys()) ]
    table.append( '\t'.join(header) )
    ref = grafico_data[ header[1] ]
    for dia in sorted(ref.keys()):
        line = [ dia ] + [ str(grafico_data[x][dia]) for x in sorted(grafico_data.keys()) ]
        table.append( '\t'.join(line) )
    
    with codecs.open( 'estoque.txt', 'w', 'utf-8') as fout:
        fout.write( '\n'.join(table) )
    

def exporta_agendamentos_complexos():
    
    hoje = cal.hoje()
    
    report = {}
    
    for x in Posologia_Smorfolipide.agendamentos():
        
        if x.datahora < hoje: continue
        
        data, horario = datahora_split( x.datahora )
        if data not in report:
            report[data] = {}
        if horario not in report[data]:
            report[data][horario] = []
        
        report[data][horario].append(u'Infusão de Smorf Lipide')


    for x in Eventos:
        
        if x.datahora() < hoje: continue
        
        if isinstance(x, EExame) or isinstance(x, EConsulta):
            
            data, horario = datahora_split( x.datahora() )
             
            if data not in report:
                report[data] = {}
            if horario not in report[data]:
                report[data][horario] = []
        
            report[data][horario].append( x.descricao() )
    
    __writedown( report, 'agendas_complexas.html', u'Agendas Complexas' )



def registra_agendamento( report, evento ):
    
    data, horario = datahora_split( evento.datahora() )
    if data not in report:
        report[data] = {}
    if horario not in report[data]:
        report[data][horario] = []
    
    if isinstance( evento, EMedicacao ):
        medicamento = evento.medicamento()
        estoque = obter_estoque( medicamento )
        mensagem = '%s: %s %s de %s'% ( evento.descricao(), evento.quantidade() , medicamento.unidade(), medicamento.nome() )
        saldo = estoque.saldo( evento.datahora() )
        infoarray = [
            mensagem,
            'restam: %03d em estoque' % saldo
        ]
        if saldo <= 0:
            infoarray[ -1 ] = 'restam: ESTOQUE ZERADO'
        report[data][horario].append( ', '.join(infoarray) )

    else: report[data][horario].append( evento.descricao() )
        
        


def exporta_registros_agendamento(report):
    __writedown( report,'agenda_medicacao.html', u'Agenda gestação')

def __writedown( report, filename, titulo ):
    
    if len(report) == 0:
        return
    
    html = ['''
<html>
<body>
<br><b>%(titulo)s</b>
<br>Emitido em: %(agora)s
    '''%{ 'titulo':titulo, 'agora': str(cal.agora())[:16] }]
    html.append('<ul>')
    for data in sorted( report.keys() ):
        html.append('<hr>')
        html.append( u'<li>%s</li>' % data )
        for horario in sorted( report[data] ):
            html.append('<ul>')
            html.append( u'<li>%s</li>' % horario )
            for informacao in report[data][horario]:
                html.append('<ul>')
                html.append( u'<li>%s</li>' % informacao )
                html.append('</ul>')
            html.append('</ul>')
        html.append('<br>')
    html.append('</ul>')
    
    html.append('''</body></html>''')
    
    with codecs.open( filename, 'w', 'utf-8') as fout:
        fout.write( u'\n'.join(html) )
    

