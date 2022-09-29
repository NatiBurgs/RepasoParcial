from libreria import * 


def heroes_app()->list:
    lista_heroes = cargar_json("C:/Users/rocio/Desktop/Labo 1/Laboratorio1-Python/Repasoparcial/data_stark.json")
    contenido = lista_heroes[:]
    while True:
        respuesta = input('''
                            1 Listar cantidad de heroes 
                            2 Ordenar por altura(asc o desc)
                            3 Ordenar por fuerza(asc o desc)
                            4 Calcular y ordenar promedio (altura/peso/fuerza) por "menor" o "mayor"
                            5 Buscar héroes por inteligencia (good, average, high)
                            6 Exportar a CSV la lista de héroes ordenada
                            7 Salir''')
        if validar_respuesta(respuesta, '^[1-7]{1}$') == True:
            print("Valor correcto!")
            pass
        else:
            print("Error. Ingrese un valor del 1 al 7")
            continue

        if(respuesta == "1"):
            top = input("Cuantos desea listar? \n")
            if validar_len_lista(lista_heroes,top) == True:
                top = int(top)
                contenido = mostrar_lista(lista_heroes[:top])
            else:
                print("Error.Ingrese un numero del rango de la lista {0} \n".format(len(lista_heroes)))
                continue
        
        elif(respuesta == "2"):
            modo = input("En forma asc o desc? \n")
            if validar_respuesta(modo,"asc|desc") == True:
                lista_para_archivo = nahuel_sort(lista_heroes[:top],"altura",modo)
                contenido = mostrar_lista(lista_para_archivo)

        elif(respuesta == "3"):
            modo = input("asc o desc? \n")
            if validar_respuesta(modo,"asc|desc") == True:
                contenido = mostrar_lista(nahuel_sort(lista_heroes[:top],"fuerza",modo))

        elif(respuesta == "4"):
            key = input("peso|altura|fuerza? \n")
            if validar_respuesta(key,"peso|altura|fuerza") == True:
                condicion = input("Desea ordenar por mayor|menor promedio? \n")
                if validar_respuesta(condicion,"menor|mayor") == True:
                    contenido = mostrar_lista(calcular_promedio_max_min(lista_heroes[:top],key,condicion))

        elif(respuesta == "5"):
            tipo=input("good/ average/ high? \n")
            if validar_respuesta(tipo,"good|average|high") == True:
                print(buscardor_inteligencia(lista_heroes[:top],tipo))

        elif(respuesta == "6"):
            exportar_csv(contenido,"C:/Users/rocio/Desktop/Labo 1/Laboratorio1-Python/Repasoparcial/heroes.csv")
            print("Se ha creado correctamente!")   

        elif(respuesta == "7"):
            print("CHAU")    
            break

heroes_app()


