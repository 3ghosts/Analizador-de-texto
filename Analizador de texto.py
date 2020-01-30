pedir = input("Introduce el nombre del archivo a analizar: ")
wrongText = open(pedir,"r")
text = wrongText.read()

stats = open("Stats.txt", "w+")

noLetras = [".",",",";",":","(",")","/","-","_","?","¿","¡","!","@","'","{","}","*","[","]","#","%",">","<"," ", "\n","^","º","ª"]
vocales = ["a","e","i","o","u","A","E","I","O","U"]

def contarLetras():
    letras = 0
    for caracter in text:
        if caracter in noLetras:
            pass
        elif caracter.isdigit() == True:
            pass
        else:
            letras += 1
    return letras

def contarMayus():
    mayus = 0
    for caracter in text:
        if ord(caracter) in range(65,91):
            mayus +=1
    return mayus

def contarMinus():
    minus = 0
    for caracter in text:
        if ord(caracter) in range(97,123):
            minus +=1
    return minus


def contarParrafos():
    parrf = 0
    for caracter in text:
        if caracter == "\n":
            parrf += 1
    return parrf
    
    
def contarPalab():
    posicion = 0
    nPalabras = 0

    while posicion < len(text):
        if (text[posicion] == " " or text[posicion] == "\n") and text[posicion - 1] != " ":
            nPalabras += 1
        posicion += 1
        
    if text[posicion-1] != " ":
        nPalabras += 1
    return nPalabras

print("Este texto contiene {} letras, de las cuales {} son mayúsculas y {} son minúsculas. El texto además se compone de {} palabras, y {} párrafos.".format(contarLetras(), contarMayus(), contarMinus(),contarPalab(), contarParrafos()))

def contarVocales():
    voc = 0
    for caracter in text:
        if caracter in vocales:
            voc +=1
        else:
            pass
    return voc

def contarConsonantes():
    cons = 0
    for caracter in text:
        if caracter in vocales:
            pass
        elif caracter in noLetras:
            pass
        elif caracter.isdigit() == True:
            pass
        else:
            cons +=1
    return cons

def contarDigits():
    digit = 0
    for caracter in text:
        if caracter.isdigit() == True:
            digit +=1
        else:
            pass
    return digit

def contarOtros():
    otros = 0
    for caracter in text:
        if caracter in noLetras:
            otros +=1
        else:
            pass
    return otros

print("Dentro de esas {} letras hay {} vocales, {} consonantes y {} dígitos, además de otros {} caracteres.\nEsta información ha sido almacenada en un Bloc de notas llamada 'Stats'.".format(contarLetras(),contarVocales(),contarConsonantes(), contarDigits(), contarOtros()))

stats.write(str("Este texto contiene {} letras, de las cuales {} son mayúsculas y {} son minúsculas.\nEl texto además se compone de {} palabras, y {} párrafos.\nDentro de esas {} letras hay {} vocales, {} consonantes y {} dígitos, además de otros {} caracteres.".format(contarLetras(), contarMayus(), contarMinus(),contarPalab(), contarParrafos(),contarLetras(),contarVocales(),contarConsonantes(), contarDigits(), contarOtros())))
stats.close()

resp = input("¿Deseas corregir el texto original?\nEscribe 'si' o 'no': ")

while True:
    if resp == "si" or resp =="SI":
        correct = open("Correccion.txt", "w+")
        text.capitalize()
        texts = text.replace("  "," ")
        tec = texts.replace("    ","\t")

        correct.write(tec)
        correct.close()
        print("El texto corregido se ha almacenado en un Bloc de notas llamado Correccion.txt")
        break
    elif resp == "no" or resp =="NO":
        print("Se ha cerrado el analizador y corrector de texto.")
        break
    else:
        print("No se reconoce la orden.")
        resp = input("Escribe 'si' o 'no': ")


wrongText.close()