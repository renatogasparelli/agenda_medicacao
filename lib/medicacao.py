#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import lib.calendario as cal

from lib.medicamentos import *

_AgendaItem = collections.namedtuple('_AgendaItem', 'datahora quantidade')
_Intervalos = collections.namedtuple('_Intervalos', 'datainicio datafim')

Posologias = {}
class __Posologia(object):
    
    def __init__(self, medicamento):
        self.__medicamento = medicamento
        self.__aplicacao = []
        self.__tratamento_inicio = None
        self.__tratamento_fim = None
        Posologias[ self.__medicamento.nome() ] = self
        
    def medicamento(self):
        return self.__medicamento
    
    def agendar(self, datahora, quantidade):
        self.__aplicacao.append( _AgendaItem( datahora, quantidade ) )
        if self.__tratamento_inicio == None or datahora < self.__tratamento_inicio:
            self.__tratamento_inicio = cal.agendamento( datahora, 0, 0 )
        if self.__tratamento_fim == None or datahora > self.__tratamento_fim:
            self.__tratamento_fim = cal.agendamento( datahora, 0, 0 )
    
    def agendamentos(self):
        return self.__aplicacao

    def estah_tratando(self, dia):
        return self.__tratamento_inicio <= dia <= self.__tratamento_fim 

def obter_posologia( medicamento ):
    return Posologias[ medicamento.nome() ]
    

Posologia_Utrogestan   = __Posologia( Utrogestan )  
Posologia_Metilfolato  = __Posologia( Metilfolato )
Posologia_VitaminaC    = __Posologia( VitaminaC )
Posologia_BTrati       = __Posologia( BTrati )
Posologia_Duphostan    = __Posologia( Duphostan )
Posologia_Omega3       = __Posologia( Omega3 )
Posologia_VitaminaE    = __Posologia( VitaminaE )
Posologia_Somalgin     = __Posologia( Somalgin )
Posologia_Enoxoparina  = __Posologia( Enoxoparina )
Posologia_AdderaD3     = __Posologia( AdderaD3 )
Posologia_CalcioK2     = __Posologia( CalcioK2 )
Posologia_Smorfolipide = __Posologia( Smorfolipide )

def data_cmp(d1, d2):
    return ( d1.year == d2.year
        and d1.month == d2.month
        and d1.day == d2.day )

for dia in cal.dias_entre( cal.DATA_CONTROLE_ESTOQUE, cal.DATA_CONTROLE_ESTOQUE_FIM ):
    
    Posologia_Enoxoparina.agendar( cal.agendamento( dia, 7, 00 ), 1 )
    Posologia_Omega3.agendar( cal.agendamento( dia, 12, 00 ), 1  )
    
    if dia <= cal.semana_gestacao(12).fim:
        Posologia_Metilfolato.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        Posologia_VitaminaC.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        Posologia_VitaminaE.agendar( cal.agendamento( dia, 13, 00 ), 1  )
        Posologia_BTrati.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        if cal.eh_sabado(dia):
            Posologia_AdderaD3.agendar( cal.agendamento( dia,  12, 00 ), 1 )
    
    if dia > cal.semana_gestacao(12).fim:
        Posologia_CalcioK2.agendar( cal.agendamento( dia, 12, 00 ), 1 )
        Posologia_CalcioK2.agendar( cal.agendamento( dia, 18, 00 ), 1 )
        
    if dia <= cal.semana_gestacao(36).fim:
        Posologia_Somalgin.agendar( cal.agendamento( dia, 12, 00 ), 1  )     
    
    if dia <= cal.semana_gestacao(8).fim:
        Posologia_Duphostan.agendar( cal.agendamento( dia,  6, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 14, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 22, 30 ), 2 )
    elif cal.semana_gestacao(8).fim < dia < cal.DATA_SANGRAMENTO:
        Posologia_Duphostan.agendar( cal.agendamento( dia,  8, 00 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 20, 00 ), 2 )
    elif cal.DATA_SANGRAMENTO <= dia < cal.semana_gestacao(12).fim:
        Posologia_Duphostan.agendar( cal.agendamento( dia,  6, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 14, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 22, 30 ), 2 )

    
    if dia < cal.DATA_BORRINHA:
        Posologia_Utrogestan.agendar( cal.agendamento( dia,  6, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 14, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
    elif data_cmp( dia, cal.DATA_BORRINHA):
        Posologia_Utrogestan.agendar( cal.agendamento( dia,  6, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 14, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 2  )
    elif cal.DATA_BORRINHA < dia < cal.DATA_SANGRAMENTO_SEGUINTE:
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 10, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 00 ), 2  )
    elif data_cmp(dia, cal.DATA_SANGRAMENTO_SEGUINTE):
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 10, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 16, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 00 ), 2  )
    elif cal.DATA_SANGRAMENTO_SEGUINTE <= dia < cal.semana_gestacao(12).fim:
        Posologia_Utrogestan.agendar( cal.agendamento( dia,  4, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 10, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 16, 00 ), 2  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 00 ), 2  )
    elif dia <= cal.semana_gestacao(16).fim:
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
    

Posologia_Smorfolipide.agendar( cal.agendamento( cal.data( 2018, 10,  2), 15, 00 ), 1 )
Posologia_Smorfolipide.agendar( cal.agendamento( cal.data( 2018, 10, 30), 15, 00 ), 1 )
Posologia_Smorfolipide.agendar( cal.agendamento( cal.data( 2018, 11, 27), 15, 00 ), 1 )
Posologia_Smorfolipide.agendar( cal.agendamento( cal.data( 2018, 12, 18), 15, 00 ), 1 )
Posologia_Smorfolipide.agendar( cal.agendamento( cal.data( 2018, 01, 15), 15, 00 ), 1 )





    




