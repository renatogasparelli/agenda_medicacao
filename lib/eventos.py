#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.medicacao import *
from lib.estoques import *

import lib.calendario as cal

eventos = []

class __Evento:
    def datahora(self): return None
    def descricao(self): return None

class Medicacao ( __Evento ):
    
    def __init__(self, medicamento, agendamento):
        self.__medicamento = medicamento
        self.__agendamento = agendamento
        
    def datahora(self): return self.__agendamento[0]
    
    def medicamento(self): return self.__medicamento
    
    def quantidade(self): return self.__agendamento[1]
    
    def descricao( self ): return u'Tomar remédio'


for medicacao in Posologias.values():
    medicamento = medicacao.medicamento()
    for agendamento in medicacao.agendamentos():
        eventos.append( Medicacao( medicamento, agendamento ) )



eventos = sorted( eventos, key=lambda x : x.datahora() )

