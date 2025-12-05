---
title: "Suma de las diagonales inferiores"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Suma de las diagonales inferiores

##  Enunciado

Implementa una función a la que se le de cómo parámetro de entrada una matriz cuadrada y dos enteros f y c (menores o iguales a la dimensión de la matriz) que representan un número de fila y columna respectivamente. La función ha de devolver la suma de los elementos que quedan debajo de las diagonales que se cruzan en la posición (f, c). 

Ejemplos: 
```text
f=2 y c=2 

   3 1 2 7 4
   4 2 7 0 0
   1 _**6**_ 1 4 0
   _**2 0 3**_ 1 9
   _**6 1 3 1**_ 2

Suma=22

f=3 y c=4

   3 1 2 7 4
   4 2 7 0 0
   1 6 1 4 0
   2 0 3 _**1**_ 9
   6 1 _**3 1 2**_

Suma=7
```

##  Soluciones

###  Programa en Matlab 
```matlab

function suma=Diagonales(m,f,c)
%Parámetros de Entrada: 
%  m: matriz de números
%  f, c: indican una posición de fila y columna dentro de la matriz
%      (menores o iguales a la dimensión de la matriz y mayores que 0) 
%Parámetros de Salida:
%  suma: suma de los elementos que quedan debajo de las
%      diagonales que se cruzan en la posición (f, c).
 
[fil,col]=size(m);
suma=m(f,c); % el primer elemento es el que hay en la posición dada
 
% el resto de elementos están en las siguientes filas y en el rango de
% columnas una más a la izquierda y derecha en cada paso de fila
inicio=c;
fin=c;
for x=f+1:fil 
    if (inicio>1) % no salir del rango de la matriz por la izquierda 
        inicio=inicio-1;
    end
    if (fin<col) % no salir del rango de la matriz por la derecha 
        fin=fin+1;
    end
    for y=inicio:fin % se suman los elementos de la fila
        suma=suma+m(x,y) 
    end
end
```