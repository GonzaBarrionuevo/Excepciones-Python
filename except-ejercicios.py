#ejercicios con excepciones

#ej1
#Escribe un programa en Python que tome dos números enteros como entrada del usuario
#y realice la división del primero por el segundo. Si el segundo número es igual a cero,
#muestra un mensaje de error indicando que la división por cero no está permitida.

# def main():
#     try:
#         numero1 = int(input("Ingrese un numero: "))
#         numero2 = int(input("Ingrese otro numero: "))
#         resultado = numero1/numero2
#         print(f'El resutado de la division es: {resultado}')
#     except ZeroDivisionError as a:
#         print(a)
#     except TypeError as a:
#         print(a)
#     except ValueError as a:
#         print(a)
#     except Exception as a:
#         print(a)
# main()


#ej2
#Definir una función llamada mostrarVisitantes que lea el archivo prueba.txt y
#muestre en pantalla la lista de visitantes cargando un diccionario por cada registro,
#el diccionario debería verse con el siguiente formato:

#{ “dni”:12067539, “nombre”: “Oliver Pérez” }

# def mostrarVisitantes ():
#     try:
#         with open("nombreCarpeta\nombreArchivo", "r") as f:
#             datos = f.readlines()
#         lista = []

#         for dato in datos:
#             DNI, nombre = dato.strip().split(";")
#             lista.append({"DNI": DNI, "Nombre": nombre})
#         print(lista)
#     except FileNotFoundError:
#         print("No se encontro el archivo")
# mostrarVisitantes()