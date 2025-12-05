---
title: "Dibujo triángulo de asteriscos"
date: 2024-01-01
draft: false
languages: ['c', 'pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Dibujo triángulo de asteriscos

##  Enunciado 

Programa que sea capaz de sacar la siguiente pirámide de “*” dada la altura que tiene (representada por medio de un número entero). Por ejemplo para altura 4 debe quedar de la siguiente forma: 
```text
   *
  * *
 * * *
* * * *
```

##  Soluciones 

###  Programa en Pascal por **lperez**
```text
program triaast;
{ENTRADAS:n, la base del tri ngulo
SALIDAS:dibuja un tri ngulo de asteriscos, ej, base 3
  *
 * *
* * *}
uses crt;
var n,i,j,limite:integer;opcion:char;
(***********************************)
procedure blanco(tope:integer);
var i:integer;
begin
 for i:=1 to tope do
   write(' ');
end;
(***************************************)
begin
 repeat
   clrscr;
   write('Introduce el n£mero de asteriscos de la base: ');
   readln(n);
   limite:=n*2+1;
   blanco(limite);
   for i:=1 to n do
     begin
       for j:=1 to i do
         write('* ');
       writeln;
       limite:=limite-1;
       blanco(limite);
     end;
   repeat
     writeln('¨Desea repetir:(S/N)?');
     readln(opcion);
     opcion:=upcase(opcion);
   until ((opcion='S') or (opcion='N'));
 until opcion='N';
end.
```