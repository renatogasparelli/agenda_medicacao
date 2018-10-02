#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal

from lib.medicamentos import *

Posologias = {}

class __Posologia(object):
    
    def __init__(self, medicamento):
        self.__medicamento = medicamento
        self.__aplicacao = []
        Posologias[ self.__medicamento.nome() ] = self
        
    def medicamento(self):
        return self.__medicamento
    
    def agendar(self, datahora, quantidade):
        self.__aplicacao.append( ( datahora, quantidade ) )
    
    def agendamentos(self):
        return self.__aplicacao


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
Posologia_Smorfolipide = __Posologia( Smorfolipide )

data_exame_beta = cal.semana_gestacao(4)[0]
data_nascimento = cal.NASCIMENTO

data_de_controle = cal.DATA_CONTROLE_ESTOQUE

for dia in cal.dias_entre( data_de_controle, data_nascimento ):
    
    Posologia_Metilfolato.agendar( cal.agendamento( dia, 7, 00 ), 1  )
    Posologia_VitaminaC.agendar( cal.agendamento( dia, 7, 00 ), 1  )
    Posologia_BTrati.agendar( cal.agendamento( dia, 7, 0 ), 1  )
    
    Posologia_Omega3.agendar( cal.agendamento( dia, 12, 00 ), 1  )
    Posologia_VitaminaE.agendar( cal.agendamento( dia, 13, 00 ), 1  )
    
    if dia >= cal.semana_gestacao(9)[0]:
        Posologia_Somalgin.agendar( cal.agendamento( dia, 7, 0 ), 1  )
    
    Posologia_Duphostan.agendar( cal.agendamento( dia,  6, 30 ), 2 )
    Posologia_Duphostan.agendar( cal.agendamento( dia, 14, 30 ), 2 )
    Posologia_Duphostan.agendar( cal.agendamento( dia, 22, 30 ), 2 )

    Posologia_Enoxoparina.agendar( cal.agendamento( dia, 7, 00 ), 1 )

    if dia < cal.semana_gestacao(9)[0]:
        Posologia_Utrogestan.agendar( cal.agendamento( dia,  6, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 14, 30 ), 1  )
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
    else:
        Posologia_Utrogestan.agendar( cal.agendamento( dia, 22, 30 ), 1  )
        
    if cal.eh_sabado(dia):
        Posologia_AdderaD3.agendar( cal.agendamento( dia,  7, 30 ), 2 )

quatro_semanas = 4 * 7 * cal.UM_DIA
dia = data_exame_beta+ cal.UM_DIA
while dia < data_nascimento:
    Posologia_Smorfolipide.agendar( cal.agendamento( dia, 15, 00 ), 1 )
    dia += quatro_semanas



    



