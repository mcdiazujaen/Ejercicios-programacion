---
title: "Reorganización de un array"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Reorganización de un array

##  Enunciado 

Realizar un procedimiento que permita reestructurar un array a partir de un elemento dado según el siguiente ejemplo: 
```text
Array inicial: 3-20-8-40
Valor de reorganización: 8

Array final: 8-40-3-20

```
##  Soluciones 

###  Diseño en pseudocódigo 
```text
PROCEDIMIENTO Reorg(VAR V: ARRAY DE ENTEROS, n:ENTERO ,x: ENTERO)
ENTRADAS:
  V: ARRAY DE REALES  _(Array que se quiere reorganizar. El array empieza en la posición 1)_
  n: ENTERO           _(Número de elementos del array V)_
  x: ENTERO           _(Elemento de reorganización)_
SALIDAS: 
  V: ARRAY DE REALES  _(Array reorganizado)_
VARIABLES: 
  W: ARRAY DE REALES
  i, k: ENTEROS
INICIO
   _(Localizar el elemento de reorganización en el array)_
   i <-- 1
   MIENTRAS ((x<>V(i)) Y (i<= n)) HACER	
        i <-- i+1
   FIN MIENTRAS

   _(Rellenar el array W con los elementos reorganizados)_
   k <-- 1
   PARA j <-- i HASTA n CON INCREMENTO DE 1 HACER 
        W(k) <-- V(j)
        k <-- k+1
   FIN PARA
   PARA j <-- 1 HASTA i-1 CON INCREMENTO DE 1 HACER 
        W(k) <-- V(j)
        k <-- k+1
   FIN PARA

   _(Copiar el array W en el array V)_
   PARA j <-- 1 HASTA n CON INCREMENTO DE 1 HACER 
        V(j) <-- W(j)
   FIN PARA
FIN

```
###  Programa en C
```c

 void Reorg(float V[1000], int n, int x){
    /*----
     ENTRADAS:
      ''V: array que se quiere reorganizar. El array empieza en 1''
      ''n: número de elementos del array unidimensional''
      ''x: elemento de reorganización''
     SALIDAS
      ''V: Array ya reorganizado''
    ----*/
    //VARIABLES
      float W[1000];
      int i, k;
 
      //''(Localizar el elemento de reorganización en el array)''
      i=1;
      while( (x!=V[i]) && (i<=n) ){
            i=i+1;
      } 
 
      //''(Rellenar la matriz W con los elementos reorganizados)''
      k=1;
      for(j=i; j<=n; j++){
             W[k]=V[j];
             k=k+1;
      }
      for(j=1; j<=i-1; j++){
             W[k]=V[j];
             k=k+1;
      }
 
      //''(Copiar el array W en V)''
      for(j=1; j<=n; j++){
             V[j]=W[k];
      }
  }
```