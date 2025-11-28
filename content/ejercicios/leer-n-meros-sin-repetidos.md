---
title: "Leer números sin repetidos"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Leer números sin repetidos

##  Enunciado

Realiza una función que lea números del teclado hasta que se introduzca un valor ya introducido. La función debe devolver un vector con los valores leídos (salvo el último que está repetido). Por ejemplo, si se leen los siguientes valores: 
```text


3 7 8 2 5 7


```
habría que devolver el vector 
```text


[3 7 8 2 5]


```
##  Soluciones 

###  Programa en Matlab 
```matlab


function vector = SinRepetidos
% Funcion vector = SinRepetidos
%    Descripción: Lee números de teclado hasta que se introduzca
%          un valor ya introducido. Devuelve los números leídos
%          salvo el último (el repetido)
%    Parámetros de salida:
%       vector: ARRAY DE REALES; el vector con los números leídos,
%            salvo el último número leído (que está repetido)
vector = [];
seguir = true;
while seguir
   num = input('Introduce un número: ');
   for pos = 1:length(vector)
      if num == vector(pos)
         seguir = false;
      end
   end
   if seguir
      vector = [vector num];
   end
end
```