def dirigiroubeber(idade):
    if(idade>=18):
        return('já pode dirigir ou beber')
    elif(idade<18):
        return('não pode nem dirigir nem beber')
idade = (int(input('Qual sua idade ')))

print(dirigiroubeber(idade))