import datetime #ME REGRESA LA HORA Y FECHA DEL SISTEMA
import re
import json

# VALIDAR ENTERO
def validar_entero(entero: str)->bool:
    '''
        Brief: Valida si es o no un numero entero

        Parameters:
            entero -> Parametro recibido a validar

        Return: Retorna True si se cumple la condicion si no False

    '''
    if entero.isdigit():
         return True
        #  print("si")
    else:
        return False
        # print("no")

# CASTEAR ENTERO
def casteo_entero(entero: str)->int:
    '''
        Brief: Valida si es o no un numero entero y devuelve un entero

        Parameters:
            entero -> Parametro recibido a castear

        Return: Retorna un int si es un entero, sino retorna un -1

    '''
    retorno_int = validar_entero(entero)

    if retorno_int:
        casteo = int(entero)
        return casteo
    else:
        return -1
    
# IMPRIME DATO
def imprimir_dato(string: str)->None:
    '''
        Brief: Imprime datos que recibe por parametro

        Parameters:
            string -> Cadena que voy a imprimir

    '''
    print(string)

# MUESTRA ACTUAL FECHA
def fecha()->list:
    '''
        Brief: La funcion utiliza un metodo datetime que me retorna la fecha y la hora del sistema en ese momento,
               ala cual la formateo selecionando solo la fecha

        Return: Retorna un lista con la fecha

    '''
    # EL MODULO DATETIME CON LA FUNC datetime.now() ME REGRESA LA HORA Y FECHA DEL SISTEMA
    fecha = datetime.datetime.now()
    fecha = str(fecha)
    fecha = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}",fecha)

    return fecha

# ELIMINA UN CARACTER ESPECIFICO
def elimina_caracter(simbolo:str,cadena:str)->list:
    '''
        Brief: Recibe como parámetro una cadena que va a formatearse y caracter/simbolo
               eliminado el [caracter/simbolo] ingresado

        Parameters:
            cadena -> Parametro sobre el cual voy a trabajar
            simbolo -> Parametro para usar una expresion regular

        Return: Una lista con caracteres deseados
    '''
    separador = re.split(simbolo, cadena)
    return separador

# ELIMINA UN SIMBOLOS Y ESPACIOS
def eleminar_simbolo_espacios(cadena:str)->list:
    '''
        Brief: Recibe como parámetro una cadena que va a formatearse sacando carateres
               no deseados, crea una lista por el retorno de la funcion elimina_caracter()
               y la recorre sacando los espacios

        Parameters:
            cadena -> Parametro sobre el cual voy a trabajar

        Return: Una lista normalizada
    '''
    lista_normalizada = []

    quita_simbolos = re.sub('\$%', '', cadena)
    # quita_simbolos = re.sub('\\^\\s+|\\s+$','', quita_simbolos)
    lista_filtrada = elimina_caracter('\|', quita_simbolos) 

    for cadena in lista_filtrada:
        cadena = cadena.strip()
        lista_normalizada.append(cadena)

    return lista_normalizada

# CREA UNA LISTA POR KEY
def listar_por_dato(lista:list,key:str)->set:
    '''
        Brief: Recibe como parámetro una lista para realizar la busqueda de una key pasado 
               como segundo paramtro

        Parameters:
            Lista -> Lista sobre el cual voy a trabajar
            Key -> Key con la que se realizara la busqueda

        Return: Un set filtrado
    '''
    tipo_de_habilidades = []
    # ACCEDO A CADA LISTA DE HABILIDAD EN CADA VUELTA
    for i in range(len(lista)):
        list_habilidades = lista[i][key]

        # AGREGO UNA HABILIDAD EN CADA VUELTA
        for habilidad in list_habilidades:
            tipo_de_habilidades.append(habilidad)

    # ELIMINO REPETIDOS E IMPRIMO
    set_habilidades = set(tipo_de_habilidades)

    return set_habilidades
    
