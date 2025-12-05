---
title: "Descompsición en monedas de una cantidad en euros"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado', 'comentario']
tags: ['sin_matlab']
---

# Descompsición en monedas de una cantidad en euros

##  Enunciado 

Dada una cantidad de dinero en euros se desea conocer el número mínimo de monedas en las que se descompone dicha cantidad. Las monedas que se han de tener en cuenta para su descomposición son las de 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02 y 0.01 euros. 

##  Soluciones 

###  Diseño 1 en Pseudocódigo por **lperez**
```text
ALGORITMO Cambio_dinero
ENTRADAS:
   dinero: REAL  _(cantidad de dinero que se tiene, dinero >=0.)_
SALIDAS: _(cantidad mínima de monedas en las que se descompone, de 2,1, 0.5, 0.2, 0.1,  0.05, 0.02 y 0.01.)_
   m2, m1, m05, m02, m01, m005, m002, m001: REAL
VARIABLES:
   resto:REAL
INICIO
  ESCRIBIR "Introduzca una cantidad de dinero: "
  LEER dinero
  m2<--0; m1<--0; m05<--0; m02<--0; m005<--0; m002<--0; m001<--0
  resto<--dinero
  MIENTRAS resto>=2) HACER
     resto<--resto-2
     m2<--m2+1
  FIN_MIENTRAS 
  MIENTRAS resto>=1) HACER
     resto<--resto-1
     m1<--m1+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.5) HACER
     resto<--resto-0.5
     m05<--m05+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.2)  HACER
     resto<--resto-0.2
     m02<--m02+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.1)  HACER
     resto<--resto-0.1
     m01<--m01+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.05)  HACER
     resto<--resto-0.05
     m005<--m005+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.02)  HACER
     resto<--resto-0.02
     m002<--m002+1
  FIN_MIENTRAS
  MIENTRAS (resto>=0.01)  HACER
     resto<--resto-0.01
     m001<--m001+1
  FIN_MIENTRAS
  (*SI resto>0
    ENTONCES m001<--1
    FIN_SI  *)  Esto puede sustituir al último mientras
  ESCRIBIR m2, m1, m05, m02, m005, m002, m001
FIN
```

###  Diseño 2 en Pseudocódigo por **lperez**
```text
ALGORITMO Cambio_dinero
ENTRADAS: dinero: REAL, cantidad de dinero que se tiene, dinero>=0.
SALIDAS: salida:ARRAY [1..8] DE ENTEROS, cantidad mínima de monedas en las que 
           se descompone, de 2,1, 0.5, 0.2, 0.1, 0.05, 0.02 y 0.01. 
VARIABLES: i: ENTERO, resto:REAL; monedas:ARRAY[1..8] DE REAL
INICIO
  PARA i=1 HASTA 8
     salida(i)<--0
  FIN_PARA
  monedas(1)<--2; monedas(2)<--1; monedas(3)<--0.5; monedas(4)<--0.2;
  monedas(5)<--0.1; monedas(6)<--0.05; monedas(7)<--0.02; monedas(8)<--0.01;
  resto<--dinero
  i<--1
  MIENTRAS (i<=8) HACER
     MIENTRAS (resto>=monedas(i)) HACER
        resto<--resto-monedas(i)
        salida(i)<--salida(i)+1
     FIN_MIENTRAS 
     SI resto>0
     ENTONCES 
        i<--i+1
     SI NO 
       i<--9
     FIN_SI
  FIN_MIENTRAS
  PARA i=1 HASTA 8 HACER
     ESCRIBIR salida(i)
  FIN_PARA
FIN
```

####  Comentario 

En la segunda forma se utiliza array para almacenar los valores de las monedas de cambio por lo que los ciclos hechos en la primera resolución para calcular las monedas de cada tipo se pueden agrupar poniendo dos ciclos aninados, lo cual simplifica la escritura, aunque el comportamiento es el mismo. 

###  Solución 1 en C
```c

#include <stdio.h>
#include <stdlib.h>
               
int main(void){
  //ENTRADAS:
  float dinero; //_(Dinero que se tiene, dinero >=0)_
  //SALIDAS: _(Cantidad mínima de monedas en que se descompone:2,1,0.5,0.2,0.1,0.05,0.02,0.01)_ 
  float m1,m2,m05,m02,m01,m005,m002,m001;
  //VARIABLES:
  float resto;
                      
  printf("Introduzca la cantidad de dinero: ");               
  scanf("%f",&dinero);                                     

  m1=0;
  m2=0;
  m05=0;
  m02=0;
  m01=0;
  m005=0;
  m002=0;
  m001=0;
  resto=dinero;
                 
  while(resto>=2){
      resto=resto-2;
      m2=m2+1;
  }
  while(resto>=1){
      resto=resto-1;
      m1=m1+1;
  }
  while(resto>=0.5){
      resto=resto-0.5;
      m05=m05+1;
  }
  while(resto>=0.2){
      resto=resto-0.2;
      m02=m02+1;
  }
  while(resto>=0.1){
      resto=resto-0.1;
      m01=m01+1;
  }
  while(resto>=0.05){
      resto=resto-0.05;
      m005=m005+1;
  }
  while(resto>=0.02){
      resto=resto-0.02;
      m002=m002+1;
  }
  while(resto>=0.01){
      resto=resto-0.01;
      m001=m001+1;
  }        
  printf("%f,%f,%f,%f,%f,%f,%f,%f",m2,m1,m05,m02,m01,m005,m002,m001);                               
}
```

