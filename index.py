import json

print("Que quiere hacer?")
print("1. Añadir estudiante")
print("2. Listar estudiantes")
print("3. Buscar estudiante por ID")
print("4. Salir")


def Cargar_Estudiantes():
    try:
        with open("estudiantes.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

lista_estudiantes = Cargar_Estudiantes()

def Añadir_Estudiante():

    id_estudiante = Generar_Id()
    nombre = Validar_Texto("Ingrese el nombre del estudiante: ")
    apellido = Validar_Texto("Ingrese el apellido del estudiante: ")

    while True:
        try:
            edad = int(input("Ingrese la edad: "))

            if 15 <= edad <= 100:
                break
            else:
                print("La edad debe estar entre 15 y 100")

        except ValueError:
            print("Debe ingresar un número entero")
    
    while True:
        try:
            semestre = int(input("Ingrese la semestre: "))

            if 1 <= semestre <= 10:
                break
            else:
                print("La edad debe estar entre 1 y 10")

        except ValueError:
            print("Debe ingresar un número entero")

    estudiante = {
        "id": id_estudiante,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "semestre": semestre
    }
    lista_estudiantes.append(estudiante)

    Guardar_Estudiantes()

    print(f"Estudiante Añadido: {estudiante}")

def Generar_Id():
    if not lista_estudiantes:
        return 1

    return max(e["id"] for e in lista_estudiantes) + 1

def Validar_Texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto and texto.replace(" ", "").isalpha():
            return texto
        else:
            print("Ingrese un texto válido, sin números.")

def Guardar_Estudiantes():
    with open("estudiantes.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_estudiantes, archivo, indent=4, ensure_ascii=False)

def Listar_Estudiantes():
    for estudiante in lista_estudiantes:
        print(estudiante)

def Buscar_Estudiante():
    id_list = []
    estudiante = None
    for estudiante in lista_estudiantes:
        estudiante_Id = estudiante["id"]
        id_list.append(estudiante_Id)
        
    while True:
        try:
            id = int(input("Escriba el id del estudiante: "))
            if id in id_list:
                break
            else:
                print("registro no encontrado")
        except ValueError:
                    print("Debe ingresar un número entero")

    for buscado in lista_estudiantes:
        if buscado["id"] == id:
            estudiante = buscado
            break
    return estudiante
    
        

while True:
    try:
        opcion = int(input("Ingrese una opcion: "))

        if 1 <= opcion <=4:
            break
        else:
            print("Elija una opcion entre 1 y 4")
    except ValueError:
        print("Debe ingresar un número entero")


if opcion == 1:
    print("Añadir un estudiante")
    Añadir_Estudiante()
elif opcion == 2:
    print("Listar estudiantes")
    Listar_Estudiantes()
elif opcion == 3:
    print("Buscar estudiante por ID")
    print(Buscar_Estudiante())
elif opcion == 4:
    print("Salir")

