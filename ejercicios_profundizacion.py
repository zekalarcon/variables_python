#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"

def ej1():  
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
    print("Ingrese dos numeros para para saber el resultado de la suma")
    primer_numero = float(input())
    segundo_numero = float(input())

    suma = primer_numero + segundo_numero
    print("La suma entre los numeros", primer_numero, "y", segundo_numero, "es:", suma)

    print("Ingrese dos numeros para para saber el resultado de la resta")
    primer_numero = float(input())
    segundo_numero = float(input())

    resta = primer_numero - segundo_numero
    print("La resta entre los numeros", primer_numero, "y", segundo_numero, "es:", resta)

    print("Ingrese dos numeros para para saber el resultado de la multiplicacion")
    primer_numero = float(input())
    segundo_numero = float(input())

    multiplicacion = primer_numero * segundo_numero
    print("La multiplicacion entre los numeros", primer_numero, "y", segundo_numero, "es:", multiplicacion)

    print("Ingrese dos numeros para para saber el resultado de la division")
    primer_numero = float(input())
    segundo_numero = float(input())

    division = primer_numero / segundo_numero
    print("La division entre los numeros", primer_numero, "y", segundo_numero, "es:", division)

    print("Ingrese dos numeros para para saber el resultado de la potencia")
    primer_numero = float(input())
    segundo_numero = float(input())

    potencia = primer_numero ** segundo_numero
    print("La potencia con base", primer_numero, "y exponente", segundo_numero, "es:", potencia)




def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''

    print("Ingrese nombre completo")

    nombre_completo = str(input())
    nombre_completo = nombre_completo.title()

    print("Ingrese numero de DNI sin puntos")
    dni = int(input())
    
    print("Ingrese su edad")
    edad = int(input())

    print("Ingrese su altura")
    altura = float(input())

    print("Nombre completo:", nombre_completo, "DNI:", dni)
    print("Nombre completo:", nombre_completo, "Edad:", edad, "Altura:", altura)

def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''

    print("Ingrese nombre y apellido de su madre y padre")
    print("Nombre y apellido de la madre:")
    nombre_madre = str(input())
    nombre_madre, apellido_madre = nombre_madre.split(" ")
    print("Nombre y apellido del padre:")
    nombre_padre = str(input())
    nombre_padre, apellido_padre = nombre_padre.split(" ")
    print("Ingrese nombre del hijo:")
    nombre_hijo = str(input())
    nombre_completo_hijo = nombre_hijo + " " + apellido_madre + " " + apellido_padre
    print("Nombre completo del hijo:", nombre_completo_hijo.title())






def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''

    print("Ingrese nombre y apellido de una persona:")
    primer_persona = str(input())
    
    print("Ahora ingrese nombre y apellido de otra persona para saber si hay parentesco:")
    segunda_persona = str(input())
    nombre, apellido = segunda_persona.split(" ")

    parentesco = apellido in primer_persona

    print("Hay parentesco entre", primer_persona.title(), "y", segunda_persona.title(), "?", parentesco)




def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    print("Ingrese su nombre completo:")
    nombre_completo = str(input())
    print("Todo miniscula:", nombre_completo.lower())
    print("Todo mayuscula:", nombre_completo.upper())
    print("Primer letra mayuscula:", nombre_completo.capitalize())
    print("Primeras letras en mayusculas:", nombre_completo.title())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
