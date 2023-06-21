import re
import json
import os

from funciones import *

archivocsv = "C:\\Users\\gonza\\Documents\\tecnicatura\\1A\\programacion1\\ejemplo1\\Gonzalo_Ceballos_primer_parcial\\insumos.csv"

def menu():
    flag_cargar_datos = False
    flag_JSON = False
    lista = cargar_datos(archivocsv)

    while True:
        os.system("cls")
        print("cerrar esto")
        print("""*** Menu de opciones ***
    --------------------------
    1-Cargar datos desde archivo
    2-Listar cantidad de insumos por marca
    3-Listar insumos por marca
    4-Buscar insumo por caracteristica
    5-Listar insumos ordenados
    6-Realizar compras
    7-Guardar en formaro JSON
    8-Leer desde formato JSON
    9-Actualizar precios
    10-Agregar insumo
    11-guardar datos actualizados en csv o json
    12-Mostrar el stock total de los productos de una marca
    13-Agregar en un archivo csv los productos que tengan 2 o menos stock
    14-Salir del programa""")
        opcion = input("Ingrese una opcion: ")
        while(not opcion.isdigit() or (float(opcion) < 1 or float(opcion) > 14)):
            opcion = input("No es una opcion valida, por favor ingrese otra: ")

        match(opcion):
            case "1":
                flag_cargar_datos = True
                lista
            case "2":
                if(flag_cargar_datos):
                    listar_cantidad_marcas(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "3":
                if(flag_cargar_datos):
                    listar_insumos_marca(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "4":
                if(flag_cargar_datos):
                    insumos_por_caracteristicas(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "5":
                if(flag_cargar_datos):
                    listar_insumos_ordenados(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "6":
                if(flag_cargar_datos):
                    realizar_compras(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "7":
                flag_JSON = True
                if(flag_cargar_datos):
                    guardar_json(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "8":
                if(flag_JSON):
                    leer_json()
                else:
                    print("Para realizar esto debes primero guardar los datos en un archivo JSON")
            case "9":
                if(flag_cargar_datos):
                    actualizar_precios(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "10":
                #validamos con una bandera que la lista fue cargada
                if(flag_cargar_datos):
                    lista = agregar_insumo_marca(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "11":
                 #validamos con una bandera que la lista fue cargada
                if(flag_cargar_datos):
                    guardar_datos_actualizados(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "12":
                if(flag_cargar_datos):
                    opcion_stock_marca(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "13":
                if(flag_cargar_datos):
                    imprimir_bajo_stock(lista)
                else:
                    print("Para realizar esto debes primero cargar los datos")
            case "14":
                print("Saliste del programa")
                break

        os.system("pause")


menu()
