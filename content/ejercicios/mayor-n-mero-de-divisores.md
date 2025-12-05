---
title: "Mayor número de divisores"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
tags: ['sin_solución']
---

# Mayor número de divisores

##  Enunciado 

Diseña un algoritmo que lea desde teclado dos enteros positivos y muestre en pantalla el entero, de los situados entre los dos enteros leídos, que tenga más divisores, así como un listado de sus divisores (el 1 y el propio número no se consideran divisores). Por ejemplo, si se leen los valores 13 y 6, el resultado a mostrar en pantalla debe ser: 
```text
Entero con mayor cantidad de divisores: 12
Divisores 2, 3, 4, 6

```
Para ello diseñar también un subalgoritmo que dado un número entero devuelva cuáles son sus divisores y la cantidad de éstos. Dicho subalgoritmo debe ser invocado en el algoritmo principal cuando se requiera dicha tarea. 

##  Soluciones 
```matlab

%Programa Masdivisores
%Entradas: dos números enteros positivos
%Salidas: número entre ambos valores enteros que más divisores tiene (sin incluir 1 y él 
%      mismo) y sus dividores
 
%Leer los número enteros positivos.
a=input('Introduce un número entero positivo: ');
while a<0 && fix(a)~=a
   disp('ERROR: el número debe ser ENTERO POSITIVO');
   a=input('Introduce un número entero positivo: ');
end
 
b=input('Introduce otro número entero positivo: ');
while b<0 && fix(b)~=b
   disp('ERROR: el número debe ser ENTERO POSITIVO');
   b=input('Introduce otro número entero positivo: ');
end
 
%Comprobar cual es el mayor y cual es el menor.
if (a>b)
   mayor=a;
   menor=b;
else
   mayor=b;
   menor=a;
end
 
%Encontrar el que mayor divisores tiene
maxdivisores=0;
num=0;
divisores=[];
 
for n=menor:mayor
    auxdivisores=[];
    for x=2:n-1
        if (rem(n,x)==0)
            auxdivisores=[auxdivisores x];
        end
    end
    ndivisores=length(auxdivisores);
    if (maxdivisores<ndivisores)
        maxdivisores=ndivisores
        divisores=auxdivisores;
        num=n;
    end
end
 
%Mostrar el resultado.
disp(['El número que más divisores tiene es el ',num2str(num),' con ',num2str(maxdivisores),' divisores']);
disp('Los divisores son: ');
disp(divisores);
```