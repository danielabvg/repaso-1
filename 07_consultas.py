from ZODB import DB
from ZODB.FileStorage import FileStorage


storage = FileStorage("biblioteca.fs")

db = DB(storage)

connection = db.open()

root = connection.root()


# CONSULTA 1
# Mostrar todos los libros

print("\n--- LIBROS ---")

for libro in root.libros:
    print(
        libro.titulo,
        "-",
        libro.autor.nombre
    )


# CONSULTA 2
# Buscar un libro por título

titulo_buscar = "1984"

print("\n--- BÚSQUEDA ---")

for libro in root.libros:
    if libro.titulo == titulo_buscar:
        print(
            "Libro encontrado:",
            libro.titulo,
            "-",
            libro.autor.nombre
        )


# CONSULTA 3
# Mostrar únicamente libros disponibles

print("\n--- LIBROS DISPONIBLES ---")

for libro in root.libros:
    if libro.disponible:
        print(libro.titulo)


# CONSULTA 4
# Buscar libros publicados después del año 2000

print("\n--- LIBROS DESPUÉS DEL AÑO 2000 ---")

for libro in root.libros:
    if libro.anio > 2000:
        print(libro.titulo, "-", libro.anio)


connection.close()
db.close()