---
title: "Sumar filas impares y columnas pares"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Sumar filas impares y columnas pares

##  Enunciado

Realiza una función que, dada una matriz, devuelva dos valores: 

  * la suma de todos los elementos ubicados en filas impares 
  * la suma de todos los elementos ubicados en columnas pares. 

Por ejemplo, para la matriz: 
```text


 1   7   2
 4   5  -1
12   6   4


```
debería devolver 32 para la suma de las filas impares (1+7+2+12+6+4) y 18 para la suma de columnas pares (7+5+6). 

##  Soluciones

###  Programa en Matlab 

####  Solución con programación clásica 
```matlab


function [sumaimpar,sumapar]=SumaMat(m)
%Parámetros de entrada:
%  m: matriz de números
%Parámetros de salida:
%  sumaimpar: suma de todos los elementos ubicados en filas impares
%  sumpar: suma de todos los elementos ubicados en columnas pares.
%Variables:
%  nf,nc,x: ENTEROS
 
[nf,nc]=size(m);
%suma de las filas impares
sumaimpar=0;
for x=1:2:nf
  sumaimpar=sumaimpar+sum(m(x,:));
end
%suma de las columnas pares
sumapar=0;
for x=2:2:nc
  sumapar=sumapar+sum(m(:,x));
end

```
####  Solución Matlab 
```text


function [sumaimpar,sumapar]=SumaMat(m)
%Parámetros de entrada:
%  m: matriz de números
%Parámetros de salida:
%  sumaimpar: suma de todos los elementos ubicados en filas impares
%  sumpar: suma de todos los elementos ubicados en columnas pares.
%Variables:
%  nf,nc: ENTEROS
 
[nf,nc]=size(m);
v=sum(m');
sumaimpar=sum(v(1:2:nf));
v=sum(m);
sumapar=sum(v(2:2:nc));
```