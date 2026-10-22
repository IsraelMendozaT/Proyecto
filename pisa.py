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
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es 1985.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "1985"):
        return 1
    else:
        return 0

def pregunta_zelda(respuesta):
    """
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es Link.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "Link"):
        return 1
    else:
        return 0

def pregunta_pokemon(respuesta):
    """
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es Pikachu.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "Pikachu"):
        return 1
    else:
        return 0

"""
=== parte principal del programa ===
"""

"""
Lista de preguntas:
Guarda el texto de cada pregunta y la funcion que comprueba
si la respuesta del usuario es correcta.
"""
preguntas = [
    ("¿En qué año se lanzó Super Mario Bros.?", pregunta_mario),
    ("¿Cuál es el nombre del protagonista de The Legend of Zelda?", pregunta_zelda),
    ("¿Cuál es el nombre del Pokémon más conocido?", pregunta_pokemon)
]

respuestas = []
puntos_obtenidos = []
total = 0

"""
Matriz de resultados:
Cada fila guarda los datos de una pregunta:
1. Texto de la pregunta.
2. Respuesta del usuario.
3. Puntos obtenidos.
Al principio, las respuestas y los puntos se guardan
como espacios vacios que se actualizaran durante el examen.
"""
matriz_resultados = [
    [preguntas[0][0], "", 0],
    [preguntas[1][0], "", 0],
    [preguntas[2][0], "", 0]
]

"""
Ciclo for:
Recibe: el rango de 3 preguntas.
Hace: repite el proceso de mostrar una pregunta, recibir la respuesta,
comprobarla y actualizar la puntuacion.
Devuelve: no devuelve un valor; ejecuta las instrucciones del ciclo.
"""
for i in range(3):
    print(preguntas[i][0])
    respuesta = input()
    respuestas.append(respuesta)
    puntos = preguntas[i][1](respuesta)
    total = total + puntos
    puntos_obtenidos.append(puntos)

    """
    Actualizacion de la matriz:
    Recibe: el indice de la pregunta, la respuesta y los puntos.
    Hace: guarda la respuesta y los puntos en la fila correspondiente.
    Devuelve: no devuelve un valor; actualiza los datos de la matriz.
    """
    matriz_resultados[i][1] = respuesta
    matriz_resultados[i][2] = puntos

    """
    Condicional de resultado:
    Recibe: los puntos obtenidos en la pregunta actual.
    Hace: determina si la respuesta fue correcta o incorrecta.
    Devuelve: no devuelve un valor; muestra el mensaje correspondiente.
    """
    if (puntos == 1):
        print("¡Correcto! Ganaste 1 punto.")
    else:
        print("Incorrecto. No ganaste puntos.")
    print("Puntos acumulados:", total)

print("Tu puntuación final es:", total, "de 3")

"""
Condicional final:
Recibe: el total de puntos obtenidos.
Hace: determina el mensaje que corresponde al resultado del usuario.
Devuelve: no devuelve un valor; muestra un mensaje de acuerdo
con la puntuacion final.
"""
if (total == 3):
    print("¡Excelente! Respondiste todas las preguntas correctamente.")
elif (total == 2):
    print("Muy bien. Respondiste dos preguntas correctamente.")
elif (total == 1):
    print("Bien, pero puedes mejorar. Respondiste una pregunta correctamente.")
else:
    print("No obtuviste puntos esta vez. ¡Puedes volver a intentarlo!")

"""
Resumen de respuestas:
Recibe: la matriz de resultados.
Hace: recorre la matriz para mostrar la informacion de cada pregunta.
Devuelve: no devuelve un valor; presenta el resumen en pantalla.
"""
print("=== Resumen de tus respuestas ===")

for i in range(3):
    print("Pregunta:", matriz_resultados[i][0])
    print("Tu respuesta:", matriz_resultados[i][1])
    print("Puntos obtenidos:", matriz_resultados[i][2])
