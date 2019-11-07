# Dicionario general
votacion = {1: " Ver Candidatos",
            2: " Registrar voto",
            3: " Flash Informativo",
            4: " Salir"}

# Opcion 1
candidatos = {1: "Luis Esperanza",
              2: "Jose Barata",
              3: "Marco Ocram"}
# Opcion 2
votos_luis = 0
votos_jose = 0
votos_marco = 0
voto_total = 0
########################

print("+=======================+")
print("VOTACION".center(24))
print("+=======================+")
for k, v in votacion.items():
    print(k, v)

opcion = int(input("Ingrese la opcion que desea elegir: "))

while ( opcion != 4):

    if ( opcion in votacion):

        if ( opcion == 1 ):
            print(votacion[1].center(24))
            print("=====================")
            print("Nro", "Numbre".center(22))
            for nro, nombre in candidatos.items():
                print(nro, nombre)

        if ( opcion == 2):
            print("=============================")
            print("REGISTRAR VOTO")
            print("=============================")
            voto = int(input("Ingrese el numero del candidato al que le dara su voto: "))
            if ( voto in candidatos ):

                if ( voto == 1):
                    votos_luis = votos_luis + 1

                if ( voto == 2):
                    votos_jose = votos_jose + 1

                if ( voto == 3):
                    votos_marco = votos_marco + 1

                voto_total = votos_jose + votos_luis + votos_marco

            else:
                print("ERROR el nro de candidato no existe")

        if ( opcion == 3):
            if ( voto_total > 0 ):
                print("Nro", "Numbre".center(22), "Votos".rjust(4))
                print("1. ", candidatos.get(1), str(votos_luis).rjust(11))
                print("2. ", candidatos.get(2), str(votos_jose).rjust(14))
                print("3. ", candidatos.get(3), str(votos_marco).rjust(14))
                print("=============================")
                print("Total de votos: ", voto_total)

            else:
                print("esta opcion no esta disponible ")


        print("+=======================+")
        print("VOTACION".center(24))
        print("+=======================+")
        for k, v in votacion.items():
            print(k, v)
        opcion = int(input("Ingrese la opcion que desea elegir: "))

    else:
        exit()

if ( voto_total > 0 ):

    if ( opcion == 4):
        if ( votos_luis > votos_jose and votos_luis > votos_marco):
            print("LUIS ES GANADOR")
            Matriz_luis = [["x"] * 6 for i in range(7)]

            for fila in Matriz_luis:
                for x in range(1, 2):
                    print(Matriz_luis[x][0])
            print(Matriz_luis[6][0], Matriz_luis[6][1], Matriz_luis[6][2], Matriz_luis[6][3], Matriz_luis[6][4],
                  Matriz_luis[6][5])

        if ( votos_jose > votos_luis and votos_jose > votos_marco):
            print("JOSE ES GANADOR")
            Matriz_jose = [["x"] * 6 for i in range(7)]

            print(Matriz_jose[0][0], Matriz_jose[0][1], Matriz_jose[0][2], Matriz_jose[0][3], Matriz_jose[0][4],
                  Matriz_jose[0][5])
            for fila in Matriz_jose:
                for x in range(1, 2):
                    print((Matriz_jose[x][3]).center(12))

            print(Matriz_jose[6][0], Matriz_jose[6][1], Matriz_jose[6][2])

        if ( votos_marco > votos_jose and votos_luis < votos_marco):
            print("MARCO ES GANADOR")
            Matriz_Marco = [["x"] * 6 for i in range(7)]

            print(Matriz_Marco[0][0], Matriz_Marco[0][1], Matriz_Marco[0][2], Matriz_Marco[0][3], Matriz_Marco[0][4],
                  Matriz_Marco[0][5])
            for fila in Matriz_Marco:
                for x in range(1, 2):
                    print((Matriz_Marco[x][0]), (Matriz_Marco[x][0].center(18)))

            print(Matriz_Marco[6][0], Matriz_Marco[6][1], Matriz_Marco[6][2], Matriz_Marco[6][3], Matriz_Marco[6][4],
                  Matriz_Marco[6][5])

else:
    print("Ha salido del programa")