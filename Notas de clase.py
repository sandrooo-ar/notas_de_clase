def calculadora_de_notas(asignatura):       #Pregunta al usuario 3 veces la nota que ha sacado en "asignatura" y devuelve la media
    notas = []
    result = 0.0

    for n in range(3):
        notas.append(float(input("Introduce tus notas en " + asignatura + ": ")))
    
    for e in notas:
        result = result + e
    
    print(" ")

    return(result/3.0)

diccionario = {}
numero_de_asignaturas = int(input("Introduce el número de asignaturas que quieres calcular: "))       #Numero de asignaturas para el for
print(" ")

for n in range(numero_de_asignaturas):
    asignatura = input("Introduce el nombre de la asignatura: ")
    diccionario[asignatura] = round(calculadora_de_notas(asignatura),2)      #Añade al diccionario la nota media de cada asignatura


llaves = list(diccionario.keys())
valores = list(diccionario.values())

i = 0
media = 0

while i < len(llaves):      #Devuelve la nota de cada asignatura
    print("Tu nota media en " + llaves[i] + " es " + str(valores[i]))
    media = media + valores[i]
    i = i + 1

print(" ")
print("Tu media del curso es " + str(media/len(valores)))        #Devuelve la nota media del curso 
xyz = 0

while xyz == 0:
    x = input("Pulsa enter para salir:  ")
    xyz = 1