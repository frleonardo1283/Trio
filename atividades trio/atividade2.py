import os
os.system('cls')

QUANTIDADE_DIAS = 7
temperatura = []

print('--- SOLICITANDO GRAUS ---\n')
for i in range(QUANTIDADE_DIAS):
    gruas = int(input(f'Digite os graus do {i+1}º dia da semana: '))
    temperatura.append(gruas)

total = sum(temperatura)
media = total / len(temperatura)
maior = max(temperatura)
menor = min(temperatura)

print('\n--- SOLICITANDO GRAUS ---\n')
print(f'Lista de temperaturas: {temperatura}')
print(f'Total: {total}')
print(f'Media: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
