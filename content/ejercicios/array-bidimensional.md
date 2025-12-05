---
title: "Array bidimensional"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_c', 'sin_matlab']
---

# Array bidimensional

##  Enunciado 

Un terreno puede representarse mediante un array bidimensional en el que los indices del array representan las coordenadas enteras `(x,y)` y el valor almacenado en la posición `(x,y)` del array representa la altura del terreno en dichas coordenadas. 

Realizar los siguientes apartados: 

a) Un sugalgoritmo al que se le pase un array que representa un terreno y un valor lógico que indique si lo que queremos realizar es la lectura del array o lo que queremos es mostrar por pantalla dicho array y actúe en consecuencia. 

b) Un subalgoritmo que se le pase un terreno representado mediante un array y obtenga en otro array el terreno invertido, por ejemplo, si las cotas estan comprendidas en el intervalo 23-530, la cota 530 debe cambiarla a la cota 23, la 529 debe cambiarse a 24, la 528 a la 25 y asi sucesivamente. 

##  Soluciones 

###  Diseño en pseudocódigo 

####  Apartado a 
```text
 PROCEDIMIENTO LeerEscribir (VAR Terreno, VAR nf, VAR nc, tipo)
 ENTRADAS: 
    tipo: LOGICO  (* VERDAD si se utiliza el procedimiento para lectura de datos y
                     FALSO si se utiliza para escritura de datos *)
    Terreno: ARRAY (1..1000, 1..1000) DE REALES  (* Altura de los distintos puntos de un terreno *)
    nf, nc: ENTEROS    (* Número de filas y de columnas de Terreno *)
 SALIDAS:
    (* Ninguna si tipo=FALSO *)
    Terreno: ARRAY (1..1000, 1..1000) DE REALES  (* Altura de los distintos puntos de un terreno *)
    nf, nc: ENTEROS    (* Número de filas y de columnas de Terreno *)
 VARIABLES:
    i, j: ENTEROS.
 INICIO
    SI tipo ENTONCES
       ESCRIBIR "Introduzca las dimensiones del terreno:"
       LEER nf, nc
       PARA i<--1 HASTA nf HACER
          PARA j<--1 HASTA nc HACER
             ESCRIBIR "Introduzca la posición (", i, ",", j, ") del terreno:"
             LEER Terreno(i,j)
          FIN_PARA
       FIN_PARA
    SI_NO
       PARA i<--1 HASTA nf HACER
          PARA j<--1 HASTA nc HACER
             ESCRIBIR "Posicion (", i, ",", j, "):", Terreno(i,j)
          FIN_PARA
       FIN_PARA
    FIN_SI
 FIN

```
####  Apartado b 
```text
 PROCEDIMIENTO Invierte (Terreno, nf, nc, VAR Invertido)
 ENTRADAS:
    Terreno: ARRAY (1..1000, 1..1000) DE REALES   (* Altura de los distintos puntos de un terreno *)
    nf, nc: ENTEROS     (* Número de filas y de columnas de Terreno *)
 SALIDAS:
    Invertido: ARRAY (1..1000, 1..1000) DE REALES  (* Altura de los distintos puntos del terreno de entrada pero invertidas *)
 VARIABLES:
    i, j: ENTEROS
    max,min: REALES
 INICIO
    (* Encontrar el mayor y menor valor de altura del terreno *)
    max<--Terreno(1,1)
    min<--Terreno(1,1)
    PARA i<--1 HASTA nf HACER
       PARA j<--1 HASTA nc HACER
          SI Terreno(i,j)>max ENTONCES
             Max<--Terreno(i,j)
          FIN_SI
          SI Terreno(i,j)<min ENTONCES
             Min<--Terreno(i,j)
          FIN_SI
       FIN_PARA
    FIN_PARA
 
    (* Invertir los valores del terreno *)
    PARA i<--1 HASTA nf HACER
       PARA j<--1 HASTA nc HACER
          Invertido(i,j)<--max-(Terreno(i,j)-min)
       FIN_PARA
    FIN_PARA
 FIN
```