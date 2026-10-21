import os
os.system('cls')

vetor = []
print("Digite 8 números inteiros:")
for i in range(8):
    numero = int(input(f"Número {i + 1}: "))
    vetor.append(numero)

alvo = int(input("\nDigite o número que deseja pesquisar: "))

encontrado = False
for posicao, numero in enumerate(vetor):
    if numero == alvo:
        print(f"Número encontrado na posição (índice): {posicao + 1}")
        encontrado = True
        break

if not encontrado:
    print("Número não encontrado.")

print('\nFeito por: Camilla Bastos')
print('R.A.: 026.082364')