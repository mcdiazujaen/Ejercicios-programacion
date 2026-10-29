---
title: "Cálculo del valor Pi"
date: 2024-01-01
draft: false
languages: ['matlab', 'pseudocódigo']
categories: ['enunciado']
---

# Cálculo del valor Pi

##  Enunciado 

Realizar un subalgoritmo que calcule el valor de la constante PI, con un error menor que el indicado. Para ello debe utilizar la siguiente serie: 
```text
PI1 = 4 * (1 – 1/3)
PI2 = 4 * (1 – 1/3 + 1/5 – 1/7)
PIn = 4 * (1 – 1/3 + 1/5 – 1/7 + ...)
```

El error se calcula como la diferencia entre un término de la serie y el anterior. 
```text
error = PIi - PIi-1
```

##  Soluciones 

###  Pseudocódigo 
```text
 FUNCION Pi (error):REAL
 ENTRADAS:
    error: REAL (* valor permitido de error en el calculo de PI *)
 SALIDAS:
    (* Aproximación al valor PI, con un error cometido menor que el dado como entrada *)
 VARIABLES:
    termino, erroractual, siguiente: REALES
    i:ENTERO
 INICIO
    (* Calcular el primer término de la sucesión *)
    termino <-- 0
    siguiente <-- 1-(1/3)
    erroractual <-- siguiente-termino
 
    (* Calcular los siguientes términos de la sucesión *)
    i<--5
    MIENTRAS 4*erroractual>=error HACER
       termino <-- siguiente
       siguiente <-- siguiente+(1/i -1/i+2)
       erroractual <-- siguiente-termino
       i <-- i+4
    FIN_MIENTRAS
 
    DEVOLVER 4*siguiente
 FIN
```

###  Programa en Matlab 
```matlab

function aproxpi = CalcularPi( valorerror )
% FUNCION aproxpi = CalcularPi( valorerror )
% DESCRIPCIÓN: Calcula el valor de PI de forma aproximada
% PARÁMETROS DE ENTRADA:
%   valorerror: REAL, valor permitido de error en el calculo de PI
% PARÁMETROS DE SALIDA:
%   aproxpi: REAL,  Aproximación al valor PI, con un error cometido menor que el dado como entrada
% VARIABLES:
%   termino, erroractual, siguiente: REALES
%   x: ENTERO
 
%Calcular el primer término de la sucesión)
termino = 0;
siguiente = 1-(1/3);
erroractual = siguiente-termino;
 
%Calcular los siguientes términos de la sucesión)
x = 5;
while 4*erroractual>=valorerror 
      termino = siguiente;
      siguiente = siguiente+(1/x -1/x+2);
      erroractual = siguiente-termino;
      x = x+4;
end
aproxpi = 4*siguiente;
```