x=int (input("ingrese el numero a calcula su factorial"))

def factorial (x):
    if x==0 or x==1:
     return 1
    else:
        return x*factorial(x-1)
    
val=factorial(x)

print(f"el resultado del factorial de {x} es de: {val}")
