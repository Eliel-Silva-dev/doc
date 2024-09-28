nota01 = 7
nota02 = 8
nota03 = 9

media = int((nota01 + nota02 + nota03) / 3)

if(media >= 7):
    print("Aprovado")
elif(media >= 5) and (media < 7): # (else if)
    print("Recuperação")
else:
    print('Reprovado')
    print('Boa sorte na proxima')