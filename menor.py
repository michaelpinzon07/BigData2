def numero_menor(arreglo):
    if len(arreglo) == 0:
        return None  
    menor = arreglo[0]  
    for numero in arreglo[1:]:
        if numero < menor:
            menor = numero
    return menor