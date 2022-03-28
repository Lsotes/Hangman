# Modulos importados
import random
import os

# Creación y enumeración de la base de datos de palabras
with open("./data.txt","r",encoding="utf-8") as f:
    palabra = [line.strip("\n").upper() for line in f]

enumerada = dict(enumerate(palabra,0))

# Desarrollo del elector de palabras aleatorio
elegida = str(enumerada.get(random.randint(0,len(enumerada))))
elegida = list(elegida)

def run():
    INTENTOS = 7 # Cuerpo del ahorcado + soga
    resultado = ["-" for i in range(len(elegida))]
    respuestas = []

    # Reemplazo de los espacios por letras
    for i in range(50):  
        print("¡Adivina la palabra!")
        print(resultado," ", len(elegida), "letras")
        print("Intentos: ", INTENTOS)
        print("Tus letras: ",respuestas)
        
        letra = input("Ingresa una letra y presiona enter: ").upper() # str al principio
        respuestas.append(letra)

        for n in range(len(elegida)):
            if letra == elegida[n]:
                resultado[n] = letra
                INTENTOS += 1
            
        INTENTOS = INTENTOS - 1
        if INTENTOS > 7:
            INTENTOS = 7

        os.system('cls')
        
        if INTENTOS == 0:
            print("¡AHORCADO!")
            print("La palabra era: ", elegida)
            break
        elif resultado == list(elegida):
            print("¡Ganaste!")
            print("La palabra era: ", elegida)
            break
        
        

if __name__ == "__main__":
    run()