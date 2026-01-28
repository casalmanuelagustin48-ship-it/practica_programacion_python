diccionario = {
    "nombre": "Agustin",
    "edad": 22, 
    "ciudad": "Mendoza",
    "profesion": "Estudiante"

}

#Copiar un diccionario

diccionario_copiado = diccionario.copy()
#print(diccionario_copiado)

# Reccorer con un bucle

#Bucle for 

#for x in diccionario:
    #print(x) #Con esta x imprimimos las claves 

#Recorrer el diccionario imprimiendo los claves valor

for key in diccionario:
    print(key)
    print(diccionario[key]) #Imprime la clave primero y luego el valor 

for key in diccionario: 
    print("Clave: ", key, "Valor", diccionario[key])

## Si quiero solamente los valores

for value in diccionario.values():
    print("Valor: ", value)

## Desempaquetado de diccionarios
for x,y in diccionario.items():
    print(x)
    print(y)

