#!/bin/python
# -*- coding: utf-8 -*-
# renato

import itertools

def main():
    V10 = range( 10 )
    digits = [ 0, 5, 9, 9, 2, 3, None, None, None ]
    for i, j, k in itertools.product( V10, V10, V10 ):
        digits[6] = i
        digits[7] = j
        digits[8] = k
        if ( calc_dv( digits ) == 4
                and  calc_dv( digits + [ 4 ] ) == 5 ):
            print digits, 45

def calc_dv( digits ):
    ldigits = len(digits)
    acm = 0
    for i in range(ldigits):
        k = ( ldigits - i + 1 )
        acm += k * digits[i]
    digit = acm % 11
    if digit == 0 or digit == 1:
        return 0
    return 11 - digit

main()
    


    
    
    
    


