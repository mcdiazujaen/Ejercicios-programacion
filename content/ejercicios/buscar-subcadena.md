---
title: "Buscar subcadena"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
tags: ['Sin Pseudocódigo']
---

# Buscar subcadena

##  Enunciado

Implementar un algoritmo que lea dos cadenas caracteres e indique si la segunda cadena está contenida en la primera. 

Para las siguientes dos cadenas el algoritmo debería indicar que SI está contenida. 
```text
Vector 1:  B U E N O S   D I A S   T E N G A   U S T E D .				
Vector 2:  D I A S .
```
##  Soluciones 

###  Programa en Matlab 
```matlab
%PROGRAMA BuscarSubcadena
%DESCRIPCIÓN: Lee dos cadenas caracteres (carácter a carácter) que contenga una frase terminada en punto, e indica si la segunda está contenida en la primera. 
%ENTRADAS: Dos cadenas de caracteres.
%SALIDAS: Mensaje de confirmación.
%VARIABLES:
%   vector1, vector2: ARRAY DE CARÁCTERES (o cadena de caracteres)
%   contiene: LÓGICO
%   pos, diferencia, conta, n: ENTEROS
 
% Leer frases
vector1 = input('Introduzca primera frase: ','s');
vector2 = input('Introduzca segunda frase: ','s');
 
%Buscar si la segunda cadena está contenida en la primera
contiene = false;
pos = 1;
diferencia = length(vector1)-length(vector2);
while pos<=diferencia && ~contiene
   if vector1(pos)==vector2(1),
      conta=0;
      n=1;
      while n<length(vector2) && vector1(pos+n)==vector2(1+n),
         n=n+1;
      end
      if n==length(vector2),
         contiene=true;
      end
   end
   pos = pos + 1;
end
 
%Mostrar el resultado de la búsqueda
if contiene
   disp('La segunda frase SI está contenida en la primera.');
else
   disp('La segunda frase NO está contenida en la primera.');
end
```