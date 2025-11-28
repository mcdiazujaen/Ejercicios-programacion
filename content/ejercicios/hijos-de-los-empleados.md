---
title: "Hijos de los empleados"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Hijos de los empleados

##  Enunciado

Una compañía almacena en una matriz información sobre las edades de los hijos de sus empleados. Cada fila almacena información sobre un empleado. En la primera columna se guarda el código del empleado; a continuación, en el resto de columnas de la fila, se almacenan las edades (en años) de los hijos del empleado. Las columnas de la derecha que no contienen edades de hijos se rellenan con el valor -1. Por ejemplo, el empleado de código 10 tiene 3 hijos cuyas edades son 2, 10 y 8 años. Como la matriz tiene 10 columnas sólo se puede almacenar edades de 9 hijos de un empleado. 

10 |  2 | 10 |  8 | -1 | -1 | -1 | -1 | -1 | -1   
---|---|---|---|---|---|---|---|---|---  
40 |  6 |  4 | -1 | -1 | -1 | -1 | -1 | -1 | -1   
20 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1   
50 |  3 |  9 | -1 | -1 | -1 | -1 | -1 | -1 | -1   
30 |  2 |  4 |  6 |  8 | -1 | -1 | -1 | -1 | -1   
  
Teniendo en cuenta esta representación, realiza funciones que calculen: 

a) El código del empleado con más hijos. Si existe más de uno devuelve el primero en aparecer en la matriz. Para la matriz de ejemplo tendría que devolver el código 30, pues el empleado con dicho código tiene 4 hijos, más que los demás empleados. 

b) De los empleados que tienen dos hijos, el código del empleado cuya diferencia de edad entre sus hijos es mayor. Si no existe ningún empleado con dos hijos se devuelve el código -1. Para la matriz de ejemplo, habría que devolver el código 50. Pues, de los dos empleados con dos hijos (códigos 40 y 50), la diferencia de edad de los dos hijos del empleado de código 50 es 6, mientras que la diferencia de edad de los dos hijos del empleado de código 40 es 2. 

##  Soluciones 

###  Programa en Matlab 

####  Apartado a 
```matlab


function codigo = MasHijos(matriz)
% Funcion codigo = MasHijos(matriz)
% Descripción: calcula el código del empleado con mayor número de hijos
% Parámetros de entrada:
%    matriz: ARRAY BIDIMENSINAL DE ENTEROS; matriz de empleados según 
%         el formato especificado en el enunciado
% Parámetros de salida:
%    codigo: ENTERO; código del empleado de la matriz con más hijos. Si el
%         máximo es compartido por varios empleados se devuelve el
%         código del empleado con más hijos que aparece en la menor
%         fila de la matriz
[nf,~] = size (matriz);
maximo = -1;
for fila = 1:nf
   %Contar cuantos hijos tiene el empleado "fila"
   nhijos = 0;
   col = 2;
   while col <= 10 && matriz(fila,col) ~= -1
      col = col + 1;
      nhijos = nhijos + 1;
   end
   %Si el empleado es el que tiene más hijos, se guarda
   if nhijos > maximo
      maximo = nhijos;
      codigo = matriz(fila,1);
   end
end

```
####  Apartado b 
```text


function codigo = MayorDiferencia(matriz)
% Funcion codigo = MayorDiferencia(matriz)
% Descripción: calcula el código del empleado con dos hijos con
%           mayor diferencia de edad entre sus hijos
% Parámetros de entrada:
%     matriz: ARRAY BIDIMENSIONAL DE ENTEROS;matriz de empleados
%           según el formato especificado en el enunciado
% Parámetros de salida:
%     codigo: ENTERO; código del empleado de la matriz con dos hijos
%           cuya diferencia de edad entre sus hijos es mayor. Si
%           existe más de uno devuelve el ubicado en la fila de
%           índice menor. Si no existe ningún empleado con dos
%           hijos devuelve el código -1
[nf,~] = size (matriz);
maximo = -1;
codigo = -1;
for fila = 1:nf
   if matriz(fila,3) ~= -1 && matriz(fila,4) == -1
      if abs(matriz(fila,2)-matriz(fila,3)) > maximo
         codigo = matriz(fila,1);
         maximo = abs(matriz(fila,2)-matriz(fila,3));
      end
   end
end
```