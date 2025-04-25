"""
Título de práctica: calculadora 2


Autor: Brayan Stiven Suarez Vargas 
Fecha: 2025-04-24
"""



def run():
    print("Calculadora básica")

    for _ in range(1000):  
        tipo_operacion = input("""
                Indique la operación a realizar:
             seleccione 1) Sumar
             seleccione 2) Restar
             seleccione 3) Multiplicar
             seleccione 4) Dividir
             seleccione 5) Potenciación
             seleccione 6) Módulo
             seleccione 7) Salir    
        """)

        if tipo_operacion == '7':
            print("Saliendo del programa.")
            break

        if tipo_operacion not in {'1', '2', '3', '4', '5', '6'}:
            print("Opción no válida. Intente de nuevo.")
            continue

        # Validar ingreso de números
        try:
            Operando_A = float(input("Ingrese el operando A: "))
            Operando_B = float(input("Ingrese el operando B: "))
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
            continue

         # Realizar operación
    if tipo_operacion == '1':
        resultado = Operando_A + Operando_B
        print(f"Resultado de la suma: {resultado}")
    elif tipo_operacion == 2:
        resultado = Operando_A - Operando_B
        print(f"Resultado de la resta: {resultado}")
    elif tipo_operacion == 3:
        resultado = Operando_A * Operando_B
        print(f"Resultado de la multiplicación: {resultado}")
    elif tipo_operacion == 4:
        resultado = Operando_A / Operando_B
        print(f"Resultado de la división: {resultado}")
    elif tipo_operacion == 5:
        resultado = Operando_A ** Operando_B
        print(f"Resultado de la potenciación: {resultado}")
    elif tipo_operacion == 6:
        resultado = Operando_A // Operando_B
        print(f"Resultado de la división entera: {resultado}")
    elif tipo_operacion == 7:
        resultado = Operando_A % Operando_B
        print(f"Resultado del módulo: {resultado}")


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
    

        
        
