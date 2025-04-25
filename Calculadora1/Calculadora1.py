"""
Título de práctica: calculadora 1

Autor: Brayan Stiven Suarez Vargas <bssuarezv@academia.usbbog.edu.co>
Fecha: 2025-04-24
"""



def run():
    """script entrypoint"""

numero_1 = int(input("Ingresa el numero 1 : "))
numero_2 = int(input("Ingresa el numero 2 : "))
operacion = int(input("""Cual operación se va a realizar? 
 Escriba 1 para suma, 
         2 para resta, 
         3 para multiplicación 
         4 para división.: """))




def operaciones(operacion:int,numero_1:int, numero_2:int):
    
    resultado = "pusiste mal el numero"

    if operacion == 1:
        resultado = numero_1 + numero_2
    elif  operacion == 2:
        resultado = numero_1 - numero_2
    elif operacion == 3:
        resultado = numero_1 * numero_2 
    elif operacion == 4:
        resultado = numero_1 / numero_2
    else:
        resultado
    return resultado
         
print(operaciones(operacion, numero_1, numero_2))
        
        

# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()

