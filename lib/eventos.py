#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.medicacao import *
from lib.estoques import *

import lib.calendario as cal

Eventos = []

class _Evento:
    def __init__(self, descricao, datahora):
        self.__descricao = descricao
        self.__datahora = datahora
    def descricao(self): return self.__descricao
    def datahora(self): return self.__datahora

class EExame ( _Evento ): pass
class EConsulta ( _Evento ): pass

class EMedicacao ( _Evento ):
    
    def __init__(self, medicamento, agendamento):
        _Evento.__init__(self, u'Tomar remédio', agendamento.datahora)
        self.__medicamento = medicamento
        self.__agendamento = agendamento
        self.suspenso = False
    
    def medicamento(self): return self.__medicamento
    def quantidade(self): return self.__agendamento.quantidade
    

for medicacao in Posologias.values():
    if medicacao.suspenso:
        continue
    medicamento = medicacao.medicamento()
    for agendamento in medicacao.agendamentos():
        Eventos.append( EMedicacao( medicamento, agendamento ) )

Eventos.append( EExame( u'Exame Controle Heparina: Anti Xa', cal.semana_gestacao(12).inicio ) )

data_inicio_heparina = cal.INICIO_GESTACAO
for dia in cal.dias_entre( data_inicio_heparina, data_inicio_heparina + 3 * 28 * cal.UM_DIA , 28 ):
    Eventos.append( EExame( u'Exame Ajuste dosagem Heparina: TTPA e TP/AP ', dia ) )

Eventos.append( EExame( u'Exame Confirmação da Continência istmo cervical', cal.semana_gestacao(16).inicio  ))
Eventos.append( EExame( u'Exame Confirmação da Continência istmo cervical', cal.semana_gestacao(18).inicio  ))
Eventos.append( EExame( u'Exame Confirmação da Continência istmo cervical', cal.semana_gestacao(20).inicio  ))
Eventos.append( EExame( u'Exame Confirmação da Continência istmo cervical', cal.semana_gestacao(22).inicio  ))

Eventos.append( EExame(u'Exame Dopplervelocimetria seriada e perfil biofísico fetal',
                       cal.semana_gestacao( cal.trimestre_gestacao(3).inicio ).inicio  ))


Eventos.append( EConsulta( u'Ginecologista - Dr. Henrique Victor Leite', cal.datahora(2018, 10, 05, 10, 0) ) )
Eventos.append( EConsulta( u'Hematologista - Drª. Fabiane', cal.datahora(2018, 10, 03, 15, 20) ) )


Eventos = sorted( Eventos, key=lambda x : x.datahora() )

