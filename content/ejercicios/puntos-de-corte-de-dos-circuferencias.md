---
title: "Puntos de corte de dos circuferencias"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Puntos de corte de dos circuferencias

##  Enunciado 

Diseñar un algoritmo que dado dos circunferencias (coordenadas en el plano x e y, y su radio) calcule cuantos puntos tienen en común dichas circunferencias (cero, uno, dos o infinitos). Para realizar este programa, tienes que calcular la suma de los radios y la distancia entre los dos centros de las circunferencias utilizando las siguientes fórmulas: 
```text
Suma_radios = Radio1+ Radio2
Distancia   = RaizCuadrada( (x1-x2)2 + (y1-y2)2 )

```
Si la distancia es cero y los radios son iguales es que se trata de la misma circunferencia y todos sus puntos coinciden (infinitos puntos de corte). Si la distancia es cero y los radios no son iguales entonces no existe ningún punto de corte. En otro caso, si la distancia es menor que la suma de los radios, entonces existen dos puntos de corte. Si la distancia es igual a la suma de los radios, entonces sólo existe un punto de corte. Por ultimo, si la distancia es mayor que la suma de los radios, entonces no existe ningún punto de corte. 

##  Soluciones 

###  Pseudocódigo por **mcdiaz**
```text
 ALGORITMO PuntosDeCorte
 ENTRADAS:
   x1, y1: REALES ''(*Coordenadas del centro de la primera circunferencia*)''
   r1: REAL       ''(*Radio de la primera circunferencia*)''
   x2, y2: REALES ''(*Coordenadas del centro de la segunda circunferencia*)''
   r2: REAL       ''(*Radio de la segunda circunferencia*)''
 SALIDAS:
   ''(*mensaje indicando en cuantos puntos se cortan las circunferencias*)''
 VARIABLES:
   suma_radios: REAL
   distancia: REAL
 INICIO
   ''(*Leer las entradas*)''
   ESCRIBIR "Introduzca las coordenadas x,y de la primera circunferencia:"
   LEER x1, y1
   ESCRIBIR "Introduzca el radio de la primera circunferencia:"
   LEER r1
 
   ''(*Calcular la distancia de las circunferencias y la suma de sus radios*)''
   suma_radios = r1+ r2
   distancia   = RaizCuadrada( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )
 
   ''(*Mostrar un mensaje según los puntos de corte*)''
   SI ( distancia = 0 ) ENTONCES
      SI ( r1=r2 ) ENTONCES
         ESCRIBIR "Existen infinitos puntos de corte."
      SI_NO
         ESCRIBIR "No hay puntos de corte."
      FIN_SI
   SI_NO ''(*si la distancia es distinta de 0*)''
      SI (suma_radios < distancia ) ENTONCES
         ESCRIBIR "Existen 2 puntos de corte."
      SI_NO
         SI (suma_radios = distancia ) ENTONCES
            ESCRIBIR "Existe 1 punto de corte."
         SI_NO
            ESCRIBIR "No hay puntos de corte."
         FIN_SI
      FIN_SI
 FIN
```