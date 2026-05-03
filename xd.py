
texto = "En una galaxia, muy muy lejana, había..."
def numeroPalabras(texto, inicio = 0, final = None):
    if final is None:
        final = len(texto) - 1
    if inicio == final:
        return len(texto[inicio].split())
    
    mitad = (inicio + final)//2
    conteo_iz = numeroPalabras(texto, inicio, mitad)
    contedo_dere = numeroPalabras(texto, mitad + 1, final)

    return conteo_iz + contedo_dere

print(numeroPalabras(texto, 0))


# Su solución aquí:

def mayoritario(nums):
   def divide(nums, left, right):
      # Caso base
      if left == right:
          return nums[left]

      mid = (right + left)//2
      # Resolver mitades
      left_candidate = divide(nums, left, mid)
      right_candidate = divide(nums, mid + 1, right)

      # Si coinciden, ese es el mayoritario
      if (left_candidate == right_candidate):
        return left_candidate
      # Contar ocurrencias en el rango actual
      # utilizar la sugerencia aquí ;)
      left_count = sum(1 for i in range(left, mid) if nums[i] == left_candidate)
      right_count = sum(1 for i in range(mid + 1, right) if nums[i] == right_candidate)

      return left_candidate if left_count > right_count else right_candidate


   # Obtener candidato
   candidato = divide(nums, 0, len(nums) - 1)
   # Verificar si realmente es mayoritario
   if nums.count(candidato) > len(nums) // 2:
        return candidato
   else:
        return None
   
nums = [2, 2, 1, 2, 3, 2, 2]

r = mayoritario(nums)

print(r)