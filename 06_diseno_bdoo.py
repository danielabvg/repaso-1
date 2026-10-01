from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction


class Autor:

    def __init__(self, nombre):
        self.nombre = nombre


class Libro:

    def __init__(self, titulo, isbn, autor, anio):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anio = anio
        self.disponible = True


class Usuario:

    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.prestamos = PersistentList()


class Prestamo:

    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha


# AUTORES

autor1 = Autor("George Orwell")
autor2 = Autor("Gabriel García Márquez")
autor3 = Autor("Antoine de Saint-Exupéry")


# LIBROS

libro1 = Libro(
    "1984",
    "9780451524935",
    autor1,
    1949
)

libro2 = Libro(
    "Rebelión en la granja",
    "9780451526342",
    autor1,
    1945
)

libro3 = Libro(
    "Cien años de soledad",
    "9780307474728",
    autor2,
    1967
)

libro4 = Libro(
    "El principito",
    "9780156012195",
    autor3,
    1943
)

libro5 = Libro(
    "El amor en los tiempos del cólera",
    "9780307389732",
    autor2,
    2007
)


# USUARIOS

usuario1 = Usuario("Daniela", "A001")
usuario2 = Usuario("Ana", "A002")
usuario3 = Usuario("Carlos", "A003")


# PRÉSTAMOS

prestamo1 = Prestamo(
    usuario1,
    libro1,
    "01/10/2026"
)

prestamo2 = Prestamo(
    usuario2,
    libro3,
    "01/10/2026"
)


# RELACIONES ENTRE OBJETOS

usuario1.prestamos.append(prestamo1)
usuario2.prestamos.append(prestamo2)

libro1.disponible = False
libro3.disponible = False


# BASE DE DATOS

storage = FileStorage("biblioteca.fs")
db = DB(storage)
connection = db.open()
root = connection.root()


root.autores = PersistentList([
    autor1,
    autor2,
    autor3
])

root.libros = PersistentList([
    libro1,
    libro2,
    libro3,
    libro4,
    libro5
])

root.usuarios = PersistentList([
    usuario1,
    usuario2,
    usuario3
])

root.prestamos = PersistentList([
    prestamo1,
    prestamo2
])


transaction.commit()


print("Base de datos creada correctamente.")
print("Autores:", len(root.autores))
print("Libros:", len(root.libros))
print("Usuarios:", len(root.usuarios))
print("Préstamos:", len(root.prestamos))


connection.close()
db.close()