#!/usr/bin/env python
# -*- coding: utf-8 -*-

_HashMedicamentos = {}
Medicamentos=set()

class __Medicamento(object):
    
    def __init__(self, nome, unidade, **params):
        self.__nome = nome
        self.__unidade = unidade
        Medicamentos.add(self)
        _HashMedicamentos[ nome ] = self
    
    def nome(self): return self.__nome
    
    def unidade(self): return self.__unidade
        
def obter_medicamento(nome_medicamento):
    return _HashMedicamentos[nome_medicamento]

Utrogestan   = __Medicamento( 'Utrogestan 200 mg', u'cápsula', dosagem='200 mg', quantidade=u'42 cápsulas')
Metilfolato  = __Medicamento( '5-Metilfolato 1 mg', 'comprimido', dosagem='1 mg')
VitaminaC    = __Medicamento( 'VitaminaC - Cewin 500mg', u'cápsula', dosagem='500mg', quantidade=u'30 cápsulas')
BTrati       = __Medicamento( 'BeTrat',  'comprimido', dosagem='100mg, 100mg e 5000mcg', quantidade=u'42 cápuslas')
Omega3       = __Medicamento( u'Ômega Mater', u'cápsula', dosagem='DHA 300 mg e EPA 120 mg', quantidade=u'30 cápsulas')
VitaminaE    = __Medicamento( 'VitaminaE - Vita E 400mg', 'comprimido', dosagem='400mg', quantidade=u'30 comprimidos')
Somalgin     = __Medicamento( 'Somalgin Cardio 81mg',  'comprimido', dosagem='81mg')
Smorfolipide = __Medicamento( 'Smorfolipide' ,  'frasco')
Enoxoparina  = __Medicamento( 'Enoxoparina', u'injeção')
Duphostan    = __Medicamento( 'Duphaston 10 mg',  'comprimido', dosagem='10 mg', quantidade=u'28 cápsulas')
AdderaD3     = __Medicamento( 'AdderaD3 7.000 Ui',  'comprimido', dosagem='7.000 Ui')
CalcioK2     = __Medicamento( u'Caldê K2',  'comprimido')




