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

Utrogestan   = __Medicamento( 'Utrogestan'   , u'cápsula'   , dosagem='200 mg', quantidade=u'42 cápsulas')
Metilfolato  = __Medicamento( '5-Metilfolato',  'comprimido', dosagem='1 mg')
VitaminaC    = __Medicamento( 'VitaminaC'    , u'cápsula'   )
BTrati       = __Medicamento( 'BTrati'       ,  'comprimido')
Omega3       = __Medicamento( 'Omega3'       , u'cápsula'   , dosagem='DHA 300 mg e EPA 120 mg', quantidade=u'30 cápsulas')
VitaminaE    = __Medicamento( 'VitaminaE'    ,  'comprimido')
Somalgin     = __Medicamento( 'Somalgin'     ,  'comprimido')
Smorfolipide = __Medicamento( 'Smorfolipide' ,  'frasco'    )
Enoxoparina  = __Medicamento( 'Enoxoparina'  , u'injeção'   )
Duphostan    = __Medicamento( 'Duphostan'    ,  'comprimido', dosagem='10 mg', quantidade=u'28 cápsulas')
AdderaD3     = __Medicamento( 'AdderaD3'     ,  'comprimido')
CalcioK2     = __Medicamento( 'CalcioK2'     ,  'comprimido')




