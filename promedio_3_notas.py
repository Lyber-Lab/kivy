#Promedio de tres notas para la próxima clase en python
"""

print("Ingresa las tres notas para calcular el promedio:\n")
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es de: {promedio:.2f}")

"""
def calcular_promedio():
    print("----Calculador de Promedio----\n")
    notas =[]
    while True:
        try:
            cantidad = int(input("Ingresa en numeros enteros la cantidad de notas que vas a calcular: "))
            if cantidad > 0:
                for i in range(cantidad):
                    while True:
                        try:
                            nota = float(input(f"\nIngrese la nota {i+1} a calcular de (0-20) y usa el punto para el decimal: "))
                            if 0 <= nota <= 20:
                                notas.append(nota)
                                break
                            else:
                                print("\nPor favor introduce una nota en el rango de 0 a 20")
                        except ValueError:
                            print("\nDebes de ingresar una nota valida")
                promedio = sum(notas) / len(notas)
                print(f"El promedio de las notas es de: {promedio:.2f}")
                notas.clear()
                break
        except ValueError:
            print("Ingresa el numero de notas que vas a calcular de manera valida debe de ser mayor a 0")

if __name__ == "__main__":
    calcular_promedio()


        

