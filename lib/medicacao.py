#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import lib.calendario as cal

from lib.medicamentos import *

_AgendaItem = collections.namedtuple('_AgendaItem', 'datahora quantidade')

Posologias = {}
class __Posologia(object):
    
    def __init__(self, medicamento):
        self.__medicamento = medicamento
        self.__aplicacao = []
        self.__tratamento_inicio = None
        self.__tratamento_fim = None
        self.suspenso = False
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

Posologia_Somalgin.suspenso = True

data_exame_beta = cal.semana_gestacao(4).inicio
data_cuidado_borrinha = cal.data( 2018, 10, 2 )

for dia in cal.dias_entre( cal.DATA_CONTROLE_ESTOQUE, cal.DATA_CONTROLE_ESTOQUE_FIM ):
    
    Posologia_Enoxoparina.agendar( cal.agendamento( dia, 7, 00 ), 1 )
    Posologia_Omega3.agendar( cal.agendamento( dia, 12, 00 ), 1  )
    
    if dia <= cal.semana_gestacao(12).fim:
        Posologia_Metilfolato.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        Posologia_VitaminaC.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        Posologia_VitaminaE.agendar( cal.agendamento( dia, 13, 00 ), 1  )
        Posologia_BTrati.agendar( cal.agendamento( dia, 7, 00 ), 1  )
        if cal.eh_sabado(dia):
            Posologia_AdderaD3.agendar( cal.agendamento( dia,  7, 30 ), 1 )
    
    if dia > cal.semana_gestacao(12).fim:
        Posologia_CalcioK2.agendar( cal.agendamento( dia, 12, 00 ), 1 )
        Posologia_CalcioK2.agendar( cal.agendamento( dia, 18, 00 ), 1 )
        
    if dia <= cal.semana_gestacao(36).fim:
        Posologia_Somalgin.agendar( cal.agendamento( dia, 7, 00 ), 1  )
    
    if dia <= cal.semana_gestacao(8).fim:
        Posologia_Duphostan.agendar( cal.agendamento( dia,  6, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 14, 30 ), 2 )
        Posologia_Duphostan.agendar( cal.agendamento( dia, 22, 30 ), 2 )

    if dia < cal.semana_gestacao(12).fim:
        if dia < data_cuidado_borrinha:
            Posologia_Utrogestan.agendar( cal.agendamento( dia,  6, 30 ), 1  )
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 14, 30 ), 1  )
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
        elif dia > data_cuidado_borrinha:
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 10, 00 ), 2  )
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 00 ), 2  )
        else:
            Posologia_Utrogestan.agendar( cal.agendamento( dia,  6, 30 ), 1  )
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 14, 30 ), 1  )
            Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 2  )
    elif dia <= cal.semana_gestacao(16).fim:
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
        
    

smfdelta = 4 * 7 # 4 semanas
doses = 5
for dia in cal.dias_entre( cal.DATA_CONTROLE_ESTOQUE,
        cal.DATA_CONTROLE_ESTOQUE + ( doses - 1 ) * smfdelta * cal.UM_DIA, smfdelta ):
    Posologia_Smorfolipide.agendar( cal.agendamento( dia, 15, 00 ), 1 )



    



