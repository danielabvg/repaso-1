class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año:", self.anio)
        print()


# NO MODIFICAR
libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)

libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry",
    1943
)


# Tercer libro
libro3 = Libro(
    "1984",
    "George Orwell",
    1949
)


# Mostrar todos los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()


# Estado:
# Los valores actuales que tiene cada objeto.

# Propiedades:
# titulo, autor y anio.

# Comportamiento:
# El método mostrar_informacion().