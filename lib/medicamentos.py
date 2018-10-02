#!/usr/bin/env python
# -*- coding: utf-8 -*-


class __Medicamento(object):
    
    def __init__(self, nome, unidade, **params):
        self.__nome = nome
        self.__unidade = unidade
    
    def nome(self): return self.__nome
    
    def unidade(self): return self.__unidade
        


Utrogestan   = __Medicamento( 'Utrogestan'  , u'cápsula'   , dosagem='200 mg', quantidade=u'42 cápsulas')
Metilfolato  = __Medicamento( 'Metilfolato' ,  'comprimido')
VitaminaC    = __Medicamento( 'VitaminaC'   , u'cápsula'   )
BTrati       = __Medicamento( 'BTrati'      ,  'comprimido')
Omega3       = __Medicamento( 'Omega3'      , u'cápsula'   , dosagem='DHA 300 mg e EPA 120 mg', quantidade=u'30 cápsulas')
VitaminaE    = __Medicamento( 'VitaminaE'   ,  'comprimido')
Somalgin     = __Medicamento( 'Somalgin'    ,  'comprimido')
Smorfolipide = __Medicamento( 'Smorfolipide',  'frasco'    )
Enoxoparina  = __Medicamento( 'Enoxoparina' , u'injeção'   )
Duphostan    = __Medicamento( 'Duphostan'   ,  'comprimido', dosagem='10 mg', quantidade=u'28 cápsulas')
AdderaD3     = __Medicamento( 'AdderaD3'    ,  'comprimido')




