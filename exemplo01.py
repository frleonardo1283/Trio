import os 
os.system("cls")

print("feito por: leo")
print("R.A: 676767")
os.system("cls")

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
os.system("cls")

print("\n" + "=" * 25)
print("       RESULTADOS")
print("=" * 25)
print(f"Ordem original : {numeros}")
print("-" * 25)
print(f"Ordem inversa  : {numeros[::-1]}")
print("=" * 25)

nome = 'cls'