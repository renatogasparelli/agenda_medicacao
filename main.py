#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal

from lib.eventos import *
from lib.estoques import *
from lib.relatorios import *

hoje = cal.hoje()
atequando = hoje + 8 * cal.UM_DIA


report = {}


for evento in eventos:
    
    if isinstance( evento, Medicacao ):
        
        medicamento = evento.medicamento()
        estoque = obter_estoque( medicamento )
    
        try:
            estoque.registrar_saida( evento.datahora(), evento.quantidade() )
        except SaldoInsuficienteException as e:
            pass
    
    if hoje <= evento.datahora() <= atequando :
        registra_agenda_medicacao( report, evento )

        
        
export_agenda_medicacao( report )
        
    

    
