---
title: "Sumar valores pares de posiciones pares"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Sumar valores pares de posiciones pares

##  Enunciado

Implementa un programa que lea desde teclado una secuencia de números enteros terminada en 0 (es decir, va pidiendo datos al usuario hasta que pulse 0) y muestre en pantalla el número de veces que un número par de la secuencia ocupa una posición par en la misma. 

**Observación:** hay que resolverlo sin utilizar arrays. Por ejemplo, si la secuencia introducida es 
```text


7 4 2 1 8 6 0


```
el programa mostraría 2 (correspondiente al 4 de la posición 2 y al 6 de la posición 6). 

##  Soluciones

###  Programa en Matlab 
```matlab


%Programa Secuencia
%Entradas: secuencia de números terminada en 0
%Salidas: número de veces que un número para está en una posición par de la secuencia
 
veces=0;
posicion=0;
num=input('Introduce un número, 0 para terminar: ');
while (num~=0)
   posicion=posicion+1;
   if (mod(num,2)==0 && mod(posicion,2)==0)
      veces=veces+1;
   end
   num=input('Introduce un número, 0 para terminar: ');
end
disp(['Veces que un número par está en una posición par de la secuencia:',num2str(veces)]);
%También se puede utilizar:
%fprintf('Veces que un número par está en una posición par de la secuencia: %d\n',veces);
```