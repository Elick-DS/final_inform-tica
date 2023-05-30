
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("CARGANDO...")
except Exception as e:
    print(e)

mydb = client["informatica1"]
mycol = mydb["Equipos"]
myres = mydb["responsables"]
myubi = mydb["ubicaciones"]

def ingresar_ubicacion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  

    codigo_ubicacion = str(random.randint(100, 999))
    print("--------------------------------------------------")
    print(f"El código de ubicación asignado es: {codigo_ubicacion}")
    
    while True:
        nombre = input("Ingresa el nombre de la ubicación: ")
        if nombre.strip() and nombre.isalpha():
            break
        else:
            print("El nombre de la ubicación no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        while True:
            bloque = input("Ingrese el bloque en el que se encuentra el dispositivo (1-5): ")
            if bloque.strip() and bloque.isnumeric() and 1 <= int(bloque) <= 5:
                break
            else:
                print("El bloque debe ser un número entre 1 y 5. Inténtelo nuevamente.")

        while True:
            piso = input("Ingresa el piso en el que se encuentra el dispositivo (1-10): ")
            if piso.strip() and piso.isnumeric() and 1 <= int(piso) <= 10:
                break
            else:
                print("El piso debe ser un número entre 1 y 10. Inténtelo nuevamente.")

        bp = f"B{bloque}P{piso}"
        break
    
    while True:
        telefono = input("Ingresa el teléfono de la ubicación: ")
        if telefono.strip() and telefono.isalnum() and 8 <= int(piso) <= 10:
            break
        else:
            print("--------------------------------------------------")
            print("El número de teléfono no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 8 o más de 10 caracteres. Inténtelo nuevamente.")
    print("--------------------------------------------------")
    
    ubicacion = {
        "codigo": codigo_ubicacion,
        "nombre": nombre,
        "bp": bp,
        "telefono": telefono
    }
    
    try:
        ubicaciones_collection.insert_one(ubicacion)
        print("--------------------------------------------------")
        print("Ubicación ingresada de forma satisfactoria.")
        print("--------------------------------------------------")
    except Exception as e:
        print("--------------------------------------------------")
        print(f"Ha ocurrido un error al ingresar la ubicación: {str(e)}")
        print("--------------------------------------------------")


def actualizar_ubicacion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    print("--------------------------------------------------")
    codigo = input("Ingresa el código de ubicación a actualizar: ")
    nombre = input("Ingresa el nuevo nombre de la ubicación: ")
    while True:
        while True:
            bloque = input("Ingrese el bloque en el que se encuentra el dispositivo (1-5): ")
            if bloque.strip() and bloque.isnumeric() and 1 <= int(bloque) <= 5:
                break
            else:
                print("El bloque debe ser un número entre 1 y 5. Inténtelo nuevamente.")

        while True:
            piso = input("Ingresa el piso en el que se encuentra el dispositivo (1-10): ")
            if piso.strip() and piso.isnumeric() and 1 <= int(piso) <= 10:
                break
            else:
                print("El piso debe ser un número entre 1 y 10. Inténtelo nuevamente.")

        bp = f"B{bloque}P{piso}"
        break
    telefono = input("Ingresa el nuevo teléfono de la ubicación: ")
    print("--------------------------------------------------")
    
    try:
        ubicaciones_collection.update_one(
            {"codigo": codigo},
            {"$set": {"nombre": nombre, "bp": bp, "telefono": telefono}}
        )
        print("--------------------------------------------------")
        print("La ubicación ha sido actualizada.")
        print("--------------------------------------------------")
    except Exception as e:
        print(f"Ha ocurrido un error al actualizar la ubicación: {str(e)}")



def buscar_ubicacion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    print("--------------------------------------------------")
    codigo = input("Ingresa el código de ubicación a buscar: ")
    print("--------------------------------------------------")
    
    ubicacion = ubicaciones_collection.find_one({"codigo": codigo})
    
    if ubicacion:
        print("--------------------------------------------------")
        print("Ubicación encontrada:")
        print("codigo:", ubicacion["codigo"])
        print("nombre:", ubicacion["nombre"])
        print("bp:", ubicacion["bp"])
        print("telefono:", ubicacion["telefono"])
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("No se pudo encontrar ninguna ubicación con el código brindado.")
        print("--------------------------------------------------")




def ver_ubicaciones():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    
    ubicaciones = ubicaciones_collection.find()
    
    print("Ubicaciones:")
    for ubicacion in ubicaciones:
        print("--------------------------------------------------")
        print("codigo:", ubicacion["codigo"])
        print("nombre:", ubicacion["nombre"])
        print("Bloque y piso", ubicacion["bp"])
        print("telefono:", ubicacion["telefono"])
        print("--------------------------------------------------")
        




def eliminar_ubicacion():
    
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    print("--------------------------------------------------")
    codigo = input("Ingresa el código de ubicación a eliminar: ")
    print("--------------------------------------------------")
    
    try:
        ubicaciones_collection.delete_one({"codigo": codigo})
        print("--------------------------------------------------")
        print("Ubicación eliminada de forma satisfactoria.")
        print("--------------------------------------------------")
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar la ubicación: {str(e)}")




