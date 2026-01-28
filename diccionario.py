#Diccionario: Coleccion no ordenada de elementos que se encuentran en pares clave:valor 

diccionario = {
    "Nombre": "Manuel Casal",
    "Edad": 24,
    "Ciudad": "Mendoza", 
}


print(diccionario["Nombre"])
print(diccionario["Edad"])
print(diccionario["Ciudad"]) #No hay un indice, pero podemos acceder a la clave mencionando al valor 

#No tiene un orden fijo, pero mantiene el orden con el que se creo

Nombre = diccionario.get("Nombre") #Otra forma de acceder a los valores 
print(Nombre)

#Si quiero cambiar algo del diccionario puedo hacer los siguiente

diccionario["Nombre"] = "Luciano Casal"


#Si solo quiero las claves

claves = diccionario.keys()
print(claves)
print(diccionario) #Cambia Manuel por Luciano pq hice el cambio 

#Podemos agregar nuevos valores con claves que no existen 

valores = diccionario.values()
print(valores)

diccionario["Hermano"] = "Manuel Casal"
print(diccionario)

items = diccionario.items()
print(items) #Nos trae una lista de tuplas con los pares clave:valor

#Chequear si existe una clave en el diccionario

if "Nombre" in diccionario:
    print("La clave Nombre existe en el diccionario")
else:
    print("La clave Nombre no existe en el diccionario")
    