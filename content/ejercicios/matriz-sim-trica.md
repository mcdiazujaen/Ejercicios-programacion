---
title: "Matriz simétrica"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
professors: ['lperez']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Matriz simétrica

##  Enunciado 

Diseñar un algoritmo que dada una matriz cuadrada y su tamaño nos diga si es o no simétrica sin utilizar subalgoritmos (funciones o procedimientos). 

Ejemplo de matriz simétrica: 

1 |  4 |  7   
---|---|---  
4 |  2 |  9   
7 |  9 |  3   
  
##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**

####  Solución 1 
```text

ALGORITMO Matriz_simetrica
ENTRADAS: Mat: ARRAY [1..tamano, 1.tamano] DE ENTEROS; matriz 
               matemática  cuadarada.
          tamano: ENTERO, nº de filas y  columnas de Mat, tamano>0. 
SALIDAS: Mensaje informa si Mat es o no simétrica.
VARIABLES: i, j: ENTERO; 
INICIO
  LEER tamano
  PARA   i=1  HASTA  tamano HACER
     PARA   j=1  HASTA  tamano  HACER
        LEER Mat(i,j)
     FIN_PARA
  FIN_PARA
  SI  Calculo_simetria(Mat,tamano)
  ENTONCES ESCRIBIR ‘La matriz es simétrica’
  SI NO ESCRIBIR ‘La matriz  no es simétrica’
  FIN_SI
FIN

```
####  Solución 2 
```text

ALGORITMO Matriz_simetrica
ENTRADAS: Mat: ARRAY [1..tamano, 1.tamano] DE ENTEROS; matriz 
               matemática  cuadarada.
          tamano: ENTERO, nº de filas y  columnas de Mat, tamano>0. 
SALIDAS: Mensaje informa si Mat es o no simétrica.
VARIABLES: i, j: ENTERO; resultado:LOGICO; 
INICIO
  LEER tamano
  PARA   i=1  HASTA  tamano HACER
     PARA   j=1  HASTA  tamano  HACER
        LEER Mat(i,j)
     FIN_PARA
  FIN_PARA
  Calculo_simetria(Mat,tamano,resultado )
  SI resultado
  ENTONCES ESCRIBIR ‘La matriz es simétrica’
  SI NO ESCRIBIR ‘La matriz  no es simétrica’
  FIN_SI
FIN

```
####  Comentario

En la primera solución para el cálculo de la simetría se realiza una llamada a la función Calculo_simetría (se puede ver en Matriz Simétrica Subalgoritmo) 

En la segunda solución el calculo se realiza haciendo una llamada al procedimiento Calculo_simetría (se puede ver en Matriz Simétrica Subalgoritmo).