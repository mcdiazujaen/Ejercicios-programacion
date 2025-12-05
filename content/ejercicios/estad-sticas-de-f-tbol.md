---
title: "Estadísticas de fútbol"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Estadísticas de fútbol

##  Enunciado 

Disponemos de un archivo de texto con información sobre un partido de fútbol. Dicho archivo almacena 4 datos por cada gol metido, que son: mitad del partido (1, 2), minuto (de 0 a 60), numero del jugador (del 0 al 99) y equipo (1 o 2). 

Ejemplo de contenido del fichero de datos: 
```text

1 12 23 1 2 3 10 2

```
En el ejemplo hay apuntadas 2 goles. Los datos del primero (1 12 23 1) indican que el gol fue en el primer tiempo, en el minuto 12, por el jugador 23 del equipo 1. 

Los datos del siguiente gol son: `2 3 10 2`

Realizar los siguientes apartados: 

  * Módulo que lea el fichero de datos. La entrada será el nombre del fichero y la salida una matriz con los datos de cada gol en cada fila, y con 4 columnas (mitad, minuto, numero de jugador y equipo). 

Ejemplo de matriz de goles: 

1 |  12 |  23 |  1   
---|---|---|---  
2 |  3 |  10 |  2   
  
  * Módulo que devuelva los goles de cada equipo. Para ello recibirá como entrada la matriz de goles. 

  * Módulo que devuelva el número del máximo goleador de un equipo. Para ello recibirá como entrada la matriz de goles y el número de equipo. Si existen varios jugadores con el mismo número de goles devolverá aquel que tenga el número de jugador más bajo. 

  * Programa principal, que utilizando los módulos anteriores, pida al usuario el nombre del fichero con los datos de los goles, lea dicho fichero y escriba en un fichero llamado **`estadistica.txt`** , con los mensajes aclaratorios correspondiente, la siguiente estadística: 
```text
* Puntuación de cada equipo. 
* Número de jugador del máximo goleador de cada equipo. 
* Equipo y número de jugador del máximo goleador del partido 

```
##  Soluciones