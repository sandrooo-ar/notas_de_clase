status = "Yes"
asignaturas_con_notas = {}

while status == "Yes":
    asignatura = input("\nWrite the name of the subject you want to enter: ")
    n_notas = int(input("Enter how many grades you have in " + asignatura + ": "))
    print(" ")
    notas = []
    media_notas = 0

    while n_notas > 0:
        nota = int(input("Enter your grade in " + asignatura + ": "))
        notas.append(nota)
        n_notas -= 1

    for element in notas:
        media_notas += element

    media_notas = media_notas / len(notas)

    asignaturas_con_notas[asignatura] = media_notas
    
    status = input("Do you want to enter another grade(Yes/No)?\n")
        
print(" ")
media_curso = 0
for element in asignaturas_con_notas:
    print("Your average grade in " + element + " it's " + str(asignaturas_con_notas[element]))
    media_curso += asignaturas_con_notas[element]

print("\nYour curse average is " + str(media_curso/len(asignaturas_con_notas.keys())))

input("\nPress enter to exit")