# ENTRADA DE DATOS Y VALIDA QUE EXISTAN
def entrada_de_input(lista:list)->str:
    '''
        Brief: Recibe como parámetro una lista para set utilizada por otras funciones para 
               hacer validaciones de que exista ese dato en la lista

        Parameters:
            Lista -> Lista sobre la cual se va filtrar y comparar

        Return: Retorna dos cadenas [habilidad_ingre , raza_ingre]
    '''
    set_habilidades = listar_por_dato(lista,"Habilidades")
    set_razas = listar_por_dato(lista,"Raza")

    imprimir_dato(f"RAZAS\n {set_razas}\n")
    imprimir_dato(f"HABILIDADES\n {set_habilidades}\n")

    # INGRESO DE DATOS
    raza_ingre = input("Ingrese una RAZA:  ")
    habilidad_ingre = input("Ingrese una HABILIDAD:  ")
    # VALIDO QUE NO SEA UN ESPACIO VACIO
    while raza_ingre not in set_razas or habilidad_ingre not in set_habilidades: 
        print("ERROR ingrese nuevamente")
        raza_ingre = input("Reingrese una RAZA:  ")
        habilidad_ingre = input("Reingrese una HABILIDAD:  ")

    return habilidad_ingre ,raza_ingre

#  ADMINISTRADOR DE CONTEXTO TXT CSV
def administrador_de_contexto(nombre_archivo:str,formato_archivo:str,lista:list)->None:
    '''
        Brief: Recibe tres parámetros creando un archivo TXT O CSV.

        Parameters:
            Nombre_archivo -> Es nombre que va a tener el archivo.
            Formato_archivo -> Selecciona el formato del archivo TXT O CSV . 
            Lista -> Sobre la cual se va a iterar agregando cada linea.

    '''
    with open(f"{nombre_archivo}.{formato_archivo}","w") as archivo:
        for i in range(len(lista)):
            archivo.write(f"{lista[i]}\n")

#  ADMINISTRADOR DE CONTEXTO JSON
def administrador_de_contexto_json(nombre_archivo:str,modo_apertuta:str,diccionario:dict={})->None:
    '''
        Brief: Recibe tres parámetro crea un archivo JSON y tambien leer el archivo segun los parametro pasados.

        Parameters:
            Nombre_archivo -> Es con el cual se va a leer un archivo o crearlo.
            Modo_apertuta -> Selecciona el modo escritura o lectura.
            Diccionario -> El que se va agregar al archivo opcionalmente del Modo_apertuta.

    '''
    match modo_apertuta:
        case "w":
            # ADMINISTRADOR DE CONTEXTO EN MODO ESCRITURA
            with open(f"{nombre_archivo}.json","w") as archivo:
                json.dump(diccionario,archivo,indent = 4,ensure_ascii = False)

        case "r":
            # ADMINISTRADOR DE CONTEXTO EN MODO LECTURA
            with open(f"{nombre_archivo}.json","r") as mi_archivo:
                lectura_data = json.load(mi_archivo)
                imprimir_dato(lectura_data)

# AGREGA COMA    
def agregar_coma(cadena:str)->str:
    '''
        Brief: Recibe parámetros una cadena para agragar una caracter -> ','.

        Parameters:
            cadena -> Cadena que va a modificar
        
        Return: Una cadena modificada 

    '''
    cadena_retorno = f"{cadena},"
    return cadena_retorno

#  SACAR PORSENTAJE
def sacar_porcentaje(porsentaje:int,numero_a_operar:float)->float:
    '''
        Brief: Recibe dos parámetros para calcular el porsentaje 

        Parameters:
            porsentaje -> valor que se va a usar para calcular el porsentaje
            numero_a_operar -> Valor base para hacer la operacion
        
        Return: Una cadena modificada 
    '''
    porsentaje_retorno = porsentaje * numero_a_operar / 100
    return porsentaje_retorno
