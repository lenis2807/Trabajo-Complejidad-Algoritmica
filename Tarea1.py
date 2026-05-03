arreglo = [3, 3, 0]
misioneros = arreglo[0]
canibales = arreglo[1]

#while(True):
    #encontrado = False
    #resultado = arreglo[i] - 1 #le resto 1  porque voy a iterar todas las combinaciones

    #validar 
    #if arreglo[i] < arreglo[j]:
     #   arreglo[2] = 0
      #  print("Argumento no valido", arreglo)

    #else:
     #   arreglo[2] = 0
        #print(f'{i}' "Consulta", arreglo)

    #me quede hasta acá        


#Algoritmo por fuerza bruta
estados = [0, 0, 0, 0, 0, 0]
for queries in range(64):
    for i in range(len(estados)):
        for j in range(len(estados)):
           for k in range(len(estados)):
               for l in range(len(estados)):
                   for m in range(len(estados)):
                       for n in range(len(estados)):
                            if (i == j):
                              pass
                            estados[i] = 0
                            estados[j] = 1

                            M_ceros = sum(1 for i in estados[0:3] if i == 0)  #cantidad de 0
                            M_izquierda = sum(1 for i in estados[0:3] if i == 1)#cantidad de 1
            
                            C_ceros = sum(1 for i in estados[3:6] if i == 0) #cantidad de 0
                            C_izquierda = sum(1 for i in estados[3:6] if i == 1) #cantidad de 1
            
            
                            if (M_ceros > 0 and C_izquierda > M_izquierda):
                                print(estados, "No valido")
                            if (M_izquierda > 0 and C_ceros > M_ceros):
                                print(estados, "No valido")     
                            else:
                                print(estados, "Valido") 
           

            