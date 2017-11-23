# -*- coding: utf-8 -*-
import sys
import os

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
if action == '-a':
    directzone=open("/var/cache/bind/db.ferrete.gonzalonazareno.org","a")
    iporalias=sys.argv[4]
    ip=iporalias.split(".")
    if len(ip) == 4:
        if regtype == '-dir':
            if hostname != '':
                directzone.write(hostname+" IN A "+iporalias+"\n")
                directzone.close()
                if ip[0] == '172':
                    inversefloatzone=open("/var/cache/bind/db.172.22.200","a")
                    inversefloatzone.write(ip[3]+" IN PTR "+hostname+"\n")
                    inversefloatzone.close()
                    restartbind
                elif ip[0] == '10':
                    inversestaticzone=open("/var/cache/bind/db.10.0.0","a")
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
                    directzone.write(hostname+" IN CNAME "+iporalias+"\n")
                    directzone.close()
                    restartbind
            else:
                print("Param [HOSTNAME] needed")

    else:
        print("Need specific [IP] or [ALIAS]")

#elif action == '-b':
