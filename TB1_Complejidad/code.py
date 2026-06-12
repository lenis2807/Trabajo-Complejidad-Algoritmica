'''
***************************************************************************************************
CONSIDERACIONES:
Tener instalado las librerias como: Pandas, Networkx, Matplotlib

Si considera trabajar con la libreria Kaggle
Si es si: pip install kaggle

Si es no: Omitir

Instalación de librerias:
1. Abrir terminal ( control + shift + letra ñ )
2. Pegar en el terminal: pip install pandas kagglehub networkx

Si se considera usar el dataset desde la misma fuente (tener instalado libreria kaggle)
path = kagglehub.dataset_download("adriana14852/airports-distances-and-others")

Si se considera usar el dataset en el mismo python

OJO: CONSIDERAR EN QUE DIRECTORIO ESTA COPIADO SU CSV

ej general: ruta = "complete_airport_flight_network_dataset.csv"
ej en algun directorio: ruta = "TB1_Complejidad/complete_airport_flight_network_dataset.csv"


3. Si Pandas llega a leer el archivo pero aparece 'ModuleNotFoundError: No module named 'scipy' '
REALIZAR EL SIGUIENTE PASO EN SU TERMINAL!!!!
pip install scipy

TENER EN CUENTA QUE ES UN DATASET DE 3000 NODOS, NO SE PREOCUPE SI SE DEMORA EN IMPRIMIR LA IMAGÉN
:)
***************************************************************************************************
'''



# ============================================================  
# SECCIÓN 1: IMPORTACIONES  # Esta parte carga módulos de Python necesarios para el desarrollo del código
# ============================================================  
import os
import heapq 
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt 




'''
***************************************************************************************************
'''
# ============================================================  
# SECCIÓN 2: VARIABLES GLOBALES #configuración de variables necesarias para el programa
# ============================================================  

#ruta para leer el archivo de kagglehub
#ruta = kagglehub.dataset_download("adriana14852/airports-distances-and-others")

ruta = "complete_airport_flight_network_dataset.csv"
df = pd.read_csv(ruta) #leemos el archivo con la libreria Pandas 

G = nx.Graph() #leemos el grafo con el nx

#importamos a la variable G (grafo) los elementos a usar del archivo csv con pandas
G = nx.from_pandas_edgelist(df, source="origin_airport_id", target="destination_airport_id", edge_attr="distance_km")
'''
***************************************************************************************************
'''


# ============================================================  
# SECCIÓN 3: Impresión de grafo normal #Se imprime el grafo a evaluar
# ============================================================  

def imprimirGrafoNormal(): #funcion para imprimir el grafo
    '''
    ***************************************************************************************************
    IMPRIMIREMOS EL GRAFO NORMAL
    ***************************************************************************************************
    '''
    
    G = nx.Graph() #leemos el grafo con el nx

    #importamos a la variable G (grafo) los elementos a usar del archivo csv con pandas
    G = nx.from_pandas_edgelist(df, source="origin_airport_id", target="destination_airport_id", edge_attr="distance_km")

    plt.figure(figsize=(15,10)) #colocamos el tamaño de nuestra pantalla
    pos = nx.spring_layout(G, k=0.5, seed=42) #configuramos el spring 

    #graficamos los nodos
    nx.draw_networkx_nodes(G, pos, node_size=20, node_color="skyblue")

    #graficamos las aristas
    nx.draw_networkx_edges(G, pos, alpha=0.8, width=0.5, edge_color="gray")

    #graficamos las etiquetas (labels)
    nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif")


    plt.title("Grafico rutas aereas", fontsize=16) #titulo del grafo 
    plt.axis("off") #dejamos unicamente los datos visibles
    plt.tight_layout() #para los margenes
    plt.show() #mostramos el grafo




