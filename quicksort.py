from filecmp import DEFAULT_IGNORES


def ordenamiento_insercion(arr):
	
  for i in range (1, len(arr)):
 
   valor_actual =arr[i]
   j -=1 
   while  j >=0 and valor_actual< arr[j]:
     arr[j+1] = arr[j]
     j=-1
     arr [j+1]= valor_actual
   return arr

     
def main():
	datos = input ("ingresa una lista de numeros separado por espacios: ")

lista = list(map(int, DEFAULT_IGNORES.split()))
lista_ordenada = ordenamiento_insercion(lista)
print ("lista ordenada:",lista_ordenada)

