import os
os.system('cls')

notas = []

for i in range(5):
    nota = float(input(f'Digite sua {i+1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

notas_acima = [n for n in notas if n > media]

print(f'Notas: {notas}')
print(f'media: {media}')
print(f'Acima da media: {notas_acima}')
