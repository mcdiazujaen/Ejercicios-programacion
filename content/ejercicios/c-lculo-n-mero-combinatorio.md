---
title: "Cálculo número combinatorio"
date: 2024-01-01
draft: false
languages: ['matlab', 'pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado', 'comentario']
---

# Cálculo número combinatorio

##  Enunciado 

Realizar el diseño y programa capaces de calcular el combinatorio de dos números a y b: 
```text

                        a!
          C(a,b) = -------------
                     b! * (a-b)!

```
##  Soluciones 

###  Diseño en Pseudocódigo 

####  Diseño 1 por **lperez**
```text

 FUNCION Factorial (n): ENTERO
 ENTRADAS: n: ENTERO, un número entero positivo.
 SALIDAS: el factorial de n.
 VARIABLES: i, f: ENTERO
 INICIO
   f<--1
   PARA i=2 HASTA n HACER
      f<--f *i
   FIN_PARA
   DEVOLVER   f
 FIN
 *********************************************
 ALGORITMO Combinatorio
 ENTRADAS: a, b: ENTERO, dos número entero positivos, a>0, b>=0 y a>b .
 SALIDAS: combi: ENTERO, el número combinatorio a sobre b, calculado de la forma:
                          a!
           C(a,b) = -------------
                      b! * (a-b)!
 VARIABLES: fa, fb, fab:ENTERO
 INICIO
   LEER a,b
   SI ( ( b = 0 ) or ( a = b ) )
   ENTONCES
      combi<--1
   SI NO
      combi<--Factorial(a)/(Factorial(b)*Factorial(a-b))
   FIN_SI   
   ESCRIBIR combi 
 FIN

```
####  Diseño 2 por **lperez**
```text

 PROCEDIMIENTO Factorial (n, VAR f)
 ENTRADAS: n: ENTERO, un número entero positivo.
 SALIDAS: f: ENTERO, el factorial de n.
 VARIABLES: i: ENTERO.
 INICIO
   f<--1
   PARA i=2 HASTA n HACER
      f<--f *i
   FIN_PARA
 FIN
 ********************************************************************
 ALGORITMO Combinatorio
 ENTRADAS: a, b: ENTERO, dos número entero positivos, a>0, b>=0 y a>b .
 SALIDAS: combi: ENTERO, el número combinatorio a sobre b, calculado de la forma:
                      a!
        C(a,b) = -------------
                   b! * (a-b)!
 VARIABLES: fa, fb, fab:ENTERO
 INICIO
   LEER a,b
   SI ( ( b = 0 ) or ( a = b ) )
   ENTONCES
      combi<--1
   SI NO
      Factorial(a,fa)
      Factorial(b,fb)
      Factorial(a-b,fab)
      combi<--fa/(fb*fab)
   FIN_SI   
   ESCRIBIR combi 
 FIN

```
####  Comentario 

En la primera solución se ha utilizado una función para resolver el factorial, mientras que en la segunda se ha utilizado un procedimiento. 

###  Programa en C 

####  Solución 1 
```c

 //''(Este programa se ha hecho con una función)''            
 int Factorial(int n){
   //ENTRADAS: ''(n: un número entero positivo)''
   //SALIDAS: ''(El factorial de n)''
   //VARIABLES
   int i, f;
 
   f=1;
   for(i=2; i<=n; i++){
       f=f*i;
   }
   return(f);
 }
 //*******************************************************
 
 #include <stdio.h>
 #include <stdlib.h>
 
 int main(void){
   //ENTRADAS
   int a, b; //''(Dos numeros enteros positivos: a>0, b>=0, a>b)''
   //SALIDAS
   int combi; //''(El numero combinatorio a sobre b calculado de la forma:
   /*                                                                                        
                               a!
                     c(a,b)=----------- )''
                             b!*(a-b)!                                     
   */
   //VARIABLES
   int fa,fb,fab;
 
   printf("Introduzca dos numeros enteros positivos: ");
   scanf("%i %i", a, b);
    if((b==0)||(a==b)){
        combi=1;
    }else{
        combi=Factorial(a)/(Factorial(b)*Factorial(a-b));
    }
    printf("%i",combi);
 }

```
####  Solución 2 
```c

  void Factorial(int n, int &f){
    //VARIABLES
    int i;
 
    f=1;
    for(i=2; i<=n; i++){
       f=f*i;
    }
  }
 //**********************************
 #include<stdio.h>
 #include<stdlib.h>
 
 int main(void){
 //ENTRADAS
   int a, b;  //''(Dos numeros enteros positivos: a>0, b>=0, a>b)''
 //SALIDAS
   int combi; /*''(El numero combinatorio a sobre b calculado de la forma:
 
                               a!
                     c(a,b)=----------- )''
                             b!*(a-b)!  
              */                                   
  //VARIABLES
    int fa, fb, fab;
 
    printf("Introduzca dos numeros enteros positivos: ");
    scanf("%i %i", a, b);
    if((b==0)||(a==b)){
        combi=1;
    }else{
        Factorial(a,fa);
        Factorial(b,fb);
        Factorial(a-b,fab);
        combi=fa/(fb*fab);
    }
    printf("%i",combi);
  }

```
####  Comentario 

