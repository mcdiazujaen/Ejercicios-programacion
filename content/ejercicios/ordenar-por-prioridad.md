---
title: "Ordenar por prioridad"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Ordenar por prioridad

##  Enunciado 

En una aplicación de gestión de tareas se tienen dos vectores de información. En uno de ellos se almacena el código de la tarea (un entero) y en el otro paralelo se almacena la prioridad de dicha tarea (el número más bajo de prioridad se corresponde con la tarea más prioritaria). Implementa una función que reciba como parámetros de entrada ambos vectores y devuelva un vector con los códigos de las tareas ordenados por prioridad decreciente. Se supone que ningún trabajo puede tener la misma prioridad que otro. 

**Ejemplo:**
```text

Vector con los códigos de las tareas:	123	543	276	27	76	34	145
Vector con las prioridades..........:	8	3	1	2	4	7	5

Vector de salida....................:	276	27	543	76	145	34	123

```
##  Soluciones 

###  Programa en Matlab 
```matlab

function sol = prioriza(t, p)
% Función sol = prioriza(t, p)
% Descripción: Calcula una lista de tareas priorizadas
% Parámetros de entrada:
%   t: ARRAY DE ENTEROS; vector de tareas
%   p: ARRAY DE ENTEROS; vector de prioridades. 
%        p(i) indica la prioridad de la tarea t(i)
% Parámetros de salida:
%   sol: ARRAY DE ENTEROS; vector con las tareas en orden de prioridad
 
sol = [];
while length(t) > 0
  [valor,pos] = min (p);
  sol = [sol t(pos)];
  t(pos) = [];
  p(pos) = [];
end
```