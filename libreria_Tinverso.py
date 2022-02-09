
#TRIANGULO INVERSO
def trianguloInverso(num, i, var):
     return

print("*** Triangulo Inverso ****")
num = int(input("Introduce la altura del triángulo: "))

for var in reversed(range(0, num)):
    for i in range(0, num - var - 1):
        #espacios
        print(end=" ")
    for i in range(0, var + 1):
        print("*", end=" ")
    print()
