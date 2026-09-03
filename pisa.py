"""
Simulador de examen de cultura general de videojuegos
El programa arroja ciertas preguntal al usuario de manera aleatoria
y si el usuario acierta o falla se le indica despues de cada pregunta.
Tambien se le indica cuantos puntos gano y cuantos puntos lleva hasta el momento
"""

"""
================== ronda de preguntas  =====================================
"""

puntos = 0

respuesta = input("¿En qué año salió Super Mario Bros.? ")

if respuesta == "1985":
    puntos += 1
    print("¡Correcto! +1 punto")
else:
    print("Incorrecto.")

print("Puntuación:", puntos)
