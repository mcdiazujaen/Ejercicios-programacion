---
title: "Número Primo"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_c', 'sin_matlab']
---


# Número Primo

##  Enunciado 

Un número se define como primo si no tiene otros divisores ademas de 1 y de el mismo. Diseñar un algoritmo para leer un número y determinar si trata o no de un número primo. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text


ALGORITMO Primo
ENTRADAS:
   numero: ENTERO  _(Valor del que se quiere saber si es primo)_
SALIDAS:
   primo: LÓGICO   _(Verdadero si "numero" es primo y falso en caso contrario)_
VARIABLES:
   i:ENTERO

INICIO
   _(Pedir el valor al usuario)_
   ESCRIBIR "Introduzca un número: "
   LEER numero

   _(Calcular si el número es primo)_
   primo <-- VERDADERO
   i <-- 2
   REPETIR
      SI (numero MOD i)=0 ENTONCES
         primo <-- FALSO
      FIN_SI
      i <-- i+1
   HASTA (i>(numero-1) O (NO primo)

   _(Mostrar el resultado)_
   SI primo ENTONCES
      ESCRIBIR "El número SI es primo"
   SI_NO
      ESCRIBIR "El número NO es primo"
   FIN_SI
FIN
```