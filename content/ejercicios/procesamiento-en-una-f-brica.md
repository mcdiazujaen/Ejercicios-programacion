---
title: "Procesamiento en una fábrica"
date: 2024-01-01
draft: false
languages: []
categories: ['enunciado']
tags: ['Sin Matlab', 'Sin solución']
---

# Procesamiento en una fábrica

##  Enunciado

En una empresa de manufactura se fabrica un total de `M` productos que están catalogados mediante una referencia (código alfanumérico). La información sobre las referencias de los productos se almacena en un array. Para la elaboración de dichos productos se utilizan máquinas de 5 tipos distintos (numeradas del 1 al 5). No todos los productos utilizan todas las máquinas ni tampoco las utilizan en el mismo orden. Para elaborar un producto este pasa por una serie de máquinas de tal manera que sufre un procesamiento en cada una de ellas. El número máximo de procesamientos que puede sufrir un producto es 7. En una matriz se almacenan las rutas de procesamiento de los distintos productos. 

Ejemplo de matriz de rutas: 

1 |  3 |  0 |  0 |  0 |  0 |  0   
---|---|---|---|---|---|---  
4 |  3 |  2 |  1 |  4 |  5 |  3   
5 |  4 |  1 |  2 |  0 |  0 |  0   
4 |  0 |  0 |  0 |  0 |  0 |  0   
… |  … |  … |  … |  … |  … |  …   
  
Ejemplo de array de referencias 

AC123   
---  
JR432   
AC222   
CA498   
…   

En este caso el producto 1 (ref. AC123) sólo se procesa dos veces y pasa por las máquinas 1 y 3. El producto 2 (ref. JR432) se procesa 7 veces pasando por las máquinas 4, 3, 2, 1, 4, 5 y 3. Así sucesivamente estaría representado en cada fila el procesamiento (secuencia de máquinas) de cada producto. 

Se quiere diseñar un algoritmo que permita obtener información del proceso de fabricación. Dicho algoritmo se ha de dividir en los siguientes apartados: 

  1. Subalgoritmo que: 
```text
 * Lea desde el teclado las referencias de los productos fabricados y las devuelva almacenadas. 
 * Lea desde el teclado para cada producto su ruta de procesamiento (números de máquinas por las que pasa) no permitiendo que se introduzca una máquina errónea (las máquinas van del 1 al 5) ni un número de procesamientos superior al máximo permitido. Debe devolver una matriz de rutas con los datos leídos y completando con 0’s los procesamientos no hechos a los productos (dado que los productos pueden estar procesados menos veces que el máximo permitido). 
```
  2. Subalgoritmo que devuelva los números de las máquinas más y menos utilizadas en el proceso de fabricación. 
  3. Subalgoritmo que dado el número de una máquina devuelva las referencias de los productos que pasan por ella. 
  4. Algoritmo principal que presente un menú de opciones de forma que el usuario pueda obtener toda la información proporcionada por los subalgoritmos anteriores. 

##  Soluciones