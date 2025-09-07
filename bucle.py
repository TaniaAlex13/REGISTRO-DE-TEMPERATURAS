# Registro de Temperaturas con una Matriz 3D (4 semanas)

# Nomenclatura de la matriz 3D:
# temperaturas[ciudad][semana][día]
# - ciudad -> 1 = Quito, 2 = Latacunga, 3 = Puyo
# - semana -> 1 = Semana 1, 2 = Semana 2, 3 = Semana 3, 4 = Semana 4
# - día    -> 1 = Lunes, 2 = Martes, 3 = Miercoles, 4 = Jueves, 5 = Viernes, 6 = Sabado, 7 = Domingo

# Lista de ciudades
ciudades = ["Quito", "Latacunga", "Puyo"]

# Lista de días para mostrar nombres
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# MATRIZ 3D (ciudad x semana x día)

temperaturas = [
    [   # Ciudad 1: Quito
        [20, 21, 19, 18, 22, 20, 21],  # Semana 1
        [19, 20, 18, 21, 20, 22, 19],  # Semana 2
        [21, 22, 20, 19, 23, 21, 22],  # Semana 3
        [20, 21, 19, 20, 22, 21, 23]   # Semana 4
    ],
    [   # Ciudad 2: Latacunga
        [15, 16, 14, 15, 17, 16, 15],  # Semana 1
        [16, 15, 14, 16, 17, 15, 16],  # Semana 2
        [15, 17, 16, 15, 18, 16, 17],  # Semana 3
        [16, 16, 15, 17, 16, 17, 16]   # Semana 4
    ],
    [   # Ciudad 3: Puyo
        [25, 26, 27, 26, 25, 24, 26],  # Semana 1
        [26, 27, 25, 26, 27, 26, 25],  # Semana 2
        [27, 28, 26, 27, 28, 27, 26],  # Semana 3
        [26, 27, 28, 26, 27, 26, 27]   # Semana 4
    ]
]
# RECORRER LA MATRIZ 3D

for i, ciudad in enumerate(ciudades, start=1):  # ciudades desde 1
    print(f"\nCiudad {i}: {ciudad}")
    for j, semana in enumerate(temperaturas[i-1], start=1):  # semanas desde 1
        promedio = sum(semana) / len(semana)
        print(f"  Semana {j}: Promedio = {promedio:.2f} °C")
        for k, temp in enumerate(semana, start=1):  # días desde 1
            print(f"    Día {k} ({dias_semana[k-1]}): {temp} °C")
