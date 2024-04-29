import random

apellido=input("Ing apellido")
apellido = apellido.lower()
numAleatorio= random.randint(0,9)
clave=""
cont=0 #cuenta consonantes
#guardo consonante
for letra in apellido:
    if((letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u") and (cont<4)):
        clave= clave + letra
        cont= cont+1
#AGREGO ASTERISCO SI LEN MENOR A 4
cantAster=4-len(clave)
clave=clave+("*"*cantAster)
clave=clave+ str(numAleatorio)
print(clave)