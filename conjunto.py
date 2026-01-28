#Conjunto: conjunto no ordenado y mutables de elementos. Los duplicados no aparecen en un conjunto


frutas ={"Manzana", "Banana", "Naranja", "Frutilla", "Manzana"}

#print(frutas) #El print no sigue el orden indicado

frutas.add("Manzana")

#print(frutas) #No muestra el nuevo "Manzana" porque no permite duplicados 

conjunto_numeros = {0,1,2,3,4,5,1,2,True, False}

#print(conjunto_numeros) #No imprimira el 1 y el 2 duplicados. Ademas al True lo toma como 1 y al false como 0 por lo que no los agrega 

#print(len(conjunto_numeros)) #Nos va a dar la cantidad de elementos unicos en el conjunto 

#Uso del contrustor set()

verduras = set("Lechuga")

#print(verduras) #Imprime los caracteres unicos de la palabra "Lechuga". Para que sea un conjunto de verduras, deberiamos usar una ","

#verduras2 = set(["Lechuga",])

#print(verduras2) #Imprime el conjunto con un solo elemento "Lechuga"

#En los conjuntos, no se puede acceder a los elementos por indice (ya que no tienen orden). Pero si podemos recorrerlos con un for

#for fruta in frutas: 
    #print(fruta)

#if "Manzana" in frutas:
 #   print("La fruta Manzana esta disponible")
#else: 
#    print("La fruta Manzana no esta disponible")

#Agregar elementos a un conjunto

frutas.add("Limon")

print(frutas)

#Agregar un conjunto a otro conjunto
frutas_tropicales = {"Mango", "Piña", "Kiwi"}

frutas.update(frutas_tropicales)

#print(frutas)

#Eliminar elementos de un conjunto


#frutas.remove("Naranja") #Si el elemento no existe, tira un error



#print(frutas)

#Usando "Pop" para eliminar un elemento aleatorio del conjunto

#frutas.pop()

#print(frutas) #Elimino aleatoriamente el elemento "Manzana"


#Operaciones de Conjuntos (Matemática de Datos)

numeros = {0,1,2,3,4,5}
letras = {"a","b","c","d","e","f"}

#Union de conjuntos
union = numeros.union(letras)

print(numeros)
print(letras)
print(union)

#Intersección de conjuntos

materias_1ro = {"Matematica", "Lengua", "Naturales", "Sociales"}
materias_2do = {"Matematica", "Lengua", "Naturales", "Sociales", "Ingles", "Robotica"}

interseccion_materias = materias_1ro.intersection(materias_2do)
print(interseccion_materias)

otra_forma = materias_1ro & materias_2do
print(otra_forma)

#Diferencia de conjuntos

diferencia_materias = materias_1ro.difference(materias_2do)
print(diferencia_materias) #Set vacio, todas la materias de 1ro estan en 2do 

diferencia_materias2 = materias_2do.difference(materias_1ro)
print(diferencia_materias2) #Robotica e ingles esta en 2do pero no en 1ro

#Copiar y eliminar  conjuntos

conjunto_materias1ro = materias_1ro.copy() 
materias_1ro.clear()

print(conjunto_materias1ro)
print(materias_1ro) #Set vacio 






                