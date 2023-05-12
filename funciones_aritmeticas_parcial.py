
from funciones_segundarias import *
import datetime #ME REGRESA LA HORA Y FECHA DEL SISTEMA
import numpy as np #MODULO NUMPY ME GENERRA UN N° ALEATORIO
import re
import json
from os import system
system("cls")

ruta_dos = "D:\\programacion\\UTN\\parcial_01\\DBZ - DBZ (1).csv"

# MENU PRINCIPAN
def mostrar_menu()->None:
    """
     Brief: Muestro el menu de opcion para el usuario

    """
    menu = ["\n1.Traer datos desde archivo", "2.Listar cantidad por raza",
            "3.Listar personajes por raza",
            "4.Listar personajes por habilidad", "5.Jugar batalla:",
            "6.Guardar Json:", "7.Leer Json", "8.Salir\n"]

    for opcion in menu:
        print(opcion)

# MENU PRINCIPAL VALIDANDO LA ENTREDA DE DATOS
def menu_principal()->int:
    '''
        Brief: Muestra el menu con sus opciones, valida que el input se un entero
            para retornarno y luego ser comparado con opcion de los 'case'

        Return: Retorna una variable con un entero [Que hace mach con una opcion] y -1 [En caso contrario]

    '''
    mostrar_menu()
    entrada_de_dato = input("Ingrese una opcion: ")

    if validar_entero(entrada_de_dato):
        casteo = int(entrada_de_dato)
        return casteo
    else:
        return -1

