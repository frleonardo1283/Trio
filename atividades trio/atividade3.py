import os
os.system("cls")

vetor = []
soma = 0
maiores_que_10 = 0

print("Digite 10 números inteiros:")
for i in range(10):
    num = int(input(f"Número {i + 1}: "))
    vetor.append(num)
    
    soma += num

    if num > 10:
        maiores_que_10 += 1

os.system("cls")

print("\n--- Resultados ---")
print(f"Vetor digitado: {vetor}")
print(f"Soma de todos os elementos: {soma}")
print(f"Quantidade de números maiores que 10: {maiores_que_10}")