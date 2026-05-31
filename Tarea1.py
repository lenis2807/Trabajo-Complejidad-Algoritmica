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

estados = [0, 0, 0, 0, 0, 0] 
#Algoritmo por fuerza bruta
estados = [0, 0, 0]
for queries in range(32):
    for i in range(0,4,1):
        for j in range(0,4,1):
            for k in [0,1]:

                estados = [i, j, k]

                M_orillaA = sum(1 for i in estados[0:3] if i == 0)  #cantidad de 0
                M_orillaB = sum(1 for i in estados[0:3] if i == 1)#cantidad de 1
            
                C_orillaA = sum(1 for i in estados[3:6] if i == 0) #cantidad de 0
                C_orillaB = sum(1 for i in estados[3:6] if i == 1) #cantidad de 1
            
                #if (M_orillaA > 0 and C_orillaB > M_orillaA):
                    #print(estados, "No valido")
                #if (M_orillaA > 0 and C_orillaB > M_orillaA):
                    #print(estados, "No valido")     
                #else:
                   # print(estados, "Valido")



for M in range(4):
    for C in range(4):
        for b in [0,1]:
            estados = [M, C, b]
            m_b = 3-M #orilla b    [2, 3, 1]  3-2 = 1 M     3-3=0 C
            c_b = 3-C
            if (M==0 or M>=C)and(m_b == 0 or m_b >=c_b):
                print(estados, "Valido")
            else:
                print(estados, "No valido")
