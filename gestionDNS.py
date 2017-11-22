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
directzone=open("/var/cache/bind/db.ferrete.gonzalonazareno.org","a")
inversefloatzone=open("/var/cache/bind/db.172.22.200","a")
inversestaticzone=open("/var/cache/bind/db.10.0.0","a")

action=sys.argv[1]
regtype=sys.argv[2]
hostname=sys.argv[3]
iporalias=sys.argv[4]

if action == '-a':
    if regtype == '-dir':
        directzone.write(hostname+" IN A "+iporalias)
        if iporalias == ''
    elif regtype == '-alias':
        directzone.write(hostname+" IN CNAME "+iporalias)
    else:
        print("Not a valid param number two")
elif action == '-b':
    
