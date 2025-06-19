# se importa el modulo random para generar aleatoriamente notas
import random

#se importa el modulo time para poder calcular la demora en la busqueda
import time

#se genera una lista de notas del 1 al 10
def alumnos(cant):
    lista_notas=[round(random.uniform(1, 10), 2) for i in range(cant)] 
    
    lista_notas= sorted(lista_notas) 
    return lista_notas# la funcion retorna una lista ordenada para que ambas busquedas esten en iguales condiciones

#se busca la calificacion objetivo de forma lineal y se retorna el tiempo de demora en encontrar el objetivo
def busqueda(list):        
    inicio= time.time()
    for i in range (len(list)):
        if list[i] == 10:    
            fin= time.time()        
    demora= (fin - inicio)*1000   
    return demora  


def busqueda_binaria(list):    
    #se divide la lista en dos mitades para ir comparando
    izquierda = 0
    derecha = len(list) - 1
    resultado= -1       
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if list[medio] >9:
            resultado= medio
            derecha= medio-1
        else:
            izquierda= medio+1
    #si no se encuentran resultados se devuelve una lista vacia
    if resultado == -1:
        return []           
    
    return list[resultado:]


#funcion que calcula la demora de busqueda binaria
def demora_binaria(list):
    inicio= time.time()
    busqueda_binaria(list)
    fin= time.time()   
    demora= (fin-inicio)*1000
    return demora


#se imprimen los valores obtenidos con la busqueda lineal
print(f"El tiempo de busqueda lineal es de {busqueda(alumnos(100000)):6f} milisegundos para 100000 alumnos ")
print(f"El tiempo de busqueda lineal es de {busqueda(alumnos(400000)):6f} milisegundos para 400000 alumnos ")
print(f"El tiempo de busqueda lineal es de {busqueda(alumnos(800000)):6f} milisegundos para 800000 alumnos ")
print(f"El tiempo de busqueda lineal es de {busqueda(alumnos(1200000)):6f} milisegundos para 1200000 alumnos ")
print(f"El tiempo de busqueda lineal es de {busqueda(alumnos(1600000)):6f} milisegundos para 1600000 alumnos ")

#se imprimen los valores obtenidos con la busqueda lineal
print(f"El tiempo de busqueda binaria es de {demora_binaria(alumnos(100000)):6f} milisegundos para 100000 alumnos")
print(f"El tiempo de busqueda binaria es de {demora_binaria(alumnos(400000)):6f} milisegundos para 400000 alumnos")
print(f"El tiempo de busqueda binaria es de {demora_binaria(alumnos(800000)):6f} milisegundos 800000 alumnos")
print(f"El tiempo de busqueda binaria es de {demora_binaria(alumnos(1200000)):6f} milisegundos 1200000 alumnos")
print(f"El tiempo de busqueda binaria es de {demora_binaria(alumnos(1600000)):6f} milisegundos 1600000 alumnos")