#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

import lib.calendario as cal

from lib.estoques import *
from lib.eventos import *
from lib.medicacao import *


def datahora_split( x ):
    sx = str(x)
    return sx[0:10] + ', ' + cal.dia_da_semana( x ), sx[10:16]

def exporta_expectativa_consumo():
    sga = cal.qual_semana_gestacao( cal.hoje() )
    sgf = min( sga + 6, cal.SEMANAS_GESTACAO_TOTAL - sga + 1)
    data = {}
    for i in range( sga, sgf ):
        sg = cal.semana_gestacao(i)
        sgkey = str(sg.inicio)[:10] + u' até ' + str(sg.fim)[:10]
        data[  sgkey ] = {}
        for medicamento in Medicamentos:
            quantidade_acumulada = 0
            posologia = obter_posologia( medicamento )
            for agendamento in posologia.agendamentos():
                if sg.inicio <= agendamento.datahora <= sg.fim:
                    quantidade_acumulada += agendamento.quantidade
            data[ sgkey ][ medicamento.nome() ] = quantidade_acumulada
    
    table = []
    header = [ 'Medicamento' ] + [ x for x in sorted(data.keys()) ]
    table.append( '\t'.join(header) )
    ref = data[ header[1] ]
    for med in sorted(ref.keys()):
        line = [ med ] + [ str(data[x][med]) for x in sorted(data.keys()) ]
        table.append( '\t'.join(line) )
    
    with codecs.open( 'consumo.txt', 'w', 'utf-8') as fout:
        fout.write( '\n'.join(table) )


def exporta_dados_planilha():
    
    hoje = cal.hoje()
    ultdia = hoje + 30 * cal.UM_DIA
    sultdia = str(ultdia)[:10]
    
    grafico_data = {}
    for medicamento in Medicamentos:
        
        if medicamento == Smorfolipide:
            continue
        
        estoque = obter_estoque( medicamento )
        posologia = obter_posologia( medicamento )
        
        estah_tratando = False
        for dia in cal.dias_entre( hoje, ultdia ):
            if posologia.estah_tratando( dia ):
                estah_tratando = True
                break
        
        if not estah_tratando:
            continue
        
        grafico_data[ medicamento.nome() ] = {}
        i = 1
        for dia in cal.dias_entre( hoje, ultdia ):
            fdia = cal.agendamento( dia, 0, 0 )
            sdia = str(fdia)[:10]
            if posologia.estah_tratando( dia ):
                saldo = estoque.saldo(fdia)
                grafico_data[ medicamento.nome() ][ sdia ] = saldo
            else:
                grafico_data[ medicamento.nome() ][ sdia ] = ''
            i+=1
        
        if  ( grafico_data[medicamento.nome()][sultdia] > 50) :
            del grafico_data[ medicamento.nome() ]
    
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
    
