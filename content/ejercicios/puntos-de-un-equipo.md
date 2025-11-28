---
title: "Puntos de un equipo"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---


# Puntos de un equipo

##  Enunciado 

En una matriz de cuatro columnas se almacena información sobre los partidos de una liga de fútbol. Su formato es el siguiente: 

**Código equipo casa** |  **Código equipo fuera** |  **Goles equipo casa** |  **Goles equipo fuera**  
---|---|---|---  
1 |  2 |  5 |  1   
3 |  1 |  2 |  2   
2 |  3 |  3 |  2   
1 |  4 |  2 |  0   
4 |  2 |  0 |  3   
  
La primera columna almacena el código del equipo que juega en casa, la segunda columna el código del equipo que juega fuera, la tercera columna el número de goles que marcó el equipo que jugó en casa y la cuarta columna el número de goles que marcó el equipo que jugó fuera de casa. Cada fila de la matriz almacena el resultado de un partido. Así, la primera fila indica que jugaron el equipo 1 contra el 2, en casa del equipo 1 y que el equipo 1 ganó por 5 goles a 1. Se supone que los códigos de los equipos están en el rango [1,20]. 

Realiza un módulo que dada una matriz de partidos y un código de equipo devuelva los puntos que lleva el equipo. Tenga en cuenta que una victoria cuenta como 3 puntos, un empate como 1 punto y una derrota como 0 puntos. Por ejemplo, en la matriz de ejemplo el equipo 1 lleva 7 puntos: 2 victorias y un empate. 

##  Soluciones