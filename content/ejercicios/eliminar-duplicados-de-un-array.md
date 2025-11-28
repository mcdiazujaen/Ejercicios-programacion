---
title: "Eliminar duplicados de un array"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---


# Eliminar duplicados de un array

##  Enunciado

Diseñar un algoritmo que lea un vector desordenado _A_ , compuesto de _n_ enteros e imprima este vector en la misma secuencia, pero ignorando los valores duplicados que se encuentren en él. También se necesita saber el número de elementos que permanecen en él (_m_); por ejemplo, dado el vector siguiente 
```text


   A1   A2   A3   A4   A5   A6   A7   A8   A9   A10
   15   31   23   15   75   23   41   15   31   85


```
compuesto de 10 enteros, el vector comprimido que resulta estará formado por 
```text


   A1   A2   A3   A4   A5   A6   A7   A8   A9   A10
   15   31   23   75   41   85


```
con _m_ = 6. 

##  Soluciones 

###  Diseño en pseudocódigo
```text


ALGORITMO Duplicados
ENTRADAS:
   v: ARRAY (1..n) DE ENTEROS (* vector con los duplicados *)
   n: ENTERO (* tamaño del vector v *)
SALIDAS:
   w: ARRAY (1..k) DE ENTEROS (* vector sin duplicados *)
   k: ENTERO (* tamaño del vector w *)
VARIABLES:
   i,j: ENTEROS 
   enc:LOGICO
INICIO
  w(1) <-- v(1)
  k <-- 1
  PARA i<--2 HASTA n HACER
     (* Buscar valor en el vector sin duplicados*)
     j<--1
     enc <-- FALSO
     MIENTRAS j<=k Y enc=FALSO HACER
        SI v(i)=w(j) ENTONCES
           enc <-- VERDAD
        SINO
           j <-- j+1
        FIN_SI
     FIN_MIENTRAS
     (* Si no está en el array sin duplicados lo copia *)
     SI enc=FALSO ENTONCES
        k <-- k+1
        w(k) <-- v(i)
     FIN_SI
 FIN_PARA
FIN
```