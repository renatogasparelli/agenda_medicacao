#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from lib.estoques import *

def datahora_split( x ):
    sx = str(x)
    return sx[0:10] + ', ' + cal.dia_da_semana( x ), sx[10:16]

def registra_agenda_medicacao( report, evento ):
    
    medicamento = evento.medicamento()
    estoque = obter_estoque( medicamento )

    data, horario = datahora_split( evento.datahora() )
    if data not in report:
        report[data] = {}
    
    if horario not in report[data]:
        report[data][horario] = []
    
    mensagem = '%s: %s %s de %s'% ( evento.descricao(), evento.quantidade() , medicamento.unidade(), medicamento.nome() )
    
    saldo = estoque.saldo( evento.datahora() )
    
    infoarray = [
        mensagem,
        'restam: %03d em estoque' % saldo
    ]
    
    if saldo <= 0:
        infoarray[ -1 ] = 'restam: ESTOQUE ZERADO'
        
    report[data][horario].append( ', '.join(infoarray) )
        


def export_agenda_medicacao(report):
    
    html = ['''
<html>
<body>
Emitido em: %(agora)s
    '''%{ 'agora': str(cal.agora())[:16] }]
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
    
    with codecs.open( 'agenda_medicacao.html', 'w', 'utf-8') as fout:
        fout.write( u'\n'.join(html) )
