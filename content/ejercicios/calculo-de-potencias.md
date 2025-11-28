---
title: "Calculo de potencias"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---


# Calculo de potencias

  

##  Enunciado 

Realiza un programa que calcule las potencias de la 2 a la 10 del número PI y la raíz cuadrada de dicha potencia. Para ello construye una función que calcule la potencia n-ésima de un número cualquiera y utiliza después la función sqrt de la librería matemática. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c


 /* fichero potencia.c */
 #include <stdio.h>
 #include <math.h>
 #define PI 3.14159265359
 /*---------------------------------------------*/
 double poten(double a, int b) {
   int i;
   double resul=1.0;
   for (i=1; i<=b; i++)
      resul*=a;
   return resul;
 }
 /*--------------------------------------------*/
 void main(void) {
   int i;
   for (i=2; i<=10; i++) {
      printf("PI elevado a %d es %5.2lf y su raiz es %5.2lf\n", i, poten(PI, i), sqrt(poten(PI, i)) );
   }
 }

```
####  Comentario 

Para calcular las potencias de la 2 a la 10 del número PI, se utiliza un bucle for que va de **i=2** a **i=10** , llamando en cada ejecución a la función **poten()**. A esta función se le pasa una constante **double** , que es el número PI, y el exponente entero **i**. La función **poten()** sirve para calcular la potencia i-ésima de cualquier número. En este caso, la variable a de la función toma el valor de PI en todas las llamadas, mientras que la variable **b** copia el valor de **i** que será distinto en cada una de las llamadas. 

###  Solución en Pseudocódigo

Para realizar el ejercicio en pseudocódigo vamos a partir de la premisa de que existe una función llamada **raiz** que calcula la raiz cuadrada de un real. 
```text


 FUNCION  poten(a,b):REAL
 ENTRADAS:
      a:REAL
      b:ENTERO
 SALIDAS:
      resul:REAL
 VARIABLES:
      i:ENTERO
 INICIO:
      resul<--1.0
      PARA i<--1 HASTA b HACER
                 resul<--resul*a
      FIN_PARA
      DEVOLVER resul
 FIN

  



 (* PROGRAMA PRINCIPAL *)
 
 ALGORITMO potencia
 ENTRADAS:
    (* No tiene entradas *)
 SALIDAS:
    (* El valor de PI elevado a potencias desde 2 hasta 10 *)
 VARIABLES:
    i:ENTERO
 CONSTANTES:
    PI=3.14159265359
 INICIO:
    PARA i<--2 HASTA 10 HACER
          ESCRIBIR "PI elevado a ", i, " es ", poten(PI,i), " y su raiz es ", raiz(poten(PI,i))
    FIN_PARA
 FIN

```
###  Programa en Matlab 
```matlab


function res=poten(base,expo)
% FUNCIÓN res=poten(base,expo)
% DESCRIPCIÓN: Devuelve el resultado de elevar un número a una potencia dada
% PARÁMETROS DE ENTRADA:
%    base: ENTERO, número que se quiere elevar
%    expo: ENTERO, exponente al que se eleva la base
% PARÁMETROS DE SALIDA:
%    res: ENTERO, resultado de elevar "base" a "expo"
% VARIABLES:
%    cont: ENTERO
res=base;
for cont=1:(expo-1)
    res=res*base;
end


% PROGRAMA Potencia
% DESCRIPCIón: Eleva el número "pi" desde la potencia 2 hasta la 10 y después le realiza la raíz cuadrada.
% ENTRADAS: Ninguna.
% SALIDAS: El resultado de elevar pi a las sucesivas potencias y realizarse la raíz cuadrada.
% VARIABLES:
%    expo:ENTERO;
 
for expo=2:10,
    disp(['pi elevado a' num2str(expo) 'es:' num2str(poten(pi,expo))]);
    disp(['y la raiz es:' num2str(sqrt(poten(pi,expo)))]);
end
```