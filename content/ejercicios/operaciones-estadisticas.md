---
title: "Operaciones estadisticas"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---

# Operaciones estadisticas

##  Enunciado 

INTRODUCCIÓN A LA ESTADÍSTICA. 

Realiza este ejercicio basándote en el programa [**maximo.c**](/ejercicios/máximo-elemento-de-un-conjunto-de-números/) y guárdalo con el nombre **numeros.c**. Este programa deberá realizar las siguientes operaciones: 

1\. Preguntar al usuario con cuántos números desea trabajar. 

2\. Leer y almacenar los números convenientemente. 

3\. Hallar su media aritmética utilizando para ello una función a la que llamarás **media( )**. 

4\. Hallar el máximo y el mínimo llamando a sendas funciones **maximo( )** y **minimo( )** , cuya programación realizaste en la práctica anterior. 

5\. Hallar la semisuma de los valores máximo y mínimo mediante la función **semisuma( )**. 

6\. Mostrar por pantalla los valores obtenidos: media, máximo, mínimo y semisuma. 

Tanto el programa principal como las funciones deberán estar en el mismo fichero **numeros.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

 /* fichero numeros.c */
 #include <stdio.h>
 #define SIZE 20
 /* declaracion de funciones */
 double media(double*, int);
 double maximo(double*, int);
 double minimo(double*, int);
 double semisuma(double, double);
 void main(void) {
   double vector[SIZE];
   int n, i;
   printf("Con cuantos valores deseas trabajar?\n");
   printf("(el numero debera ser menor que 20)\n");
   printf("Teclea n: ");
   scanf("%d", &n);
   printf("\n");
   printf("Introduce los %d valores:\n",n);
   for (i=0 ;i<n; i++) {
      printf("Valor %d: ", i+1);
      scanf("%lf", &vector[i]);
   }
   printf("\n");
   printf("media= %5.2lf \n", media(vector,n));
   printf("maximo= %5.2lf \n", maximo(vector,n));
   printf("minimo= %5.2lf \n", minimo(vector,n));
   printf("semisuma= %5.2lf \n", semisuma(maximo(vector, n), minimo(vector, n))); 
 }
 double media(double* valores, int num) {
   double suma=0.0, med;
   int i;
   for (i=0; i<num; i++)
   suma+=valores[i];
   med=suma/num;
   return (med);
 }
 double minimo(double* valores, int num) {
   int i;
   double min;
   min=valores[0];
   for (i=1; i<num; i++)
      if (valores[i]<min)
         min=valores[i];
   return (min);
 }
 double maximo(double* valores, int num) {
   int i;
   double max;
   max=valores[0];
   for (i=1; i<num; i++)
      if (valores[i]>max)
          max=valores[i];
   return (max);
 }
 double semisuma(double max, double min) {
    return ((max+min)/2.0);
 }
```

####  Comentario 

En este fichero se presentan funciones para calcular la media, el máximo, el mínimo, y la semisuma del máximo y el mínimo de los elementos de un conjunto. Cada uno de estos cálculos es muy sencillo. El interés de este ejercicio está en ver cómo se definen, declaran y llaman las distintas funciones que en él aparecen. El resultado de todas estas funciones es un valor único que se devuelve como valor de retorno.