def somar(lista):
    total = 0

    for x in lista:
        total += x
    
    return total

def somarRecursivo(lista):

    if lista == []: # caso-base
        return 0
    return lista[0] + somarRecursivo(lista[1:]) # caso recursivo

def contarItens(lista):

    if lista==[]: # caso-base
        return 0
    
    return 1 + contarItens(lista[1:]) # caso recursivo

def maiorValor(lista):

    if len(lista) == 2: # caso-base
        return lista[0] if lista[0] > lista[1] else lista[1]
    
    sub_max = maiorValor(lista[1:])
    
    return lista[0] if lista[0] > sub_max else sub_max # caso recursivo

lista = [1, 2, 3, 4]
print("Somar..........: {}".format(somar(lista)))
print("Somar Recursivo: {}".format(somar(lista)))
print("Quant Itens....: {}".format(contarItens(lista)))
print("Maior Valor....: {}".format(maiorValor(lista)))
