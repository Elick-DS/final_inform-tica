from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from functions import input_no_vacio

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("CARGANDO..")
except Exception as e:
    print(e)

mydb = client["informatica1"]
myres = mydb["responsables"]

def gestionar_responsables():
    while True:
        print("--------------------------------------------------")
        print("Menú Responsables")
        print("1. Ingresar nuevo responsable")
        print("2. Actualizar información de un responsable")
        print("3. Buscar un responsable")
        print("4. Ver información de todos los responsables")
        print("5. Eliminar un responsable")
        print("6. Volver al menú principal")
        print("--------------------------------------------------")

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
            print("--------------------------------------------------")
            print("¡Gracias por utilizar el sistema!")
            print("--------------------------------------------------")
            break
        else:
            print("--------------------------------------------------")
            print("Error, ingrese una opción válida.")
            print("--------------------------------------------------")

def ingresar_responsable():
    """
    Permite ingresar la información de un nuevo responsable en la base de datos de Mongo DB.

    Solicita al usuario el código, nombre, apellido, documento de identidad y cargo del responsable.
    Verifica que los valores ingresados cumplan con los criterios de validación y, en caso contrario,
    muestra mensajes de error correspondientes. Si todos los datos son válidos, se crea un diccionario
    con la información y se inserta en la base de datos. Finalmente, se muestra el ID del documento
    recién insertado.

    Requisitos de validación:
    - El código del responsable debe tener entre 4 y 6 caracteres y contener solo números.
    - El nombre y apellido del responsable no pueden estar vacíos y no pueden contener caracteres especiales.
    - El número de documento de identidad debe tener entre 9 y 10 caracteres y contener solo números.
    - El cargo del responsable no puede estar vacío y no puede contener caracteres especiales.

    Ejemplo de uso:
    >> ingresar_responsable()
    Crea el código del responsable del equipo (Debe tener entre 4 y 6 caracteres, sólo números): 12345
    Ingrese el nombre del responsable: Maria
    Ingrese el apellido del responsable: Reyes
    Ingrese el número del documento de identidad: 287454323
    Ingrese el cargo del responsable: Manager
    ObjectId("60b5a4cdd88d2d2e64032c7c")
    """
    while True:
        print("--------------------------------------------------")
        codigo_responsable = input("Crea el código del responsable del equipo (Debe tener entre 4 y 6 caracteres, sólo números): ")
        print("--------------------------------------------------")
        a = len(codigo_responsable)
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (a <= 6 and a >= 4) :
            break
        else:
            print("--------------------------------------------------")
            print("El código del responsable no puede estar vacío, no puede contener caracteres especiales y no puede tener menos de 4 carácteres o más de 6. Inténtelo nuevamente.")
            print("--------------------------------------------------")

    while True:
        print("--------------------------------------------------")
        nombre = input("Ingrese el nombre del responsable: ")
        print("--------------------------------------------------")
        if nombre.strip() and nombre.isalpha():
            break
        else:
            print("--------------------------------------------------")
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
            print("--------------------------------------------------")

    while True:
        print("--------------------------------------------------")
        apellido = input("Ingrese el apellido del responsable: ")
        print("--------------------------------------------------")
        if apellido.strip() and apellido.isalpha():
            break
        else:
            print("--------------------------------------------------")
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
            print("--------------------------------------------------")

    while True:
        print("--------------------------------------------------")
        num_documento = input("Ingrese el número del documento de identidad: ")
        print("--------------------------------------------------")
        if num_documento.strip() and num_documento.isnumeric() and (len(num_documento) >= 9 and len(num_documento) <= 10):
            break
        else:
            print("--------------------------------------------------")
            print("El documento del responsable no puede estar vacío, no puede contener caracteres especiales y debe tener entre 9 y 10 caracteres. Inténtelo nuevamente.")
            print("--------------------------------------------------")
    
    while True:
        print("--------------------------------------------------")
        cargo = input("Ingrese el cargo del responsable: ")
        print("--------------------------------------------------")
        if cargo.strip() and cargo.isalpha():
            break
        else:
            print("--------------------------------------------------")
            print("El nombre del responsable no puede estar vacío y no puede contener caracteres especiales. Inténtelo nuevamente.")
            print("--------------------------------------------------")

    nuevo_usuario = {"codigo_responsable":codigo_responsable,"nombre":nombre,"apellido":apellido,"documento":num_documento,"cargo":cargo}

    x=myres.insert_one(nuevo_usuario)
    print(x.inserted_id)

    # help(ingresar_responsable)


