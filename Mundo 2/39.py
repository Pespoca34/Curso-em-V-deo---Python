from time import strftime, gmtime
ano = int(input("Digite seu ano de nascimento: "))
anoatual = int(strftime("%Y", gmtime()))
diff = anoatual - ano
anoalistamento = ano + 18
print(f"Em {anoatual} você tem {diff}")
if(diff < 18):
    print(f"Falta {19 - diff} anos para você se alistar")
elif(diff > 18):
    print(f"Você deveria ter se alistado há {anoatual - anoalistamento} anos")
else:
    print("Aliste-se \033[1;31;40mIMEDIATAMENTE\033[m")