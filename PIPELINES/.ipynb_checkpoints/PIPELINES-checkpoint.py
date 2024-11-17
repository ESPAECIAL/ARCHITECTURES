import random
from typing import Tuple
from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, IntSlider

# List of student names
studentNames = [
    "John Smith", "Emily Davis", "Michael Johnson", 
    "Sarah Wilson", "Chris Brown", "Anna Taylor",
    "David Anderson", "Jessica White"
]

# Define the 3x3 grid coordinates, excluding the center (1, 1)
coordinates = [
    (0, 0), (0, 1), (0, 2),
    (1, 0),         (1, 2),
    (2, 0), (2, 1), (2, 2)
]

# Create the dictionary with student names and their coordinates
estudiantes = {
    "John Smith": (0, 0),
    "Emily Davis": (0, 1),
    "Michael Johnson": (0, 2),
    "Sarah Wilson": (1, 0),
    "Chris Brown": (1, 2),
    "Anna Taylor": (2, 0),
    "David Anderson": (2, 1),
    "Jessica White": (2, 2)
}

@dataclass
class Estudiante:
    nombre: str
    coordenadas: Tuple[int, int]
    saludAceptable: bool = random.choice([True, False])

# Functions operate on Estudiante objects
def estudianteAEstudiar(estudiante: Estudiante, climaAceptable: bool) -> bool:
    return estudiante.saludAceptable and climaAceptable

def rest(estudiante: Estudiante):
    estudiante.saludAceptable = True

def estudianteAEscuela(estudiante: Estudiante):
    estudiante.coordenadas = (1, 1)  # School coordinates

# Create a list of Estudiante objects
estudiantes_list = [Estudiante(nombre=nombre, coordenadas=coordenadas) for nombre, coordenadas in estudiantes.items()]

# Function to plot the students and the school
def plot_students(step: int):
    plt.figure(figsize=(6, 6))
    plt.xlim(-1, 3)
    plt.ylim(-1, 3)
    plt.xticks(range(3))
    plt.yticks(range(3))
    plt.grid(True)
    plt.title("Movimiento de Estudiantes a la Escuela")

    # Plot the school
    plt.plot(1, 1, 'ro', markersize=10, label='Escuela')

    # Plot the students
    for estudiante in estudiantes_list:
        if step == 0:
            plt.plot(estudiante.coordenadas[0], estudiante.coordenadas[1], 'bo', markersize=5, label=estudiante.nombre)
        else:
            climaAceptable = random.choice([True, False])
            if estudianteAEstudiar(estudiante, climaAceptable):
                estudianteAEscuela(estudiante)
            else:
                rest(estudiante)
            plt.plot(estudiante.coordenadas[0], estudiante.coordenadas[1], 'bo', markersize=5, label=estudiante.nombre)

    plt.legend()
    plt.show()

# Ensure interactive mode for matplotlib
plt.ion()

# Interactive slider to show the movement
def __main__():
    interact(plot_students, step=IntSlider(min=0, max=1, step=1, description='Paso:'))

__main__()