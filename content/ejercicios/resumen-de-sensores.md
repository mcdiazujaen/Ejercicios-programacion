---
title: "Resumen de sensores"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Resumen de sensores

##  Enunciado

Hemos diseñado un dispositivo con 5 sensores de diversa índole. El dispositivo almacena en un archivo de texto los datos captados por los sensores durante todo el día. La primera línea del archivo contiene el día, mes y año al que corresponden los valores captados. Las siguientes líneas contienen 5 valores, separados por espacios, que son: hora, minuto, segundo, número de sensor y valor captado. 

Ejemplo del contenido del fichero de datos del sensor: 
```text

24 11 2013
00 12 24 2 530
00 12 25 1 100
00 12 30 5 300
01 00 00 2 101

```
Implementar los siguientes módulos: 

###  Módulo para leer el fichero 

Módulo que lea el fichero de datos. La entrada será el nombre del fichero y las salidas un vector con la fecha (día, mes y año) y una matriz con los datos de cada captura en cada fila, y con 5 columnas (hora, minuto, segundo, sensor y valor). 

Ejemplo del vector fecha: 
```text

24 11 2013

```
Ejemplo de matriz de datos: 
```text

0 12 24 2 530
0 12 25 1 100
0 12 30 5 300
1  0  0 2 101

```
###  Módulo de datos captados por hora 

Módulo que devuelva cuantos datos se han captado en cada hora. Para ello recibirá como entrada la matriz de datos y devolverá un vector con el número de datos captados en cada hora. 

###  Módulo de media de un sensonr 

Módulo que devuelva la media de los valores captados por un sensor dado. Para ello recibirá como entrada la matriz de datos y un número que indique el sensor. 

###  Programa principal 

Programa principal, que utilizando los módulos anteriores, pida al usuario el nombre del fichero que contiene los datos del dispositivo. A continuación leerá dicho fichero y escribirá en un fichero llamado **resumen.txt** , con los mensajes aclaratorios correspondiente, el siguiente resumen: 

  * La fecha (separada por guiones) del fichero a la que corresponde el resumen. Ejemplo: 

```text

Resumen de sensores del día 24-11-2013

```
  * El número de valores que se han recogido. Ejemplo: 

```text

- Se han recogido 4 valores

```
  * Cuanto datos se han recogido en cada hora. Si durante alguna hora no se han recogido datos 

no deberá escribirse información de dicha hora. Ejemplo: 
```text

- Los datos recogidos en cada hora son:
   Hora 0: 3 datos.
   Hora 1: 1 datos.

```
  * La media de los valores recogidos por cada sensor. Si algún sensor no ha recogido valores 

se escribirá su media como 0. Ejemplo: 
```text

- La media de cada sensor es:
   Sensor 1: 100
   Sensor 2: 315.50000
   Sensor 3: 0
   Sensor 4: 0
   Sensor 5: 300

```
##  Soluciones