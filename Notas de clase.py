status = "Si"
asignaturas_con_notas = {}

while status == "Si":
    asignatura = input("\nEscribe el nombre de la asignatura que quieres introducir: ")
    n_notas = int(input("Introduce cuantas notas tienes de " + asignatura + ": "))
    print(" ")
    notas = []
    media_notas = 0

    while n_notas > 0:
        nota = int(input("Introduce una nota en " + asignatura + ": "))
        notas.append(nota)
        n_notas -= 1

    for element in notas:
        media_notas += element

    media_notas = media_notas / len(notas)

    asignaturas_con_notas[asignatura] = media_notas
    
    status = input("\nQuieres introducir otra nota más(Si/No)?\n")
        
print(" ")
media_curso = 0
for element in asignaturas_con_notas:
    print("Tu nota media en " + element + " es de " + str(asignaturas_con_notas[element]))
    media_curso += asignaturas_con_notas[element]

print("\nTu media de curso es de " + str(media_curso/len(asignaturas_con_notas.keys())))
