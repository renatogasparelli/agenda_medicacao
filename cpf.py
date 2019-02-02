#!/bin/python
# -*- coding: utf-8 -*-
# renato

import os
import hashlib
import json
import codecs


def main():

    def md5sun( x ):
        m = hashlib.md5()
        with open( x, 'rb' ) as fin:
            m.update( fin.read() )
        return m.hexdigest()

    data = []

    home = '/cygdrive/f/Musics'
    for albumname in os.listdir( home ):
        albumhome = os.path.join( home, albumname )
        if not os.path.isdir( albumhome ):
            continue
        print albumhome        
        for root, dirs, files in os.walk( albumhome ):
    
            album = {
                'home':albumhome,
                'album':albumname,
                'musicas':[]
            }
            
            for fname in files:
                filefullpath = os.path.join( root, fname )
                
                album['musicas'].append(
                    {
                        'arquivo':fname,
                        'md5': md5sun( filefullpath )
                    }
                )
                
            data.append ( album )
    
    with codecs.open( 'md5_music_f.txt', 'w', 'UTF-8' ) as fout:
        fout.write( json.dumps(data, indent=4, sort_keys=True) )
        

main()
    


    
    
    
    


