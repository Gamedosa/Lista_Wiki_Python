# Faça um Programa que peça as 4 notas bimestrais e mostre a média.


soma_notas = 0
for nota in range(4):
    nota = float(input("Informe a sua nota :"))
    soma_notas  += nota
media = soma_notas / 4
print(f"A sua média é : {media}")

