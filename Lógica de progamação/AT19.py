peso = float (input("Digite seu peso"))
alt = float (input("Digite sua altura"))
media = peso/ (alt*alt)
if media<18.6:
    print("Abaixo do peso")
elif media<25:
    print("Peso Normal")
elif media<30:
    print("Sobrepeso")
else:
    print("Obesidade")