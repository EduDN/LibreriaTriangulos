
#TRIANGULO EQUILATERO
def triangulo_equilatero(max, separacion, j, i, linea):
    return

print("***** Triángulo Equilatero ***** ")
import math
max=21
separacion=5
j=1
 
# creamos triangulo
for i in range(0,max,2):
   
    # ponemos los espacios
    linea=(separacion+math.ceil(max/2)-j)*" "
    
    # ponemos los asteriscos
    linea+=i*"*"
 
    j+=1
    print(linea)

