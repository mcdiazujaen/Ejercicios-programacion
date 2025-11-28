---
title: "Análisis de la salida de ciclos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Análisis de la salida de ciclos

##  Enunciado 

En cada uno de los siguientes segmentos de algoritmos, indicar cuándo el ciclo termina y cuándo no lo hace. Suponer que todas las variables son enteras. 

**a)**
```text


   Contador <-- 0
   Total <-- 0
   MIENTRAS Contador >= 0 HACER
        Total <-- Total +2
   FIN_MIENTRAS


```
**b)**
```text


   Contador <-- 0
   Total <-- 0
   MIENTRAS Contador <= 10 HACER
         Total <-- Total +2
         Contador <-- Contador+1
   FIN_MIENTRAS


```
**c)** En caso de que este ciclo termine, ¿cúando sería y qué valores tendrían `h`, `a` y `termina` al finalizar?. 
```text


   suma <-- 0
   a <-- 0
   h <-- 1
   termina <-- FALSO
   REPETIR
       MIENTRAS  h<20   HACER
               ESCRIBIR “Introduce el elemento”, h
               LEER a
               SI   a>100 ENTONCES
                       termina <-- VERDAD
                       h <-- 20
               SI NO
                       suma <-- suma + a
               FIN_SI
       FIN_MIENTRAS
   HASTA QUE termina 


```
##  Soluciones

**a)**
```text


   Contador <-- 0
   Total <-- 0
   MIENTRAS Contador >= 0 HACER
        Total <-- Total +2
   FIN_MIENTRAS


```
El ciclo no acabaría nunca porque `Contador` será siempre mayor o igual que 0, ya que dentro del bucle mientras no se modifica el valor de dicha variable. 

**b)**
```text


   Contador <-- 0
   Total <-- 0
   MIENTRAS Contador <= 10 HACER
         Total <-- Total +2
         Contador <-- Contador+1
   FIN_MIENTRAS


```
El ciclo acabaría después de dar 11 vueltas, ya que en ese instante el valor de `Contador` llegaría a 10 y saldría del bucle. El valor final de `Total` será **22** porque por cada vuelta se le suma 2.