# ============================================================  
# SECCIÓN 4: DESARROLLO DE ALGORITMOS A USAR  #En está parte desarrollamos y justificamos el desarrollo de los algoritmos a usar
# ============================================================  
def algoritmoDikjstra(grafo, inicio, destino): 
    '''
    ***************************************************************************************************
    JUSTIFICACION: EL ALGORITMO DE DIJKSTRA NOS PERMITIRA ENCONTRAR EL MEJOR CAMINO ENTRE DOS NODOS
    CONSIDERANDO EL PESO DE LAS ARISTAS COMO LAS DISTANCIAS MEDIDAS EN KILOMETROS

    SI NO SE ENCUENTRA EL CAMINO, DEVOLVERA NONE (NULL)
    ESTAMOS USANDO LA LIBRERIA HEAP PARA LA EVALUACION DE LOS NODOS
    ***************************************************************************************************
    '''
    cola = [] #creamos una cola para evaluar los nodos 

    heapq.heappush(cola, (0, inicio, [inicio])) #hacemos un heappush para evaluar
    #los elementos de la cola a su vez que agregamos el costo y mostraremos el camino

    costo_g = {n : float('inf') for n in grafo} #inicializamos los costos en infinito
    costo_g[inicio] = 0 #colocamos el nodo inicio en 0

    #hacemos una validacion que si el nodo ingresado es igual al del final
    #no retorne nada 
    if inicio == destino: 
        print("Seas pendejo pues :v") #retornamos 
        return 0, [inicio] #devolvemos el costo 0 y el "camino" xd

    #haremos un while "recursivo"
    while cola: #mientras la cola no este vacia
        costo_acumulado, nodo, camino = heapq.heappop(cola)
        #sacamos del heapq.heappush(cola, (0, inicio, [inicio]))
        #donde: costo_Acumulado = 0
        #       nodo = inicio
        #       camino = [inicio]

        if nodo == destino: #si el nodo inicial es igual al nodo del destino
            #retornamos el costo_Acumulado y el camino
            return costo_acumulado, camino 

        if costo_acumulado > costo_g[nodo]: #si el costo_Acumulado actual es mayor al costo del diccionario en la pos nodo
            continue #saltamos porque no vale la pena cambiar el costo, bruh

        #para cada vecino y su costo de aristas evaluado en el grafo de pos nodo
        for vecinos, datos_arista in grafo[nodo].items(): 

            #sumamos a la variable de costo actual el costo acumulado mas el costo de aristas
            #de cada vecino
            costo_aristas = datos_arista['distance_km']
            costo_Actual = costo_acumulado + costo_aristas 


            #hacemos la condicion de evaluar la cantidad del costo actual contra la de los costos en g
            if costo_Actual < costo_g[vecinos]:
                costo_g[vecinos] = costo_Actual #hacemos un swap de costos

                #hacemos un heappush para cada vecino que cumpla la condicion
                #además que en cada push mostramos el camino con el nodo de menor
                #peso encontrado
                heapq.heappush(cola, (costo_Actual, vecinos, camino + [vecinos]))

    return None #si no encontramos camino retornamos None (Null)

