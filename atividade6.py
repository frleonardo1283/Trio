import os
os.system("cls")

print("Digite 5 números inteiros para o vetor A:")
A = []
for i in range(5):
    num = int(input(f"A[{i}]: "))
    A.append(num)

print("\nDigite 5 números inteiros para o vetor B:")
B = []
for i in range(5):
    num = int(input(f"B[{i}]: "))
    B.append(num)

C = []
for i in range(5):
    C.append(A[i] + B[i])

os.system("cls")

print("\n--- Resultados ---")
print(f"Vetor A: {A}")
print(f"Vetor B: {B}")
print(f"Vetor C (A + B): {C}")