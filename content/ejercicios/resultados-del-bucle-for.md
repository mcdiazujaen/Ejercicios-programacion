---
title: "Resultados del bucle FOR"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Resultados del bucle FOR

##  Enunciado 

En cada uno de los siguientes segmentos indicar el valor que se imprimirá para la variable `Var`. Suponer que todas las variables son enteras. 

a) 
```text


    Var <-- 0
    PARA i <-- 1 HASTA 10 CON INCREMENTO DE 1 HACER
       Var <-- Var+1
    FIN_PARA
    ESCRIBIR Var


```
b) 
```text


    Var <-- 0
    PARA i <-- 4 HASTA 36 CON INCREMENTO DE 4 HACER
       Var <-- Var+1
    FIN_PARA
    ESCRIBIR Var


```
c) 
```text


    Var <-- 0
    PARA i <-- 1 HASTA 14 CON INCREMENTO DE 1 HACER
         PARA j <-- 1 HASTA 8 CON INCREMENTO DE 1 HACER
            Var <-- Var+1
         FIN_PARA
    FIN_PARA
    ESCRIBIR Var


```
d) 
```text


   Var <-- 0
   PARA i <-- 10 HASTA 1 CON DECREMENTO DE 1 HACER
      Var <-- Var+1
   FIN_PARA
   ESCRIBIR Var


```
##  Soluciones 

###  Solución a) 
```text


    Var <-- 0
    PARA i <-- 1 HASTA 10 CON INCREMENTO DE 1 HACER
       Var <-- Var+1
    FIN_PARA
    ESCRIBIR Var


```
En este caso el bucle da 10 vueltas (con los valores de `i`: 1,2,3,...,10), por lo tanto, la variable `Var` valdrá 10. 

###  Solución b) 
```text


    Var <-- 0
    PARA i <-- 4 HASTA 36 CON INCREMENTO DE 4 HACER
       Var <-- Var+1
    FIN_PARA
    ESCRIBIR Var


```
Como el bucle está definido para que el incremento sea de 4, dará 9 vueltas (con los valores de `i`: 4,8,12,...,36) antes de llegar a 36 (porque 36/4 = 9) además como `Var` empieza en 0 y por cada vuelta se le suma 1, el resultado será: 9. 

###  Solución c) 
```text


    Var <-- 0
    PARA i <-- 1 HASTA 14 CON INCREMENTO DE 1 HACER
         PARA j <-- 1 HASTA 8 CON INCREMENTO DE 1 HACER
            Var <-- Var+1
         FIN_PARA
    FIN_PARA
    ESCRIBIR Var


```
Por cada vuelta que dé el primer bucle, el segundo bucle da 8 vueltas (con valores de `j`: 1,2,3,...,8). Como el primero da 14 vueltas (con valores de `i`: 1,2,3,...,14) y por cada vuelta se le suma uno a la variable quedaría: 14*8 = 112 Como comienza valiendo 0, el valor de `Var` será 112. 

###  Solución d) 
```text


   Var <-- 0
   PARA i <-- 10 HASTA 1 CON DECREMENTO DE 1 HACER
      Var <-- Var+1
   FIN_PARA
   ESCRIBIR Var


```
El bucle está definido para que decrezca, comenzando el valor de `i` en 10. El bucle dará 10 vueltas (con valores de `i`: 10,9,8,...,1) y la variable `Var` tendría el valor de 10, ya que comienza en 0 y en cada vuelta se le suma 1.