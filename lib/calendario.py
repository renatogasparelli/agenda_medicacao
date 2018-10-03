#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

import collections 

_Semana = collections.namedtuple('_Semana', 'inicio fim')
_Trimestre = collections.namedtuple('_Trimestre', 'inicio fim')

UM_DIA = datetime.timedelta(days=1)

DATA_CONTROLE_ESTOQUE = datetime.datetime(2018, 10, 02, 0, 0, 0)

INICIO_GESTACAO         = datetime.datetime(2018, 10, 01,  0,  0, 0)  - 3 * 7 * UM_DIA
INICIO_GESTACAO_FIM_DIA = datetime.datetime(2018, 10, 01, 23, 59, 59) - 3 * 7 * UM_DIA

SEMANAS_GESTACAO_TOTAL = 41

SEMANAS_GESTACAO = []
for i in range(0, SEMANAS_GESTACAO_TOTAL):
    SEMANAS_GESTACAO.append(
        _Semana( INICIO_GESTACAO         +         7 * i * UM_DIA,
                 INICIO_GESTACAO_FIM_DIA + ( 7 * i + 6 ) * UM_DIA )
    )

NASCIMENTO = SEMANAS_GESTACAO[ SEMANAS_GESTACAO_TOTAL - 1 ].fim

DATA_CONTROLE_ESTOQUE_FIM = NASCIMENTO + 60 * UM_DIA

TRIMESTRES_GESTACAO = [ _Trimestre(1, 13), _Trimestre(14, 27), _Trimestre(28, 41) ]

DIAS_DA_SEMANA = [ 'Segunda', u'Terça', 'Quarta', 'Quinta', 'Sexta', u'Sábado', 'Domingo' ]

def qual_semana_gestacao( dia ):
    for i in range(0, SEMANAS_GESTACAO_TOTAL):
        sg = SEMANAS_GESTACAO[i]
        if sg.inicio <= dia <= sg.fim:
            return i + 1
    return -1

def semana_gestacao( i ):
    if i == 'fim':
        i = SEMANAS_GESTACAO_TOTAL
    return SEMANAS_GESTACAO[ i - 1 ]

def trimestre_gestacao( i ):
    return TRIMESTRES_GESTACAO[ i - 1 ]

def agora():
    return datetime.datetime.now()

def data(ano, mes, dia):
    return datahora(ano, mes, dia, 0, 0, 0)

def agendamento( dia, hora, minuto, segundo=0):
    return datahora(dia.year, dia.month, dia.day, hora, minuto, segundo)

def datahora(ano, mes, dia, hora, minuto, segundo=0):
    return datetime.datetime(ano, mes, dia, hora, minuto, segundo)

def hoje():
    return agendamento( agora(), 0, 0)

def eh_sabado( data ):
    return data.weekday() == 5

def dia_da_semana( data ):
    return DIAS_DA_SEMANA[ data.weekday() ]

def dias_entre(data_inicio, data_fim, jump=1):
    dia = data_inicio
    while True:
        yield dia
        if dia >= data_fim:
            break
        dia += jump*UM_DIA

