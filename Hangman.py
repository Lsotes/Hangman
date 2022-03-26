import random
import os

palabra = []
with open("./data.txt","r",encoding="utf-8") as f:
    for line in f:
        palabra.append(str(line))
enumerada = enumerate(palabra)

def run():
    print("¡Adivina la palabra!")
    print(type(enumerada))


    letra = str(input("Ingresa una letra: "))





if __name__ == "__main__":
    run()