def dls(grafo, inicio, destino, limite): #creamos una funcion dls para iterar los nodos
    '''
    ***************************************************************************************************
    ESTA SERÁ NUESTRA FUNCIÓN PARA ENCONTRAR Y VERIFICAR EL CAMINO ENCONTRADO
    CON PARAMETROS COMO:
    INICIO = INGRESADO POR EL USUARIO
    DESTINO = INGRESADO POR EL USUARIO
    LIMITE = ESCALA, EL USUARIO INGRESARA LA ESCALA CORRESPONDIENTE A SU GUSTO

    SI EL DLS NO ENCUENTRA UN CAMINO CORRESPONDIENTE EN EL NIVEL ACTUAL 
    DEVOLVERA UN NONE

    SI LO ENCUENTRA DEVOLVERA EL RESULTADO FINAL

    LA VARIABLE DE VISITADOS ESTA CREADA BAJO UN SET PARA MEJORAR LA EFICIENCIA DEL ALGORITMO
    COMPLEJIDAD TEMPORAL
    ***************************************************************************************************
    '''

    visitados = set() #creamos un set de visitados para la eficiencia temporal

    def dls(nodo, camino, limite): #funcion recursiva dls
        #donde nodo es igual al nodo actual a evaluar
        #el limite es el limite pues :v
    
        if nodo == destino: #si el nodo actual es igual al destino
            return camino #retornamos el camino 

        if limite == 0: #si llegamos al 0
            return None #retornamos None
                     
        visitados.add(nodo) #agregamos al set visitados el nodo actual a evaluar

        #si el limite es mayor a 0 
        if limite > 0 : 
            for vecinos, _ in grafo[nodo].items(): #para cada vecino del grafo en pos nodo
                #hacemos "_" para que no haya problema al buscar elementos en la tupla de cosas (se puede modificar ese caracter)
                #ejemplo:  [ ... , (1234, {'distance_km': 500} ) , ... ]
                #vecinos = 1234       and            _ = {'distance_km':500}

                if vecinos not in visitados: #si el vecino no esta en el arreglo de visitados
                    
                    #agregamos una variable resultado que llama a la funcion recursivamente dls
                    #en cada iteracion del bucle for
                    resultado = dls(vecinos, camino + [vecinos], limite-1)

                    #si el resultado no esta vacio (contiene elementos)                    
                    if resultado is not None:
                        return resultado #retorna el resultado y mostrara el camino
            
            visitados.remove(nodo) #fuera del bucle for pero dentro de la condicional, removemos el nodo actual
            #para que en la siguiente iteración del bucle for, el nodo actual no aparezca como visitado
            
            return None #si no hay camino retorna None


    resultado_final = dls(inicio, [inicio], limite) #llamamos a la funcion dls
    
    #nos mostrara el camino y el limite encontrado
    return resultado_final #retornamos el resultado final

                

#funcion BUSQUEDA EN PROFUNDIDAD LIIMITADA ITERATIVA
#esta funcion nos servira para la busqueda de escalas
def IDDFS(grafo, inicio, destino, limite): 
    '''
    ********************************************************************************************************
    JUSTIFICACION: USAREMOS EL ALGORITMO DE BUSQUEDA EN PROFUNDIDAD LIMITADA ITERATIVA, PUESTO 
    QUE DLS (BUSQUEDA EN PROFUNDIDAD LIMITADA) NOS SERÁ DE VITAL IMPORTANCIA PARA ENCONTRAR EL CAMINO 
    CORRESPONDIENTE, SI NO SE ENCUENTRA EN EL NIVEL ACTUAL EL IDDFS PASARA A EVALUAR EL SIGUIENTE NIVEL

    CON ESTO EVITAREMOS ENCONTRAR UN CAMINO NO EFICIENTE

    SI SE USARA EL ALGORITMO DE DFS (BUSQUEDA EN PROFUNDIDAD) PODEMOS LLEGAR A ENCONTRAR CAMINOS DE 50 PASOS
    LO CUAL NO ES MUY EFICIENTE
    ********************************************************************************************************
    '''

    #iteraremos hasta el rango del limite ingresado por el usuario
    #incrementaremos en + 1 para evaluar los limites exactos

    #si fuera limite = 5, el compilador lo va a leer hasta el rango 4
    #incrementar en +1 nos garantizara evaluar las escalas deseadas por el usuario
    for nivel_Actual in range(limite + 1): 

        #la variable camino devolvera la funcion dls

        #la variable nivel_Actual es la que iterara el dls
        camino = dls(grafo, inicio, destino, nivel_Actual) 
        
        #si el camino no esta vacio (tiene un resultado)
        if camino is not None:
            return camino #retornamos el camino

    return None #si no hemos encontrado nada retornamos None (Null)



