
                                          # Factorial con recursividad

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n-1)

# numero = int(input("Ingrese el numero:"))

# if numero < 0:
#     print("No se puede ingresar numeros negativos, ingrese un numero mayor o igual a 0")
# elif numero == 0:
#     print("El factorial de 0 es 1")
# else:
#     print("El factorial del ", numero, "es: " ,factorial(numero))



                                        #Factorial sin recursividad1

# numero=int(input("Por favor introduzca un numero: "))
# factorial=1
# while(numero>0):
#     factorial=factorial*numero
#     numero=numero-1
#     print("El factorial del numero es:", factorial)





                                       #Fibonacci con recursividad

# def fibonacci(cant):
#     if(cant <=1):
#            return cant
#     else: 
#         return(fibonacci(cant-1) + fibonacci(cant-2))
# cant = int(input("Ingrese la cantidad de numeros: "))
# print("Secuencia Fibonacci")
# for i in range(cant):
#     print(fibonacci(i))       



            
                                  #Fibonacci sin recursividad

numero1 = int(input("Por favor ingrese el primer numero: "))
numero2  = int(input("Por favor ingrese el segundo numero: "))
cant = int(input("Por favor ingrese la cantidad de numeros: "))
print(numero1,numero2,end=" ")

while(cant-2):

    result=numero1+numero2
    numero1=numero2
    numero2=result
    print(result,end=" ")
    cant=cant-1