---
title: "Criba de Eratóstenes"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['comentario', 'enunciado']
tags: ['Sin C', 'Sin Matlab']
---

# Criba de Eratóstenes

##  Enunciado 

La criba de Eratóstenes, renombrado astrónomo y geógrafo griego del siglo III a. De C., es una técnica para generar números primos. Se comienza escribiendo todos los enteros impares desde 3 hasta N; luego se elimina cada tercer elemento después de 3, cada quinto elemento después de 5, etc., hasta que los múltiplos de todos los enteros impares menores que hayan sido eliminados. Los enteros que quedan constituyen la lista exacta de los números primos entre 3 y N. 

Diseñar un algoritmo para generar los números primos entre 2 y N, utilizando la técnica de la criba. 

##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**
```text
PROCEDIMIENTO Criba (N, VAR primos, VAR t)
ENTRADAS: N: ENTERO, controla el número de primos que queremos obtener, N>0.
SALIDAS: primos: ARRAY [1..t] DE ENTEROS, contiene los números primos menores que 
                  N. 
         t: ENTERO, número de primos encontrados.
VARIABLES: aux: ARRAY [m] DE ENTEROS; i, k, pos, j, tope,ele: ENTERO. 
INICIO
  i<--3
  k<--1
  MIENTRAS i<= N HACER
     aux(k)<--i
     k<--k+1
     i<--i+2
  FIN_MIENTRAS
  k<--k-1
  tope<--Redondeo (Raiz(N))
  pos<--1
  MIENTRAS pos<tope HACER
     SI aux(pos)<>-1
     ENTONCES
        ele<--aux(pos)		
        PARA  j=ele+pos  HASTA k CON INCREMENTO DE ele
           aux(j)<---1
        FIN_PARA
     FIN_SI
     pos<--pos+1
  FIN_MIENTRAS
  primos(1)<--2
  t<--1
  PARA i=1 HASTA k CON INCREMENTO DE 1
     SI  aux(i)<>-1
     ENTONCES
        t<--t+1
        primos(t)<--aux(i)
     FIN_SI
  FIN_PARA
FIN
(**************************************************************)
PROGRAMA Criba_Erastostenes
VARIABLES numero,tamano,i,seguir:ENTERO; resultado:ARRAY[1..tamano] DE ENTEROS;
INICIO
 REPETIR
   LEER(numero);
   Criba(numero,resultado,tamano);
   PARA i=1 HASTA  tamano HACER
     ESCRIBIR resultado(i)
   LEER seguir;
 HASTA QUE seguir=0
FIN
```

####  Comentario 

El algoritmo lee el número hasta el que queremos obtener la secuencia de primos, llama a un procedimiento que calcula dichos números primos y es el algoritmo el que los muestra por pantalla. En el procedimiento se ha utilizado Raiz(), se supone que es una función a la que se le da un número y devuelve un real que es su raíz cuadrada. En cuanto a Redondeo(), se supone que es una función a la que se le da un real y devuelve un entero resultado de redondear el real dado como entrada. 

La operación se puede repetir hasta que deseemos terminar. 

###  Programa en Pascal por **lperez**

```pascal
program Criba_Erastostenes;
uses crt;
type vector=array[1..100] of integer;
(*************************************)
procedure Criba(N:integer; var primos:vector; var t:integer);
{ENTRADAS: N: ENTERO, controla el número de primos que queremos obtener, N>0.
SALIDAS: primos: ARRAY [1..t] DE ENTEROS, contiene los números primos menores que
                 N. 
         t: ENTERO, número de primos encontrados.
}
var aux: vector; i, k, pos, j, tope,ele: integer;
begin
 i:=3;
 k:=1;
 while i<= N do
   begin
      aux[k]:=i;
      k:=k+1;
      i:=i+2;
   end;
 k:=k-1;
 tope:=round (sqrt(N));
 pos:=1;
 while pos<tope do
    begin
       if aux[pos]<>-1
       then
         begin
            ele:=aux[pos];
            j:=ele+pos;
            while j<=k do
               begin
                  aux[j]:=-1;
                  j:=j+ele;
               end;
         end;
       pos:=pos+1
    end;
 primos[1]:=2;
 t:=1;
 for i:=1 to k do
    if  aux[i]<>-1
    then
       begin
          t:=t+1 ;
          primos[t]:=aux[i];
      end;
end;
(***********************************)
var numero,tamano,i,seguir:integer; resultado:vector;
begin
 repeat
   clrscr;
   writeln('El programa calcula los n£meros primos desde 2');
   writeln('          hasta el número que introduzcas');
   write('Introduce un número positivo: ');
   readln(numero);
   Criba(numero,resultado,tamano);
   writeln('Los n£meros primos menores que ',numero,' son:');
   for i:=1 to tamano do
     writeln(resultado[i]);
   writeln('Si quieres terminar con el programa pulsa 0');
   writeln('Si quieres continuar pulsa cualquier otro n£mero');
   readln(seguir);
 until seguir=0;
end.
```