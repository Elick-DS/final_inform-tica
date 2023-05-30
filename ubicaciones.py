
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
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
    
    codigo = input("Ingresa el código de ubicación: ")
    nombre = input("Ingresa el nombre de la ubicación: ")
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
    telefono = input("Ingresa el teléfono de la ubicación: ")
    
    ubicacion = {
        "codigo": codigo,
        "nombre": nombre,
        "bp": bp,
        "telefono": telefono
    }
    
    try:
        ubicaciones_collection.insert_one(ubicacion)
        print("Ubicación ingresada de forma satisfactoria.")
    except Exception as e:
        print(f"Ha ocurrido un error al ingresar la ubicación: {str(e)}")


def actualizar_ubicacion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    
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
    
    try:
        ubicaciones_collection.update_one(
            {"codigo": codigo},
            {"$set": {"nombre": nombre, "bp": bp, "telefono": telefono}}
        )
        print("La ubicación ha sido actualizada.")
    except Exception as e:
        print(f"Ha ocurrido un error al actualizar la ubicación: {str(e)}")



def buscar_ubicacion():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.informatica1
    ubicaciones_collection = db.ubicaciones  
    
    codigo = input("Ingresa el código de ubicación a buscar: ")
    
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
        print("No se pudo encontrar ninguna ubicación con el código brindado.")




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
    
    codigo = input("Ingresa el código de ubicación a eliminar: ")
    
    try:
        ubicaciones_collection.delete_one({"codigo": codigo})
        print("--------------------------------------------------")
        print("Ubicación eliminada de forma satisfactoria.")
        print("--------------------------------------------------")
    except Exception as e:
        print(f"Ha ocurrido un error al eliminar la ubicación: {str(e)}")




