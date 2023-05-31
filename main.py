""" 
      INFORMÁTICA 1

Elick David Newball Rodriguez
Juan Felipe Pereira Molina

"""

from functions import menu_principal
from account import ingresar_responsable

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://informatica1:bio123@clusterinfo1.vzk1bse.mongodb.net/?retryWrites=true&w=majority"
"""
URI de conexión a la base de datos MongoDB.
"""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
"""
Crea un nuevo cliente de MongoDB y establece la conexión al servidor utilizando la URI especificada.
"""

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("CARGANDO.....")
except Exception as e:
    print(e)
    """
    Realiza una prueba de conexión enviando un ping al servidor para confirmar una conexión exitosa.
    Si ocurre una excepción, se muestra el mensaje de error.
    """

mydb = client["informatica1"]
myres = mydb["responsables"]
"""
Obtiene la base de datos "informatica1" y la colección "responsables" de la base de datos.

Nota: Se asume que la base de datos y la colección ya existen en el servidor de MongoDB.
"""

def bienvenida():
    """
    Función que muestra un mensaje de bienvenida y permite al usuario seleccionar una opción.
    """
    print("--------------------------------------------------")
    print("BIENVENIDO A NUESTRO SISTEMA DE CONTROL DE INVENTARIOS MÉDICOS")

    while True:
        while True:
            print("--------------------------------------------------")
            opcion = input("1.Iniciar sesión\n2.Crearse una cuenta\n3.Salir\nOpción:")
            print("--------------------------------------------------")
            if opcion.isnumeric() and opcion == "1":
                break
            elif opcion.isnumeric() and opcion == "2":
                break
            elif opcion.isnumeric() and opcion == "3":
                exit()
            else:
                print("Ingresa una opción correcta")
                """
                Solicita al usuario ingresar una opción válida (1, 2 o 3).
                Si la opción no es válida, se muestra un mensaje de error y se vuelve a solicitar la opción.

                Si la opción es "3", se finaliza el programa.

                Si la opción es "1" o "2", se procede a realizar las acciones correspondientes.
                """

        if opcion == "1":
            code1 = input("Ingresa el código de responsable: ")
            usuario_encontrado = False
            for a in myres.find({'codigo_responsable': code1}):
                print("--------------------------------------------------")
                print(f"BIENVENIDO {a['nombre']} {a['apellido']}")
                code = a['nombre']
                usuario_encontrado = True
                menu_principal(code)
                break
            
            if not usuario_encontrado:
                print("--------------------------------------------------")
                print("El código de responsable no se encuentra en la base de datos, creese una cuenta o verifique que ha escrito bien su código.")
                """
                Busca un responsable en la base de datos utilizando el código ingresado por el usuario.
                Si se encuentra un responsable con ese código, se muestra un mensaje de bienvenida y se llama a la función "menu_principal".

                Si no se encuentra ningún responsable con ese código, se muestra un mensaje de error.
                """

        if opcion == "2":
            ingresar_responsable()
            """
            Llama a la función "ingresar_responsable" para permitir al usuario crear una cuenta de responsable.
            """

bienvenida()
"""
Llama a la función "bienvenida" para iniciar el programa.
"""



     
    

