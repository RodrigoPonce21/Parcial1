import random

def direccion_archivo(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

def leer_archivo(nombre_archivo):
    with open(direccion_archivo(nombre_archivo), "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            id, titulo, genero, rating = linea
            pelicula["id"] = int(id)
            pelicula["titulo"] = titulo
            pelicula["genero"] = genero
            pelicula["rating"] = float(rating)
            lista.append(pelicula)
    return lista

def mostrar_menu():
    print("Menú:")
    print("1. Cargar archivo CSV")
    print("2. Imprimir lista")
    print("3. Asignar calificación")
    print("4. Asignar género")
    print("5. Filtrar por género")
    print("6. Ordenar películas")
    print("7. Informar Mejor Calificación")
    print("8. Guardar películas")
    print("9. Salir")

def guardar_archivo(lista, nombre_archivo):
    with open(direccion_archivo(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for pelicula in lista:
            values = list(pelicula.values())
            l = []
            for value in values:
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l)  + "\n"
            archivo.write(linea)

def imprimir_lista(lista):
    for pelicula in lista:
        print(f"{pelicula['id']}, {pelicula['titulo']}, {pelicula['genero']}, {pelicula['rating']}")

def asignar_valor_aleatorio(pelicula, campo, valores_posibles):
    if campo == "rating":
        pelicula[campo] = round(random.uniform(1, 10), 1)
    else:
        pelicula[campo] = random.choice(valores_posibles)
    return pelicula

def asignar_rating(lista):
    lista = list(map(lambda pelicula: asignar_valor_aleatorio(pelicula, "rating", []), lista))
    return lista

def asignar_genero(lista):
    generos = ["drama", "comedia", "acción", "terror"]
    lista = list(map(lambda pelicula: asignar_valor_aleatorio(pelicula, "genero", generos), lista))
    return lista

def filtrar_por_genero(lista, genero):
    lista_filtrada = [pelicula for pelicula in lista if pelicula["genero"] == genero]
    return lista_filtrada

def ordenar_peliculas(lista):
    lista_ordenada = sorted(lista, key=lambda x: (x["genero"], -x["rating"]))
    return lista_ordenada

def informar_mejor_rating(lista):
    pelicula_mejor_rating = max(lista, key=lambda x: x["rating"])
    print(f"La película con mejor rating es {pelicula_mejor_rating['titulo']} con un rating de {pelicula_mejor_rating['rating']}")

def escribir_json(lista, nombre_archivo):
    with open(direccion_archivo(nombre_archivo), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values: 
                if isinstance(value, int):
                    l.append(str(value))
                elif isinstance(value, float):
                    l.append(str(value))
                else:
                    l.append(value) 
            linea = ",".join(l)  + "\n"
            archivo.write(linea)
