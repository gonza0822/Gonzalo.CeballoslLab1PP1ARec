import re
import json
import random

archivocsv = "C:\\Users\\gonza\\Documents\\tecnicatura\\1A\\programacion1\\ejemplo1\\Gonzalo_Ceballos_primer_parcial\\insumos.csv"

def mostrar_datos_ordenados(lista:list):
    for elementos in lista:
        print(f'{elementos["ID"]}, {elementos["NOMBRE"]}, {elementos["MARCA"]}, {elementos["PRECIO"]}, {elementos["CARACTERISTICAS"]},')

def cargar_datos(archivo:str):
    with open(archivo, "r", encoding='utf-8') as file:
        contenido = file.read()
    lista_contenido = contenido.split("\n")
    lista_listas = []
    lista_contenido = list(filter(lambda cadenas: cadenas != "", lista_contenido))
    for insumos in lista_contenido:
        elementos = insumos.split(",")
        lista_listas.append(elementos)   
    lista_insumos = []
    for i in range(len(lista_listas)):
        diccionario_insumos = {}
        if(i == 0):
            keys = lista_listas[i]
        else:
            diccionario_insumos[keys[0]] = lista_listas[i][0]
            diccionario_insumos[keys[1]] = lista_listas[i][1]
            diccionario_insumos[keys[2]] = lista_listas[i][2]
            diccionario_insumos[keys[3]] = lista_listas[i][3]
            diccionario_insumos[keys[4]] = lista_listas[i][4]
            lista_insumos.append(diccionario_insumos)
    lista_stock = list(map(lambda insumos: random.randrange(0, 11), lista_insumos))
    for i in range(len(lista_insumos)):
        lista_insumos[i]["STOCK"] = lista_stock[i] 
    return lista_insumos


def listar_cantidad_marcas(lista:list):
    lista_marcas = set()
    diccionario_cantidad_marcas = {}
    for insumos in lista:
        lista_marcas.add(insumos["MARCA"])
    for marcas in lista_marcas:
        diccionario_cantidad_marcas[marcas] = 0
    for i in range(len(lista)):
       for marcas in lista_marcas:
           if(lista[i]["MARCA"] == marcas):
               diccionario_cantidad_marcas[marcas] += 1
    for marcas in diccionario_cantidad_marcas:
        print(f"La marca {marcas} tiene {diccionario_cantidad_marcas[marcas]} insumos")



def listar_insumos_marca(lista:list):
    lista_marcas = set()
    lista_global_insumos_marca = []
    for insumos in lista:
        lista_marcas.add(insumos["MARCA"])
    for marcas in lista_marcas:
        lista_insumos_marca = [marcas]
        for i in range(len(lista)):
            if (marcas == lista[i]["MARCA"]):
                lista_insumos_marca.append(lista[i])
        lista_global_insumos_marca.append(lista_insumos_marca)     
    for listas in lista_global_insumos_marca:
        print(f"La marca {listas[0]} tiene estos insumos: ")
        for i in range(len(listas) - 1):
            print(f'      {listas[i + 1]["NOMBRE"]} y el precio es {listas[i + 1]["PRECIO"]}')



def insumos_por_caracteristicas(lista:list):
    caracteristica = input("¿Que caracteristica desea listar?")
    caracteristica = caracteristica.capitalize()
    print(caracteristica)
    lista_insumos_caracteristicas = list(filter(lambda insumo: re.search(caracteristica, insumo["CARACTERISTICAS"]), lista))
    if(len(lista_insumos_caracteristicas) == 0):
        print("Error esa carcteristica no exite")
    else:
        print(lista_insumos_caracteristicas)
    
def listar_insumos_ordenados(lista:list):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i +1, tam):
            if (lista[i]["MARCA"] > lista[j]["MARCA"]) or ((lista[i]["MARCA"] == lista[j]["MARCA"]) and (lista[i]["PRECIO"] < lista[j]["PRECIO"])):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    mostrar_datos_ordenados(lista)

