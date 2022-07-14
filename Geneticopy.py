# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 00:33:12 2021

@author: JParra

Compilado en spyder, python 3.8
"""

import csv
import itertools
import sys
import random
import pandas as pd
from matplotlib import pyplot as plt


#id =0, nombre =1 autor=2 tipo= 3, velocidad=4 contable=5 bailable=6 likes=7 dislikes=8
#rating=9,vistas=10,duracion=11,eficacia=11,cantable=12, baible=13
#evento = eventos[random.randint(0, len(eventos)-1)]
#lugar = lugar[random.randint(0, len(lugar)-1)]

""Delaracion de parametros para funcionamiento del genetico""

""guardado de 
    historial de generaciones
    mejor generacion
    promedio generacion""
histGen = []
listageneraciones = []
promedioGen = []

""Variables de acuerdo a evento y generito""
lugar = 'Toluca'
#evento = 'boda'
edad = '15-30'
tamgenes = 30
principio = 15 
generacionesMax = 100
genes = []
probabilidad = 1 #
eventos = ['comunion','15 años','boda','cumpleaños']
lugares= ['Metepec','Toluca','San gaspar','Rayon','Lerma','Ocoyoacac','Tianguistenco','Gualupita','Tenango']
lugCancion ={
           'Cumbia':['Metepec','Toluca','San Gaspar','Rayon','Lerma','Ocoyoacac','Tianguistenco','Gualupita','Tenango'],
           'Electro Cumbia':['Metepec','Toluca','San Gaspar','Rayon','Lerma','Ocoyoacac','Tianguistenco','Gualupita','Tenango'],
           'Banda':['Toluca','Metepec','San Gaspar'],
           'Sonidera':['Gualupita','Santiago','Metepec','Toluca'],
           'Salsa':['Metepec','Toluca','San Gaspar','Rayon','Lerma','Ocoyoacac','Tianguistenco','Gualupita','Tenango'],
           'Danzon':['Metepec','Toluca','San Gaspar','Rayon','Lerma','Ocoyoacac','Tianguistenco','Gualupita','Tenango']
           }
edadCancion ={
           'Cumbia':['15-30','30-40','40-100'],
           'Electro Cumbia':['15-30'],
           'Banda':['15-30','30-40'],
           'Sonidera':['15-30','30-40'],
           'Salsa':['30-40'],
           'Danzon':['30-40','40-100']
           }
edades = [15,30,40,100]

""Archivo de lista de canciones ""
ruta = 'C:/Users/JParra/Documents/9noSemestre/Computo-Evolutivo/Proyecto/lista.xlsx'
tamanio = 15 
cabeceras= ['id','nombre','autor','tipo','velocidad','rating','cantable','bailable']
eficiencia = [
              ['tipo','lugar','edades','cancion'],
              ['Todos','15-30,30-40'],
              ['Toluca','Metepec' ,'San gaspar','15-30,30-40'],
              ['Gualupita' ,'Santiago','Metepec','Toluca','30-40'],
              ['Todos , 15-30, 30-40, 40-100']
              ]



"Se genera la lista de canciones"
def generarListas(excel):
    canciones = []
    for i in range(30):
        canciones.append([])
        for n in range(len(cabeceras)):
            canciones[i].append(excel[cabeceras[n]][i])
            #print(excel[cabeceras[n]][i])
    return canciones
            

"Seleccion mediante el metodo de ruleta"        
def seleccionRuleta(canciones,eficiencia):
    #print("Ruleta")
    #print(eficiencia)
    acumulados = []
    acumulado = 0
    #print("eficiencia")
    #print(eficiencia)
    for i in range(len(eficiencia)):
        acumulado += eficiencia[i]
        acumulados.append(acumulado)
    #print(canciones)
    #print("acumulados")
    #print(acumulados)
    #print(acumulado)
    aleatorio = random.randrange(1, acumulado)
    print("Acumulados")
    print(acumulados)
    print("Aleatorio",aleatorio)
    #print("Aletorio = ",aleatorio)
    for i in range(len(acumulados)):
        #print("interaccion",i)
        if (aleatorio < acumulados[i]):
            #print ("id",canciones[i], "Aleatorio",aleatorio,"acumulado",acumulados[i])
            return i                        
        #else:
            #print ("Rechazado",canciones[i][0], "Aleatorio",aleatorio,"acumulado",acumulados[i])

""

#Generacion de  padres aleatorios , primera generacion
def padreAleatorio():
    padre = []
    while (len(padre) != 15):
        aleatorio = random.randrange(1, tamgenes)
        #print("Aleatorio",aleatorio)
        #print(padre)
        if (not aleatorio in  padre):
            #print("Agregando aleatorio")
            padre.append(aleatorio)
            #print(padre)
    return padre

#Retorna las caracteristicas de una lista de ids
def traerDatos(padre):
    padreDat = []
    #Traer datos mejorar busqueda
    for idcancion in padre:
        for i in range(tamgenes): ###############V
            #print("Gen",genes[i][0],"idcancion",idcancion)
            if(genes[i][0] == idcancion):
                padreDat.append(genes[i])    
    return padreDat

#Retorna una lista con las aptitudes de las canciones
def aptitud(canciones):
    aptitudTotal = []
    eflugar=0
    efedad=0
    for i in range(len(canciones)):
        #print("contador aptitud",i)
        eflugar = 20 if lugar in lugCancion.get(canciones[i][3]) else 0
        efedad= 20 if edad in edadCancion.get(canciones[i][3]) else 0
        #print("lugar",eflugar)    
        #print("edad",efedad)    
        aptitudTotal.append(canciones[i][5]+canciones[i][6]+canciones[i][7]+efedad+eflugar)
#        print("id:", canciones[i][0] , "eficiencia", canciones[i][5]+canciones[i][6]+canciones[i][7]+efedad+eflugar)
        #print("Metodo apitud")
        #print(aptitudTotal)
    return aptitudTotal         
  
    
  
#Cruza por ciclos, se rompe el ciclo  
def cruzaCiclos(padre1,padre2):
    print("Entrando a ciclos")
    indices = []
    indice = random.randrange(0,principio-1)
    inicial = padre1[indice]
    numero1 = padre1[indice]
    aux =1000
    cont = 0
    indices.append(indice)
    print("numeroInicial",numero1)
    print("indice",indice)
    while(aux != inicial ):
        cont += 1
        print("contador ",cont)
        if(numero1 in padre2):
            
            indice = padre2.index(numero1)
            print("Indice ",indice)
            indices.append(indice)
            
            numero1 = padre1[indice]
            aux = padre1[indice]
            print("numero siguiente ",numero1)
        
        else:
            print("ERROR EN CRUZA POR CICLOS NO HAY CICLO")
            aux = 0
            inicial = 0
    print("Indices")
    print(indices)
    hijo1 = []
    hijo2 = []
    
    for i in range(principio):
        if(i in indices):
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        else:
            hijo2.append(padre1[i])
            hijo1.append(padre2[i])
    print("Hijo 1")
    print(hijo1)
    print("Hijo 2")
    print(hijo2)
        
        
#Cruza por emparejamiento parcial
def cruzaEmparejamientoParcial(padre1,padre2):
    repetido1 = True
    repetido2 = True
    repite = True
    
    print("Padre 1")
    print(padre1)
    print("Padre 2")
    print(padre2)
    
    
    while(repite):
        #print("Entrando")
        #print(++contador)
        corte1 = random.randrange(0,principio-1)
        corte2 = random.randrange(0,principio-1)
        if (corte1 == corte2):
            corte2 = random.randrange(0,14)
        if (corte2 < corte1):
            aux = corte1
            corte1 = corte2
            corte2 = aux
        #corte1=8
        #corte2=13       
        print("corte1",corte1,"corte2",corte2)
        sublista1 = padre1[corte1:corte2]
        sublista2 = padre2[corte1:corte2]
        print("sublista1")
        print(sublista1)
        print("sublista2")
        print(sublista2)
        hijo1 = []
        hijo2 = []
        #-----------------Proceso de creacion de hijos----------------
        for i in range(len(padre1)):
            #-----------------hijo 1----------------
            if(i < corte1 or i> corte2-1):
                if(not padre1[i] in sublista2):
                    hijo1.append(padre1[i])
                else:
                    indice = padre2.index(padre1[i])
                    hijo1.append(padre1[indice])
            else:
                hijo1.append(padre2[i])
            #--------------hijo 2-----------------
            if(i < corte1 or i> corte2-1):
                if(not padre2[i] in sublista1):
                    hijo2.append(padre2[i])
                else:
                    indice = padre1.index(padre2[i])
                    hijo2.append(padre2[indice])
            else:
                hijo2.append(padre1[i])
        """
        
        print("Corte 1")
        print(corte1)
        print("Corte 2")
        print(corte2)
        """
        print("Hijo 1")
        repetido1 = evaluaHijo(hijo1)
        print("Hijo 2")
        repetido2 = evaluaHijo(hijo2)
        if(repetido1 == False and repetido2 == False):
            repite = False
    print("*****************************AMBOS HIJOS CORRECTOS***********************************")
    return hijo1,hijo2

#Verifica si hay algun dato repetido en la permutacion, se llama en cruza
def evaluaHijo(hijo1):
    for j in range(len(hijo1)):
        #print("elemento: ",elementos[i][j],"repetido: ", elementos[i].count(elementos[i][j]))
        if(hijo1.count(hijo1[j]) > 1 ):
            print("********REPETIDO EN CRUZA***************")
            print(hijo1) 
            return True
    print("----------------------------------HIJO CORRECTO---------------------------------")
    print(hijo1) 
    return False

#Mutacion por intercambio 
def mutacionIntercambio(padre,probabilidad):
    #muta = probabilidad * 100
    prob = probabilidad *10
    for i in range(len(padre)):
        aleat = random.randrange(0, 1000)
        if(aleat <=prob):
            aleatorio = random.randrange(0,len(padre))
            aux = padre[i] 
            padre[i] = padre[aleatorio]
            padre[aleatorio] = aux
    return padre
            
#guarda en listagen,promgen,histGen
def guardaDatos(generacion,padres,aptitudes):
    datos = []
    print("Generacion",generacion)
    print("Padres guarda: ", len(padres))
    print(padres)
    print("aptitudes guarda", len(aptitudes))
    print(aptitudes)
    indice = 0
    numero = 0
    
    
   ##Guarda generacion,individuo,promedio 
    for i in range(len(aptitudes)):
        if(aptitudes[i] > numero):
            numero = aptitudes[i]
            indice = i
    datos.append(generacion)
    datos.append(padres[indice])
    datos.append(numero)
    print("aptitudes")
    #input("aptitudes")
    
    listageneraciones.append(generacion)
    promedioGen.append(sum(aptitudes)/len(aptitudes))
    #datosprom = []
    #datosprom.append(generacion)
    #datosprom.append(sum(aptitudes)/len(aptitudes))
    #promedioGen.append(datosprom)
    histGen.append(datos)
    
#Verifica que no haya datos repetidos 
def evaluaElementos(elementos,modulo):
    for i in range(len(elementos)):
        print("Elemento numero: ",i)
        for j in range(len(elementos[i])):
            #print("elemento: ",elementos[i][j],"repetido: ", elementos[i].count(elementos[i][j]))
            
            
            if(elementos[i].count(elementos[i][j]) > 1 ):
                print(modulo)
                print("********REPETIDO EVALUA ELEMENTOS***************")
                
                print("Elemento" )
                print(elementos[i]) 
                sys.exit()
            

#Graficacion de promedios
def graficarPromedios(listaPromedios, listaIdes):
    plt.title("Promedios por generación", fontsize=20)
    plt.plot(listaIdes, listaPromedios, marker="o", color="red", label="Promedios por generación")
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Aptitud",fontsize=15)
    plt.legend()
    plt.show()

def graficarIndividuos(listaMejores, listaIdes):
    plt.title("Mejores individuos por generación", fontsize=20)
    plt.plot(listaIdes, listaMejores, marker="o", color="blue", label="Mejores individuos por generación")
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Aptitud",fontsize=15)
    plt.legend()
    plt.show()

def graficarf(listaMejores, listaPromedios, listaIdes):
    plt.title("Mejores individuos VS Promedios por generación", fontsize=20)
    plt.plot(listaIdes, listaPromedios, marker="o", color="red", label="Promedios por generación")
    plt.plot(listaIdes, listaMejores, marker="o", color="blue", label="Mejores individuos por generación")
    plt.xlabel("Generación", fontsize=15)
    plt.ylabel("Aptitud",fontsize=15)
    plt.legend()
    plt.show()    
       
    
#Main del genetico
if __name__ == "__main__":
    excel = pd.read_excel(ruta, sheet_name='lista')    
    genes= generarListas(excel)
    """
    print("Generando padre aleatorio 1")
    padre1 = padreAleatorio()
    print("Genero Padre aleatorio")
    #padre1 = [15, 2, 27, 12, 26, 5, 22, 14, 19, 9, 10, 17, 7, 18, 21]
    padreDat1 = traerDatos(padre1)
    print(padre1)
    print("Generando padre aleatorio 2")
    padre2 = padreAleatorio()
    #padre2  = [25, 13, 10, 23, 24, 14, 19, 17, 7, 4, 18, 15, 27, 9, 20]
    padreDat2 = traerDatos(padre2)
    print(padre2)
    print(padreDat2)
    #aptitud(padreDat2)
    """
    ##GENERACION DE PADRES
    listapadres = []
    #-------------------------------Generacion de padres--------------------------------------
    for i in range(16):
        listapadres.append(padreAleatorio())
        
    evaluaElementos(listapadres,"generacion padres")        
    print("Padres validados")
    #for i in range(len(listapadres)):
    #    print(listapadres[i])
    #input("Padres")
    
    generacion = 0
    #--------------------------------------Generaciones-----------------------------------------------
    #correcto
    while(generacion < generacionesMax):
        listaapt = []
        aptitudes = [] #listas 
        apt = []
        print("PAdres")
        print(listapadres)
        
        generacion = generacion + 1
        #print("--------------------------Generacion:", generacion,"--------------------------")
        #input()
        
     #-------------------------------Generacion de aptitudes--------------------------------------
        for i in range(len(listapadres)):
            listadatos = traerDatos(listapadres[i])
            #print(listadatos)
            apt = aptitud(listadatos)
            #print("Aptitud")
            #print(aptitud)
            aptitudes.append(apt)
            print("aptitudes")
            listaapt.append(sum(apt)/len(apt))
        indices = []
        for i in range(len(aptitudes)):
            print(aptitudes[i])
        #input("aptitudes")
            
        guardaDatos(generacion, listapadres, listaapt)
        
      #-------------------------------Seleccion ruleta--------------------------------------
      #
        for i in range(len(listapadres)):
            indices.append(seleccionRuleta(listapadres[i],aptitudes[i]))
            print(indices[i])
        #print("Indices")
        #print(indices)
        
        #print("Generacion de hijos")
        evaluaElementos(listapadres,"generacion hijos")        
        
        
       # -------------------------------Generacion de cruzas--------------------------------------"""
        
        indices1 = indices[0:8]
        indices2 = indices[8:int(len(indices))]
        #print(indices[0:8])
        #print(indices[8:int(len(indices))])
        print(indices)
        #input("Seleccion Ruleta")
        print(indices1)
        print(indices2)
        listHijos = []
        for i in range(len(indices1)):
            hijo1, hijo2 = cruzaEmparejamientoParcial(listapadres[indices1[i]], listapadres[indices2[i]])
            listHijos.append(hijo1)
            listHijos.append(hijo2)
        for i in range(len(listHijos)):
            print(listHijos[i])
        #input("cruza")
        #print("Cruza ")
        #print("Generacion",generacion)
        evaluaElementos(listHijos,"Cruza")        
    
        # -------------------------------Mutacion--------------
        
        for i in range(len(listHijos)):
            listHijos[i] = mutacionIntercambio(listHijos[i], 1)
            
        print("Mutacion")
        
        #evaluaElementos(listHijos)        
        
       # -------------------------------Preparando siguiente generacion--------------------------------------"""
        #print("Padres")
        #print(listapadres)
        #print("Hijos")
        #print(listHijos)
        listapadres.clear()
        listapadres= listHijos.copy()
        listHijos.clear()
        #listaapt = []
        
        print("Nuevos Padres")
        print(listapadres)
        
    
    #print("Historial Generaciones")    
    #print(histGen)
    #print("Lista Generaciones", len(listageneraciones))    
    #print(listageneraciones)
    #print("Promedio Generaciones", len(promedioGen))    
    #print(promedioGen)
    mejorProm = []
    
    for i in range(len(histGen)):
        mejorProm.append(histGen[i][2])

    """
    print("Mejor Promedio")
    print(mejorProm)
    print("mejor Promedio tam",len(mejorProm))
    """
    #graficarPromedios(mejorProm, listageneraciones)
    #graficarPromedios(promedioGen, listageneraciones)
    graficarf(mejorProm,promedioGen,listageneraciones)
    
    
    numero = 0 
    indice = 0
    for i in range(len(histGen)):
        if(histGen[indice][2] < histGen[i][2]):
            numero = histGen[i][2]
            indice = i            
    #print("*********************HISTORIAL************************")
    #for i in range(len(histGen)):
    #    print(histGen[i])
    print("----------------Mejor lista--------------")
    print("generacion",histGen[indice][0])
    print("Lista")
    print(histGen[indice][1])
    print("Aptitud",histGen[indice][2])
    print("Numero de Generacion",indice)
    #listacan = traerDatos(histGen[indice][1])
    #print(listacan)
    """
    print("Promedio Gen")
    print(promedioGen)        
    print("Lista Generaciones")
    print(listageneraciones)
    """
    finales = traerDatos(histGen[indice][1])
    for i in range(len(finales)):
        print(finales[i])
    
    
    
    