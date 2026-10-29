---
title: "Suma primeros cinco números naturales"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Matlab', 'Sin Pseudocódigo']
---

# Suma primeros cinco números naturales

##  Enunciado 

Se presenta a continuación un programa que utiliza la sentencia while para definir un bucle. El programa sumará de forma automática los cinco primeros números naturales. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero sumaInt.c */
/* Programa para calcular la suma de los enteros del 1 al 5 */
#include <stdio.h>
void main(void) {
  int i=1, suma=0;
  while (i<=5) { /* se ejecuta el bloque mientras i<=5 */
      suma+=i; /* equivale a suma=suma+i; */
      ++i;     /* equivale a i=i+1; */
  }
printf("suma = %d\n", suma);
}
```

####  Comentario 

El bucle while realiza la sentencia simple o compuesta que le sigue mientras la condición definida entre paréntesis sea verdadera (es decir distinta de cero). El bucle while del programa anterior podía también haberse escrito en la siguiente forma (más compacta): 
```text
   while (i<=5)    /* se ejecuta el bloque mientras i<=5 */
      suma += i++; /* equivale a suma=suma+i e i=i+1; */
```

No hacen falta las llaves porque sólo hay una sentencia simple detrás del while.