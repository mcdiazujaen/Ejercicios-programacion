---
title: "División entera y resto utilizan restar y sumar"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado', 'análisis']
tags: ['sin_matlab']
---


# División entera y resto utilizan restar y sumar

##  Enunciado 

Realizar un algoritmo que obtenga la división entera y el resto de la misma utilizando únicamente los operadores suma y resta. 

##  Análisis del problema 

La división se puede considerar como una sucesión de restas. El algoritmo debe de tratar de contar cuantas veces se puede restar el divisor al dividendo y dicho contador será el cociente. Cuando ya no se pueda restar más sin que salga un número positivo, se tendrá el resto. 

##  Soluciones 

###  Pseudocódigo 
```text


 ALGORITMO DivisiónEnteraYResto
 ENTRADAS:
   dividendo: ENTERO  (*Número que se va a dividir*)
   divisor:   ENTERO  (*Número que divide*)
 SALIDAS:
   cociente:  ENTERO  (*resultado de la división entera*)
   resto:     ENTERO  (*resto de la división*)
 VARIABLES:
   (*no son necesarias*)
 INICIO
   (*Leer dividendo y divisor*)
   ESCRIBIR "Introduzca el dividendo:"
   LEER dividendo
   ESCRIBIR "Introduzca el divisor"
   LEER divisor
 
   (*Calcular el cociente y el resto*)
   resto <-- dividendo     (*Si dividendo<divisor entonces el dividendo es el resto*)
   cociente <-- 0          (*Si dividendo<divisor entonces el cociente es 0*)
   MIENTRAS resto >= divisor HACER
      resto <-- resto - divisor
      cociente <-- cociente + 1
   FIN_MIENTRAS
 
   (*Mostrar el cociente y el resto*)
   ESCRIBIR "El cociente de la división es:", cociente
   ESCRIBIR "El resto es:", resto
 FIN

```
###  Programa en C
```c


  #include <stdio.h>
  #include <stdlib.h>
  int main (void){
      /*ENTRADAS*/
      int dividendo; //''Número que se va a dividir''
      int divisor;   //''Número que divide''
 
      /*SALIDAS*/
      int cociente;  //''resultado de la división entera''
      int resto;     //''resto de la división''
 
      /*INICIO*/
      //''Leer dividendo y divisor''
      printf ("Introduzca el dividendo: ");
      scanf("%i",&dividendo);
      printf ("Introduzca el divisor: ");
      scanf("%i",&divisor);
 
      //''Calcular el cociente y el resto.''
      resto=dividendo;   //''Si dividendo<divisor entonces el dividendo es el resto''
      cociente=0;        //''Si dividendo<divisor entonces el cociente es 0''
      while(resto>=divisor){
          resto=resto-divisor;
          cociente=cociente+1;
      }
 
      //''Mostrar el cociente y el resto''
      printf ("El cociente de la division es: %i.",cociente);
      printf ("El resto es: %i",resto);
      system ("PAUSE");
  }
```