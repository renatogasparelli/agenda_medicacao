#!/bin/python
# -*- coding: utf-8 -*-
# renato

import os
import hashlib
import json
import codecs
import datetime

def main():
    configs = [
        ( u'/home/renato/Música', 'musicas_pbh_%(now)s.json'),
        ( '/cygdrive/f/Musics', 'musicas_desktop_f_%(now)s.json'),
        ( '/cygdrive/w/Music', 'musicas_hd-e_%(now)s.json')
    ]
    now = datetime.datetime.now()
    data = {'now':now.strftime("%Y.%m.%d_%H.%M")}
    for config in configs:
        home = config[0]
        if not os.path.exists( home ):
            continue
        size = len( os.listdir(home) )
        query = u'$> Processar diretorio %s (%d items) [y/n] ? '%( home, size)
        answer = raw_input( query.encode('utf-8') )
        if ( answer.lower() == 'y' ):
            print 'Processando %s'%home
            process ( home, config[1]%data )
        else:
            print 'Ignorando destino %s'%home    

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
    


    
    
    
    


