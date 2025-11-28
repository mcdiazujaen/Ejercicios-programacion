---
title: "Premios Primitiva"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Premios Primitiva

##  Enunciado

Implementa un módulo para calcular cuántos premios nos han tocado en “La Primitiva”. Para ello el módulo recibirá como entradas un vector de 6 números enteros, que representa la combinación ganadora, y una matriz de enteros de 6 columnas, en el que cada fila representa las combinaciones que nosotros hemos jugado (una selección de 6 números entre el 1 y el 49). El módulo devolverá tres valores que indiquen cuántos premios de 6, de 5 y de 4 aciertos hemos obtenido. Se considera que una fila de la matriz tiene un “premio de N” cuando contenga N números de la combinación ganadora. Ejemplo: si la combinación ganadora es: 
```text


5  16  18  19  26  31


```
Y nuestras apuestas son 5: 
```text


Apuesta 1:  3  18  20  26  40  48  --> 2 aciertos
Apuesta 2:  5  16  18  26  30  31  --> 5 aciertos
Apuesta 3: 16  18  26  31  32  49  --> 4 aciertos
Apuesta 4:  5   7  16  17  18  26  --> 4 aciertos
Apuesta 5:  1   6  24  33  37  45  --> 0 aciertos


```
El módulo debe devolver que hemos obtenido 0 premios de 6 aciertos, 1 premio de 5 aciertos y 2 premios de 4 aciertos. 

##  Soluciones

###  Programa en Matlab 
```matlab


function [premios6, premios5, premios4]=Primitiva(v,m)
%Parámetros de entrada:
%    v: vector de 6 números enteros, que representa la combinación ganadora de
%       la primitiva
%    m: matriz de enteros de 6 columnas, en el que cada fila representa las 
%        combinaciones que nosotros hemos jugado 
%       (una selección de 6 números entre el 1 y el 49).
%Parámetros de salida:
%  premios6, premios5, premios4: número de premios de 6, 5 y 4 aciertos
%     respectivamente
 
%se cuenta el número de aciertos en cada apuesta
[napuestas,~]=size(m);
totalpremios=zeros(1,6);
for x=1:napuestas
    aciertos=0;
    for y=1:6
        if (sum(v(y)==m(x,:))>0)
            aciertos=aciertos+1;
        end
    end
    if (aciertos>0)
       totalpremios(aciertos)=totalpremios(aciertos)+1;
    end
end
premios6=totalpremios(6);
premios5=totalpremios(5);
premios4=totalpremios(4);
```