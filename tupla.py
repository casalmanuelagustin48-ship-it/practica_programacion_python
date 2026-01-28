#Tubla lista de elementos ordenados e inmutables 

#frutas = ("Manzana", "Banana", "Naranja", "Frutilla")

#print(frutas)
#print(type(frutas))
#print(len(frutas))
#print(frutas[0])
#print(frutas[:2])

#Fruta_buscada = input("Ingrese la fruta a buscar: ")


#if Fruta_buscada in frutas:
#   print(f"La fruta {Fruta_buscada} esta disponible")





tupla_verduleria = ("Tomate", "Lechaga", "Cebolla", "Acelga", "Zanahoria")
tupla_frutas = ("Manzana", "Banana", "Naranja", "Frutilla")

tupla_verduleria += tupla_frutas

#print(tupla_verduleria)
#print(tupla_frutas)

tupla_verduleria += ("Perejil",)

#print(tupla_verduleria)

lista_verduleria =list(tupla_verduleria)
lista_verduleria.remove("Cebolla")
tupla_verduleria = tuple(lista_verduleria)

#print(tupla_verduleria)
#print(type(tupla_verduleria))

#Desempaquetado de tuplas

a,e,*resto = tupla_verduleria


#print(a)
#print(e)  
#print(resto)

#for  fruta in tupla_verduleria:
 #   print(fruta)

#for i in range(len(tupla_verduleria)):
    #print(tupla_verduleria[i], "Con el indice ", i)

#i  = 0
#while i < len(tupla_verduleria):
 #   print(tupla_verduleria[i], "Con el indice ", i)
  #  i += 1


tupla_verduleria2 =("Kiwi","Mango", "Pera", "Manzana")

tupla_verduleria_completa = 2*tupla_verduleria + tupla_verduleria2

print(tupla_verduleria_completa)

print(tupla_verduleria_completa.count("Manzana"))
print(tupla_verduleria_completa.index("Manzana"))


