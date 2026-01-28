#Diccionario anidado: un diccionario dentro de otro diccionario

familia = {
    "padre": {"nombre": "Juan",
              "edad": 50
              }, 
    "madre": {"nombre": "Ana",
              "edad": 48},
    "hijo": {"nombre": "Agustin",
             "edad": 22}

}

#Acceder a los items internos

print(familia["padre"]["nombre"])

#Bucle en un diccionario anidado

for pariente, obj in familia.items():
    print("pariente: ", pariente)

    for clave in obj:
        print(clave + ":", obj[clave])

