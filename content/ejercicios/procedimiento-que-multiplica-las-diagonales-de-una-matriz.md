---
title: "Procedimiento que multiplica las diagonales de una Matriz"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado']
tags: ['Sin C', 'Sin Matlab']
---

# Procedimiento que multiplica las diagonales de una Matriz

##  Enunciado 

Un subalgoritmo que dada una matriz cuadrada de enteros, obtenga un vector de reales de la siguiente forma: cada elemento del vector será el valor obtenido tras el producto de elementos de la diagonal correspondiente de la matriz. Ejemplo: 

![Imagen:diagonales.jpg](images/4/41/Diagonales.jpg)

##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**
```text
 PROCEDIMIENTO Diagonales(A, t, VAR B, VAR h)
 ENTRADAS: A: ARRAY[1..t, 1..t] DE ENTEROS, // matriz cuadrada
           t: ENTERO, // número de filas y columnas de A, t>0
 SALIDAS: B: ARRAY[1..h] DE ENTEROS, (* contiene en cada elemento la suma de 
                          una de las diagonales de la matriz de entrada.*)
          h: ENTERO, tamaño de B.
 VARIABLES: 
 INICIO
   h<--0
   PARA  k=1 HASTA  t-1 HACER   // En esta parte hace A(1,1)    
      i<--k                     // A(2,1)*A(1,2)
      j<--1                     // A(3,1)*A(2,2)*A(1,3)
      prod<--1
      MIENTRAS (i>=1) AND (j<=t) HACER
         prod<--prod*A(i,j)
         i<--i-1
         j<--j+1
      FIN_MIENTRAS
      h<--h+1
      B(h)<--prod
   FIN_PARA
   PARA k=1 HASTA  t HACER   // En esta parte hace A(4,1)*A(3,2)*A(2,3)*A(1,4)
      j<--k                  // A(4,2)*A(3,3)*A(2,4)
      i<--t                  // A(4,3)*A(3,4)
      prod<--1               // A(4,4) 
      MIENTRAS  (i>=1) AND (j<=t) HACER
         prod<--prod*A(i,j)
         i<--i-1
         j<--j+1
      FIN_MIENTRAS
      h<--h+1
      B(h)<--prod
   FIN_PARA
 FIN
```

###  Programa en Pascal por **lperez**
```text
 Procedure Diagonales(var a:matriz;t:integer;var b:vector;var n:integer);
 (* Entradas: a, una matriz cuadrada y t su tama¤o
    Salidas: b, un array de una columna que contiene en cada elemento la suma
            de una de las diagonales de la matriz (empezando la suma por la
            diagonal de m s a la izquierda) y n el n£mero de elementos de b*)
 var i,j,k,prod:integer;
 begin
  n:=1;
  for k:=1 to t-1 do
    begin
      i:=k;
      j:=1;
      prod:=1;
      while (i>=1) and (j<=t) do
        begin
          prod:=prod*a[i,j];
          i:=i-1;
          j:=j+1;
        end;
      b[n]:=prod;
      n:=n+1;
    end;
  for k:=1 to t do
    begin
      j:=k;
      i:=t;
      prod:=1;
      while (i>=1) and (j<=t) do
        begin
          prod:=prod*a[i,j];
          i:=i-1;
          j:=j+1;
        end;
      b[n]:=prod;
      n:=n+1;
    end;
    n:=n-1;
 end;
```