---
title: "Descomposición en factores primos"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Descomposición en factores primos

##  Enunciado 

Se quire realizar un programa al que se le de un número positivo y devuelva su descomposición como producto de fatores primos. 

##  Soluciones 

###  Programa en Pascal por **lperez**
```text
 program desompone_primos;
 uses crt;
 type vector=array[1..30] of integer;
 var num,i:integer;
    d:vector;
    lon:integer;
 (*****************)
 function Primo(n:integer):boolean;
 (*ENTRADAS: n entero positivo
  SALIDAS: verdad si n es primo y falso si no lo es*)
 var i:integer;
 begin
  i:=2;
  while i<n do
    if (n mod i)=0
    then
      i:=n+1
    else
      i:=i+1;
  if i=n
  then  Primo:=true
  else  Primo:=false;
 end;
 (*****************)
 procedure Descomp(n:integer;var sal:vector;var tam:integer);
 (*ENTRADAS: n, entoro positivo, n£mero a descomponer
  SALIDAS: sal, un array con los factores primos de n
           tam: el n£mero de factores primos de n, tama¤o de sal*)
 var a:integer;
 begin
  if Primo(n)
  then
    begin
      tam:=1;
      sal[tam]:=n;
    end
  else
    begin
      a:=2;
      tam:=0;
      while n>1 do
          if Primo(a)
          then
            begin
              if (n mod a)=0
              then
                begin
                  tam:=tam+1;
                  sal[tam]:=a;
                  n:=n div a;
                end
              else
                a:=a+1;
            end
          else
           a:=a+1;
    end;
 end;
 (*****************)
 (* ENTRADAS: num, un entero positivo
   SALIDAS: su descomposici¢n como producto de primos *)
 begin
  clrscr;
  write('Introduce un entero positivo:');
  readln(num);
  Descomp(num,d,lon);
  writeln('Su descomposici¢n en primos es:');
  for i:=1 to lon do
    begin
      write(d[i]);
      if i<lon
      then
        write('*');
    end;
  repeat until keypressed;
 end.
```

####  Comentario 

El programa se ha descompuesto de forma modular. De forma que existe una función que se encarga de ver si un número es primo o no y un procedimiento que se encarga de obtener los factores primos de un número.