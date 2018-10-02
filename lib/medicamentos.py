#!/usr/bin/env python
# -*- coding: utf-8 -*-


class __Medicamento(object):
    
    def __init__(self, nome, unidade):
        self.__nome = nome
        self.__unidade = unidade
    
    def nome(self): return self.__nome
    
    def unidade(self): return self.__unidade
        


Utrogestan   = __Medicamento( 'Utrogestan'  ,  'capsula' )
Metilfolato  = __Medicamento( 'Metilfolato' ,  'comprimido' )
VitaminaC    = __Medicamento( 'VitaminaC'   ,  'capsula' )
BTrati       = __Medicamento( 'BTrati'      ,  'comprimido' )
Omega3       = __Medicamento( 'Omega3'      ,  'comprimido' )
VitaminaE    = __Medicamento( 'VitaminaE'   ,  'comprimido' )
Somalgin     = __Medicamento( 'Somalgin'    ,  'comprimido' )
Smorfolipide = __Medicamento( 'Smorfolipide',  'frasco' )
Enoxoparina  = __Medicamento( 'Enoxoparina' , u'injeção' )
Duphostan    = __Medicamento( 'Duphostan'   ,  'comprimido' )
AdderaD3     = __Medicamento( 'AdderaD3'    ,  'comprimido' )




