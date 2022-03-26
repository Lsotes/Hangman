# Modulos importados
import random
import os

# Creación y enumeración de la base de datos de palabras
palabra = []
with open("./data.txt","r",encoding="utf-8") as f:
    for line in f:
        palabra.append(str(line))
enumerada = dict(enumerate(palabra,0))

# Desarrollo del elector de palabras aleatorio
cuenta = len(enumerada)
elegida = str(enumerada.get(random.randint(0,cuenta)))

intentos = 7

def run():
    print("¡Adivina la palabra!")
    resultado = []
    
    for i in range(intentos):
        letra = str(input("Ingresa una letra y presiona enter: "))
        if letra == elegida[range(0,len(elegida)+1)]:
            resultado.append(letra)

    




if __name__ == "__main__":
    run()