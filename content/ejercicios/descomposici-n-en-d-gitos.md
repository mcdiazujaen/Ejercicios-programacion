---
title: "Descomposición en dígitos"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Descomposición en dígitos

##  Enunciado 

Crear un módulo o subalgoritmo que devuelva un array en el que cada posición contenga un dígito de un número entero dado. Por ejemplo, si el número de entrada fuera **109884** , el resultado sería el siguiente array: 

1 |  0 |  9 |  8 |  8 |  4   
---|---|---|---|---|---  
  
##  Soluciones 

###  Programa en Matlab 

####  Solución con programación básica 
```matlab


function vec = DescomponerEntero( n )
% FUNCION vec = DescomponerEntero( n )
% DESCRIPCIÓN: Devuelve un array en el que cada posición contiene un dígito del entero "n". 
% PARÁMETROS DE ENTRADA:
%    n: ENTERO; número que se va a descomponer
% PARÁMETROS DE SALIDA:
%    vec: ARRAY DE ENTEROS; dígitos del número "n"
 
% VARIABLES INTERNAS:
%    pos, tama: ENTEROS
%    v: ARRAY DE ENTEROS
 
%Obtener el valor absoluto de "n"
if n<0
    n = -n;
end
%Descomponer en dígitos
pos = 1;
while n>9
    v(pos) = rem(n,10);
    n = fix(n/10);
    pos = pos+1;
end
v(pos)=n;
%Dar la vuelta al array v porque tiene los dígitos de derecha a izquierda.
tama = length(v);
vec = zeros(1,tama);
for pos=1:tama
    vec(tama-pos+1)=v(pos);
end

```
####  Solución con programación Matlab avanzada 

Para esta solución se va a utilizar la función **num2str** que convierte un número a un array de caracteres (cada elemento del array es el carácter de un dígito). A continuación se le resta el código ASCII de caracter '0' para que el array se convierta en la representación en número entero de cada dígito. 
```text


function vec = DescomponerEntero( n )
% FUNCION vec = DescomponerEntero( n )
% DESCRIPCIÓN: Devuelve un array en el que cada posición contiene un dígito del entero "n". 
% PARÁMETROS DE ENTRADA:
%    n: ENTERO; número que se va a descomponer
% PARÁMETROS DE SALIDA:
%    vec: ARRAY DE ENTEROS; dígitos del número "n"
 
% VARIABLES INTERNAS: ninguna
 
vec = num2str(n) - '0';
```