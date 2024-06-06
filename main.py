from funciones import *

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del archivo.CSV: ")
            nombre_archivo = f"{nombre}.CSV"
            lista = leer_archivo(nombre_archivo)
        elif opcion == "2":
            imprimir_lista(lista)
        elif opcion == "3":
            lista = asignar_rating(lista)
            imprimir_lista(lista)
        elif opcion == "4":
            lista = asignar_genero(lista)
            imprimir_lista(lista)
        elif opcion == "5":
            genero = input("Ingrese el género a filtrar: ")
            lista_filtrada = filtrar_por_genero(lista, genero)
            nombre_archivo = f"{genero}.csv"
            guardar_archivo(lista_filtrada, nombre_archivo)
            print(f"Archivo {nombre_archivo} generado correctamente")
        elif opcion == "6":
            lista_ordenada = ordenar_peliculas(lista)
            imprimir_lista(lista_ordenada)
        elif opcion == "7":
            informar_mejor_rating(lista)
        elif opcion == "8":
            nombre = input("Ingrese el nombre del archivo JSON a generar: ")
            nombre_archivo = f"{nombre}.JSON"
            guardar_archivo(lista, nombre_archivo)
            print(f"Archivo {nombre_archivo} generado correctamente")
        elif opcion == "9":
            break
        else:
            print("Opción inválida")

main()