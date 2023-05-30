""" 
      INFORMÁTICA 1

Elick David Newball Rodriguez
Juan Felipe Pereira Molina

"""

from functions import menu_principal
from account import ingresar_responsable

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


def bienvenida():
    print("BIENVENIDO A NUESTRO SISTEMA DE CONTROL DE INVENTARIOS MÉDICOS")

    while True:
        while True:
            opcion = input("1.Iniciar sesión\n2.Crearse una cuenta\n3.Salir\nOpción:")
            if opcion.isnumeric() and opcion == "1":
                break
            elif opcion.isnumeric() and opcion == "2":
                break
            elif opcion.isnumeric() and opcion == "3":
                exit()
            else:
                print("Ingresa una opción correcta")


        if opcion == "1":
            code1 = input("Ingresa el código de responsable: ")
            usuario_encontrado = False
            for a in myres.find({'codigo_responsable': code1}):
                print("--------------------------------------------------")
                print(f"BIENVENIDO {a['nombre']} {a['apellido']}")
                code  = a['nombre']
                usuario_encontrado = True
                menu_principal(code)
                break
            
            if not usuario_encontrado:
                print("El código de responsable no se encuentra en la base de datos, creese una cuenta o verifique que ha escrito bien su código.")


        if opcion == "2":
            ingresar_responsable()

bienvenida()



     
    

