---
title: "Matriz transpuesta"
date: 2024-01-01
draft: false
languages: ['pseudocódigo', 'matlab']
categories: ['enunciado']
tags: ['sin_c']
---

# Matriz transpuesta

##  Enunciado 

Dada una matriz A su transpuesta A’ es: 

![Imagen:Transpuesta.png](images/4/49/Transpuesta.png)

Realizar un subalgoritmo al que se le de una matriz de orden _**NxM**_ y devuelva su transpuesta. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text
 PROCEDIMIENTO transpuesta( mat, n, m, VAR trans)
 
 ENTRADAS:
     mat:ARRAY(n,m) DE REALES  (* Matriz original *)
     n: ENTERO   (* Filas de la matriz original o columnas de la transpuesta *)
     m: ENTERO   (* Columnas de la matriz original o filas de la transpuesta *)
 SALIDAS:
     trans: ARRAY (n,m) DE REALES     (* Matriz transpuesta *)
 VARIABLES:
     i,j: ENTEROS
 
 INICIO
     PARA i<--1 HASTA n HACER
          PARA j<--1 HASTA m HACER
               trans (j,i)<-- mat(i,j)
          FIN_PARA
     FIN_PARA
 FIN

```
###  Programa en Matlab 

####  Solución con programación básica 
```matlab

function b = Transpuesta( a )
% FUNCION b = Transpuesta( a )
% DESCRIPCIÓN: Devuelve una matriz b que es la transpuesta de a
% PARÁMETROS DE ENTRADA:
%    a: ARRAY(n,m) DE REALES; matriz original
% PARÁMETROS DE SALIDA:
%    b: ARRAY(m,n) DE REALES; matriz transpuesta
 
% VARIABLES INTERNAS:
%    x, y, n, m: ENTEROS
 
[n,m] = size( a );
for x=1:n
    for y=1:m
        b(y,x) = a(x,y);
    end
end

```
####  Solución con programación Matlab avanzada 
```text
function b = Transpuesta( a )
% FUNCION b = Transpuesta( a )
% DESCRIPCIÓN: Devuelve una matriz b que es la transpuesta de a
% PARÁMETROS DE ENTRADA:
%    a: ARRAY(n,m) DE REALES; matriz original
% PARÁMETROS DE SALIDA:
%    b: ARRAY(m,n) DE REALES; matriz transpuesta
 
% VARIABLES INTERNAS: Ninguna
 
b=a';
```