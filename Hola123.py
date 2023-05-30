from data_base import ingresar_equipo_manual, buscar_equipo,eliminar_equipo, actualizar_equipo, ingresar_equipos_automaticamente, ver_equipos
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from main import code
#from functions import input_no_vacio

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
myres = mydb["responsables"]
# import csv
# def ingresar_equipos_automaticamente():
#     print("----- Ingresar Equipos Automáticamente -----")
#     archivo_csv = "InventarioIPS.csv"

#     try:
        
#         client = MongoClient(uri, server_api=ServerApi('1'))
#         db = client.informatica1


       
#         equipos_collection = db.equipos

#         with open(archivo_csv, newline='') as archivo:
#             reader = csv.DictReader(archivo)

#             for row in reader:
#                 if "Serial" not in row or not row["Serial"]:
#                     continue  

#                 equipo = {
#                     "Serial": row["Serial"],
#                     "Número de activo": int(row.get("Número de activo", 0)),
#                     "Nombre del equipo": row.get("Nombre del equipo", ""),
#                     "Marca": row.get("Marca", ""),
#                     "Código de ubicación": int(row.get("Código de ubicación", 0)),
#                     "Código responsable": int(row.get("Código responsable", 0))
#                 }

#                 equipos_collection.insert_one(equipo)

#             print("Se han ingresado los equipos automáticamente.")
#     except FileNotFoundError:
#         print("El archivo CSV no existe.")
#     except Exception as e:
#         print(f"Error al ingresar equipos automáticamente: {str(e)}")




# def ver_equipos():
#     equipos = mycol.find()
#     if equipos.count() > 0:
#         print("Equipos registrados:")
#         for equipo in equipos:
#             print(f"Serial: {equipo['serial']}")
#             print(f"Número de activo: {equipo['numero_activo']}")
#             print(f"Nombre: {equipo['nombre_equipo']}")
#             print(f"Marca: {equipo['marca']}")
#             print(f"Código de ubicación: {equipo['codigo_ubicacion']}")
#             print(f"Código de responsable: {equipo['codigo_responsable']}")
#             print("----------")
#     else:
#         print("No hay equipos registrados.")


#def validador_codigo_responsable(code):
#    for a in myres.find({'codigo_responsable': code}):
#        nombre_en_sesion = a['nombre']
#        usuario_encontrado = True
#        break
#    usuario_encontrado = False
#    for a in myres.find({'codigo_responsable': code}):
#        hola = a['codigo_responsable']
#        usuario_encontrado = True
#        return hola
#    
#print(validador_codigo_responsable(code))

def menu_equipos():
    while True:
        print("Menú equipos")
        print("1. Ingresar un nuevo equipo en forma manual")
        print("2. Ingresar un nuevo equipo en forma automática")
        print("3. Actualizar la información de un equipo (por número de activo)")
        print("4. Buscar un equipo (por número de activo)")
        print("5. Ver la información de todos los equipos almacenados")
        print("6. Eliminar un equipo (por número de activo)")
        print("7. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ingresar_equipo_manual(code)
        elif opcion == "2":
            ingresar_equipos_automaticamente()
        elif opcion == "3":
            actualizar_equipo()
        elif opcion == "4":
            buscar_equipo()
        elif opcion == "5":
            ver_equipos()
        elif opcion == "6":
            eliminar_equipo()
        elif opcion == "7":
            break
        else:
            print("Error, ingrese una opción válida")


    