# ============================================================  
# SECCIÓN 5: GRAFICOS RESULTANTES #funciones que muestran el gráfico resultante 
# ============================================================  
def graficarDijsktra(grafo, camino): #creamos una funcion para graficar el algoritmo de dijkstra
 
    plt.figure(figsize=(15,10)) #colocamos el tamaño de nuestra pantalla
    pos = nx.spring_layout(G, k=0.5, seed=42) #configuramos el spring 

    colores = [] #arreglo de colores
    for nodo in grafo.nodes(): #para cada nodo en el grafo
        if nodo not in camino: #si el nodo no esta en el camino 
            colores.append("red") #agregamos al arreglo colores el color rojo
        else: #sí, si esta en el camino
            colores.append("skyblue") #agregamos al arreglo colores el color celeste 

    #use IA
    aristas_del_camino = list(zip(camino[:-1], camino[1:]))

    #graficamos los nodos
    nx.draw_networkx_nodes(G, pos, node_size=20, node_color="skyblue")

    #graficamos las aristas
    nx.draw_networkx_edges(G, pos, alpha=0.8, width=0.5, edge_color="gray")

    #remarcamos el camino encontrado con rojo
    nx.draw_networkx_edges(G, pos, edgelist=aristas_del_camino, edge_color="red", width=3.0)

    #graficamos las etiquetas (labels)
    nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif")

    plt.title("Algoritmo de Dijkstra", fontsize=16) #titulo del grafo 
    plt.axis("off") #dejamos unicamente los datos visibles
    plt.tight_layout() #para los margenes
    plt.show() #mostramos el grafo
 
 
def graficarIDDFS(camino):
    G_camino = nx.DiGraph()

    edges = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
    G_camino.add_edges_from(edges)
 
    plt.figure(figsize=(10,6))
    pos = nx.spring_layout(G_camino, seed=42)
    nx.draw_networkx_nodes(G_camino, pos, node_color='tomato', node_size=700)
    nx.draw_networkx_edges(G_camino, pos, edge_color='gray', width=2, arrowsize=20)
    nx.draw_networkx_labels(G_camino, pos, font_size=12, font_family='sans-serif', font_weight='bold')
    
    plt.title("Ruta Óptima Encontrada por IDDFS", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.show()


def main():
    '''
    ***************************************************************************************************
    FUNCION PRINCIPAL (MAIN)
    ***************************************************************************************************
    '''
    while True:
   
        print("MENU DE OPCIONES\n")
        print("1. MOSTRAR GRAFO")
        print("2. MOSTRAR DIJSKTRA")
        print("3. MOSTRAR BUSQUEDA PROFUNIDAD ITERADA LIMITADA")
        print("4. FIN\n")
        
        opcion = (input("Seleccione su opcion: ")) #variable de selección de opciones
         
        if opcion == "1":
            print("Cargando ... ")
            print(imprimirGrafoNormal()) #imprimimos el grafo normal
        

        if opcion == "2":
            #debemos evaluar si los datos ingresado por el usuario estan dentro del grafo-archivo
            #evaluar el nodo inicial y el nodo final

            inicio = int(input("INGRESE SU AEROPUERTO DE INICIO: "))
            destino = int(input("INGRESE SU AEROPUERTO DE DESTINO: "))

            if inicio in G and destino in G:  #verificamos que el inicio y el destino esten en el grafo G
                resultado = algoritmoDikjstra(G, inicio, destino) #resultado almacena el algoritmo de dijkstra
                
                if resultado is not None: #si el resultado si tiene ALGO que mostrar
                    costo_minimo, camino = resultado #separamos los elementos de costo minimo y el camino encontrado

                    print(f"\nCamino: {camino}") #imprimimos el camino encontrado :v
                    
                    print("Cargando ... ")
                    graficarDijsktra(G, camino)

                else: #si el resultado es vacio (no hay nada ... :c)
                    print("Lo siento papu, no podras salir de tu choza")

        if opcion == "3":
            inicio = int(input("INGRESE SU AEROPUERTO DE INICIO: "))
            destino = int(input("INGRESE SU AEROPUERTO DE DESTINO: "))
            escalas = int(input("INGRESE EL LIMITE DE ESCALAS: "))
            if inicio in G and destino in G:  #verificamos que el inicio y el destino esten en el grafo G
                resultado = IDDFS(G, inicio, destino, escalas) #resultado almacena el algoritmo IDDFS para las escalas

                if resultado is not None: #si el resultado si tiene ALGO que mostrar
                    print("cargando ...")
                    graficarIDDFS(resultado)
            
                else:
                    print("No se encontraron resultados")

        if opcion == "4":
            print("Gracias :v\n")
            print("¡NO REGRESES!!!!!")
            break



#usamos esta condicional para que la funcion main sea la funcion principal, referencia a c++ :v
#me apoye de la IA XD
if __name__ == "__main__":
    main()