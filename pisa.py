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
    if (respuesta == "link"):
        return 1
    else:
        return 0

def pregunta_pokemon(respuesta):
    """
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es Pikachu.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "pikachu"):
        return 1
    else:
        return 0

def pregunta_minecraft(respuesta):
    """
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es Mojang.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "mojang"):
        return 1
    else:
        return 0

def pregunta_tetris(respuesta):
    """
    Recibe: la respuesta del usuario como cadena de texto.
    Hace: comprueba si la respuesta del usuario es 1984.
    Devuelve: 1 si la respuesta es correcta y 0 si es incorrecta.
    """
    if (respuesta == "1984"):
        return 1
    else:
        return 0

"""
Funcion para normalizar respuestas:
Recibe: una respuesta del usuario como cadena de texto.
Hace: elimina espacios innecesarios y convierte las letras a minusculas.
Devuelve: la respuesta limpia y normalizada.
"""
def normalizar_respuesta(respuesta):
    respuesta = respuesta.strip()
    respuesta = respuesta.lower()
    return respuesta

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
    ("¿Cuál es el nombre del Pokémon más conocido?", pregunta_pokemon),
    ("¿Qué empresa desarrolló Minecraft originalmente?", pregunta_minecraft),
    ("¿En qué año se lanzó Tetris?", pregunta_tetris)
]
respuestas = []
puntos_obtenidos = []
total = 0

# NUEVO AVANCE: solicitar el nombre del participante
nombre = input("Escribe tu nombre: ")

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
    [preguntas[2][0], "", 0],
    [preguntas[3][0], "", 0],
    [preguntas[4][0], "", 0]
]

"""
Ciclo for:
Recibe: el rango de 5 preguntas.
Hace: repite el proceso de mostrar una pregunta, recibir la respuesta,
comprobarla y actualizar la puntuacion.
Devuelve: no devuelve un valor; ejecuta las instrucciones del ciclo.
"""
for i in range(5):
    print(preguntas[i][0])
    respuesta = input()
    respuesta = normalizar_respuesta(respuesta)
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
print("Tu puntuación final es:", total, "de 5")

"""
Condicional final:
Recibe: el total de puntos obtenidos.
Hace: determina el mensaje que corresponde al resultado del usuario.
Devuelve: no devuelve un valor; muestra un mensaje de acuerdo
con la puntuacion final.
"""
if (total == 5):
    print("¡Excelente! Respondiste todas las preguntas correctamente.")
elif (total >= 3):
    print("Muy bien. Obtuviste una buena puntuación.")
elif (total >= 1):
    print("Bien, pero puedes mejorar.")
else:
    print("No obtuviste puntos esta vez. ¡Puedes volver a intentarlo!")

"""
Resumen de respuestas:
Recibe: la matriz de resultados.
Hace: recorre la matriz para mostrar la informacion de cada pregunta.
Devuelve: no devuelve un valor; presenta el resumen en pantalla.
"""
print("=== Resumen de tus respuestas ===")
for i in range(5):
    print("Pregunta:", matriz_resultados[i][0])
    print("Tu respuesta:", matriz_resultados[i][1])
    print("Puntos obtenidos:", matriz_resultados[i][2])

"""
Funcion de busqueda:
Recibe: una palabra y la matriz de resultados.
Hace: busca la palabra dentro del texto de las preguntas.
Devuelve: muestra las preguntas que contienen la palabra buscada.
"""
def buscar_pregunta(palabra, matriz):
    encontrado = 0
    palabra = palabra.strip().lower()
    for i in range(5):
        pregunta = matriz[i][0].lower()
        if (palabra in pregunta):
            print("Pregunta encontrada:", matriz[i][0])
            print("Tu respuesta:", matriz[i][1])
            print("Puntos obtenidos:", matriz[i][2])
            encontrado = 1
    if (encontrado == 0):
        print("No se encontraron preguntas con esa palabra.")

"""
Busqueda de preguntas:
Permite al usuario buscar una palabra dentro de las preguntas del examen.
"""
print()
print("=== Busqueda de preguntas ===")
palabra = input("Escribe una palabra para buscar en las preguntas: ")
buscar_pregunta(palabra, matriz_resultados)

"""
Funcion para guardar resultados:
Recibe: el nombre del participante, la matriz y la puntuacion final.
Hace: guarda los resultados del examen en un archivo de texto.
Devuelve: no devuelve un valor; escribe la informacion en el archivo.
"""
def guardar_resultados(nombre, matriz, total):
    archivo = open("resultados_examen.txt", "a", encoding="utf-8")
    archivo.write("====================================\n")
    archivo.write("Participante: " + nombre + "\n")
    archivo.write("Puntuacion final: " + str(total) + " de 5\n")
    archivo.write("Resultados de las preguntas:\n")
    for i in range(5):
        archivo.write("Pregunta: " + matriz[i][0] + "\n")
        archivo.write("Respuesta: " + matriz[i][1] + "\n")
        archivo.write("Puntos: " + str(matriz[i][2]) + "\n")
    archivo.write("====================================\n\n")
    archivo.close()
    print("Tus resultados se guardaron correctamente.")

"""
Funcion para cargar resultados:
Recibe: el nombre del archivo que contiene los resultados guardados.
Hace: abre y lee la informacion almacenada anteriormente.
Devuelve: muestra en pantalla el contenido del archivo.
"""
def cargar_resultados():
    try:
        archivo = open("resultados_examen.txt", "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        print()
        print("=== Resultados guardados anteriormente ===")
        print(contenido)
    except FileNotFoundError:
        print("Todavia no existen resultados guardados.")

"""
Guardar y cargar informacion:
Primero guarda los resultados del examen actual.
Despues carga y muestra todos los resultados almacenados.
"""
guardar_resultados(nombre, matriz_resultados, total)
cargar_resultados()
