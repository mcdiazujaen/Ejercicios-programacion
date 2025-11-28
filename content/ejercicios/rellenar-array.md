---
title: "Rellenar array"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---


# Rellenar array

##  Enunciado 

Dispones de 2 arrays (A y B) de enteros de tamaño n. El array A contiene enteros positivos y el array B enteros entre 0 y n. Diseña un subalgoritmo que a partir de dichos arrays devuelva una matriz M(n x n) donde en cada fila aparezca el entero del array A repetido tantas veces como indique el mismo valor del array B. Los enteros empezarán a colocarse por la última fila y última columna de M. Las posiciones no ocupadas se rellenarán con ceros. 

Ejemplo: 

```text
Si las entradas fueran las siguientes: 


n = 5
A = (5, 4, 2, 9, 3)
B = (3, 2, 1, 3, 5)


La matriz `M` de salida tendría: 


3  3  3  3  3
0  0  9  9  9
0  0  0  0  2
0  0  0  4  4
0  0  5  5  5


```
##  Soluciones