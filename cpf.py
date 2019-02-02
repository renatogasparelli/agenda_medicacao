#!/bin/python
# -*- coding: utf-8 -*-
# renato

import os
import hashlib
import json
import codecs


def main():
    #home, jsonname = ( '/cygdrive/f/Musics', 'md5_music_f2.json')
    home, jsonname = ( '/cygdrive/w/Music', 'md5_music_w2.json')
    process( home, jsonname )

def process(home, jsonname):
    
    
    
    data = []
    
    for albumname in os.listdir( home ):
        albumhome = os.path.join( home, albumname )
        if not os.path.isdir( albumhome ):
            continue
        print albumhome        
        for root, dirs, files in os.walk( albumhome ):
            if len( files ) == 0:
                continue
    
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
                        'filefullpath':filefullpath,
                        'md5': md5sun( filefullpath ),
                        'size': os.path.getsize( filefullpath )
                    }
                )
                
            data.append ( album )
    
    with codecs.open( jsonname, 'w', 'UTF-8' ) as fout:
        fout.write( json.dumps(data, indent=4, sort_keys=True) )
        

def md5sun( x ):
    m = hashlib.md5()
    with open( x, 'rb' ) as fin:
        m.update( fin.read() )
    return m.hexdigest()

main()
    


    
    
    
    


