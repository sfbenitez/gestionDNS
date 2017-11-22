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

if action == '-a':
    directzone=open("/var/cache/bind/db.ferrete.gonzalonazareno.org","a")
    inversefloatzone=open("/var/cache/bind/db.172.22.200","a")
    inversestaticzone=open("/var/cache/bind/db.10.0.0","a")
    iporalias=sys.argv[4]
    ip=iporalias.split(".")
    if regtype == '-dir':
        if hostname != '':
            if iporalias != '':
                directzone.write(hostname+" IN A "+iporalias)
                inversefloatzone.write(ip[3]+" IN PTR "+hostname)
            else:
                print("Param [IP] needed")
        else:
            print("Param [HOSTNAME] needed")
    elif regtype == '-alias':
        if hostname != '':
            if iporalias != '':
                directzone.write(hostname+" IN CNAME "+iporalias)
            else:
                print("Param [ALIAS] needed")
        else:
            print("Param [HOSTNAME] needed")
    else:
        print("Not a valid param number two")
#elif action == '-b':
