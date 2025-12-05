---
title: "Operación con dos vectores"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Operación con dos vectores

##  Enunciado 

Realizar un subalgoritmo que dados dos arrays `x` e `y` de `n` reales, calcule lo siguiente: 

![Imagen:formulaSum.png](images/2/2c/FormulaSum.png)

##  Soluciones 

###  Solución en pseudocódigo 
```text
FUNCION Suma (X, Y, n): REAL
ENTRADAS:
   X,Y: ARRAY[1...n] DE REALES  _(representan dos vectores matemáticos)_
   n: ENTERO,                   _(el tamaño de los arrays de entrada; n >0)_
SALIDAS:
   suma: REAL   _(el resultado de calcular la formula)_
VARIABLES:
   i, k: ENTERO;
   s2: REAL
INICIO
   Suma<--0
   PARA i <-- 1 HASTA n CON INCREMENTO DE 1 HACER
      s2<--0
      PARA k <-- 1 HASTA i CON INCREMENTO DE 1 HACER
         s2<--s2 + Y(k) /X (i-k + 1)
      FIN_PARA
      suma<--suma+X(i)*s2
   FIN_PARA
   DEVOLVER suma
FIN
```