def actualizar_responsable():
    """
    Actualiza la información de un responsable en la base de datos.

    El usuario debe ingresar el código del responsable que se desea actualizar.
    Si el responsable se encuentra en la base de datos, se le solicita ingresar
    los nuevos valores para nombre, apellido, documento y cargo. Luego, se actualiza
    la información del responsable en la base de datos.

    Ejemplo:
    >>> actualizar_responsable()
    Actualizar Responsable
    Ingrese el código del responsable que se quiere actualizar: 12345
    Nombre nuevo: Pedro
    Apellido nuevo: Piedra
    Documento nuevo: 987654321
    Cargo nuevo: Auxiliar
    El Responsable ha sido actualizado de forma satisfactoria.
    """
    print("Actualizar Responsable ")
    print("--------------------------------------------------")

    print("--------------------------------------------------")
    codigo_responsable = input("Ingrese el código del responsable que se quiere actualizar: ")
    print("--------------------------------------------------")

    responsable = myres.find_one({"codigo_responsable": codigo_responsable})

    if responsable:
        print("--------------------------------------------------")
        nombre = str(input("Nombre nuevo: "))
        apellido = str(input("Apellido nuevo: "))
        documento= input("Documento nuevo: ")
        cargo = str(input("Cargo nuevo: "))
        print("--------------------------------------------------")

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
    # help(actualizar_responsable)




def buscar_responsable():
    """
    Busca un responsable en la base de datos de MongoDB utilizando su código de responsable.

    Solicita al usuario ingresar el código del responsable a buscar. Realiza la búsqueda en la
    base de datos y muestra la información del responsable si se encuentra. Si no se encuentra
    ningún responsable con el código proporcionado, se muestra un mensaje indicando que no se
    encontró ningún responsable.

    Ejemplo de uso:
    >> buscar_responsable()
    Ingrese el código del responsable a buscar: 12345
    --------------------------------------------------
    Codigo responsable: 12345
    Nombre: Dora
    Apellido: Narvaez
    Documento: 347554327
    Cargo: Secretaria
    --------------------------------------------------

    """
    print("Buscar Responsable")
    print("--------------------------------------------------")

    try:
        print("--------------------------------------------------")
        codigo_responsable = input("Ingrese el código del responsable a buscar: ")
        print("--------------------------------------------------")

        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        responsables_collection = db.responsables

        responsable = responsables_collection.find_one({"codigo_responsable": codigo_responsable})

        if responsable:
            print("--------------------------------------------------")
            print("Codigo responsable:", responsable["codigo_responsable"])
            print("Nombre:", responsable["nombre"])
            print("Apellido:", responsable["apellido"])
            print("Documento:", responsable["documento"])
            print("Cargo:", responsable["cargo"])
            print("--------------------------------------------------")
        else:
            print("No se pudo encontrar un responsable con el código proporcionado.")

    except Exception as e:
        print(f"Error al buscar el responsable: {str(e)}")

    # help(buscar_responsable)




def ver_responsables():
     """
    Muestra todos los responsables almacenados en la base de datos de MongoDB.

    Realiza una consulta a la colección de responsables en la base de datos y muestra la
    información de cada responsable. La información mostrada incluye el código de responsable,
    nombre, apellido, documento y cargo.

    Ejemplo de uso:
    >> ver_responsables()
    --------------------------------------------------
    Codigo responsable: 12345
    Nombre: Erick
    Apellido: Parra
    Documento: 2331320121
    Cargo: Conserje
    --------------------------------------------------
    --------------------------------------------------
    Codigo responsable: 97892
    Nombre: Janeth
    Apellido: Correa
    Documento: 123456789
    Cargo: Analista
    --------------------------------------------------

    """
     print("Ver Responsables")
     print("--------------------------------------------------")

     try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client.informatica1
        responsables_collection = db.responsables

        responsables = responsables_collection.find()

        for responsable in responsables:
            print("--------------------------------------------------")
            print("Codigo responsable:", responsable["codigo_responsable"])
            print("Nombre:", responsable["nombre"])
            print("Apellido:", responsable["apellido"])
            print("Documento:", responsable["documento"])
            print("Cargo:", responsable["cargo"])
            print("--------------------------------------------------")

     except Exception as e:
        print(f"Ha ocurrido un error al ver los responsables: {str(e)}")

    # help(ver_responsables)




def eliminar_responsable():
    """
    Elimina un responsable de la base de datos de MongoDB.

    Solicita al usuario ingresar el código del responsable que se desea eliminar. Verifica que el código
    cumpla con las condiciones de longitud y formato adecuadas. Luego, realiza la eliminación del responsable
    correspondiente en la colección de responsables.

    Ejemplo de uso:
    >> eliminar_responsable()
    Ingrese el código de responsable que se desea eliminar: 12345
    Se eliminaron 1 documentos con el código 12345.

    """
    print("Eliminar Responsable")
    
    while True:
        codigo_responsable = input("Ingrese el código de responsable que se desea eliminar: ")
        if codigo_responsable.strip() and codigo_responsable.isnumeric() and (len(codigo_responsable) >= 4 and len(codigo_responsable) <= 6):
            break
        else:
            print("El número de activo no puede estar vacío, no puede contener caracteres especiales y no puede tener más de 4 caracteres. Inténtelo nuevamente.")

    delete_result = myres.delete_many({"codigo_responsable": codigo_responsable})
    print(f"Se eliminaron {delete_result.deleted_count} documentos con el código {codigo_responsable}.")

# help(eliminar_responsable)
   
