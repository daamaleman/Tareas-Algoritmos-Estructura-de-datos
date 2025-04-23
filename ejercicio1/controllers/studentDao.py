from models.student import Estudiante
from models.lista_enlazada import ListaEnlazada
import random

def generar_estudiantes(n):
    nombres = ["Carlos", "Ana", "Luis", "Sofía", "Pedro", "Lucía"]
    apellidos = ["Martínez", "Gómez", "Ruiz", "Torres", "López", "Castro"]
    sexos = ["M", "F"]
    lista = ListaEnlazada()

    for i in range(n):
        carnet = f"U{random.randint(1000,9999)}"
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        peso = round(random.uniform(30, 70), 2)
        estatura = round(random.uniform(1.2, 1.8), 2)
        sexo = random.choice(sexos)
        promedio = round(random.uniform(60, 100), 2)
        estudiante = Estudiante(carnet, nombre, apellido, peso, estatura, sexo, promedio)
        lista.agregar(estudiante)
    
    return lista

def mostrar_lista(lista):
    actual = lista.cabeza
    while actual:
        e = actual.estudiante
        print(f"Carnet: {e.carnet}, Nombre: {e.nombres}, Apellido: {e.apellidos}, Peso: {e.peso}kg, Estatura: {e.estatura}m, Sexo: {e.sexo}, Promedio: {e.promedio}")
        actual = actual.siguiente
