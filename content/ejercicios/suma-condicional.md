---
title: "Suma condicional"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['Sin C', 'Sin Matlab']
---

# Suma condicional

##  Enunciado

Elabora un algoritmo que calcule la suma de los números múltiplos de 3 a partir del número 9 y finaliza en el número 450. No deben incluirse en la suma los números comprendidos entre 21 y 270\. 

##  Soluciones

###  Diseño en pseudocódigo
```text
ALGORITMO SumaMultiplos
ENTRADAS:
   (* Ninguna *)
SALIDA:
   suma: ENTERO (* la suma de los enteros que cumplen la condición dada en el enunciado *)
VARIABLES:
   i: ENTERO
INICIO
   suma <-- 0
   PARA i <--9 HASTA 450 HACER
      SI (i MOD 3 = 0) Y (i<21 O i>270)
         suma <-- suma+i
      FIN_SI
   FIN_PARA
   ESCRIBIR "El resultado es: ", suma
FIN
```