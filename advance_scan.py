#!/usr/bin/python

from socket import *
import optparse
from threading import *
import argparse

# cette fonction ouvrira un socket pour essayer de se connecter a l'adresse spécifier; c'est comme un ping 
def connScan(tgthost, tgtport):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgthost,tgtport))
        print("[+] %d/tcp Open" %tgtport)
    except:
        print("[-] %d/tcp Closed" %tgtport)
    finally:
        sock.close()

# cette fonction va verifier si les adresses sont bonnes et les resoudres si par exemple l'adresse indiqué est un nom de domaine
def port_scan(tgthost,tgtport):
    try:
        tgtip=gethostbyname(tgthost)
    except:
        print(" %d is an invalid host" %tgthost)
    try:
        tgtname=gethostnamebyaddr(tgtip)
        print("[+] Scan results for: " +tgtname)
    except :
        print("[+] Scan Results for:" +tgtip)
    setdefaulttimeout(1)
    for tgtport in tgtport:
        t=Thread(target=connScan, args=(tgthost, int(tgtport)))
        t.start()

#def main():
#   parser=optparse.OptionParser("Usage of program" + "-h <target host> -p <target port>")
#    parser.add_option("-h", dest="tgthost", type="string" , help="specify targett host")
#    parser.add_option("-p", dest="tgtport", type="string", help="specify target ports separated by vcomma")
#    (options, args)=parser.parse_args()
#    tgtport=str(options.tgtport).split(',')
#    tgthost=options.tgthost
#    if (tgthost==None) or  (tgtport[0]==None):
#        print(parser.usage)
#        exit(0)
#    port_scan(tgthost,tgtport)

# Cette fonction analyse les arguments de ligne de commande en utilisant le module argparse et appelle la fonction port_scan avec les arguments spécifiés
def main():
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("-H", dest="host", required=True, help="specify target host")
    parser.add_argument("-p", dest="port", required=True, help="specify an intervall of target ports separated by -")
    args = parser.parse_args()
    tgthost = args.host
    tgtport = str(args.port).split('-')
    if not tgthost or not tgtport:
        parser.error("Missing arguments")
    port_scan(tgthost, tgtport)

# Cette ligne appelle la fonction main si le script est exécuté directement
if __name__=='__main__':
    main()