# -*- coding: utf-8 -*-
import sys
import os
import mmap

action=sys.argv[1]
restartbind=os.system("systemctl restart bind9")
directzonefile="/var/cache/bind/db.ferrete.gonzalonazareno.org"
inversefloatzonefile="/var/cache/bind/db.172.22.200"
inversestaticzonefile="/var/cache/bind/db.10.0.0"
if action == '-a':
    regtype=sys.argv[2]
    hostname=sys.argv[3]
    iporalias=sys.argv[4]
    ip=iporalias.split(".")
    filetosearch=open(directzonefile)
    mmapfile=mmap.mmap(filetosearch.fileno(), 0, access=mmap.ACCESS_READ)
    filetosearch.close()
    if mmapfile.find(hostname+" ") != -1:
        print("That hostname already exist, you can check it: dig "+hostname+".ferrete.gonzalonazareno.org")
    else:
        if len(ip) == 4:
            if regtype == '-dir':
                if hostname != '':
                    directzone=open(directzonefile,"a")
                    directzone.write(hostname+" IN A "+iporalias+"\n")
                    directzone.close()
                    if ip[0] == '172':
                        inversefloatzone=open(inversefloatzonefile,"a")
                        inversefloatzone.write(ip[3]+" IN PTR "+hostname+"\n")
                        inversefloatzone.close()
                        restartbind
                        print("Done!.")
                    elif ip[0] == '10':
                        inversestaticzone=open(inversestaticzonefile,"a")
                        inversestaticzone.write(ip[3]+" IN PTR "+hostname+"\n")
                        inversestaticzone.close()
                        restartbind
                        print("Done!.")
                    else:
                        print("Added direct resolution for: "+hostname+".ferrete.gonzalonazareno.org at "+iporalias+", but this server has no auhtority of that inverse zone")
                else:
                    print("Param [HOSTNAME] needed")
            else:
                print("Can not create ALIAS of IP")
        elif len(ip) == 1:
            if regtype == '-alias':
                if hostname != '':
                        directzone=open(directzonefile,"a")
                        directzone.write(hostname+" IN CNAME "+iporalias+"\n")
                        directzone.close()
                        restartbind
                        print("Done!.")
                else:
                    print("Param [HOSTNAME] needed")
        else:
            print("Need specific [IP] or [ALIAS]")

elif action == '-b':
    hostname=sys.argv[2]
    f = open(directzonefile)
    output = []
    for line in f:
        if not hostname in line.strip():
            output.append(line)
    f.close()
    f = open(directzonefile, 'w')
    f.writelines(output)
    f.close()
    print("Done!.")