###  Solución 2 en C
```c

#include <stdio.h>
#include <stdlib.h>
                 
int main(void){
 //ENTRADAS
  float dinero;  //_(Cantidad de dinero que se tiene, dinero >=0)_
 //SALIDAS
  int salida[9]; //_(Cantidad minima de monedas en que se descompone:_
                 //  de 2,1,0.5,0.2,0.1,0.05,0.02,0.01)
 //VARIABLES
  int i;
  float resto;
  float monedas[9];
         
  for(i=1; i<=8; i++){
         salida[i]=0;
  }
  monedas[1]=2;
  monedas[2]=1;
  monedas[3]=0.5;
  monedas[4]=0.2;
  monedas[5]=0.1;
  monedas[6]=0.05;
  monedas[7]=0.02;
  monedas[8]=0.01;
  resto=dinero;
  i=1;
               
  while(i<=8){
       while(resto>=monedas[i]){
               resto=resto-monedas[i];
               salida[i]=salida[i]+1;
       }
       if(resto>0){
               i=i+1;
       }else{
               i=9;
       }
  }
  for(i=1; i<=8; i++){
       printf("%i",salida[i]);
  }
}
```

###  Programa 1 en Pascal por **lperez**
```text
(* ENTRADAS: dinero: REAL, cantidad de dinero que se tiene, dinero>=0.
SALIDAS: m2, m1, m05, m02,m01, m005, m002, m001, cantidad mínima de monedas en
las que se descompone, de 2,1, 0.5, 0.2, 0.05, 0.02 y 0.01 *)
(***************************************)
program Cambio_dinero;
uses crt;
var m2, m1, m05, m02, m01, m005, m002, m001:integer;dinero,resto:REAL;
begin
    clrscr;
    write('Introduce la cantidad total de dinero: ');
    readln(dinero);
    m2:=0; m1:=0; m05:=0; m01:=0; m02:=0; m005:=0; m002:=0; m001:=0;
    resto:=dinero;
    while (resto>=2) do
       begin
  	  resto:=resto-2;
         m2:=m2+1;
       end;
    while (resto>=1) do
       begin
  	  resto:=resto-1;
         m1:=m1+1;
       end;
    while (resto>=0.5) do
       begin
  	  resto:=resto-0.5;
         m05:=m05+1;
       end;
    while (resto>=0.2) do
       begin
  	  resto:=resto-0.2;
         m02:=m02+1;
       end;
    while (resto>=0.1) do
       begin
  	  resto:=resto-0.1;
         m01:=m01+1;
       end;
    while (resto>=0.05) do
       begin
  	  resto:=resto-0.05;
         m005:=m005+1;
       end;
    while (resto>=0.02) do
       begin
  	  resto:=resto-0.02;
         m002:=m002+1;
       end;
    while (resto>=0.01) do
       begin
  	  resto:=resto-0.01;
         m001:=m001+1;
       end;
    writeln('Monedas de 2= ', m2);
    writeln('Monedas de 1= ', m1);
    writeln('Monedas de 0.5= ', m05);
    writeln('Monedas de 0.2= ', m02);
    writeln('Monedas de 0.1= ', m01);
    writeln('Monedas de 0.05= ', m005);
    writeln('Monedas de 0.02= ', m002);
    writeln('Monedas de 0.01= ', m001);
    writeln('Pulse enter para acabar');
    readln;
end.
```

###  Programa 2 en Pascal por **lperez**
```text
(* ENTRADAS: dinero: REAL, cantidad de dinero que se tiene, dinero>=0.
SALIDAS: salida, array con la cantidad mínima de monedas en
     las que se descompone, de 2,1, 0.5, 0.2, 0.05, 0.02 y 0.01 *)
(*********************************)
program Cambio_dinero;
uses crt;
var salida:array[1..8] of integer;dinero,resto:REAL;
   monedas:array[1..8] of real;i:integer;
begin
    clrscr;
    write('Introduce la cantidad total de dinero: ');
    readln(dinero);
    for i:=1 to 8 do
        salida[i]:=0;
    resto:=dinero;
    monedas[1]:=2;monedas[2]:=1;monedas[3]:=0.5;monedas[4]:=0.2;
    monedas[5]:=0.1;monedas[6]:=0.05;monedas[7]:=0.02;monedas[8]:=0.01;
    i:=1;
    while (i<=8) do  
      begin
         while (resto>=monedas[i]) do
           begin
  	      resto:=resto-monedas[i];
             salida[i]:=salida[i]+1;
           end;
         if resto>0
         then i:=i+1
         else i:=9;
       end;
    for i:=1 to 8 do
       writeln('Monedas de ',monedas[i]:2:2,'=',salida[i]);
    writeln('Pulsa enter para acabar');
    readln;
end.
```