---
title: "Triángulo de Pascal centrado"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Triángulo de Pascal centrado

##  Enunciado 

Implementa una función que reciba como parámetro de entrada un número entero **n** y devuelva una matriz de **n** x **(2n-1)** , que represente el triángulo de Pascal. 

**Ejemplo:** si n=5, devolvería la matriz: 

0 |  0 |  0 |  0 |  1 |  0 |  0 |  0 |  0   
---|---|---|---|---|---|---|---|---  
0 |  0 |  0 |  1 |  0 |  1 |  0 |  0 |  0   
0 |  0 |  1 |  0 |  2 |  0 |  1 |  0 |  0   
0 |  1 |  0 |  3 |  0 |  3 |  0 |  1 |  0   
1 |  0 |  4 |  0 |  6 |  0 |  4 |  0 |  1   
  
Para resolver el problema se parte de una matriz de ceros y se empieza poniendo un 1 en la posición central de la primera fila. Cada elemento del resto de filas se obtiene sumando los elementos que están a su izquierda y derecha en la fila de arriba. 

  

##  Soluciones 

###  Programa en Matlab 
```matlab


function t = triangPascal (n)
% FUNCION t = triangPascal (n)
% DESCRIPCIÓN: Calcula un triángulo de Pascal
% PARÁMETROS DE ENTRADA:
%   n: ENTERO; el número de filas de la matriz que guarda el triángulo
% PARÁMETROS DE SALIDA:
%   t: ARRAY BIDIMENSIONAL DE ENTERSO; la matriz guardando el triángulo
t = zeros (n,2*n-1);
t(1,n) = 1;
[nf,nc] = size(t);
for f = 2:nf
    for c = 1:nc
        if c > 1
            supizq = t(f-1,c-1);
        else
            supizq = 0;
        end
        if c < nc
            supder = t(f-1,c+1);
        else
            supder = 0;     
        end
        t(f,c) = supizq + supder;
    end
end
```