from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("CARGANDO.")
except Exception as e:
    print(e)

mydb = client["informatica1"]
mycol = mydb["Equipos"]
myres = mydb["responsables"]



ultima_posicion = 0
def ingresar_equipos_automaticamente():
    global ultima_posicion
    print("Ingresar Equipo Automáticamente")
    archivo_csv = "InventarioIPS.csv"

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        Equipos_collection = db.Equipos

        with open(archivo_csv, newline='') as archivo:
            Equipos = csv.DictReader(archivo, delimiter=';')

            for _ in range(ultima_posicion):
                next(Equipos)

            Equipo = next(Equipos, None)
            if Equipo:

                Equipo_doc = {
                "serial": Equipo["serial"],
                "numero_activo": Equipo["numero_activo"],
                "nombre_equipo": Equipo["nombre_equipo"],
                "marca": Equipo["marca"],
                "ubicacion": Equipo["ubicacion"],
                "codigo_responsable": Equipo["codigo_responsable"]
            }

    
                Equipos_collection.insert_one(Equipo_doc)

                print(f"Se ha ingresado el equipo automáticamente: {Equipo['nombre_equipo']}")

                ultima_posicion += 1
            else:
                print("No hay más equipos para ingresar automáticamente.")

    except FileNotFoundError:
        print("El archivo CSV no existe.")
    except Exception as e:
        print(f"Error al ingresar equipo automáticamente: {str(e)}")

    # help(ingresar_equipos_automaticamente)



def actualizar_equipo():
     numero_activo = input("Ingrese el número de activo del equipo a actualizar: ")
     print("--------------------------------------------------")
     equipo = mycol.find_one({"numero_activo": numero_activo})
     if equipo:
         print("--------------------------------------------------")
         nuevo_nombre = input("Ingrese el nuevo nombre del equipo: ")
         nuevo_marca = input("Ingrese la nueva marca: ")
         while True:
            bloque = input("Ingrese el bloque en el que se encuentra el dispositivo: ")
            piso = input("Ingresa el piso en el que se encuentra el dispositivo: ")
            nuevo_bp = f"B{bloque}P{piso}"
            if nuevo_bp.strip() and nuevo_bp.isalnum():
                break
            else:
                print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
         print("--------------------------------------------------")
         nuevo_equipo = {
            "$set": {
                "nombre_equipo": nuevo_nombre,
                "marca": nuevo_marca,
                "ubicacion": nuevo_bp
            }
        }
     
         mycol.update_one({"numero_activo": numero_activo}, nuevo_equipo)
         print("Equipo actualizado satisfactoriamente.")
     else:
         print("No se encontro el equipo.")

# help(actualizar_equipo)



def ver_equipos():
    print("Ver Equipos")
    print("--------------------------------------------------")

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        Equipos_collection = db.Equipos

        Equipos = Equipos_collection.find()

        for Equipo in Equipos:
            print("--------------------------------------------------")
            print("serial:", Equipo["serial"])
            print("numero_activo:", Equipo["numero_activo"])
            print("nombre_equipo:", Equipo["nombre_equipo"])
            print("marca:", Equipo["marca"])
            print("ubicacion:", Equipo["ubicacion"])
            print("codigo_responsable:", Equipo["codigo_responsable"])
            print("--------------------------------------------------")

    except Exception as e:
        print(f"Error al ver los equipos: {str(e)}")

# help(ver_equipos)





            