En la primera solución se ha utilizado una función para resolver el factorial, mientras que en la segunda se ha utilizado un procedimiento. 

###  Programa en Pascal por **lperez**
```text

 program Combinatorio;
 {ENTRADAS: a,b, dos n£meros enteros positivos, a>b y a<>0
 SALIDAS: combi, el n£mero combinatorio a sobre b, calculado de la forma:
                       a!
        C(a,b) = -------------
                  b! * (a-b)!
 }
 uses crt;
 (****************************************************)
 procedure Lectura(var n, m:integer);
 {ENTRADAS: Ninguna;
 SALIDAS: n y m, dos n£meros enteros que cumplen que n>0, m>=0 y n>m}
 begin
   {repite la entrada de los datos hasta conseguir que n sea un entero positivo,
     m sea positivo o 0 y n sea mayor que m}
  repeat
     clrscr;
     writeln('Este programa calcula un el n£mero combinatorio n sobre m');
     writeln('              n!');
     writeln('C(n,m) = -------------');
     writeln('           m! * (n-m)!');
     writeln('Reglas de utilizaci¢n: ');
     writeln('      El primer operando ha de ser mayor que 0');
     writeln('      El segundo operando ha de ser mayor o igual que 0');
     writeln('      El primer operando ha de ser mayor o igual que el segundo');
     write('Introduce el primer operando: ');
     readln(n);
     write('Introduce el segundo operando:') ;
     readln(m);
  until (n>=m) and (n>0) and (m>=0);
 end;
 (****************************************************************)
 function factorial(n:integer):integer;
 {ENTRADAS: n, un número entero positivo
 SALIDAS: el factorial de n}
 var i,f:integer;
 begin
  f:=1;
  for i:=1 to n do
    f:=f*i;
  factorial:=f;
 end;
 (*****************************************************************)
 procedure factorial2(n:integer;var f:integer);
 {ENTRADAS: n, un número entero positivo
 SALIDAS: f, el factorial de n}
 var i:integer;
 begin
  f:=1;
  for i:=1 to n do
    f:=f*i;
 end;
 (***************************************************************)
 {variables LOCALES del programa principal}
 var a,b,combi:integer;opcion:char;
    fa,fb,fab:integer; {estas variables son necesarias si se utiliza el
                        procedimiento para calcular el factorial}
 begin
  repeat  {repite el programa hasta que se pulsa el caracter n};
    Lectura(a,b);
    { C(a,0) = C(a,a) = 1. En este caso no es necesario llamar al subprograma
       que calcula el factorial }
    if ( ( b = 0 ) or ( a = b ) )
    then
       begin
        combi := 1;
       end
    else
      begin
         factorial2(a,fa);    {llamadas }
         factorial2(b,fb);     {al}
         factorial2(a-b,fab); {procedimiento }
         combi:= fa DIV (fb*fab);
         {combi:=factorial(a)/(factorial(b)*factorial(a-b))  llamada a la funci¢n
          si utilizamos la función la línea anterior comentada sustituye a las
          4 líneas anteriores}
      end;
    writeln('Combinatorio( ',a,',',b,')=',combi);
    write('Pulsa n para acabar y otro para repetir  ');
    readln(opcion);
  until opcion='n';
 end.

```
####  Comentario 

Tal y como está el programa anterior, utiliza el procedimiento para resolver el cálculo del factorial. Si se quiere utilizar la función se tendría que quitar de comentario la línea que lo hace y se tendría que comentar las líneas de llamadas al procediemiento. 

###  Programa en Matlab 

Para realizar este programa utilizamos el módulo **factorial** existente en Matlab. 
```matlab

%Programa CalcularCombinatorio
%Descripción: Calcula el combinatorio de dos números a y b, de la forma:
%                          a!
%           C(a,b) = -------------
%                      b! * (a-b)!
%Entradas: Dos números enteros.
%Salidas:El combinatorio de los dos números.
%Variables:
%   a,b,c,res:ENTEROS
%   texto:CADENA (o ARRAY) DE CARACTERES.
 
a = input('Introduzca el primer valor:');
b = input('Introduzca el segundo valor:');
%Asignar a la variable a el mayor valor
if a<b
    c=a;
    a=b;
    b=c;
end
%Calculamos el combinatorio si es posible
if b==0 || a==b
    res = -1;
else
    res = factorial(a)/(factorial(b)*factorial(a-b));
end    
texto=['el combinatorio es: ' num2str(res)];
disp(texto);
```