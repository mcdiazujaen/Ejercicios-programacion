---
title: "Fábrica de electrodomésticos"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Fábrica de electrodomésticos

##  Enunciado

En una fábrica de electrodomésticos se quiere informatizar las estadísticas del proceso de fabricación. Para ello se almacena en un vector la información referente al código del producto fabricado, el número de máquinas por las que procesa y el tiempo en minutos que tarda en el procesamiento. La información de cada producto se almacena de forma consecutiva. Un ejemplo de vector con información es el siguiente: 
```text
 10  3  20  10  8  40  2  6  40  20  50  2  15  34  ...
```

El primer producto tiene código 10 y pasa por 3 máquinas; la duración de procesamiento en cada una de las máquinas es de 20, 10 y 8 minutos respectivamente. El segundo producto tiene código 40 y pasa por 2 máquinas y tarde en ellas 6 y 40 minutos respectivamente. Y así sucesivamente se irán almacenando los datos de todos los productos. 

Realiza una función que reciba como parámetro de entrada un vector con el formato descrito y devuelva el código del producto cuyo tiempo de procesamiento medio es mayor. 

##  Soluciones

###  Programa en Matlab 
```matlab

function codigoMax=ProcesamientoMax(v)
% FUNCION codigoMax=ProcesamientoMax(v)
% Parámetro de entrada:
%   v: vector con la información. El formato es: código producto,
%    número de máquinas por las que se procesa y el tiempo en cada 
%    una de estas máquinas, y así para cada producto 
% Parámetro de salida:
%   codigoMax: código del producto que tiene mayor tiempo de 
%     proceso medio
tam=length(v);
tmax=0;
pos=1;
while (pos<=tam)
    codigo=v(pos);  % código del producto
    pos=pos+1;
    nMaq=v(pos); % número de máquinas por las que pasa
    tiempoMedio=0;
    for m=1:nMaq
        tiempoMedio=tiempoMedio+v(pos+m);
    end
    tiempoMedio=tiempoMedio/nMaq;  % suponemos que hay máquinas
    if (tiempoMedio>tmax)
        codigoMax=codigo;
        tmax=tiempoMedio;
    end
    pos=pos+nMaq+1;
end
```