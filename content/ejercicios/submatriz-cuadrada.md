---
title: "Submatriz cuadrada"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Submatriz cuadrada

##  Enunciado

Realiza un módulo que tome como parámetros de entrada: 

  * Una matriz **m** de números 
  * Una posición **p** de la matriz 
  * Un tamaño **t**

La función debe devolver dos valores. En primer lugar un valor lógico indicando si se puede construir una submatriz cuadrada de **m** , empezando en la posición **p** y de tamaño **t**. En caso de que se pueda construir la submatriz el máximo de los elementos de la submatriz. Por ejemplo, dada la matriz: 

4 |  5 |  6 |  7 |  8   
---|---|---|---|---  
2 |  33 |  1 |  2 |  4   
5 |  4 |  3 |  6 |  -5   
  
Para los valores de entrada p = (1,4) y t = 3 hay que devolver que no se puede construir una submatriz de tamaño 3 empezando en la fila 1 y columna 4. Si los valores fueran p = (2,2) y t = 2, entonces se puede construir la submatriz, que sería: 

33 |  1   
---|---  
4 |  3   
  
En este caso habría que devolver 33 que es el máximo de la submatriz. 

##  Soluciones