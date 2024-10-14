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

# 3. Escribe los números pares del 2 hasta un número que se pida por teclado previamente.

numero = int(input("¿Introduce un número?: ")) 

#Al ser numeros pares, x%2==0. CUIDADO con las lineas del while y del if al no tener {}.
x=1
while x <= numero:
    if x % 2==0:
        print(x)
    x+=1
     