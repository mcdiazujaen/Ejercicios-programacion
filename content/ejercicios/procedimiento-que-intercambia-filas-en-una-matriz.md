---
title: "Procedimiento que intercambia filas en una matriz"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado']
tags: ['Sin Matlab']
---

# Procedimiento que intercambia filas en una matriz

##  Enunciado 

Se desea un subalgoritmo que permute las columnas de la matriz, moficándola y devolviendo el resultado en la misma matriz. Ejemplo: 

![Imagen:intercambiofilas.jpg](/images/2/20/Intercambiofilas.jpg)

##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**
```text
PROCEDIMIENTO Intercambia(VAR A,n)
ENTRADAS: A: ARRAY[1..n, 1..n] DE ENTEROS, matriz cuadrada
          n: ENTERO, número de filas y columnas de A, n>0
SALIDAS: A, la misma de entrada pero en la cual se han cambiado sus 
           columnas de orden, la primera con la última, la segunda con la 
           penúltima y así.
VARIABLES: i, primero, ultimo, aux: ENTERO.
INICIO
  primero<--1
  ultimo<--n
  MIENTRAS primero<ultimo HACER
     PARA i=1 HASTA n HACER
        aux<--A(i,primero)
        A(i,primero)<--A(i, ultimo)
        A(i,ultimo)<-- aux
     FIN_PARA
     primero<--primero+1
     ultimo<--ultimo-1
     FIN_MIENTRAS
FIN
```

###  Programa en Pascal por **lperez**
```text
Procedure Intercambia(var a:matriz;t:integer);
(* Entradas:a, una matriz y t su tamaño
Salidas: la matriz en la que se ha intercambiado la primera columna
     por la última, la segunda por la penúltima y así.*)
var i,primero,ultimo,aux:integer;
begin
 primero:=1;
 ultimo:=t;
 while primero<ultimo do
   begin
     for i:=1 to t do
       begin
         aux:=a[i,primero];
         a[i,primero]:=a[i,ultimo];
         a[i,ultimo]:=aux;
       end;
     primero:=primero+1;
     ultimo:=ultimo-1;
   end;
end;
```