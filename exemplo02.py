import os
os.system("cls")
print("feito por: Guilherme Barbosa ")
print("R.A: 4267 ")

vetor_temperatura = []
temperatura_max = 0
temperatura_min = 0

TEMPERATURA = 7

for i in range(TEMPERATURA):
    temperatura = float(input(f"digite a {i+1}ª temperatura da semana:"))
    vetor_temperatura.append(temperatura)
    media = sum(vetor_temperatura)/7
    temperatura_max = max(temperatura_max, temperatura)
    temperatura_min = min(temperatura_min, temperatura)

print(f"média da semana: {media}.")
print(f"a maior temperatura: {temperatura_max}.")
print(f"a menor temperatura: {temperatura_min}")

