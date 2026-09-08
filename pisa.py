"""
Simulador de examen de cultura general de videojuegos
El programa arroja ciertas preguntas al usuario de manera aleatoria
y si el usuario acierta o falla se le indica despues de cada pregunta.
Tambien se le indica cuantos puntos gano y cuantos puntos lleva hasta el momento
"""

"""
================== funciones de preguntas  =====================================
"""

def pregunta_mario(respuesta):
    """
    (uso de condicionales, funciones y operadores)
    recibe: respuesta del usuario como cadena de texto
    comprueba si la respuesta del usuario es 1985
    devuelve: 1 si la respuesta es correcta y 0 si es incorrecta
    """
    if (respuesta == "1985"):
        return 1
    else:
        return 0


def pregunta_zelda(respuesta):
    """
    (uso de condicionales, funciones y operadores)
    recibe: respuesta del usuario como cadena de texto
    comprueba si la respuesta del usuario es Link
    devuelve: 1 si la respuesta es correcta y 0 si es incorrecta
    """
    if (respuesta == "Link"):
        return 1
    else:
        return 0


def puntuacion(puntos1, puntos2):
    """
    (uso de funciones, parametros y operadores)
    recibe: puntos1 y puntos2 como valores numericos
    suma los puntos obtenidos en las dos preguntas
    devuelve: puntuacion total del usuario
    """
    total = puntos1 + puntos2
    return total


"""
================== parte principal del programa =============================
"""

print("¿En qué año se lanzó Super Mario Bros.?")
respuesta1 = input()

puntos1 = pregunta_mario(respuesta1)

print("¿Cuál es el nombre del protagonista de The Legend of Zelda?")
respuesta2 = input()

puntos2 = pregunta_zelda(respuesta2)

total = puntuacion(puntos1, puntos2)

print("Tu puntuación final es:", total, "de 2")
