tupla1=(1,2,3)
tupla2=(4,5,6)
       

# print(tupla1*tupla2)
resultado=[0]*(len(tupla2))
for i in range(3):
    resultado[i]=tupla1[i]*tupla2[i]
   
tuple_resultado=tuple(resultado)    
print(tuple_resultado)
