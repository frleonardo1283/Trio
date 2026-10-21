import os
os.system('cls' if os.name == 'nt' else 'clear')

QUANTIDADE_FUNCIONARIOS = 5

nomes = []
salarios = []

print('--- CADASTRO DE FUNCIONÁRIOS ---\n')
for i in range(QUANTIDADE_FUNCIONARIOS):
    nome = input(f'Digite o nome do {i + 1}º funcionário: ')
    salario = float(input(f'Digite o salário de {nome}: R$ '))
    
    nomes.append(nome)
    salarios.append(salario)

maior_salario = max(salarios)
posicao_maior = salarios.index(maior_salario)
nome_maior_salario = nomes[posicao_maior]

acima_2000 = sum(1 for salario in salarios if salario > 2000.00)

print('\n--- RESULTADOS ---\n')
print(f'Maior salário: R$ {maior_salario:.2f} ({nome_maior_salario})')
print(f'Funcionários com salário acima de R$ 2.000,00: {acima_2000}')

print('\nFeito por: Richard')