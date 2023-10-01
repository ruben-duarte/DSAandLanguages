
palabras = ["habito","hacer","sonreir", "lectura","conocer","cono"]
palabras2 = ["habito","hacer","lectura", "cono", "conocer","sonreir"]
palabras3 = ["habito","habito","lectura", "cono", "conocer","sonreir"]

def diccionario():
    orden = "hlabcdefgijkmnopqrstuvwxyz"
    diccionario_alien = dict()
    for letra in range(len(orden)):
        diccionario_alien[orden[letra]] = letra
    return diccionario_alien

def comparar(palabra1,palabra2):
    longitud = min(len(palabra1),len(palabra2))
    for index in range(longitud):
        if diccionario()[palabra1[index]] <diccionario()[palabra2[index]]:
            return True
        elif diccionario()[palabra1[index]] > diccionario()[palabra2[index]]:
            return False
    return len(palabra1) < len(palabra2)

def  alien_ordenado(palabras):
    #revisar orden de las palabras 
    for i in range(1,len(palabras)):
        if comparar(palabras[i-1], palabras[i]) == False:
            return False
    return True

prueba = alien_ordenado(palabras)
print(prueba)
prueba2 = alien_ordenado(palabras2)
print(prueba2)
prueba3 = alien_ordenado(palabras3)
print(prueba3)
        


