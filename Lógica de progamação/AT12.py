idade = int(input("digite sua idade"))

if idade > 0 and idade <13 :
    print("criança")
elif idade > 13 and idade <18:
    print("adolecente")
elif idade > 19 and idade < 60:
    print("adulto")
else:
    print("idoso")