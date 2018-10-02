#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

import lib.calendario as cal

from lib.eventos import *
from lib.estoques import *

agora = cal.hoje()
atequando = agora + 8 * cal.UM_DIA

def datahora_split( x ):
    sx = str(x)
    return sx[0:10] + ', ' + cal.dia_da_semana( evento.datahora() ), sx[10:16], 


report = {}

for evento in eventos:
    
    if evento.datahora() >= atequando:
        break
    

    if isinstance( evento, Medicacao ):
    
        medicamento = evento.medicamento()
        estoque = obter_estoque( medicamento )
    
        if evento.datahora() < agora:
            try:
                estoque.registrar_saida( evento.datahora(), evento.quantidade() )
            except SaldoInsuficiente as e:
                pass
            continue
        
        
        data, horario = datahora_split( evento.datahora() )
        if data not in report:
            report[data] = {}
        
        if horario not in report[data]:
            report[data][horario] = []
        
        mensagem = '%s: %d %s de %s'% ( evento.descricao(), evento.quantidade() \
            , medicamento.unidade(), medicamento.nome() )
        
        try:
            estoque.registrar_saida( evento.datahora(), evento.quantidade() )
            saldo = estoque.saldo()
            
            infoarray = [
                mensagem, 
                'restam: %03d em estoque' % estoque.saldo()
            ]
            
            if saldo <= 0:
                infoarray[ -1 ] = 'restam: ESTOQUE ZERADO'
                
            report[data][horario].append( ', '.join(infoarray) )
                
        except SaldoInsuficienteException as e:
            
            infoarray = [
                'MEDICAMENTO EM FALTA!!!!!!!'
                , '%d %s de %s'% (evento.quantidade() , medicamento.unidade(), medicamento.nome() )
            ]
            
            report[data][horario].append( ', '.join(infoarray) )
        
    
html = ['''
<html>
<body>
''']
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

html.append('''            
</body>
</html>
''')

with codecs.open( 'agenda_medicacao.html', 'w', 'utf-8') as fout:
    fout.write( u'\n'.join(html) )
    
