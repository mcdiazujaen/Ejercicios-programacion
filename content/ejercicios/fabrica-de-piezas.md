---
title: "Fabrica de piezas"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Fabrica de piezas

##  Enunciado

Tenemos una fábrica de piezas metálicas, dónde tenemos almacenadas las medidas de estas piezas en una matriz llamada medidas, donde cada fila representa una pieza y las columnas se corresponderán con las medidas de las mismas, esto es, el alto, ancho y largo de la pieza. Por otro lado se hacen los pedidos de fabricación de las piezas, por tanto tendremos un vector llamado cantidad que almacena el número o cantidad de piezas a fabricar. Cuando se fabrican dichas piezas el vector cantidad se pone al valor del número de piezas que queremos fabricar. 

Las estructuras que tenemos tendrían el siguiente aspecto: 
```text

**Matriz medidas**                     **Vector cantidad**
-----------------------            --------------
Pieza 1 | 10 | 20 |  3             Pieza 1 |  40
Pieza 2 |  3 |  5 |  8             Pieza 2 | 250
Pieza 3 |  6 |  5 |  7             Pieza 3 |  10
Pieza 4 |  4 |  5 | 23             Pieza 4 | 500
...                                ...
----------------------             --------------

```
Se quiere diseñar un algoritmo que permita obtener información del proceso de fabricación. Dicho algoritmo se ha de dividir en los siguientes apartados: 

###  Apartado a

Subalgoritmo que inserte una nueva pieza en el sistema, para ello habrá que tener en cuenta: 

  * Que el alto, ancho y largo de la pieza siempre es mayor que 0 
  * Que por cada pieza que se dé de alta en el sistema, o sea en la matriz medidas, también habrá que hacer lo propio en el vector cantidad que está asociada a la misma, pero el pedido estará inicializado al número de piezas que se desee fabricar. Este número siempre será mayor que 0. 

###  Apartado b

Subalgoritmo que nos devuelva el número de pieza más grande, para ello habrá que calcular el tamaño de la misma. El tamaño se obtiene multiplicando las 3 medidas: alto, largo y ancho. 

###  Apartado c

Subalgoritmo que fabrique una pieza y la elimine del sistema, es decir, que dado el número de pieza como entrada, y la ganancia de fabricar una unidad de la misma: 

  * Devuelva la ganancia que tendremos al fabricar todas las unidades de dicha pieza. 
  * Desplace todas las piezas de la matriz medidas, una fila hacia arriba, para que no quede ningún hueco vacío en la matriz. 
  * Haga el mismo desplazamiento en el vector cantidad. 

###  Apartado d

Algoritmo principal que realice las siguientes acciones: 

  * Inserte 3 piezas en el sistema 
  * Calcule la pieza más grande y devuelva el resultado por pantalla 
  * Fabrique la pieza número 2, dado el precio de 0,47 céntimos la pieza 

##  Soluciones