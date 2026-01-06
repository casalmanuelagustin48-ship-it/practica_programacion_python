#Practica de listas
            #0         #1       #2        #3           #4      #5          



frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Piña"]

print(frutas[1])
print(frutas[:3])
print(frutas[-1])
print(frutas[2:6])
print(frutas[:4])

#Cambiar el nombre de un indice 
frutas[1] = "Platano"
print(frutas)

#Cambiar multiples elementos 
frutas[4:] = ["Frutilla","Anana"]
print(frutas)

#Agregar elementos

frutas.append("Aguacate")
print(frutas)

frutas.insert(2,"Aguacate")
print(frutas)
#Unir listas
frutas_exoticas = ["Mango", "Kiwi", "Tunas"]

frutas.extend(frutas_exoticas)
print(frutas)

#Eliminación y Limpieza
frutas.remove("Aguacate")
print(frutas) #Borre el duplicado de Aguacate (quedo uno solo)

frutas.pop(0)
print(frutas) #Borre Manzana 

del frutas[3] #Borre Frutilla
print(frutas)


#for fruta in frutas: 
    #print(fruta)

#for i in range(len(frutas)):
    #print(frutas[i])
    #print(i)
    
i = 0
while i < len(frutas):
    print(i)
    print(frutas[i])
    i += 1

[print(fruta) for fruta in frutas]

frutas_con_e = [fruta for fruta in frutas if "e" in fruta]
print(frutas_con_e)

frutas_mayuscula = [fruta.upper() for fruta in frutas]
print(frutas_mayuscula)


nueva_frutas =[]

for fruta in frutas:
    if fruta == "Pera":
        nueva_frutas.append("Aguacate")
    else:
        nueva_frutas.append(fruta)

print(nueva_frutas)

#Orden y organización 

lista = [1,4,5,3,2,8,6,7,9]
lista.sort()
print(lista)

lista.sort(reverse = True)
print(lista)

frutas.sort()
print(frutas)

frutas.append("manzana")
frutas.append("Manzana")
print(frutas)

frutas.sort()
print(frutas)

frutas.sort(key = str.lower)
print(frutas)

copia_frutas = frutas.copy()
copia2_frutas = list(frutas)

print(copia_frutas)


frutas.append("Manzana")
print(frutas.count("Manzana"))


