'''
Eduardo Cruz
DIV B
Parcial

Necesitamos crear un programa para poder gestionar nuestra colección de personajes de Dragon Ball. Para
ello, disponemos de un archivo CSV con el siguiente formato:

Id, Nombre, Raza, Poder de pelea, Poder de ataque, Habilidades
Por ejemplo:
"1", "Goku", "Saiyan", "500000", "10000", "Kamehameha|$%Genki Dama|$%Super Saiyan"


'''

from os import system
system("cls")    
from funciones_aritmeticas_parcial import *


ruta_dos = "D:\\programacion\\UTN\\parcial_01\\Parcial_1\\DBZ - DBZ (1).csv"


def iniciar_programa(ruta:str):
    '''
        Brief: Ejecuta programa ultilados la funciones 'stark_'
        la variable 'retorno' recibe un entero validado el cual sera
        el parametro del 'match' para embocar ala funcion correcta
        segun la opcion del menu

        Parameters:
            ruta -> Ruta sobre la cual voy a acceder los datos
    
    '''

    seguir = True
    ban = True
    msj_parseado = "Datos parseados con EXITO!!"
    msj_error = "Seleccione opcicion 1 para 'Parsear Los Datos'"
    
    while seguir == True:
        retorno = menu_principal()

        while retorno < 0 or retorno > 8:
            imprimir_dato("Opcion incorrecta. REINGRESE UNA OPCION: ")
            retorno = menu_principal()
            
        match retorno:
            case 1:
                # Traer datos desde archivo:
                if ban == True:            
                    lista_retorno = parser_csv(ruta_dos)
                    imprimir_dato(msj_parseado)
                    ban = False
            case 2:
                # Listar cantidad por raza:
                if ban == False:
                    listar_cantidad_raza(lista_retorno)
                else:
                    imprimir_dato(msj_error)
            case 3:                
                # Listar personajes por raza:
                if ban == False:
                    listar_personajes_por_raza(lista_retorno)
                else:
                    imprimir_dato(msj_error) 
            case 4:
                # Listar personajes por habilidad:
                if ban == False:
                    listar_por_habilidad(lista_retorno)
                else:
                    imprimir_dato(msj_error)
            case 5:
                # Jugar batalla:
                if ban == False:
                    jugar_batalla(lista_retorno)
                else:
                    imprimir_dato(msj_error)
            case 6:
                # Guardar Json:
                if ban == False:
                    prueba = guarda_json(lista_retorno)
                else:
                    imprimir_dato(msj_error) 
            case 7:
                # Leer Json:
                if ban == False:
                    leer_json(prueba)
                else:
                    imprimir_dato(msj_error)
            case 8:
                #  Salir del programa.
                 seguir = False

iniciar_programa(ruta_dos)  