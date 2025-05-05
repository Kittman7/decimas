#Playlist
duracion = float(input("Duración de la canción (min): "))
genero = input("Género de la canción: ")
año = float(input("Año de lanzamiento: "))

if 2 <= duracion <= 4 and genero in ["rock", "pop", "trap"] and año >= 2010:
    print("¡La canción es perfecta para tu playlist!")
else:
    print("La canción no cumple con los requisitos.")