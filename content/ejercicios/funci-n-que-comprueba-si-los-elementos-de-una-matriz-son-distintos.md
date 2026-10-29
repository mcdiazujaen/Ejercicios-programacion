---
title: "Función que comprueba si los elementos de una Matriz son distintos"
date: 2024-01-01
draft: false
languages: ['c', 'pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['comentario', 'enunciado']
tags: ['Sin Matlab']
---

# Función que comprueba si los elementos de una Matriz son distintos

##  Enunciado 

Vamos a contruir un subalgoritmo para saber si todos los elementos dentro de una matriz son distintos o no. 

##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**
```text
FUNCION Distintos(A, n): LOGICO
ENTRADAS: A: ARRAY [1..n, 1..n] DE ENTEROS; matriz cuadrada.
                     n: ENTERO, nº de filas y de columnas de A; n>0. 
SALIDAS: VERDAD si todos los elementos de A son distintos y FALSO en otro 
                 caso.
VARIABLES: i, j, k, z: ENTERO; p:LOGICO;
INICIO
  p<--VERDAD
  PARA   i<--1  HASTA  n  HACER
     PARA   j<--1  HASTA  n  HACER
        PARA   k<--1  HASTA  n  HACER
           PARA   z<--1  HASTA  n  HACER
              SI  (i<>k) OR (j<>z)
              ENTONCES
                 SI A(i,j)=A(k,z)
                 ENTONCES 
                    p<-- FALSO
                 FIN_SI
              FIN_SI
           FIN_PARA
        FIN_PARA
     FIN_PARA
  FIN_PARA
  DEVOLVER VERDAD
FIN
```

###  Programa en C
```c

 int Distintos(int A[1000][1000], int n){
    /*VARIABLES*/
    int i,j,k,z;
    int p;
    
    /*INCIO*/
    p=1;  //_Verdad._
    for(i=1; i<=n; i++){
         for(j=1; j<=n; j++){
                  for(k=1; k<=n; k++){
                         for(z=1; z<=n; z++){
                                  if ((i!=k)||(j!=z)){
                                         if(A[i][j]==A[k][z]){
                                                  p=0;  //_Falso._
                                         }
                                  }
                         }
                  }
         }
    }  
    return p;
 }
```

####  Comentario 

Los arrays en C deben tener un tamaño fijo, por eso se ha optado por darles una tamaño de 1000. Si dicho tamaño no es suficiente debe cambiarse por otro superior. 

###  Diseño en Pseudocódigo por **lperez**
```text
FUNCION Distintos(A, n): LOGICO
ENTRADAS: A: ARRAY [1..n, 1..n] DE ENTEROS; matriz cuadrada.
                     n: ENTERO, nº de filas y de columnas de A; n>0. 
SALIDAS: VERDAD si todos los elementos de A son distintos y FALSO en otro 
                 caso.
VARIABLES: i, j, fila, columna: ENTERO; p: LOGICO.
INICIO
  p<--VERDAD
  i<--1
  MIENTRAS (i<= n) AND p  HACER
     j<--1
     MIENTRAS (j<= n) AND p HACER
        SI  j=n
        ENTONCES
           fila<--i+1
           columna<--1
        SI NO
        fila<--i
        columna<--j+1
        FIN_SI
        MIENTRAS  (fila<= n) AND p  HACER
           MIENTRAS  (columna<= n) AND p  HACER
              SI A(i,j)=A(fila, columna)
              ENTONCES
                 p<--FALSO
              FIN_SI
              columna<--columna+1
           FIN_MIENTRAS
           fila<--fila+1
           columna<--1
        FIN_MIENTRAS
        j<--j+1	
     FIN_MIENTRAS
     i<--i+1
  FIN_MIENTRAS
  DEVOLVER p
FIN
```

####  Comentario 

En la primera solución se compara un elemento con todos los de la martriz, incluido el mismo, por lo que tenemos que comprobar que si es con él mismo no debemos tener en cuenta la comparación. En la segunda cada elemento de la matriz no se compara con todos sino sólo con aquellos elementos siguientes a él. 

###  Programa en Pascal por **lperez**
```text
Function Distintos(var a:matriz;t:integer):boolean;
(* Entradas: a,una matriz y t su tama¤o
  Salidas: verdadero si todos los elementos de la matriz son distintos y
           falso en otro caso *)
var  i,j,k,z:integer;
    p:boolean;
begin
 p:=true;
 for i:=1 to t do
   for j:=1 to t do
     for k:=1 to t do
       for z:=1 to t do
         if (i<>k) or (j<>z)
         then
           if a[i,j]=a[k,z]
           then p:=false;
 Distintos:=p;
end;
```

###  Programa en Pascal por **lperez**
```text
Function Distin2(var a:matriz;t:integer):boolean;
(* Entradas: a,una matriz y t su tama¤o
  Salidas: verdadero si todos los elementos de la matriz son distintos y
           falso en otro caso *)
var  i,j,k,z,fila,col:integer;
    p:boolean;
begin
 p:=true;
 for i:=1 to t do
   for j:=1 to t do
     begin
       if j=t
       then
         begin
           fila:=i+1;
           col:=1;
         end
       else
         begin
           fila:=i;
           col:=j+1;
         end;
       k:=fila;
       z:=col;
       while k<=t do
         begin
           while z<=t do
             begin
               if a[i,j]=a[k,z]
               then p:=false;
               z:=z+1;
             end;
           z:=1;
           k:=k+1;
         end;
     end;
 Distin2:=p;
end;
```

####  Comentario 

En las funciones anteriores hemos utilizado el tipo martiz, que debe estar declarado en la sección type del programa principal. Por ejemplo type matriz=array[1..10,1..10] of integer;