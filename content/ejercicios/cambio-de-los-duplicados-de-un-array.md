---
title: "Cambio de los duplicados de un array"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---


# Cambio de los duplicados de un array

##  Enunciado 

Diseñar un procedimiento que acepte como parámetro un vector que pueda contener elementos duplicados. El procedimiento debe reemplazar cada elemento repetido por -1 y devolver el vector modificado, además del número de modificaciones hecho. 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text


  PROCEDIMIENTO Repeticion(VAR V: ARRAY DE REALES; n: ENTERO; VAR nmodif: ENTERO)
  ENTRADAS:
    V: ARRAY DE REALES  ''(*Array que contiene los elementos repetidos. En array empieza en la posición 1*)''
    n: ENTERO           ''(*Número de elementos del array*)''
  SALIDA:
    V: ARRAY DE REALES  ''(*Array con los elementos repetidos sustituidos por -1*)''
    nmodif: ENTERO      ''(*Número de elementos modificados en el array*)''
  VARIABLES: 
    i, j: REAL 
  INICIO
    nmodif <-- 0
    PARA i <-- 1 HASTA n-1 CON INCREMENTO DE 1 HACER
      PARA j <-- i+1 HASTA n CON INCREMENTO DE 1 HACER
        SI ( V(i)=V(j) Y V(j)<>-1 ) ENTONCES
          V(j) <-- -1
          nmodif <-- nmodif+1
        FIN SI
      FIN PARA
    FIN PARA
  FIN

```
###  Programa en C 
```c


 #include <stdio.h>
 #include <stdlib.h>
 
 void Repeticion(float V[n], int n , int &nmodif){
    /*-------
    ENTRADAS:
      V: Array contiene los elementos repetidos. El array empieza en la posición 0
      n: Números de elementos del array
    SALIDAS:
      V:      Array con los elementos repetidos sustituidos por -1
      nmodif: número de elementos modificados en el array
    ---------*/
    //VARIABLES:
    float i,j;
 
    nmodif=0;
    for (i=0; i<=n-2; i++){
       for (j=i+1; j<=n-1; j++){
          if ( V[i]==V[j] && V[j] != -1 ){
             V[j]=-1;
             nmodif=nmodif+1;
          }
       }
    }         
 }

```
###  Solución en Matlab 
```matlab


function [v,nrepe]=Repeticion(w)
%FUNCION [v,nrepe]=Repeticion(w)
%DESCRIPCION: Cambia los elementos repetidos de un vector por -1.
%PARÁMETROS DE ENTRADA:
%   w: ARRAY DE ENTEROS, vector con elementos repetidos.
%PARÁMETROS DE SALIDA:
%   v: ARRAY DE ENTEROS, vector con los repetidos cambiados por -1
%   nrepe: ENTERO, número de repeticiones encontradas.
%VARIABLES:
%   n,pos1,pos2:ENTEROS
 
v=w;
n=length(v)
nrepe=0;
for pos1=1:n
    for pos2=pos1+1:n
        if(v(pos1))==(v(pos2))&&(v(pos2)~=-1),
            v(pos2)=-1;
            nrepe=nrepe+1;
        end
    end
end
```