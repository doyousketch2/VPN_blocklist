#!/usr/bin/env python3
'''
Convert nginx blacklist to iptables entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VPN blacklist

https://www.lowendtalk.com/discussion/44388/vpn-ip-blacklist

https://github.com/Zalvie/nginx_block_files


Better to place in iptables, so it doesn't waste processor cycles.

https://serverfault.com/questions/432716/where-to-place-nginx-ip-blacklist-config-file

https://www.cyberciti.biz/faq/how-do-i-block-an-ip-on-my-linux-server

AGPL -- https://www.gnu.org/licenses/agpl-3.0.en.html
'''

import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root  = os .curdir
folder  = 'nginx_block_files'
directory  = os .path .join( root, folder )

output  = []

for filename in os .listdir( directory ):
  if filename .endswith('.asn'):
    print( filename )

    filepath  = os .path .join( directory, filename )
    with open( filepath ) as f:
      for line in f:  #  deny xx.xx.xx.xx;
        column  = line .strip() .rstrip(';') .split(' ')
        if column[0] == 'deny':
          IP  = column[1]
          # iptables -A INPUT -s xx.xx.xx.xx -j DROP
          output .append( 'iptables -A INPUT -s '  + IP + ' -j DROP' )

with open('output.txt', 'w') as data:
  data .write( '\n'.join( output ) )

