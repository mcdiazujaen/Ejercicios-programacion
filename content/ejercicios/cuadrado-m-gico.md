---
title: "Cuadrado Mágico"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
tags: ['sin_solución']
---

# Cuadrado Mágico

##  Enunciado 

Diseña un algoritmo que determine si una matriz cuadrada forma un cuadrado mágico. Se considera un cuadrado mágico aquel en el cual las filas, columnas y las diagonales principal y secundaria suman lo mismo. Para ello el algoritmo deberá hacer uso de los subalgoritmos citados a continuación, y que también se han de diseñar: 

  1. Subalgoritmo al que se le de la matriz y un número de fila y devuelva la suma de dicha fila 
  2. Subalgoritmo al que se le de la matriz y un número de columna y devuelva la suma de dicha columna 
  3. Subalgoritmo al que se le de la matriz y devuelva la suma de la diagonal principal y de la secundaria. 

##  Soluciones 

###  Programa en Matlab 

####  Programa principal 
```matlab

%Programa CuadradoMagico
%Descripción: Determina si una matriz cuadrada forma un cuadrado mágico.
%Entradas: La matriz a estudiar.
%Salidas: Mensaje de “Es cuadrado mágico” o “No es cuadrado mágico”.
%Variables:
%   m: ARRAY(tama,tama) DE REALES
%   tama, x, y, pos, sdp, sds: ENTERO.
%   vf, vc: ARRAY(tama) DE REALES
 
%Pedir la matriz cuadrada al usuario
tama = input('Introduzca el tamaño de la matriz cuadrada: ');
m = zeros(tama);
disp('Introduzca los valores de la matriz:');
for x=1:tama
   for y=1:tama
      fprintf(Valor %i, %i',x,y);
      m(x,y)=input(': ');
   end
end
 
%Calcular las sumas de filas, columnas y diagonales.
for pos=1:tama
   vf(pos)=sumaf(m,pos);
   vc(pos)=sumac(m,pos);
end
[sdp sds]=sumad(m);
 
%Comprobar si es un cuadrado mágico
if sdp==sds
   pos=1;
   while (sdp==vf(pos))&&(sdp==vc(pos))&&(pos<=tama)
      pos=pos+1;
   end
   if pos>tama
      disp('Cuadrado mágico');
   else
      disp('No es cuadrado mágico');
   end
else
   disp('No es cuadrado mágico');
end

```
####  Módulo 1 
```matlab

function suma=sumaf(m,f)
%FUNCIÓN suma=sumaf(m,f)
%DESCRIPCIÓN: Devuelve la suma de una fila de una matriz.
%PARÁMETROS DE ENTRADA:
%   m: ARRAY(?,?) DE REALES, Matriz cuadrada
%   f: ENTERO, Número de fila.
%PARÁMETROS DE SALIDA:
%   suma: REAL, Suma de dicha fila.
 
%VARIABLES:
%   pos: ENTERO
 
suma=0;
for pos=1:size(m,2)
   suma = suma+m(f,pos);
end

```
####  Módulo 2 
```text

function suma=sumac(m,c)
%FUNCIÓN suma=sumac(m,c)
%DESCRIPCIÓN: Devuelva la suma de una columna de una matriz.
%PARÁMETROS DE ENTRADA: 
%   m: ARRAY(?,?) DE REALES, Matriz cuadrada
%   c: ENTERO, Número de columna.
%PARÁMETROS DE SALIDA:
%   suma: REAL, Suma de dicha columna.
 
%Variables: 
%   pos: ENTERO.
 
suma=0;
for pos=1:size(m,1)
   suma=suma+m(pos,c);
end

```
####  Módulo 3 
```matlab

function [dp ds]=sumad(m)
%Programa: Devuelva la suma de la diagonal principal y de la secundaria de una matriz cuadrada.
%PARÁMETROS DE ENTRADA: 
%   m: ARRAY(?,?) DE REALES, Matriz cuadrada
%PARÁMETROS DE SALIDA:
%   dp: REAL, Suma de la diagonal principal.
%   ds: REAL, Suma de la diagonal secundaria.
 
%Variables:
% pos, tama: ENTEROS
dp=0;
ds=0;
tama = size(m,1);
for pos=1:tama
    dp=dp+m(pos,pos);
    ds=ds+m(pos,tama-pos+1);
end
```