---
title: "Diferencia entre elementos consecutivos de un vector"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
categories: ['enunciado']
---

# Diferencia entre elementos consecutivos de un vector

##  Enunciado 

Realizar un subalgoritmo que dado un vector _A_ de _n_ números reales, obtener la diferencia mas grande y la menor diferencia entre dos elementos consecutivos de ese vector. 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text
 PROCEDIMIENTO Diferencias (A, n, VAR mayor, VAR menor)
 ENTRADAS:
    A: ARRAY (0..1000) DE REALES  ''(*Array donde buscar la menor y mayor diferencia de elementos*)''
    n: ENTERO                     ''(*Número de elementos útiles del array*)''
 SALIDAS:
    mayor: REAL ''(*Mayor diferencia entre elementos consecutivos*)''
    menor: REAL ''(*Menor diferencia entre elementos consecutivos*)''
 VARIABLES:
    dif: REAL
    pos: ENTERO
 INICIO
    ''(*Calcular la primera diferencia*)''
    dif <-- A(1) - A(0)
    SI dif<0 ENTONCES
       dif <-- -dif
    FIN_SI
    mayor <-- dif
    menor <-- dif
 
    ''(*Calcular la diferencia del resto de los elementos*)''
    PARA pos <--2 HASTA n-1 HACER
       dif <-- A(pos)-A(pos-1)
       SI dif<0 ENTONCES
          dif<-- -dif
       FIN_SI
 
       ''(*Comprobar si la diferencia es mayor*)''
       SI dif>mayor ENTONCES
          mayor <-- dif
       FIN_SI
 
       ''(*Comprobar si la diferencia es mayor*)''
       SI dif<menor ENTONCES
          menor <-- dif
       FIN_SI
    FIN_PARA
 FIN
```

###  Programa en C++ 
```c

 #include <stdio.h> 
 #include <stdlib.h>
 
 void Diferencias ( float A[1001], int n, float &mayor, float &menor){
    /*------
    ENTRADAS:
       A: Array donde buscar la mayor y menor diferencia de elementos.
       n: Números de elementos útiles del array.                            
    SALIDAS:
       mayor: Mayor diferencia entre elementos consecutivos
       menor: Menor diferencia entre elementos consecutivos
    ------*/
    //VARIABLES:
    float dif;   
    int pos;
 
    //Calcular la primera diferencia
    dif = A[1]-A[0];
    if (dif<0){
       dif=-dif;
    }
    mayor=dif;
    menor=dif;   
 
    //Calcular la diferencia del resto de los elementos   
    for (pos=2; pos<=n-1; pos++){
       dif=A[pos]-A[pos-1];
       if (dif<0){
          dif=-dif;
       }
 
       //Comprobar si la diferencia es mayor
       if (dif>mayor){
          mayor=dif;
       }
 
       //Comprobar si la diferencia es menor
       if (dif<menor){
          menor=dif;
       }
    }
}
```

###  Programa en Matlab 

####  Solución con programación básica 
```matlab

function [mayor,menor] = Diferencias( A )
%FUNCIÓN [mayor,menor] = Diferencias( A )
%DESCRIPCIÓN: Dado un vector A de n números reales, obtener la diferencia mas grande y 
%    la menor diferencia entre dos elementos consecutivos de ese vector. 
%ENTRADAS:
%   A: ARRAY(n) DE REALES; El vector.
%SALIDAS:
%   mayor: REAL; la mayor diferencia
%   menor: REAL; la menor diferencia
 
%VARIABLES:
%   n, pos: ENTEROS;
%   dif: REAL
 
n = length( A );
%Calcular la primera diferencia
dif = A(2)-A(1);
if dif<0
    dif = -dif;
end
mayor = dif;
menor = dif;
%Calcular la diferencia del resto de los elementos
for pos=2:n-1
    dif = A(pos+1)-A(pos);
    if dif<0,
        dif = -dif;
    end
    %Comprobar si la diferencia es mayor.
    if dif>mayor
        mayor = dif;
    end
    %Comprobar si la diferencia es menor.
    if dif<menor
        menor = dif;
    end
end
```

####  Solución con programación Matlab avanzada 

Para realizar esta función se utilizan las siguientes funciones de Matlab: 

  * **length** : para calcular la longitud de un array. 
  * **abs** : para obtener los valores absolutos de todos los elementos de un array. 
  * **max** y **min** : para encontrar el máximo y el mínimo de array, respectivamente. 

```text
function [mayor,menor] = Diferencias( A )
%FUNCIÓN [mayor,menor] = Diferencias( A )
%DESCRIPCIÓN: Dado un vector A de n números reales, obtener la diferencia mas grande y 
%    la menor diferencia entre dos elementos consecutivos de ese vector. 
%ENTRADAS:
%   A: ARRAY(n) DE REALES; El vector.
%SALIDAS:
%   mayor: REAL; la mayor diferencia
%   menor: REAL; la menor diferencia
 
%VARIABLES:
%   n: ENTERO
%   dif: ARRAY(n-1) DE REALES
 
n = length( A );
dif = abs( A(1:n-1)-A(2:n) );
mayor = max(dif);
menor = min(dif);
```