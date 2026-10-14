"""
Simulador de examen de cultura general de videojuegos
El programa arroja ciertas preguntas al usuario.
Si el usuario acierta o falla se le indica despues de cada pregunta.
Tambien se le indica cuantos puntos gano y cuantos puntos lleva hasta
el momento.
"""

"""
=== funciones de preguntas ===
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


def pregunta_pokemon(respuesta):
    """
    (uso de condicionales, funciones y operadores)
    recibe: respuesta del usuario como cadena de texto
    comprueba si la respuesta del usuario es Pikachu
    devuelve: 1 si la respuesta es correcta y 0 si es incorrecta
    """
    if (respuesta == "Pikachu"):
        return 1
    else:
        return 0


"""
=== parte principal del programa ===
"""

preguntas = [
    ("¿En qué año se lanzó Super Mario Bros.?", pregunta_mario),
    ("¿Cuál es el nombre del protagonista de The Legend of Zelda?", pregunta_zelda),
    ("¿Cuál es el nombre del Pokémon más conocido?", pregunta_pokemon)
]

# Lista para guardar las respuestas del usuario
respuestas = []

# Lista para guardar los puntos obtenidos en cada pregunta
puntos_obtenidos = []

total = 0

for i in range(3):
    print(preguntas[i][0])
    respuesta = input()

    # Guardar la respuesta del usuario en la lista
    respuestas.append(respuesta)

    puntos = preguntas[i][1](respuesta)
    total = total + puntos

    # Guardar los puntos obtenidos en la lista
    puntos_obtenidos.append(puntos)

    if (puntos == 1):
        print("¡Correcto! Ganaste 1 punto.")
    else:
        print("Incorrecto. No ganaste puntos.")

    print("Puntos acumulados:", total)

print("Tu puntuación final es:", total, "de 3")

if (total == 3):
    print("¡Excelente! Respondiste todas las preguntas correctamente.")
elif (total == 2):
    print("Muy bien. Respondiste dos preguntas correctamente.")
elif (total == 1):
    print("Bien, pero puedes mejorar. Respondiste una pregunta correctamente.")
else:
    print("No obtuviste puntos esta vez. ¡Puedes volver a intentarlo!")

# Mostrar las respuestas y los puntos guardados en las listas
print("Resumen de tus respuestas")

for i in range(3):
    print("Pregunta:", preguntas[i][0])
    print("Tu respuesta:", respuestas[i])
    print("Puntos obtenidos:", puntos_obtenidos[i])
