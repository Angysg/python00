#Boletin1

'''
#1. Escribe un programa que pregunte el nombre y después de que el usuario lo introduzca muestre por pantalla las cadenas
#  ¡Hola <nombre>! - Me alegro de conocerle, <nombre>  donde <nombre> es el nombre que el usuario haya introducido.

 a = input("¿Cómo te llamas?")
 print(f"¡Hola {a}!, me alegro de conocerte.")

'''


'''
#2. Escribe un programa que pregunte el nombre y después de que el usuario lo introduzca muestre por pantalla el nombre en mayúsculas
# y el número de caracteres que tiene. Después deberá escribir el nombre tantas veces como letras contiene el nombre en líneas distintas.

a = input("¿Cómo te llamas?")
print(a.upper())
print(len(a))

#Guardamos la longitud del nombre en una variable
b=len(a)
x = 1
while x <= b:
    print(a)
    x+=1

'''


'''
# 3. Escribe los números pares del 2 hasta un número que se pida por teclado previamente.

numero = int(input("¿Introduce un número?: ")) 

#Al ser numeros pares, x%2==0. CUIDADO con las lineas del while y del if al no tener {}.
x=1
while x <= numero:
    if x % 2==0:
        print(x)
    x+=1
'''


'''
#4. Escribe un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=float(input("Dime tu peso en kg: "))
estatura=float(input("Dime tu altura en metros:"))

#Formula de imc=peso/altura elevado a 2
imc=peso/pow(estatura,2)
#Tambien se puede poner asi: imc=peso/(altura**2)

#Se rerondea con round
imc_redondeado=round(imc,2)

print(f"Tu índice de masa corporal es {imc_redondeado}")

'''



#5. Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta  
# o no es correcta, y en este caso escribir la correcta.

import random

#Generar dos números aleatorios.
x=random.randrange(2,10)
y=random.randrange(2,10)

#Calculo la multiplicacion de ambos numeros
multiplicacion=x*y

#Pregunto al usuario
respuesta_usuario=int(input(f"¿Cuánto es {x} x {y}?"))

#Veo si es correcto o no
if respuesta_usuario==multiplicacion:
    print("¡Correcto!")
else:
    print(f"No es correcto. La respuesta correcta es: {multiplicacion}")