def realizar_compras(lista:list):
    flag_stock = False
    lista_compras = []
    lista_cantidades = []
    lista_marcas = set()
    for insumos in lista:
            lista_marcas.add(insumos["MARCA"])
    while True:
        lista_elementos = []
        print("Las marcas son: ")
        for marcas in lista_marcas:
            print(f"   {marcas}")
        marca_usuario = input("¿Que marca desea comprar?")
        marca_usuario = marca_usuario.lower()
        lista_elementos = list(filter(lambda elementos: marca_usuario == elementos["MARCA"].lower(), lista))
        if(len(lista_elementos) == 0):
            print("Esa marca no existe") 
            break
        print("Estos son los productos de esa marca")
        for insumos in lista_elementos:
            print(f'{insumos["ID"]} ,{insumos["NOMBRE"]}, {insumos["MARCA"]} {insumos["PRECIO"]}, {insumos["CARACTERISTICAS"]}')
        producto_usuario = input("¿Que producto desea comprar?(escriba el numero del producto)")
        try:
            cantidad_usuario = int(input("¿Cuantos desea comprar?"))
        except ValueError:
            print("Debe ingresar un numero valido")
            break
        lista_cantidades.append(cantidad_usuario)
        for i in range(len(lista_elementos)):
            if(producto_usuario == lista_elementos[i]["ID"]):
                flag_stock = True
                if (lista_elementos[i]["STOCK"] == 0 or lista_cantidades[-1] > lista_elementos[i]["STOCK"]):
                    print(f'El stock de ese producto es {lista_elementos[i]["STOCK"]}, por favor eliga menos cantidad en caso de que se pueda')
                else:
                    lista_elementos[i]["STOCK"] -= lista_cantidades[-1]
                    lista_compras.append(insumos)
                    print("Agregado al carrito")
        if(not flag_stock or len(lista_compras) == 0):
            print("Ese producto no esta en esa marca")
        eleccion_usuario = input("¿Desea seguir comprando s/n?")
        while(eleccion_usuario != "n" and eleccion_usuario != "s"):
            eleccion_usuario = input("la respuesta debe ser s(si) o n(no)")
            print(eleccion_usuario)
        if(eleccion_usuario == "n"):
            contador = 0
            total_compra = 0
            with open("texto.txt", "w", encoding="utf-8") as file:
                file.write("Compra de insumos: \n---------------------------\n")
                for i in range(len(lista_compras)):
                    contador += lista_cantidades[i]
                    precio = float(lista_compras[i]["PRECIO"].replace("$", "")) * lista_cantidades[i]
                    total_compra += precio 
                    file.write(f'{lista_compras[i]["NOMBRE"]}, {lista_compras[i]["MARCA"]}, {lista_compras[i]["CARACTERISTICAS"]},  PRECIO: {lista_compras[i]["PRECIO"]}, cantidad: {lista_cantidades[i]}\n')
                file.write(f"Cantidad de productos: {contador}\nTotal: {total_compra:.2f}")
            print("compra realizada")
            break


def guardar_json(lista:list):
    lista_alimentos = []
    for insumos in lista:
        coincidencia = re.search(r"Alimento", insumos["NOMBRE"])
        if(coincidencia):
            lista_alimentos.append(insumos)
    with open("alimentos.json", "w", encoding="utf-8") as file:
        json.dump(lista_alimentos, file, ensure_ascii=False, indent=4)


def leer_json():
    with open("alimentos.json", "r") as file:
        contenido = file.read()
        lista_alimentos = json.loads(contenido)
    mostrar_datos_ordenados(lista_alimentos)

#esta funcion solo es para la funcion actuatizar_precios
def aumentar_precios(insumos):
        aumento = 8.4
        insumos["PRECIO"] = str(round(float(insumos["PRECIO"].replace("$", "")) + (float(insumos["PRECIO"].replace("$", "")) * (aumento/100)), 2))
        return insumos

