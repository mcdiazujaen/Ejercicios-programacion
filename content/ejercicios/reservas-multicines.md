---
title: "Reservas Multicines"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---


# Reservas Multicines

##  Enunciado 

Se quiere realizar un programa que gestione las reservas de las salas de un Multicines. El número de salas es _**M**_ y el número de asientos por sala es _**N**_. Para guardar la información sobre la ocupación se utiliza una matriz de _**MxN**_ donde cada fila representa una de las salas y cada columna uno de los asientos en las mismas. Esta matriz está rellena de 0’s y 1’s para indicar si un asiento de una determinada sala está libre o está ocupado. Cada sala está identificada por un nombre (un carácter) que se puede almacenar en un array de tamaño _**M**_. 

Ejemplo de matriz de ocupación (1 ocupado, 0 libre): 
```text


1							N
-----------------------------------------------------------	
1	1	0	0	0	0	0	…  |	1
1	1	1	1	1	1	1	…  |	
1	0	0	1	0	0	1	…  |	
0	1	0	0	0	0	0	…  |	
…	…	…	…	…	…	…	…  |	M


```
Ejemplo de array con los nombres de las salas 
```text


A  |	1
P  |	
B  |	
H  |	
…  |	M


  
```
Con este planteamiento implementa los siguientes apartados, especificando de forma clara las variables de entrada, salida e intermedias así como sus tipos para cada uno de los módulos: 

###  Apartado A 

Módulo que lea desde un fichero llamado **SalasMulticines.txt** los nombres de las salas y las devuelva en un array. El formato del fichero es: _**A P B H ...**_ , los nombres de todas las salas en la misma fila separados por espacios en blanco. 

###  Apartado B 

Módulo que lea desde un fichero llamado **OcupacionMulticines.txt** la información sobre la ocupación de las salas y devuelva la matriz de ocupación. El formato del fichero es: _**N 1 1 0 0 0 0 1 …**_ , donde _**N**_ es el número de asientos por sala y a continuación las ocupaciones de la primera sala, de la segunda, etc…, todos los datos en la misma línea y separados por espacios en blanco. 

###  Apartado C 

Módulo que dado el nombre de una sala y la ocupación de los multicines obtenga el porcentaje de ocupación para dicha sala. 

###  Apartado D 

Programa principal que, **utilizando los módulos anteriores** , lea los datos desde fichero y permita al usuario introducir el nombre de una sala desde teclado y conocer el porcentaje de ocupación de la misma. Este proceso de lectura del nombre de la sala y salida de su ocupación deberá terminar cuando el usuario así lo indique. 

##  Soluciones