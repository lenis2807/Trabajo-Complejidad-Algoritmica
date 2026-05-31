arreglox = [[52, 23, 72, 67], [21, 15, 98]]

def obtener_suma(arreglo):
    total = 0
    for i in arreglo:
        total += i
    return total
    

def merge(arreglo, izquierda, mitad, derecha):
    L = arreglo[izquierda:mitad+1] # pos 0 , != pos 1
    R = arreglo[mitad+1:derecha+1]
    i = j = 0
    k = izquierda
    while (i < len(L) and j < len(R)):
        if (obtener_suma(L[i]) < obtener_suma(R[j])):
            arreglo[k] = L[i]
            i+=1
        else:
            arreglo[k] = R[j]
            j +=1
        k+=1

    while (i < len(L)):
        arreglo[k] = L[i]
        i+=1
        k+=1
    while (j < len(R)):
        arreglo[k] = R[j]
        j +=1 
        k+=1


def mergesort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        mitad = (izquierda + derecha)//2
        mergesort(arreglo, izquierda, mitad)
        mergesort(arreglo, mitad + 1, derecha)
        merge(arreglo, izquierda, mitad, derecha)
    return arreglo
    
    
    

resultado = mergesort(arreglox, 0, len(arreglox)-1)
print(resultado)


#print(ordenamiento(arreglox))

#[[23, 24, 22], [54, 21], [64, 46], [21, 15, 98], [82, 55], [16, 49, 24, 72], [91, 95], [52, 23, 72, 67], [53, 84, 94], [66, 53, 56, 79]]



#
#def ordenamiento(arreglo):
 #   arregloOrdenado = []
  #  def ordenar(arreglo, izquierda, derecha):
   #     if izquierda == derecha:
    #        return [arreglo[izquierda]]
     #   
      #  mitad = (izquierda + derecha)//2
       # left_candidate = ordenar(arreglo, izquierda, mitad)
        #right_candidate = ordenar(arreglo,mitad+1, derecha)

        #sumar los elementos de cada arreglo
        #suma_left = sum(left_candidate)
        #suma_der = sum(right_candidate)
        #return left_candidate if suma_left > suma_der else right_candidate
      
    #ordenar(arreglo, 0, len(arreglo)-1)
    #return arregloOrdenado