def actualizar_precios(lista:list):
    lista_actualizada = list(map(aumentar_precios, lista))
    with open(archivocsv, "w", encoding="utf-8") as file:
        file.write("\nID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
        for insumos in lista_actualizada:
            file.write(f'{insumos["ID"]},{insumos["NOMBRE"]},{insumos["MARCA"]},${insumos["PRECIO"]},{insumos["CARACTERISTICAS"]}\n')

#creamos la funcion agregar insumos marca que recibira una lista
def agregar_insumo_marca(lista:list):
    #declaramos las variables que usamos mas adelante en la funcion
    eleccion_correcta_marca = False
    caracteristicas = ""
    caracteristica_agregadas = 0
    #le pedimos al usuario que ingrese el nombre y precio del producto que va a agregar
    #y los guardamos en variables
    nombre_insumo_usuario = input("¿Cual es el nombre del producto que quiere agregar?")
    precio_insumo_usuario = input("¿Cual es el precio del producto?")
    #abrimos el archivo marcas.txt para lectura
    with open("Gonzalo_Ceballos_primer_parcial\\marcas.txt", "r") as file:
        #guardamos el contenido del archivo en contenido y lo mostramos para que el usuario vea las marcas
        contenido = file.read()
        print(f"Las marcas que puede elegir son:\n{contenido}")
        #convertimos el contenido en una lista dividida por saltos de linea y la guardamos en una variable
        lista_contenido_marcas = contenido.split("\n")
        #le quitamos las listas que quedaron con una cadena vacia para eliminar los espacios en blanco del archivo
        lista_contenido_marcas = list(filter(lambda cadenas: cadenas != "", lista_contenido_marcas))
    #le pedimos al usuario que eliga una marca
    marca_eleccion_usuario = input("¿Que marca quiere que sea su producto?")
    #la validamos en la lista con las marcas que creamos
    for marcas in lista_contenido_marcas:
        if(marca_eleccion_usuario.lower() == marcas.lower()):
            #usamos una bandera para saber que hubo la marca que eligio el usuario fue correcta
            eleccion_correcta_marca = True
            marca_eleccion_usuario = marcas
     #mientras la bandera sea false, es decir que el usuario eligio una marca incorrecta
     # le volvera a preguntar cual es la marca hasta que ingrese una correcta       
    while(not eleccion_correcta_marca):
        marca_eleccion_usuario = input("Esa marca no existe por favor ingrese una marca existente: ")
        for marcas in lista_contenido_marcas:
            if(marca_eleccion_usuario.lower() == marcas.lower()):
                eleccion_correcta_marca = True
                marca_eleccion_usuario = marcas
    #caracteristicas agregadas es una variable que sirve para saber cuantas caracteristicas agrego y no se pase de 3
    while(caracteristica_agregadas >= 0 and caracteristica_agregadas <3):
        #le decimos al usuario que agregue una caracteristica
        caracteristicas_insumo_usuario = input("¿Que caracteristicas tiene el insumo?")
        #caracteristicas contiene un string con todas las caracteristicas
        caracteristicas += caracteristicas_insumo_usuario
        #validamos si el usuario quiere seguir agregando mas caracterisitcas
        eleccion_usuario = input("¿Desea agregar otra caracteristica s/n?")
        if(eleccion_usuario == "n"):
            caracteristica_agregadas = 4
        caracteristica_agregadas +=1
    #iteramos toda la lista hasta llegar al ultimo elemento para al id sumarle uno y ese sera el id del producto nuevo
    for insumos in lista:
        id_insumos = int(insumos["ID"]) + 1
    #creamos el diccionario del producto y lo agregamos a la lista para luego retornarla
    insumo_nuevo = {
        "ID": id_insumos,
        "NOMBRE": nombre_insumo_usuario,
        "MARCA": marca_eleccion_usuario,
        "PRECIO": "$" + str(float(precio_insumo_usuario)),
        "CARACTERISTICAS": caracteristicas 
    }
    lista.append(insumo_nuevo)
    print(lista)
    return lista

#creamos la funcion guardar datos actualizados que recibira una lista
def guardar_datos_actualizados(lista:list):
    #le pedimos al usuario que ingrese el nombre del archivo en donde se va a guardar y la extension
    #luego pasamos ese archivo a minuscula
    archivo_usuario = input("¿Que nombre desea ponerle al archivo donde se guardara los datos?")
    opcion_usuario = input("¿En que tipo de archivo desea guardar los datos(CSV o JSON)?")
    opcion_usuario = opcion_usuario.lower()
    #dependiendo que extension eligio el usuario lo guardamos en diferentes archivos
    if(opcion_usuario == "csv"):
        #abrimos el archivo en escritura y le escribimos iterando la lista los insumos en el formato csv
        with open(archivo_usuario+".csv", "w", encoding="utf-8") as file:
            file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
            for insumos in lista:
                file.write(f'{insumos["ID"]},{insumos["NOMBRE"]},{insumos["MARCA"]},${insumos["PRECIO"]},{insumos["CARACTERISTICAS"]}\n')
    elif(opcion_usuario == "json"):
        #abrimos el archivo en escritura y utilizamos dump para agregar la lista al archivo json
        with open(archivo_usuario+".json", "w", encoding="utf-8") as file:
            json.dump(lista, file, ensure_ascii=False, indent=4)

#creamos la funcion opcion_stock_marca que recibira un lista
def opcion_stock_marca(lista:list):
    stock_total = 0
    flag_marca = False
    lista_global_insumos_stock = []
    #creamos un set que guardara las marcas
    lista_marcas = set()
    for insumos in lista:
        lista_marcas.add(insumos["MARCA"])
    #el usuario elige una marca y validamos que sea correcta con una bandera
    print("Las marcas son: ")
    for marcas in lista_marcas:
        print(f"   {marcas}")
    marca_usuario = input("De que marca desea saber el stock: ")
    marca_usuario = marca_usuario.lower()
    for marcas in lista_marcas:
        if marca_usuario == marcas.lower():
            flag_marca = True
    
    while (not flag_marca):
        marca_usuario = input("Esa marca no existe, eliga otra: ")
        marca_usuario = marca_usuario.lower()
        for marcas in lista_marcas:
            if marca_usuario == marcas.lower():
                flag_marca = True
    #creamos una lista de listas en donde cada una de ellas contiene el nombre y el stock de cada producto de la marca elegida
    for insumos in lista:
        if marca_usuario == insumos["MARCA"].lower():
            lista_insumo_stock = [insumos["NOMBRE"], insumos["STOCK"]]
            lista_global_insumos_stock.append(lista_insumo_stock)
    #imprimimos los productos, el stock de cada uno y el stock total que lo obtenemos al sumar el segundo elemento de cada lista en la lista
    print(f"La marca {marca_usuario} tiene un stock:")
    for insumos in lista_global_insumos_stock:
        print(f" producto: {insumos[0]}, stock: {insumos[1]}")
        stock_total += insumos[1]
    print(f"Stock total: {stock_total}")
    
#creamos la funcion imprimir_bajo_stock que recibira un lista
def imprimir_bajo_stock(lista:list):
    #le pedimos al usuario que ingrese un nombre para el archivo
    contador = 0
    archivo_usuario = input("¿Que nombre desea ponerle al archivo donde se guardara los datos?")
    #abrimos el archivo agregandole el formato csv en modo escritura
    with open(archivo_usuario+".csv", "w", encoding="utf-8") as file:
            file.write("ID,NOMBRE,STOCK\n")
            #recorremos la lista de insumos y los que tengan stock menor o igual a 2 se listaran en el archivo
            for i in range(len(lista)):
                if(lista[i]["STOCK"] <= 2):
                    contador += 1
                    file.write(f'{contador},{lista[i]["NOMBRE"]},{lista[i]["STOCK"]}\n')


        





