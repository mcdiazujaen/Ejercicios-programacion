---
title: "Máximo de una submatriz"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Máximo de una submatriz

##  Enunciado 

Realiza una función que tome como parámetros de entrada: 

  * Una matriz m de números 
  * Una posición p de la matriz 
  * Un tamaño t 

La función debe devolver dos cosas. En primer lugar un valor lógico indicando si se puede construir una submatriz cuadrada de m, empezando en la posición p y de tamaño t. En caso de que se pueda construir la submatriz el máximo de los elementos de la submatriz. Por ejemplo, dada la matriz: 
```text
4  5  6  7  8
2 33  1  2  4
5  4  3  6 -5
```

y los valores p = (1,4) y t = 3 hay que devolver que no se puede construir una submatriz de tamaño 3 empezando en la fila 1 y columna 4. Si los valores fueran p = (2,2) y t = 2, entonces se puede construir la submatriz, que sería: 
```text
33  1
 4  3
```

y habría que devolver el máximo de la submatriz (33 en este caso). 

##  Soluciones