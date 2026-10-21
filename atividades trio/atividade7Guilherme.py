import os
os.system("cls")

vetor_numero =  []
vetor_positivo = []
QUANTIDADE_NUMEROS = 10

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}º número: "))
    vetor_numero.append(numero)
vetor_positivo = []
for numero in vetor_numero:
    if numero >  0:
        vetor_positivo.append(numero)
print("===MOSTRANDO DADOS===")

print(f"números copiados: {vetor_positivo}")
print(f"quantidade de elementos copiados: {len(vetor_positivo)}")
