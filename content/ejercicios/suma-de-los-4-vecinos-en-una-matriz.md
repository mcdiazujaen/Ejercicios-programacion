---
title: "Suma de los 4 vecinos en una matriz"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Suma de los 4 vecinos en una matriz

##  Enunciado

Diseña un módulo al que se le dé como parámetro de entrada una matriz **M** de números y devuelva en una matriz de dos filas las coordenadas de aquellos valores de **M** que sean mayores a la suma de sus cuatro vecinos (arriba, abajo, derecha e izquierda). En la primera fila de la matriz de salida se almacenarán las coordenadas de las filas de los valores y en la segunda fila las coordenadas de las columnas. 

**Ejemplo** : 
```text
 Si la matriz M es:         El módulo devolvería la matriz:
   1  7 -8  7                 1  1  2  2  3
   5  0  9  8                 2  4  1  3  2
   1 14  3  5

```
Observe que el primer valor que es mayor a la suma de sus vecinos es 7 (fila 1, columna 2). Sus vecinos valen 1 (izquierda), 0 (abajo) y -8 (derecha), arriba no tiene vecino. 

Usando el módulo anterior diseña un algoritmo que lea una matriz de un archivo y muestre en la pantalla la suma de los valores de la matriz que son mayores a la suma de sus cuatro vecinos. El formato del fichero tiene en la primera fila el número de filas y columnas de la matriz y en las filas siguientes los elementos de la matriz por filas. 

**Ejemplo** : Para el caso de la matriz anterior, el fichero contendría lo siguiente: 
```text
    3  4
    1  7 -8  7  
    5  0  9  8
    1 14  3  5

```
Para el fichero de ejemplo el algoritmo debe mostrar _42_ , que es la suma de los valores mayores a sus vecinos (7+7+5+9+14). 

##  Soluciones 

###  Programa en Matlab 

####  Apartado a 
```matlab

function coord = mayorVecinos (m)
% Funcion coord = mayorVecinos (m)
% Descripción: calcula las coordenadas de los valores de m que son mayores 
%      a la suma de sus 4 vecinos (arriba, abajo, izquierda y derecha)
% Parámetros de entrada:
%   m: matriz de números
% Parámetros de salida:
%   coord: matriz con las coordenadas de los valores de m mayores que sus vecinos. 
%      Tiene dos filas: en la primera se guarda las filas de las coordenadas 
%      y en la segunda las columnas de las coordenadas
 
coord = [];
[nf,nc] = size (m);
calculados = 0;
for f = 1:nf
    for c = 1:nc
        suma = 0;
        if f > 1
            suma = suma + m(f-1,c); % suma vecino arriba
        end
        if f < nf 
            suma = suma + m(f+1,c); % suma vecino abajo
        end
        if c > 1
            suma = suma + m(f,c-1); % suma vecino izqda
        end
        if c < nc
            suma = suma + m(f,c+1); % suma vecino derecha
        end
        if m(f,c) > suma
            calculados = calculados + 1;
            coord(:,calculados) = [f c];
        end
    end
end

```
####  Apartado b 
```matlab

% Programa Ejer2Principal
% Entradas: el nombre de un fichero que contiene una matriz con 
%      el formato especificado en el enunciado del ejercicio.
% Salidas: Suma de los elementos de la matriz que verifican la 
%      siguiente condición: el valor es mayor a la suma de sus 
%      4 vecinos (arriba,abajo,izquierda y derecha)
 
nombref = input('Introduce el nombre del fichero: ', 's');
fid = fopen (nombref, 'r');
if fid == -1
    disp(['No se pudo abrir el fichero ',nombref]);
else
    nf = fscanf (fid,'%f', 1);
    nc = fscanf (fid,'%f', 1);
    m = fscanf (fid,'%f', [nc nf]);
    m = m';
    coord = mayorVecinos (m);
    [nf,nc] = size(coord);
    suma = 0;
    for c = 1:nc
        suma = suma + m(coord(1,c),coord(2,c));
    end
    disp(['La suma de los elementos es ',num2str(suma)]);
end
```