import json
import re 

'''
{
    "heroes": [
        {
            "nombre": "Howard the Duck",
            "identidad": "Howard (Last name unrevealed)",
            "altura": 79.35,
            "peso": 18.45,
            "fuerza": 2,
            "inteligencia": ""
        }

'''

def cargar_json(path:str)->list:
    """
    
    """
    buffer_dict = []
    with open(path,"r",encoding="utf-8") as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["heroes"]

def mostrar_menu()-> str:
    respuesta = input( "\n1 Listar heroes "
                        "\n2 Ordenar por altura(asc o desc)"
                        "\n3 Ordenar por fuerza(asc o desc"
                        "\n4 Calcular y ordenar promedio (altura/peso/fuerza) por menor o mayor"
                        "\n5 Buscar héroes por inteligencia (good, average, high)"
                        "\n6 Exportar a CSV la lista de héroes ordenada(elegir del 1 al 4)"
                        "\n7 Salir\n\n")
    return respuesta

def validar_respuesta(respuesta:str, patron_regex:str)->bool:
    """
    Valida que el valor ingresado por el usuario

    Parámetro: str
    Retorno: True si es correcto,
            False si no.
    """
    if respuesta: 
        if re.match(patron_regex,respuesta):
            return True
    else:
        return False

def validar_len_lista(lista:list, tam:str)->bool:
    """
    Valida que la cantidad de la lista no sea mayor al tamaño de la lista,
    y tampoco menor a 0.

    Parámetro: lista:list , tam(valor ingresado por usuario):str
    Retorno: bool
    """
    if int(tam) > 0 and int(tam) <= len(lista):
        return True
    else:
        return False 

def mostrar_lista(lista:list)->list:
    """
    Muestra los elementos de la lista.

    Parámetro: list
    Retorno: los elementos formateados "Nombre|Altura|Peso|Fuerza|Inteligencia", 
    con sus valores respectivos.
    """
    lista_mostrar = []
    for elemento in lista:
        lista_mostrar.append(elemento)
        print("Nombre: {0} | Altura: {1} | Peso: {2} | Fuerza: {3} | Inteligencia: ".format(elemento["nombre"],elemento["altura"],elemento["peso"],elemento["fuerza"]),elemento["inteligencia"])
    return lista_mostrar

def buscar_min_max(lista_heroes:list,key:str,modo:str)->int:
    """
    Busca el max o min de una lista.

    Parámetro: lista:list, key:str
    Retorno: la posicion del elemento max o min.
    """
    i_min_max = 0
    for i in range(len(lista_heroes)):
        if modo == "asc" and lista_heroes[i][key] < lista_heroes[i_min_max][key] or modo =="desc" and lista_heroes[i][key]>lista_heroes[i_min_max][key]:
            i_min_max = i
            #lista_heroes[i],lista_heroes[i_min_max] = lista_heroes[i_min_max],lista_heroes[i]
    return i_min_max
            
def nahuel_sort(lista_heroes:list,key:str,modo:str)->list:
    """
    Ordena una lista, en modo "asc" o "desc" según indique el usuario.

    Parámetro: lista:list, key:str, modo:str
    Retorno: lista ordenada.
    """
    lista_a_ordenar = lista_heroes[:]
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        index_max_min = buscar_min_max(lista_a_ordenar,key,modo)
        elemento = lista_a_ordenar.pop(index_max_min)
        lista_ordenada.append(elemento)
    return lista_ordenada

def calcular_sumar(lista_heroes:list, key:str)->int:
    """
    Recorre lista de heroes y suma los valores de la key ingresada de cada heroe.

    Parámetro: lista_heroes:list, key:str
    Retorno: la sumatoria de las keys.
    """
    acumulador = 0
    for heroe in lista_heroes:
        acumulador = acumulador + int(heroe[key]) 
    return acumulador
 

def calcular_promedio(dividendo:int, divisor:int)->int:
    """
    Realiza una division entre el dividendo y el divisor ingresado.

    Parámetro: dividendo:int, divisor:int
    Retorno: el resultado de la division(int)
    """
    
    if dividendo > 0:
        promedio = dividendo/divisor 
        return promedio
    else:
        return -1

def calcular_promedio_max_min(lista_heroes:list,key:str,condicion:str)->list:
    """
    Calcula el promedio y devulve aquellos heroes que se encuentran por debajo(menor) 
    o por arriba(mayor) del promedio calculado.

    Parámetro: lista_heroes:list, key:str, condicion:str("mayor"/"menor")
    Retorno: lista_promedio:list
    """
    lista_promedio = []
    promedio = calcular_promedio(calcular_sumar(lista_heroes,key),len(lista_heroes))

    for heroe in lista_heroes:
        if condicion =="menor" and int(heroe[key]) < promedio or condicion == "mayor" and int(heroe[key]) > promedio:
            lista_promedio.append(heroe)
    return lista_promedio


def buscardor_inteligencia(lista_heroes:list, tipo:str)->list:
    """
    Busca aquellos heroes de la lista_heroes que cumplen con el tipo de inteligencia
    ingresado("good"/"average"/"high")

    Parámetros: lista_heroes:list, tipo:str("good"/"average"/"high")
    Retorno: lista_inteligencia:list
    """
    lista_inteligencia = [] 
    for elemento in lista_heroes:
        match = re.search(tipo,elemento["inteligencia"],re.IGNORECASE)
        if(match):
            lista_inteligencia.append(elemento)
    mostrar_lista(lista_inteligencia)
        
def exportar_csv(lista:list, path:str):
    """
    Transforma a csv la lista elegida por el usuario

    Parámetros: lista_heroes:list, path:str(direccion de retorno)
    Retorno: archivo csv
    """
    with open(path,"w") as file:
        for elemento in lista:
            file.write("{0},{1},{2}\n".format(elemento["nombre"],elemento["identidad"],elemento["fuerza"]))
