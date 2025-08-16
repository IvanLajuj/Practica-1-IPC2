import random
import string

# ===== Clase base =====
class MaterialBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.codigo = self.generar_codigo()
        self.estado = "Disponible"

    def generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def prestar(self):
        if self.estado == "Prestado":
            print(f"⚠ El material '{self.titulo}' ya está prestado.")
        else:
            self.estado = "Prestado"
            print(f"✅ Material '{self.titulo}' prestado con éxito.")

    def devolver(self):
        if self.estado == "Disponible":
            print(f"⚠ El material '{self.titulo}' no está prestado.")
        else:
            self.estado = "Disponible"
            print(f"✅ Material '{self.titulo}' devuelto con éxito.")

    def mostrar_info(self):
        print(f"📚 Código: {self.codigo}")
        print(f"   Título: {self.titulo}")
        print(f"   Autor: {self.autor}")
        print(f"   Estado: {self.estado}")

# ===== Subclase Libro Físico =====
class LibroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self.numero_ejemplar = numero_ejemplar
        self.max_dias_prestamo = 7

    def mostrar_info(self):
        super().mostrar_info()
        print(f"   N° Ejemplar: {self.numero_ejemplar}")
        print(f"   Días máximo de préstamo: {self.max_dias_prestamo}\n")

# ===== Subclase Libro Digital =====
class LibroDigital(MaterialBiblioteca):
    def __init__(self, titulo, autor, tamano_mb):
        super().__init__(titulo, autor)
        self.tamano_mb = tamano_mb
        self.max_dias_prestamo = 3

    def mostrar_info(self):
        super().mostrar_info()
        print(f"   Tamaño del archivo: {self.tamano_mb} MB")
        print(f"   Días máximo de préstamo: {self.max_dias_prestamo}\n")

# ===== Gestión de Biblioteca =====
class Biblioteca:
    def __init__(self):
        self.materiales = []

    def registrar_material(self):
        print("\n--- Registrar Material ---")
        tipo = input("¿Tipo de material? (1: Libro Físico, 2: Libro Digital): ")

        titulo = input("Título: ")
        autor = input("Autor: ")

        if tipo == "1":
            numero_ejemplar = input("Número de ejemplar: ")
            material = LibroFisico(titulo, autor, numero_ejemplar)
        elif tipo == "2":
            tamano = input("Tamaño del archivo (MB): ")
            material = LibroDigital(titulo, autor, tamano)
        else:
            print("❌ Opción inválida.")
            return

        self.materiales.append(material)
        print(f"✅ '{titulo}' registrado con éxito.")

    def mostrar_materiales(self):
        print("\n--- Lista de Materiales ---")
        if not self.materiales:
            print("No hay materiales registrados.")
            return
        for i, material in enumerate(self.materiales, start=1):
            print(f"{i}. {material.titulo} ({material.estado})")

    def prestar_material(self):
        self.mostrar_materiales()
        if not self.materiales:
            return
        opcion = int(input("Seleccione el número de material a prestar: ")) - 1
        if 0 <= opcion < len(self.materiales):
            self.materiales[opcion].prestar()
        else:
            print("❌ Selección inválida.")

    def devolver_material(self):
        self.mostrar_materiales()
        if not self.materiales:
            return
        opcion = int(input("Seleccione el número de material a devolver: ")) - 1
        if 0 <= opcion < len(self.materiales):
            self.materiales[opcion].devolver()
        else:
            print("❌ Selección inválida.")

    def consultar_info(self):
        self.mostrar_materiales()
        if not self.materiales:
            return
        opcion = int(input("Seleccione el número de material para ver información: ")) - 1
        if 0 <= opcion < len(self.materiales):
            print()
            self.materiales[opcion].mostrar_info()
        else:
            print("❌ Selección inválida.")

# ===== Menú principal =====
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== Menú Biblioteca =====")
        print("1. Registrar Material")
        print("2. Prestar Material")
        print("3. Devolver Material")
        print("4. Consultar Información")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.registrar_material()
        elif opcion == "2":
            biblioteca.prestar_material()
        elif opcion == "3":
            biblioteca.devolver_material()
        elif opcion == "4":
            biblioteca.consultar_info()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida.")

# Ejecutar
if __name__ == "__main__":
    menu()
    