texto1 = "hoLa mUndO"
texto2 ="   Hola mundo  "
texto3 = "HolaJupiter"
texto4 = "Martin  Mariela Luciano  Manuel  Isabel"
Lista = ["Manzanas", "Banana", "Naranja", "Frutilla"]
lista_alumnos = "Manuel, Luciano, Agustin, Martin, Magdalena" 
frase = "El mundo gira mientra el mundo se mantiene quieto"
frase2 = "Son2y4amigos"

#Modificación mayuscula/minuscula 
print("Capitalize: ", texto1.capitalize())
print("Upper: ", texto1.upper())
print("Lower: ",texto1.lower())

#Limpieza y remplazo
print("Strip: ", texto2.strip())
print("Replace: ",texto3.replace("Jupiter","Marte"))
#Separación y unión 
print("Split: ", texto4.split())

#Busqueda e indices 

print("Find: ",lista_alumnos.find("Martin"))
print("Rfind: ",lista_alumnos.rfind("Martin"))
print("Index: ", frase.upper().count("MUNDO"))

#Verificación 
print("Empieza con: ", frase.upper().startswith("EL"))
print("Termina con: ", frase.upper().endswith("QUIETO"))
print("es un numero: ", frase.isdigit())
print("Es texto:", texto3.isalpha())
print("Tiene letras y numeros: ",frase2.isalnum())
print("Esta compuesto solo por espacio: ", frase2.isspace())
