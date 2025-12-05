---
title: "Comparar dos arrays desordenados"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Comparar dos arrays desordenados

##  Enunciado

Implementa una función que reciba como parámetros de entrada dos vectores y devuelva un valor lógico indicando si tienen los mismos elementos. Los elementos en los vectores pueden estar en cualquier orden y pueden tener elementos duplicados. La única función permitida dentro del código es aquella que nos indique el tamaño del vector (en Matlab se puede utilizar _length_ para conocer el tamaño de un vector). 

##  Soluciones

###  Programa en Matlab 
```matlab

function igual=VectoresIguales(v1, v2)
% FUNCION igual=VectoresIguales(v1, v2)
% Parámetros de entrada:
%   v1 ,v2: vectores de números. Los elementos de ambos pueden 
%       estar en cualquier orden
% Parámetro de salida:
%   igual: LOGICO, verdadero si los vectores tienen los mismos elementos y 
%       falso en otro caso 
%  Para resolverlo sólo se puede usar de Matlab la función length
tam1=length(v1);
tam2=length(v2);
if (tam1~=tam2)
    igual=false;
else
    igual=true;
    p=1;
    while(p<=tam1 && igual) 
      veces1=0;
      for z=1:tam1
          if (v1(p)==v1(z))
             veces1=veces1+1; % veces que está el elemento en el vector 1
          end
      end
      veces2=0;
      for z=1:tam2
          if (v1(p)==v2(z)) 
             veces2=veces2+1; % veces que está el elemento en el vector 2
          end
      end
      if (veces1~=veces2)
          igual=false;
      else
          p = p+1;
      end 
  end
end
```