# 1 Traer datos desde archivo:
def parser_csv(path:str)->list:
    '''
        Brief: Recibe como parámetro un 'str' de una ruta de un archivo.csv para
               para guardar en una coleccion
               Ejemplo:

                    {
                        'Id': 1,
                        'Nombre': 'Goku',
                        'Raza': [Saiyan],
                        'Poder de pelea': 500000,
                        'Poder de ataque': 10000,
                        'Habilidades': [Kamehameha, Genki Dama, Super Saiyan]
                    }

        Parameters:
            path -> Ruta del archivo.csv que se va a leer para trabajar

        Return: Una lista parseada
    '''
    lista_parseada = []

    with open(path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # lectura = re.split(",|\n", linea) #-> Hace el corte por ',' o '\n' y return una lista
            # -> Hace el corte por ',' o '\n' y return una lista
            lectura = elimina_caracter(",|\n", linea)

            personaje = {}  # -> Creo dict vacio
            personaje["Id"] = casteo_entero(lectura[0])
            personaje["Nombre"] = lectura[1]
            personaje["Raza"] = elimina_caracter('-', lectura[2])
            personaje["Poder de pelea"] = casteo_entero(lectura[3])
            personaje["Poder de ataque"] = casteo_entero(lectura[4])
            personaje["Habilidades"] = eleminar_simbolo_espacios(lectura[5])

            lista_parseada.append(personaje)

        return lista_parseada

# 2 Listar cantidad por raza:
def listar_cantidad_raza(lista: list)->None:
    '''
        Brief: Recibe como parámetro una lista iterable que agrupar por
              "Raza" y la cantidad de personajes que corresponden a esa raza.

        Parameters:
            lista -> lista sobre el cual voy a recorrer
    '''
    if type(lista) == list and len(lista) > 0:
        tipo_raza = {}

        for i in range(len(lista)):
            # -> Es una lista con las razas de c/ personaje
            razas = lista[i]["Raza"]

            for raza in razas:
                # SI NO EXISTE LA CREO
                if raza not in tipo_raza:
                    tipo_raza[raza] = 1
                # SI EXISTE LE SUMO 1
                else:
                    tipo_raza[raza] += 1

        # IMPRIME LA RAZA : VALOR DE LA RAZA
        for raza in tipo_raza:
            imprimir_dato(f"{raza}: {tipo_raza[raza]}")

    else:
        imprimir_dato("ERROR: Lista vacia")

# 3 Listar personajes por raza:
def listar_personajes_por_raza(lista:list)->None:
    '''
        Brief: Recibe como parámetro una lista iterable para agrupar por
               "Raza" , los nombres que corresponden a esa raza y poder de ataque.
                Ejemplo de salida:

            Saiyan : [{'Nombre':'Goku','Poder de ataque': 10000},
                {'Nombre':'Broly','Poder de ataque': 300000}]

        Parameters:
            lista -> lista sobre el cual voy a recorrer
    '''

    if type(lista) == list and len(lista) > 0:
        raza_personaje = {}

        for i in range(len(lista)):
            # -> Es una lista con las razas de c/ personaje
            tipo_razas = lista[i]["Raza"]

            # Creo un dict vacio. creo las claves para el dict con los valores
            dict_nombre_ataque = {}
            dict_nombre_ataque["Nombre"] = lista[i]["Nombre"]
            dict_nombre_ataque["Poder de ataque"] = lista[i]["Poder de ataque"]

            for raza in tipo_razas:
                # Si no existe le agrego el Dict dentro de una lista
                if raza not in raza_personaje:
                    raza_personaje[raza] = [dict_nombre_ataque]

                # Si existe le hago un append a raza_personaje[raza] que guarda una []
                else:
                    raza_personaje[raza].append(dict_nombre_ataque)

        # IMPRIME LA RAZA : VALOR DE LA RAZA
        for raza, nombre_poder in raza_personaje.items():
            imprimir_dato(f"{raza}: {nombre_poder}\n")

    else:
        imprimir_dato("ERROR: Lista vacia")

# 4. Listar personajes por habilidad:
def listar_por_habilidad(lista:list)->None:
    '''
        Brief: Recibe como parámetro una lista iterable, para agrupar por la
               "Habilidad" que ingrese el usuario. Agrupando nombre, raza y promedio
                de quien coinsida con esa habilidad
                Ejemplo de salida:

        Kamehameha : [
            {'Nombre': 'Goten', 'Raza': ['Saiyan', 'Humano'], 'Promedio P-Ataque | P-Pelea': 2900.0}, 
            {'Nombre': 'Yamcha', 'Raza': ['Humano'], 'Promedio P-Ataque | P-Pelea': 1150.0}, 
            {'Nombre': 'Goku', 'Raza': ['Saiyan'], 'Promedio P-Ataque | P-Pelea': 255000.0}
            ]

        Parameters:
            lista -> lista sobre el cual voy a recorrer
    '''
    if type(lista) == list and len(lista) > 0:

        set_habilidades = listar_por_dato(lista,"Habilidades")

        imprimir_dato("TIPO DE HABILIDADES")
        imprimir_dato(f"\n{set_habilidades}\n")

        # -------------------
        list_filtrada = []

        habilidad_ingresada = input("Ingrese habilidad: ")
        #VALIDO QUE EL DATO INGRESADO ESTE EN LA LISTA
        while habilidad_ingresada not in set_habilidades:
            imprimir_dato(f"LA HABILIDAD -> {habilidad_ingresada} NO EXISTE!!")
            habilidad_ingresada = input("Ingrese habilidad: ")

        # ITERO UNA LISTA 
        for i in range(len(lista)):
            list_habilidades = lista[i]["Habilidades"]
            # ITERO UNA LIST DE HABILIDADES
            for habilidad in list_habilidades:
                # BUSCO COINCIDENCIA CON EL DATO INGRESADO
                if habilidad == habilidad_ingresada:
                    dict_nombre_raza_promedio = {}

                    dict_nombre_raza_promedio["Nombre"] = lista[i]["Nombre"]
                    dict_nombre_raza_promedio["Raza"] = lista[i]["Raza"]

                    poder_ataque = lista[i]["Poder de ataque"]
                    poder_pelea = lista[i]["Poder de pelea"]

                    promedio = (poder_ataque + poder_pelea) / 2
                    dict_nombre_raza_promedio["Promedio P-Ataque | P-Pelea"] = promedio

                    list_filtrada.append(dict_nombre_raza_promedio)
                else:
                    pass
    else:
        imprimir_dato("La lista no contiene datos []")
    imprimir_dato(list_filtrada)

# 5. Jugar batalla:
def jugar_batalla(lista: list)->None:
    '''
        Brief: Recibe como parámetro una lista iterable, pide un personaje al usuario y la maquina elije uno al azar.
               compara sus 'poderes de ataque' elijiedo al ganador y lo guarda en un archivo de texto

        Parameters:
            lista -> lista sobre el cual voy a recorrer
    '''

    # LISTA NOMBRE DE PERSONAJES
    nombre_personajes = []
    contador = 0
    # ACCEDO A CADA NOMBRE EN CADA VUELTA
    for i in range(len(lista)):
        nombres = lista[i]["Nombre"]
        nombre_personajes.append(nombres)
        contador += 1

    imprimir_dato("NOMBRES DE PERSONAJES:  ")
    imprimir_dato(f"\n{nombre_personajes}\n")
    #  print(contador)

    # EL MODULO NUMPY CON LA FUNC np.random.randint(X,Y) ME GENERRA UN N° ALEATORIO CON UN RANGO
    aleatorio = np.random.randint(0, contador)
    
    personaje_maquina = lista[aleatorio]
    personaje_jugador = ""

    personaje_ingresado = input("Ingrese un personaje: ").capitalize()

    while personaje_ingresado not in nombre_personajes:
        imprimir_dato("El personaje EXISTE esta en la lista")
        personaje_ingresado = input("Ingrese un personaje: ").capitalize()

    for i in range(len(lista)):
        nombres = lista[i]["Nombre"]

        if personaje_ingresado == nombres:
            # LE ASIGNO EL DICT  
            personaje_jugador = lista[i]

    imprimir_dato(f"\n{personaje_maquina}\n")
    imprimir_dato(f"{personaje_jugador}\n")
    
    # NOMBRES
    nombre_jugador = personaje_jugador['Nombre']
    nombre_maquina = personaje_maquina['Nombre']
    
    # PODER DE ATAQUE
    poder_a_jugador = personaje_jugador['Poder de ataque']
    poder_a_maquina = personaje_maquina['Poder de ataque']

    msj_ganador = ""
    msj_perdedor = ""

    # MAYOR PODER
    if poder_a_jugador > poder_a_maquina:
        msj_ganador = nombre_jugador
    else:
        msj_ganador = nombre_maquina

    # MENOR PODER
    if poder_a_jugador < poder_a_maquina:
        msj_perdedor = nombre_jugador
    else:
        msj_perdedor = nombre_maquina

    imprimir_dato(f"""                              PODER DE ATAQUE
                {nombre_jugador}: {poder_a_jugador} -- FIGHT!! -- {nombre_maquina}: {poder_a_maquina}

                              GANADOR: {msj_ganador}
            \n""")

    # LISTA CON DATOS ANEXADOS
    list_resultado_pelea = []
    date = fecha()

    list_resultado_pelea.append(f"Fecha de la pelea -> {date}")
    list_resultado_pelea.append(f"GANADOR -> {msj_ganador}")
    list_resultado_pelea.append(f"PERDEDOR -> {msj_perdedor}")

    # ADMINISTRADOR DE CONTEXTO EN MODO ESCRITURA
    # ESCRIBO POR ITERACION EL CONTENIDO DE LA list_resultado_pelea []
    texto_txt = f"pelea_{nombre_jugador}-{nombre_maquina}"
     
    with open(f"{texto_txt}.txt",'w') as archivo:
        for i in range(len(list_resultado_pelea)):
            archivo.write(f"{list_resultado_pelea[i]}\n")

    imprimir_dato(list_resultado_pelea)

# 6. Guardar Json: 
def guarda_json(lista:list)->list:
    '''
        Brief: Recibe como parámetro una lista iterable, para agrupar por la
               "Habilidad" que ingrese el usuario. Agrupando nombre, raza y promedio
                de quien coinsida con esa habilidad
                Ejemplo de salida:

        Kamehameha : [{'Nombre': 'Goten', 'Raza': ['Saiyan', 'Humano'], 'Promedio P-Ataque / P-Pelea': 0.9333333333333333}, 
                      {'Nombre': 'Yamcha', 'Raza': ['Humano'], 'Promedio P-Ataque / P-Pelea': 0.7692307692307693}, 
                      {'Nombre': 'Goku', 'Raza': ['Saiyan'], 'Promedio P-Ataque / P-Pelea': 0.02}
                     ]

        Parameters:
            lista -> lista sobre el cual voy a recorrer
    ''' 

    habilidad_ingresada, raza_ingresada = entrada_de_input(lista)

    lista_de_coinsidencia = []

    for i in range(len(lista)):
        # PREGUNTO QUE SI COINSIDEN LOS DATOS, AGREGO ESA POSICION A LA -> lista_de_coinsidencia = []
        if raza_ingresada in lista[i]["Raza"] and habilidad_ingresada in lista[i]["Habilidades"]:
            imprimir_dato("HUBO COINCIDENCIA")
            lista_de_coinsidencia.append(lista[i])
        else:
            pass
            # imprimir_dato("NO HUBO COINCIDENCIA")
                   
    # NOMBRE NOMENCLADO
    nombre_archivo = f"{raza_ingresada}_{habilidad_ingresada}"
   
    datos_terminados = {}
    datos_terminados[nombre_archivo] = []

    if len(lista_de_coinsidencia) > 0:

        for i in range(len(lista_de_coinsidencia)):
            personajes = {}
            personajes["Nombre"] = lista_de_coinsidencia[i]["Nombre"]
            personajes["Poder de ataque"] = lista_de_coinsidencia[i]["Poder de ataque"]
            list_habilidades = lista_de_coinsidencia[i]["Habilidades"]

            habilidades_filtrada = []

            for habilidad in list_habilidades:
                # REMPLAZO habilidad_ingresada POR ""
                eliminar_habilidad = re.sub(f"{habilidad_ingresada}","",habilidad)
                eliminar_habilidad = eliminar_habilidad.strip()
                # COMO LA habilidad_ingresada ES "" NO LO AGREGA A LA LISTA
                if eliminar_habilidad != "":
                    habilidades_filtrada.append(eliminar_habilidad)

            # NUEVA CLAVE CON LA LISTA   
            personajes["Habilidades"] = habilidades_filtrada
            datos_terminados[nombre_archivo].append(personajes)
            
            # SOLO RECORRE HAS LA POSICION 1
            if i == 1:
                break
    else:
            datos_terminados[nombre_archivo].append("NO HUVO COINDIDENCIAS")

    # ADMINISTRADOR DE CONTEXTO EN MODO ESCRITURA
    with open(f"{nombre_archivo}.json","w") as archivo:
        json.dump(datos_terminados,archivo,indent = 4,ensure_ascii = False)

    return nombre_archivo

# 7. Leer Json:
def leer_json(ruta:str)->None:
    '''
        Brief: Recibe como parámetro una ruta(path)
               para abrir el archivo y mostrarlo

        Parameters:
            ruta -> Ruta del archivo para acceder
    ''' 
    # for i in range(len(lista)):
    with open(f"{ruta}.json","r") as mi_archivo:
        data = json.load(mi_archivo)

    imprimir_dato(data)

