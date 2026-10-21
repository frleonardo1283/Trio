import os
os.system("cls")

numeros = []

QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"DIGITE O {i+1}º NÚMERO:" ))
    numeros.append(numero)
print(f"{numeros}")
print(f"{numeros[::-1]}")
    