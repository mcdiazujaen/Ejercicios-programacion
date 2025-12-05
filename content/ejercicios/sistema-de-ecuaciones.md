---
title: "Sistema de ecuaciones"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab']
---

# Sistema de ecuaciones

##  Enunciado 

Se quiere resolver un sistema de m ecuaciones con n incógnitas mediante el método de Gauss. Dicho método consiste en triangular la matriz de coeficientes. 

##  Análisis 

Para ello vamos a obtener un sistema equivalente en el que la primera ecuación tenga n incógnitas, la segunda n-1, la tercera n-2, y así sucesivamente hasta llegar a la última ecuación , que tendrá solo una incógnita. Hecho esto, resolveremos la última ecuación, a continuación la penúltima, y así hasta llegar a la primera. 

##  Soluciones 

###  Diseño en Pseudocódigo por **lperez**
```text
PROCEDIMIENTO Ceros(VAR a,nf,nc)
ENTRADAS: a: ARRAY [1..nf,1..nc] DE REALES, representa la matriz
             ampliada de un sistema de ecuaciones (coeficientes y términos 
             independientes)
          nf,nc: ENTERO, número de filas y de columnas de a (nc=nf+1, nf=nº 
             ecuaciones)
SALIDAS: a, la misma matriz de entrada pero triangulada.
VARIABLES: i,j,k: ENTERO; p1,p2:REAL.
INICIO
  PARA i=1 HASTA nf-1
     PARA k=i+1 HASTA nf
        p1<--a(i,i)
        p2<--a(k,i)
        PARA j=i HASTA nc
           a(k,j)<--a(k,j)*p1-a(i,j)*p2
        FIN_PARA
     FIN_PARA
  FIN_PARA
FIN
******************************* 
PROCEDIMIENTO Resuelve(a, nf, nc, VAR b, VAR t)
ENTRADAS: a: ARRAY [1..nf,1..nc]  DE REALES, representa la matriz
             ampliada de un sistema de ecuaciones (coeficientes y términos 
             independientes)
          nf,nc: ENTERO, número de filas y de columnas de a (nc=nf+1, nf=nº 
             ecuaciones)
SALIDAS: b: ARRAY [1..t] DE REALES, matriz con los resultados de resolver el 
             sistema
         t:ENTERO, nº de soluciones= tamaño de b (0 si no tiene solución) 
VARIABLES: suma:REAL; i,j:ENTERO.
INICIO
  SI a(nf,nc-1)=0   (*sistema sin solución*)
  ENTONCES
     t<--0
  SI NO
     PARA  i=nf HASTA 1 CON DECREMENTO DE 1
        suma<--0
        PARA  j=i+1 HASTA nf
           suma<--suma+a(i,j)*b(j);
        FIN_PARA
        b(i)<--(a(i,nc)-suma)/a(i,i)
     FIN_PARA
     t<--nf
  FIN_SI
FIN
*************************************************
ALGORITMO Gauss
ENTRADAS: e: ARRAY [1..filas,1..columnas] DE REALES, matriz ampliada, continene 
             los coeficientes y los términos independientes de un sistema de 
             ecuaciones lineales con el mismo número de ecuaciones que de 
             incógnitas.
          filas: ENTERO, nº de filas de e = nº de ecuaciones=nº de incógnitas
             (el número de columnas de e va a ser filas+1), filas>0
          incog: ARRAY [1..filas] DE CARACTERES, va a contener los nombres
             de las incógnitas.
SALIDAS: sol: ARRAY [1..filas] DE REALES, las soluciones del sistema, si las hay.
VARIABLES: columnas, i,j,tam:ENTERO; 
INICIO
  LEER filas
  columnas<--filas+1
  PARA  i=1 HASTA  filas  HACER
     PARA  j=1 HASTA  columnas  HACER
        LEER e(i,j)
     FIN_PARA
  FIN_PARA
  PARA  i=1 HASTA  filas  HACER
     LEER incog(i)
  FIN_PARA
  Ceros(e,filas,columnas)
  Resuelve(e,filas,columnas,sol,tam)
  SI tam=0
  ENTONCES
     ESCRIBIR “El sistema es indeterminado”
  SI NO
     PARA  i=1 HASTA  tam  HACER
        ESCRIBIR incog(i), “=”,sol(i)
     FIN_PARA
  FIN_SI
FIN
```

###  Programa en Pascal por **lperez**
```text
program Gauss;
{ENTRADAS: e: una matriz que contine los coeficientes y t‚rminos independientes
              de un sistema de ecuaciones lineales(con el mismo número de
              ecuaciones que de incógnitas)(la matriz tendrá una columna más
              que filas ya que es la matiz ampliada con los términos independientes)
           filas: número de ecuaciones del sistema, filas>0 .
           incog: contiene los nombres de las incógnitas.
 SALIDAS: sol: contendrá las soluciones del sistema}
uses crt;
type matriz=array[1..10,1..10] of real;
     matriz2=array[1..10]of real;
(******************************)
procedure ceros (var a:matriz;nf,nc:integer);
{ENTRADAS: a matriz ampliada de los coeficientes y términos independientes
           nf: número de filas
           nc: número de columnas
 SALIDAS: a, la misma matriz de entrada pero triangulada          }
var i,j,k:integer;p1,p2:real;
begin
 for i:=1 to  nf-1 do
   begin
     for k:=i+1 to nf do
       begin
         p1:=a[i,i];
         p2:=a[k,i];
         for j:=i to nc do
           a[k,j]:=a[k,j]*p1-a[i,j]*p2;
       end;
    end;
end;
(*************************************************)
procedure resuelve(var a:matriz;nf,nc:integer;var b:matriz2;var t:integer);
{ENTRADAS: a, matriz ampliada de los coeficientes y términos independientes
           nf: número de filas
           nc: número de columnas
 SALIDAS: b, contiene los resultados para cada incógnita
          t, devuelve el número de soluciones y 0 si el sistema no tiene
            solución}
var suma:real;i,j:integer;
begin
 if a[nf,nc-1]=0       {sistema sin solucion}
 then  t:=0
 else
  begin
    for i:=nf downto 1 do
      begin
        suma:=0;
        for j:=i+1 to nf do
          suma:=suma+a[i,j]*b[j];
        b[i]:=(a[i,nc]-suma)/a[i,i];
      end;
    t:=nf;
 end;
end;
(**********************************************)
var e:matriz;
   filas,columnas,i,j,tam:integer;
   sol:matriz2;
   incog:array[1..10]of char;
begin
 clrscr;
 writeln('Numero de ecuaciones (= inc¢gnitas): ');
 read(filas);
 columnas:=filas+1;
 writeln('Introduce la matriz ampliada');
 for i:=1 to filas do
   for j:=1 to columnas do
     begin
       write('Elemento (',i,',',j,') ');
       readln(e[i,j]);
      end;
 writeln('Introduce los nombres de las inc¢gnitas');
 for i:=1 to filas do
    begin
      write('Inc¢gnita ',i, ':');
      readln(incog[i]);
    end;
 ceros(e,filas,columnas);
 resuelve(e,filas,columnas,sol,tam);
 if tam=0
 then
   writeln('El sistema es indeterminado')
 else
   for i:=1 to tam do
       writeln(incog[i],'=',sol[i]:4:2);
 writeln('Pulsa enter para acabar');
 repeat until keypressed;
end.
```

###  Comentario 

En el programa en Pascal el tamaño de los arrays utilizados se ha de especificar por lo que tiene un límite superior que es de matrices de 10x10.