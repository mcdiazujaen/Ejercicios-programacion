---
title: "Números perfectos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_c', 'sin_matlab']
---

# Números perfectos

##  Enunciado 

Un **número perfecto** es un número natural que es igual a la suma de sus divisores propios positivos, sin incluirse él mismo. Así, 6 es un número perfecto, porque sus divisores propios son 1, 2 y 3; y 6 = 1 + 2 + 3. 

Realizar los siguientes apartados para el cálculo de números perfectos: 

  1. Un subalgoritmo al que se le de un entero, y devuelva los divisores de dicho numero, así como el número de ellos. 
  2. Un subalgoritmo que reciba como entradas un número, y devuelva VERDADERO si la suma de divisores es igual al número y FALSO en otro caso. 
  3. Un algoritmo que devuelva los `k` primeros números perfectos, apoyándose en los módulos anteriores. 

##  Soluciones 

###  Diseño en pseudocódigo 

####  Apartado 1 
```text
PROCEDIMIENTO DIVISORES(N, VAR VEC, VAR POS)
ENTRADAS:
   N: ENTERO  _(NÚMERO PARA SACAR SUS DIVISORES, N > 0 )_
SALIDAS:
   VEC: ARRAY (1..1000) DE ENTEROS   _(VECTOR PARA ALMACENAR LOS DIVISORES)_
   POS: ENTERO                       _(NUMERO DE DIVISORES)_
VARIABLES:
   DIVISOR, J: ENTEROS
INICIO
   DIVISOR <-- N – 1
   J <-- 1;
   MIENTRAS ( DIVISOR <> 0 ) HACER
      SI ((N MOD DIVISOR ) = 0) ENTONCES 
         VEC(J) <-- DIVISOR
         J <-- J + 1
      FIN_SI
      DIVISOR <-- DIVISOR-1
   FIN_MIENTRAS
   SI N = 1 ENTONCES 
      VEC(J) <-- 1
      J <-- J + 1
   FIN_SI
   POS<--J-1
FIN
```

####  Apartado 2 
```text
FUNCIÓN SUMADIVISORES(NUM): LÓGICO
ENTRADAS:
   NUM: ENTERO    _(NÚMERO QUE ESTUDIAMOS PARA VER SI LA SUMA DE SUS DIVISORES ES IGUAL AL NÚMERO O NO, NUM > 0)_
SALIDAS:
   RESULT: LÓGICO _(VERDADERO SI LA SUMA DE LOS DIVISORES ES EL NUMERO Y FALSO SI NO LO ES)_
VARIABLES:
   K, SUM, LONG : ENTEROS
   VECTOR:ARRAY (1..1000) DE ENTEROS
INICIO
   _(Calcular divisores)_
   DIVISORES(NUM, VECTOR, LONG)
   _(Sumar los divisores)_
   SUM <-- 0
   PARA K <-- 1 HASTA LONG HACER
      SUM <-- SUM + VECTOR(K)
   FIN_PARA
   _(Comprobar si la suma de los divisores es igual al número)_
   SI ( SUM = NUM ) ENTONCES
        RESULT <-- VERDADERO
   SINO
        RESULT <-- FALSO
   FIN_SI
   DEVOLVER RESULT
FIN
```

####  Apartado 3 
```text
PROCEDIMIENTO PERFECTO (TOPE, VAR DESTINO)
ENTRADAS:
   TOPE: ENTERO  _(CANTIDAD DE NÚMEROS PERFECTOS QUE DEBEMOS ENCONTRAR)_
SALIDAS:
   DESTINO: ARRAY (1..1000) DE ENTEROS  _(VECTOR EN EL QUE ALMACENAMOS LOS NÚMEROS PERFECTOS)_
VARIABLES:
   A, B: ENTEROS
INICIO
   A <-- 1
   B <-- 1
   MIENTRAS (B<=TOPE) HACER
      SI SUMADIVISORES(A) ENTONCES
               DESTINO(B)  <-- A
               B <-- B+1
      FIN_SI
      A <-- A + 1
   FIN_MIENTRAS
FIN

ALGORITMO NUMEROPERFECTO
ENTRADAS:
   P: ENTERO  _(CANTIDAD DE NÚMEROS PERFECTOS HA ENCONTRAR, P > 0)_
SALIDAS:
   SOLUCIÓN: ARRAY (1..1000) DE ENTEROS  _(NÚMEROS PERFECTOS ENCONTRADOS)_ 
VARIABLES:
   I: ENTERO
INICIO
  ESCRIBIR "¿CUANTOS NÚMEROS PERFECTOS DESEA CALCULAR? : "
  LEER P
  PERFECTO(P, SOLUCION)
  ESCRIBIR "LOS ",P," Nº PERFECTOS SON: "
  PARA  I <-- 1  HASTA P HACER
     ESCRIBIR "  ", SOLUCION(I)
  FIN_PARA
FIN.
```