from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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

def gestionar_responsables():
    while True:
        print("Menú Responsables")
        print("1. Ingresar nuevo responsable")
        print("2. Actualizar información de un responsable")
        print("3. Buscar un responsable")
        print("4. Ver información de todos los responsables")
        print("5. Eliminar un responsable")
        print("6. Volver al menú principal")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ingresar_responsable()
        elif opcion == "2":
            actualizar_responsable()
        elif opcion == "3":
            buscar_responsable()
        elif opcion == "4":
            ver_responsables()
        elif opcion == "5":
            eliminar_responsable()
        elif opcion == "6":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Error, ingrese una opción válida.")

def ingresar_responsable():
    while True:
        codigo_responsable = input("Crea el código del responsable del equipo (Debe tener entre 4 y 6 caracteres, sólo números): ")
        a = len(codigo_responsable)
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (a <= 6 and a >= 4) :
            break
        else:
            print("El código del responsable no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 4 carácteres o más de 6. Inténtelo nuevamente.")
    
    while True:
        nombre = input("Ingrese el nombre del responsable: ")
        if nombre.strip() and nombre.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    
    while True:
        apellido = input("Ingrese el apellido del responsable: ")
        if apellido.strip() and apellido.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    
    while True:
        num_documento = input("Ingrese el número del documento de identidad: ")
        if num_documento.strip() and num_documento.isnumeric() and (len(num_documento) >= 9 and len(num_documento) <= 10):
            break
        else:
            print("El documento del responsable no puede estar vacío, no puede contener caracteres especiales y debe tener entre 9 y 10 caracteres. Inténtelo nuevamente.")

    
    while True:
        cargo = input("Ingrese el cargo del responsable: ")
        if cargo.strip() and cargo.isalpha():
            break
        else:
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
    
    nuevo_usuario = {"codigo_responsable":codigo_responsable,"nombre":nombre,"apellido":apellido,"documento":num_documento,"cargo":cargo}

    x=myres.insert_one(nuevo_usuario)
    print(x.inserted_id)


def actualizar_responsable():
    print("Actualizar Responsable ")

    codigo_responsable = input("Ingrese el código del responsable que se quiere actualizar: ")

    responsable = myres.find_one({"codigo_responsable": codigo_responsable})

    if responsable:
        nombre = str(input("Nombre nuevo: "))
        apellido = str(input("Apellido nuevo: "))
        documento= input("Documento nuevo: ")
        cargo = str(input("Cargo nuevo: "))

        nuevo_responsable ={
            "$set": {
                "nombre": nombre,
                "apellido": apellido,
                "documento": documento,
                "cargo": cargo
            }}

        myres.update_one({"codigo_responsable": codigo_responsable}, nuevo_responsable)
        print("El Responsable ha sido actualizado de forma satisfactoria.")
    else:
        print("No se encontró ningún responsable.")



def buscar_responsable():
    codigo_responsable = input("Ingrese el código del responsable que se desea buscar: ")
    usuario_encontrado = False
    for y in myres.find({'codigo_responsable': codigo_responsable}):          
        print(f"---------------------------------------------")
        print(f"codigo_responsable:", y["codigo_responsable"])
        print(f"nombre:", y["nombre"])
        print(f"apellido:", y["apellido"])
        print(f"documento:", y["documento"])
        print(f"cargo:", y["cargo"])
        print(f"---------------------------------------------")
    if not usuario_encontrado:
            print("No ha sido posible encontrar el código del responsable .")



def ver_responsables():
    print("Ver Responsables")

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        responsables_collection = db.responsables

        responsables = responsables_collection.find()

        for responsable in responsables:
            print("codigo_responsable:", responsable["codigo_responsable"])
            print("nombre:", responsable["nombre"])
            print("apellido:", responsable["apellido"])
            print("documento:", responsable["documento"])
            print("cargo:", responsable["cargo"])

    except Exception as e:
        print(f"Ha ocurrido un error al ver los responsables: {str(e)}")


def eliminar_responsable():
    print("Eliminar Responsable")
    
    while True:
        codigo_responsable = input("Ingrese el código de responsable que se desea eliminar: ")
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (len(codigo_responsable) >= 4 and len(codigo_responsable) <= 6):
            break
        else:
            print("El número de activo no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")

    delete_result = myres.delete_many({"codigo_responsable": codigo_responsable})
    print(f"Se eliminaron {delete_result.deleted_count} documentos con el código {codigo_responsable}.")
   
