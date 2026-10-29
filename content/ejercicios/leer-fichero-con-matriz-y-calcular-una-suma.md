---
title: "Leer fichero con matriz y calcular una suma"
date: 2024-01-01
draft: false
languages: []
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Leer fichero con matriz y calcular una suma

##  Enunciado 

Implementa un módulo al que se le dé cómo parámetro de entrada el nombre de un fichero, que contiene una serie de valores enteros para formar una matriz, y devuelva como parámetros de salida los siguientes: 

  * Un lógico indicando si la matriz extraída del fichero es o no cuadrada 
  * Un entero que sea la suma de su diagonal principal, en caso de ser cuadrada la matriz; o la suma de la columna central en caso de no ser cuadrada. 

En una matriz con un número par de columnas suponemos que la central es cualquiera de las dos centrales. 

El formato del fichero es como el siguiente (este es solo un ejemplo): 
```text
4 3
8 7 6 5 4 3 21 -8 2 3 4 0
```

En la primera fila aparece el número de filas y columnas de la matriz y en la segunda fila los elementos de la matriz. 

##  Soluciones