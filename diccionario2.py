
diccionario = {
    "nombre": "Agustin",
    "edad": 22, 
    "ciudad": "Mendoza",
    "profesion": "Estudiante"

}

diccionario["nombre"] = "Manuel"
print(diccionario)

diccionario.update({"edad": 24, "profesion": "Administrativo"})
print(diccionario)

#Agregar nuevos pares claves:valor

diccionario["hobby"] = "Jugar futbol"

print(diccionario)

diccionario.update({"Equipo de futbol": "Belgrano"})
print(diccionario)

# Eliminar elementos

diccionario.pop("hobby")
print(diccionario)

diccionario.popitem() #Elimina el ultimo elemento agregado 
print(diccionario)
            
