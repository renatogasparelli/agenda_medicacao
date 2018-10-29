#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal
import collections as col

Registro = col.namedtuple( 'Registro', 'datahora quantidade sentido valor' )

from lib.medicamentos import *


class SaldoInsuficienteException ( Exception ): pass

class __Estoque(object):
    
    def __init__(self, medicamento):
        self.__medicamento = medicamento
        self.__registros = []
        
    def medicamento(self):
        return self.__medicamento

    def datasregistros(self):
        return sorted( [ x.datahora for x in self.__registros ] )

    def registrar_entrada( self, datahora, quantidade, valor=0 ):
        self.__registros.append( Registro( datahora, quantidade, 'e', valor ) )
    
    def registrar_saida( self, datahora, quantidade ):
        if self.saldo( datahora ) <= 0:
            raise SaldoInsuficienteException('Medicamento em falta')
        self.__registros.append( Registro( datahora, quantidade, 's', 0 ) )
    
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

Estoques = { x.nome() : __Estoque( x ) for x in Medicamentos }


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


dataregistro = cal.datahora( 2018, 10, 2, 1, 00 )
obter_estoque( Metilfolato ).registrar_entrada( dataregistro, 90 )

dataregistro = cal.datahora( 2018, 10, 2, 12, 00 )
obter_estoque( Omega3 ).registrar_entrada( dataregistro, 30, 58.83 )
obter_estoque( Duphostan ).registrar_entrada( dataregistro, 28, 45.00 )
obter_estoque( Utrogestan ).registrar_entrada( dataregistro, 42, 120.08 )

dataregistro = cal.datahora( 2018, 10, 5, 12, 00 )
obter_estoque( Utrogestan ).registrar_entrada( dataregistro, 3 * 42, 3 * 117.00 )

dataregistro = cal.datahora( 2018, 10, 7, 12, 00 )
obter_estoque( Duphostan ).registrar_entrada( dataregistro, 2 * 28, 87.17 )

dataregistro = cal.datahora( 2018, 10, 8, 12, 00 )
obter_estoque( Duphostan ).registrar_entrada( dataregistro, 2 * 28 + 3 * 14, 149.17 )

dataregistro = cal.datahora( 2018, 10, 15, 13, 00 )
obter_estoque( Enoxoparina ).registrar_entrada( dataregistro, 30, 0 )

dataregistro = cal.datahora( 2018, 10, 17, 13, 00 )
obter_estoque( VitaminaE ).registrar_entrada( dataregistro, 30, 32.52 )
obter_estoque( VitaminaC ).registrar_entrada( dataregistro, 30, 21.55 )

dataregistro = cal.datahora( 2018, 10, 29, 12, 00 )
obter_estoque( Omega3 ).registrar_entrada( dataregistro, 30, 74.49 )
obter_estoque( Duphostan ).registrar_entrada( dataregistro, 2 * 28, 2*43.32 )
obter_estoque( BTrati ).registrar_entrada( dataregistro, 42, 64.37 )



