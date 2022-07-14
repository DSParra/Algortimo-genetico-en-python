# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 02:49:55 2021

@author: JParra
"""
import csv
import itertools
import sys
import random
import pandas as pd



histGen = []
listageneraciones = []
promedioGen = []
lugar = 'Toluca'
evento = 'boda'
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




    
def cruzaEmparejamientoParcial(padre1,padre2):
    repetido1 = True
    repetido2 = True
    while(repetido1 and repetido2):
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
        #print("corte1",corte1,"corte2",corte2)
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
        print("Padre 1")
        print(padre1)
        print("Padre 2")
        print(padre2)
        print("Corte 1")
        print(corte1)
        print("Corte 2")
        print(corte2)
        """
        print("Hijo 1")
        repetido1 = evaluaHijo(hijo1)
        print("Hijo 2")
        repetido2 = evaluaHijo(hijo2)
    return hijo1,hijo2
    
def evaluaHijo(hijo1):
    for j in range(len(hijo1)):
        #print("elemento: ",elementos[i][j],"repetido: ", elementos[i].count(elementos[i][j]))
        if(hijo1.count(hijo1[j]) > 1 ):
            print("********REPETIDO EN CRUZA***************")
            print(hijo1) 
            return False
    print("----------------------------------HIJO CORRECTO---------------------------------")
    print(hijo1) 
    return True

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
        if (i==0 ):
            numero  = aptitudes[i]
        elif (aptitudes[i] > numero):
            numero = aptitudes[i]
            indice = i
    datos.append(generacion)
    datos.append(padres[indice])
    datos.append(aptitudes[i])
    
    listageneraciones.append(generacion)
    promedioGen.append(sum(aptitudes)/len(aptitudes))
    #datosprom = []
    #datosprom.append(generacion)
    #datosprom.append(sum(aptitudes)/len(aptitudes))
    #promedioGen.append(datosprom)
    histGen.append(datos)



def padreAleatorio():
    padre = []
    while (len(padre) != 15):
        aleatorio = random.randrange(1, 30)
        #print("Aleatorio",aleatorio)
        print(padre)
        if (not aleatorio in  padre):
            #print("Agregando aleatorio")
            padre.append(aleatorio)
            #print(padre)
    return padre

def traerDatos(padre):
    padreDat = []
    #Traer datos mejorar busqueda
    for idcancion in padre:
        for i in range(tamgenes): ###############V
            #print("Gen",genes[i][0],"idcancion",idcancion)
            if(genes[i][0] == idcancion):
                padreDat.append(genes[i])    
    return padreDat

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
    #print("Aletorio = ",aleatorio)
    for i in range(len(acumulados)):
        #print("interaccion",i)
        if (aleatorio < acumulados[i]):
            print ("id",canciones[i], "Aleatorio",aleatorio,"acumulado",acumulados[i])
            return i                        
        #else:
            #print ("Rechazado",canciones[i][0], "Aleatorio",aleatorio,"acumulado",acumulados[i])

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

if __name__ == "__main__":
    listapadres = []
    listaapt = []
    aptitudes = [] #listas 
    apt = []
    for i in range(16):
        listapadres.append(padreAleatorio())
    print("si es")
    print(listapadres)
    

#   -------------------------------Generacion de aptitudes--------------------------------------
    for i in range(len(listapadres)):
        listadatos = traerDatos(listapadres[i])
        #print(listadatos)
        apt = aptitud(listadatos)
        #print("Aptitud")
        #print(aptitud)
        aptitudes.append(apt)
        listaapt.append(sum(apt)/len(apt))
    indices = []
      
    guardaDatos(0, listapadres, listaapt)
    #  -------------------------------Generacion de indices--------------------------------------
    for i in range(len(listapadres)):
          indices.append(seleccionRuleta(listapadres[i],aptitudes[i]))
          print(indices[i])
      #print("Indices")
      #print(indices)
      
    print("Generacion de hijos")
    
    
      
      
