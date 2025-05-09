

import sqlite3

# Conexión y creación de tabla

conn = sqlite3.connect("alumnos.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    correo TEXT NOT NULL)
""")

conn.commit()



# Funciones principales

def agregar_estudiante(nombre1, edad2, correo3):
    cursor.execute("INSERT INTO estudiantes (nombre, edad, correo) VALUES (?, ?, ?)",
        (nombre1, edad2, correo3))

def mostrar_estudiantes():

    cursor.execute("""SELECT * FROM estudiantes""")

    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

def buscar_por_nombre(nombre):
    cursor.execute("SELECT * FROM estudiantes WHERE nombre = ?", (nombre,))
    estudiantes = cursor.fetchall()
    for estudiante in estudiantes:
        print(estudiante)

def validar_correo(correo):
    es_correcto = True
    validador = correo.split('@')

    if len(validador) > 2:
        es_correcto = False
        print("CORREO INVALIDO \n Existen dos @")
    else:

        if len(validador) > 1:
            print(f"si cuenta con el arroba(validador)")
        else:
            es_correcto = False
            print("correo no valido, por favor poner el arroba")

        nombreCorreo = validador[0]
        if nombreCorreo.startswith('.') or nombreCorreo.endswith('.'):
            es_correcto = False
            print("Error, no puede iniciar o terminar con '.'")

        caracteresNoPermitidos = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '=', '{', '}', '[', ']', '\\', '/', '<',
                                  '>', '?', ';', ':', '"', "'", ',', '|', '~', '`']
        for caracter in caracteresNoPermitidos:

            if caracter in correo:
                es_correcto = False
                print("caracter: " + caracter)
                print("Contiene caracteres no permitidos")

    return es_correcto

######################################################################

while True:

    print("\n1. Agregar estudiante\n"
          "2. Mostrar todos\n"
          "3. Buscar por nombre\n"
          "4. Salir")

    op = input("Elige una opción: ")

    if op == '1':
        nombre = input("Nombre: ")
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad inválida.")
            continue

        correo = input("Correo: ")
        correo_validado = validar_correo(correo)

        if correo_validado == True:
            agregar_estudiante(nombre, edad, correo)
        else:
            print("Correo invalido")

    elif op == '2':

        mostrar_estudiantes()

    elif op == '3':

        nombre = input("Nombre a buscar: ")

        buscar_por_nombre(nombre)

    elif op == '4':

        break

    else:

        print("Opción no válida.")



# Cierre de conexión

conn.close()

