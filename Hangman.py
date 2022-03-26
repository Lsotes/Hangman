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

INTENTOS = 7 # Cuerpo del ahorcado + soga

def run():
    print("¡Adivina la palabra!")
    
    resultado = ["-" for i in range(len(elegida)-1)]
    print(resultado)
    
    for i in range(INTENTOS):
        letra = str(input("Ingresa una letra y presiona enter: "))
        for n in range(len(elegida)-1):
            if letra == elegida[n]:
                resultado[n] = letra
                INTENTOS += 1
        break
        
print(resultado)

    




if __name__ == "__main__":
    run()