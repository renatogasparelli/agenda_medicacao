#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal

from lib.eventos import *
from lib.estoques import *
from lib.relatorios import *
from lib.medicacao import *

hoje = cal.hoje()
atequando = hoje + 8 * cal.UM_DIA

report = {}

for evento in Eventos:
    
    if isinstance( evento, EMedicacao ):
        medicamento = evento.medicamento()
        estoque = obter_estoque( medicamento )
        try:
            estoque.registrar_saida( evento.datahora(), evento.quantidade() )
        except SaldoInsuficienteException as e:
            pass
        
    if hoje <= evento.datahora() <= atequando :
        registra_agendamento( report, evento )

exporta_registros_agendamento( report )
exporta_agendamentos_complexos()
exporta_dados_planilha()
        
    
    

    
