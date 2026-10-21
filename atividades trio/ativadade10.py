import os
os.system('cls')

QUANTIDADE = 5
idade = []
maioridade = []

for i in range(QUANTIDADE):
    idades = int(input(f'Digite a {i+1}º idade: '))
    if idades >= 0 and idades <= 120:
        idade.append(idades)
        if idades >= 18:
            maioridade.append(idades)

maior = max(idade)
menor = min(idade)

print(f'Maior idade: {maior}')
print(f'Menor idade: {menor}')
print(f'maiores idades: {maioridade}')

print('\nFeito por: Richard')
