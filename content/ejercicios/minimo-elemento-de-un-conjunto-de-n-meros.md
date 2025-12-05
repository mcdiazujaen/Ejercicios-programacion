---
title: "Minimo elemento de un conjunto de números"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Minimo elemento de un conjunto de números

##  Enunciado 

Modifica el programa [**maximo.c**](/ejercicios/máximo-elemento-de-un-conjunto-de-números/), de forma que calcule el mínimo valor del conjunto. Guárdalo con el nombre **minimo.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

/*fichero minimo.c */
#include <stdio.h>
#define SIZE 5
void main(void) {
  int i, min, imin;
  int conjunto[SIZE];
  printf("Introduce %d valores:\n", SIZE);
  for (i=0; i<SIZE; i++) {
     printf("%d: ", i+1);
     scanf("%d", &conjunto[i] );
     printf("\n"); 
  }
  min=conjunto[0];
  imin=0;
  for (i=0; i<SIZE; i++) {
     if (conjunto[i] < min) {
          min=conjunto[i];
          imin=i;
      }
  }
  printf("\nEl minimo valor del conjunto es: %d.\n", min);
  printf("\ny esta en la posicion %d.\n", imin+1);
}

```
####  Comentario 

Este programa es prácticamente idéntico al anterior. En lugar de las variables max e imax se emplean las variables min e imin que almacenan el valor mínimo y su posición, respectivamente. Una vez hechos estos cambios de nombre de variables, la única línea del programa que varía es la correspondiente a la condición del if, que como se está buscando el valor mínimo, habrá de ser: 
```text

if (conjunto[i]<min)

```
es decir, habrá de chequear si el elemento considerado es menor que el valor mínimo encontrado hasta ese momento.