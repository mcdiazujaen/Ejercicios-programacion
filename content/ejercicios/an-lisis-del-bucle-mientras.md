---
title: "Análisis del bucle MIENTRAS"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---


# Análisis del bucle MIENTRAS

##  Enunciado 

Analiza los siguientes trozos de pseudocódigo y responde a las preguntas. 

###  Enunciado a) 

¿Cuántas veces se ejecutará la `_Acción 1_`? 
```text


 Cont <- 0
 MIENTRAS Cont<10 HACER
   Cont <- Cont+1
   SI Cont=10 ENTONCES
      _Accion 1_
   FIN SI
 FIN MIENTRAS


```
###  Enunciado b) 

¿Qué escribirá el siguiente bucle? 
```text


 Numero <-- 1
 MIENTRAS Numero < 11 HACER
    Numero <-- Numero + 1
    ESCRIBIR Numero
 FIN_MIENTRAS


```
###  Enunciado c) 

¿Cuántas iteraciones del bucle se realizarán? 
```text


 Numero <-- 2
 hecho <-- FALSO
 MIENTRAS NO hecho HACER
      Numero <-- Numero * 2
      SI Numero > 64 ENTONCES 
           hecho <-- verdadero
      FIN_SI
 FIN_MIENTRAS


```
##  Soluciones 

###  Solución a) 
```text


 Cont <- 0
 MIENTRAS Cont<10 HACER
   Cont <- Cont+1
   SI Cont=10 ENTONCES
      _Accion 1_
   FIN SI
 FIN MIENTRAS


```
La `_Accion 1_` no se ejecutará nunca porque, según el diseño, para que se ejecute, la variable `Cont` tiene que ser igual a 10, pero la orden condicional `SI` está dentro de un bucle `MIENTRAS` que se ejecuta sólo si la variable `Cont` es menor que 10. Por lo tanto no se ejecutará en ningún momento ya que `Cont` no llega a ser nunca 10. 

###  Solución b) 
```text


 Numero <-- 1
 MIENTRAS Numero < 11 HACER
    Numero <-- Numero + 1
    ESCRIBIR Numero
 FIN_MIENTRAS


```
A la variable `Numero` en cada vuelta del bucle `MIENTRAS` se le suma 1, como entra en el bucle valiendo 1 irá tomando valores desde 2 hasta **11** que será su valor final, ya que el bucle acaba cuando `Numero` es menor que 11. Por lo tanto, escribirá en el dispositivo de salida todos los números del 2 al 11. 

###  Solución c) 
```text


 Numero <-- 2
 hecho <-- FALSO
 MIENTRAS NO hecho HACER
      Numero <-- Numero * 2
      SI Numero > 64 ENTONCES 
           hecho <-- VERDADERO
      FIN_SI
 FIN_MIENTRAS


```
El bucle se ejecuta 6 veces, ya que en la quinta iteración, el valor de `Numero` (en la condición `SI`) es de 64, por lo tanto, no entra dentro de la condición. Sin embargo en la sexta iteración el valor de `Numero` (en la condición `SI`) es de 128, haciendo verdadera la condición y cambiando el valor de `hecho` a _VERDADERO_. Al cambiar el valor de `hecho` a verdadero, no vuelve a entrar en el bucle `MIENTRAS`.