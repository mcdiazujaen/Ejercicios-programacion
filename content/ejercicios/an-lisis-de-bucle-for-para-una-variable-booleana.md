---
title: "Análisis de bucle FOR para una variable booleana"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Análisis de bucle FOR para una variable booleana

  

##  Enunciado 

¿Cuál es el valor de la variable booleana `test` después de la ejecución de los siguientes bucles? 

###  Enunciado a) 
```text


 test <-- VERDADERO
 PARA contador <-- 1 HASTA N HACER
    test <-- NO test
 FIN_PARA


```
###  Enunciado b) 
```text


 test <-- (N MOD 2 = 0)
 PARA contador <-- 1 HASTA N HACER
    test <-- NO test
 FIN_PARA


```
##  Soluciones 

###  Solución de a) 

En este caso el valor de la variable depende de si `N` es par o impar: 

  * Si `N` es un número par la variable `test` será **VERADADERA**. 
  * Si por el contrario es un número impar la variable será **FALSA**. 

###  Solución de b) 

Al contrario que en el caso anterior el valor de la variable **NO** depende de la variable `N`. 

  * Si `N` es par entonces la primera asignación (`test <-- (N MOD 2 = 0)`) da a la variable `test` el valor de **VERDADERO**. Como el bucle itera un número par de veces (ya que `N` es par), la variable `test` se queda como está, es decir, `test` será **VERDADERO**. 
  * Si la variable `N` es impar entonces `test` coménzará con el valor **FALSO**. Al iterar el bucle un número impar de veces (ya que `N` es impar), la variable `test` cambia su valor, es decir, `test` será **VERDADERO**.