#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal
import collections as col

Registro = col.namedtuple( 'Registro', 'datahora quantidade sentido' )

from lib.medicamentos import *

Estoques = {}

class SaldoInsuficienteException ( Exception ): pass

class __Estoque(object):
    
    def __init__(self, medicamento):
        self.__medicamento = medicamento
        self.__registros = []
        Estoques[ self.__medicamento.nome() ] = self
        
    def medicamento(self):
        return self.__medicamento

    def registrar_entrada( self, datahora, quantidade ):
        self.__registros.append( Registro( datahora, quantidade, 'e' ) )
    
    def registrar_saida( self, datahora, quantidade ):
        if self.saldo( datahora ) <= 0:
            raise SaldoInsuficienteException('Medicamento em falta')
        self.__registros.append( Registro( datahora, quantidade, 's' ) )
    
    def saldo( self, ate=None ):
        acm = 0
        for registro in sorted( self.__registros, key=lambda x : x.datahora):
            if ate != None and registro.datahora > ate:
                break
            if registro.sentido == 'e':
                acm += registro.quantidade
            else:
                acm -= registro.quantidade
        return acm


def obter_estoque( medicamento ):
    return Estoques[ medicamento.nome() ]

__Estoque( Utrogestan   )
__Estoque( Metilfolato  )
__Estoque( VitaminaC    )
__Estoque( BTrati       )
__Estoque( Omega3       )
__Estoque( VitaminaE    )
__Estoque( Somalgin     )
__Estoque( Smorfolipide )
__Estoque( Enoxoparina  )
__Estoque( Duphostan    )
__Estoque( AdderaD3     )



databalanco = cal.DATA_CONTROLE_ESTOQUE
obter_estoque( Utrogestan ).registrar_entrada( databalanco, 12 )
obter_estoque( Metilfolato ).registrar_entrada( databalanco, 0 )
obter_estoque( VitaminaC ).registrar_entrada( databalanco, 18 )
obter_estoque( BTrati ).registrar_entrada( databalanco, 33 )
obter_estoque( Omega3 ).registrar_entrada( databalanco, 1 )
obter_estoque( VitaminaE ).registrar_entrada( databalanco, 21 )
obter_estoque( Somalgin ).registrar_entrada( databalanco, 45 )
obter_estoque( Duphostan ).registrar_entrada( databalanco, 26 )
obter_estoque( Smorfolipide ).registrar_entrada( databalanco, 1 )
obter_estoque( Enoxoparina ).registrar_entrada( databalanco, 25 )
obter_estoque( AdderaD3 ).registrar_entrada( databalanco, 7 )


dataregistro = cal.datahora( 2018, 10, 02, 9, 00 )
obter_estoque( Metilfolato ).registrar_entrada( dataregistro, 90 )






