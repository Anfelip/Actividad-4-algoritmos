import json
def Cargar_Estudiantes():
    try:
        with open("estudiantes.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

print(Cargar_Estudiantes()[1])