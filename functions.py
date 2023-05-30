import random
from data_base import ingresar_equipos_automaticamente, ver_equipos, actualizar_equipo
from account import gestionar_responsables
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ubicaciones import ingresar_ubicacion, actualizar_ubicacion, ver_ubicaciones, eliminar_ubicacion, buscar_ubicacion

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

def ingresar_equipo_manual(code):
    print("--------------------------------------------------")
    while True:
        serial = input("Ingrese el número de serie: ")
        if serial.strip() and serial.isalnum() and len(serial) == 10:
            break
        else:
            print("El número de serie no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 10 caracteres. Inténtelo nuevamente.")

    numero_activo = str(random.randint(1000, 9999))
    print(f"El número de activo asignado es: {numero_activo}")    

    while True:
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        if nombre_equipo.strip() and nombre_equipo.isalpha():
            break
        else:
            print("El nombre de equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
    while True:
        marca = input("Ingrese la marca del equipo: ")
        if marca.strip() and marca.isalpha():
            break
        else:
            print("La marca del equipo no puede estar vacío, no puede contener caracteres especiales. Inténtelo nuevamente.")
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
    
    print(f"Nombre del responsable: {code}")
    print("--------------------------------------------------")

    nuevo_equipo = {"serial": serial,"numero_activo": numero_activo,"nombre_equipo": nombre_equipo,"marca": marca,"ubicacion":bp,"codigo_responsable": code}

    x=mycol.insert_one(nuevo_equipo)
    print(x.inserted_id)

def buscar_equipo():
    code = input("Ingresa el número de activo: ")
    equipos_encontrados = 0
    
    for y in mycol.find({'numero_activo': code}):
        equipos_encontrados += 1
        print(f"+------------------------------------------+\n"
              f"| Serial             | {y['serial']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Numero activo      | {y['numero_activo']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Nombre equipo      | {y['nombre_equipo']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Ubicación          | {y['ubicacion']:<10}          |\n"
              f"|------------------------------------------|\n"
              f"| Marca              | {y['marca']:<10}          |\n" 
              f"|------------------------------------------|\n"
              f"| Codigo responsable | {y['codigo_responsable']:<10}          |\n"
              f"|------------------------------------------|\n")
    
    if equipos_encontrados == 0:
        print("Error, no se encontró ningún equipo.")

def eliminar_equipo():
    while True:
        numero_activo = input("Ingrese el número de activo: ")
        if numero_activo.strip() and numero_activo.isnumeric() and len(numero_activo) == 4:
            break
        else:
            print("El número de activo no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")
    delete_result = mycol.delete_many({"numero_activo": numero_activo})
    print(f"Se eliminaron {delete_result.deleted_count} documentos con el número de activo {numero_activo}.")




def menu_principal(code):
    while True:
        print("--------------------------------------------------")
        print("Menú Principal")
        print("1. Gestionar información equipos")
        print("2. Gestionar información responsables")
        print("3. Gestionar información ubicaciones")
        print("4. Salir")
        print("--------------------------------------------------")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_equipos(code)
        elif opcion == "2":
            gestionar_responsables()
        elif opcion == "3":
            menu_ubicaciones()
        elif opcion == "4":
            print("¡Gracias por utilizar el sistema!")
            exit()
        else:
            print("Error, ingrese una opción válida.")


def menu_equipos(code):
    while True:
        print("--------------------------------------------------")
        print("Menú equipos")
        print("1. Ingresar un nuevo equipo en forma manual")
        print("2. Ingresar un nuevo equipo en forma automática")
        print("3. Actualizar la información de un equipo (por número de activo)")
        print("4. Buscar un equipo (por número de activo)")
        print("5. Ver la información de todos los equipos almacenados")
        print("6. Eliminar un equipo (por número de activo)")
        print("7. Volver al menú principal")
        print("--------------------------------------------------")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ingresar_equipo_manual(code)
        elif opcion == "2":
            ingresar_equipos_automaticamente(code)
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





def menu_ubicaciones():
    while True:
     print("--------------------------------------------------")
     print("Menú Ubicaciones")
     print("1. Ingresar nueva ubicación")
     print("2. Actualizar información de una ubicación")
     print("3. Buscar una ubicación")
     print("4. Ver información de todas las ubicaciones")
     print("5. Eliminar una ubicación")
     print("6. Volver al menú principal")
    
     opcion = input("Selecciona una opción: ")

     if opcion == "1":
         ingresar_ubicacion()
     elif opcion == "2":
         actualizar_ubicacion()
     elif opcion == "3":
         buscar_ubicacion()
     elif opcion == "4":
         ver_ubicaciones()
     elif opcion == "5":
         eliminar_ubicacion()
     elif opcion == "6":
        break
     else:
            print("Error, ingrese una opción válida")

            

    








    