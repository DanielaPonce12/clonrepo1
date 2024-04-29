import random

nombre=input("Ingrese su nombre")
cant=0
cadena=""
for letra in nombre:
    if letra!="a" and letra!="e" and letra!="i" and letra!="o" and letra!="u":
        if cant<4:
            cadena+=letra
            cant+=1
if cant<4:
    for i in range(cant,4+1):
        cadena+="*"

aleatorio=str (random.randrange(10))

cadena=cadena+aleatorio
print(cadena)