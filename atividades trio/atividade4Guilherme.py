import os
os.system("cls")

vetor_numeros = []
QUANTIDADE_NUMEROS = 8
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"digite o {i+1}º numero: "))
    vetor_numeros.append(numero)

print("====PESQUISANDO====")

pesquisa = int(input("digite um número para pesquisa:"))

encontrado = False
for posicao, numero in enumerate(vetor_numeros):
    if numero == pesquisa:
        print(f"número encontrado na posição (indice): {posicao+1}")
        encontrado = True
        break
if not encontrado:
    print("número não encontrado.")