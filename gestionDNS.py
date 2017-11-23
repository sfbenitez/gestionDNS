# -*- coding: utf-8 -*-
import sys
import os
import mmap

#* ``-a`` o ``-b``: Si recibe ``-a`` añadirá un nuevo nombre,
# si recibe ``-b`` borrará el nombre que ha recibido.
#* ``-dir`` o ``-alias``, si recibe ``-dir`` va a crear un registro tipo A,
# si recibe ``-alias`` va a crear un registro CNAME
#* El nombre de la máquina para añadir o borrar
#* El nombre del alias o la dirección ip: Si has usuado la opción ``-dir``
#recibirá una ip y si has usuado ``-alias`` recibirá el nombre de la máquina
# a la que le vamos a hacer el alias. Si has utilizado -b no teendrá
# este parámetro.

action=sys.argv[1]
regtype=sys.argv[2]
hostname=sys.argv[3]
restartbind=os.system("systemctl restart bind9")
directzonefile="/var/cache/bind/db.ferrete.gonzalonazareno.org"
inversefloatzonefile="/var/cache/bind/db.172.22.200"
inversestaticzonefile="/var/cache/bind/db.10.0.0"
if action == '-a':
    iporalias=sys.argv[4]
    ip=iporalias.split(".")
    filetosearch=open("")
    mmapfile=mmap.mmap(filetosearch.fileno(), 0, access=mmap.ACCESS_READ)
    filetotsearch.close()
    if mmapfile.find(hostname+" ") != -1:
        print("That hostname already exist, you can check it: dig "+hostname+".ferrete.gonzanlonazareno.org")
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
                    elif ip[0] == '10':
                        inversestaticzone=open(inversestaticzonefile,"a")
                        inversestaticzone.write(ip[3]+" IN PTR "+hostname+"\n")
                        inversestaticzone.close()
                        restartbind
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
                else:
                    print("Param [HOSTNAME] needed")
        else:
            print("Need specific [IP] or [ALIAS]")

elif action == '-b':
    f = open(directzonefile)
    output = []
    for line in f:
        if not hostname in line:
            output.append(line)
    f.close()
    f = open(directzonefile, 'w')
    f.writelines(output)
    f.close()
