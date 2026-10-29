---
title: "Producto de una matriz por un vector"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Matlab', 'Sin Pseudocódigo']
---

# Producto de una matriz por un vector

##  Enunciado 

Para que no dejes sin explotar todas las posibilidades de los bules for, te proponemos este sencillo programa que multiplica una matriz por un vector (en este orden). Escribe el programa y guárdalo como **vmatriz.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero vmatriz.c */
/* Producto de matriz por vector */
#include <stdio.h>
#define SIZE 3
void main(void) {
  double matriz[SIZE][SIZE];
  double vector[SIZE];
  double solucion[SIZE];
  double sum;
  int i,j;
  printf("Introduce los datos de la matriz:\n");
  for(i=0; i<SIZE ; i++) {
     for(j=0; j<SIZE; j++) {
        printf("\nElemento (%d,%d): ", (i+1), (j+1));
        scanf(" %lf", &matriz[i][j]);
     }
  }
  printf("\n\nIntroduce los datos del vector:\n");
  for(i=0; i<SIZE ; i++) {
     printf("\nElemento %d: ", (i+1));
     scanf("%lf", &vector[i]);
  }
  for(i=0; i<SIZE; i++) {
     sum=0;
     for(j=0; j<SIZE; j++) {
        sum+=matriz[i][j]*vector[j];
     }
     solucion[i]=sum;
  }
  printf("\nEl vector solucion es:\n");
  for(i=0; i<SIZE; i++) {
     printf("Elemento %d = %lf\n", i+1, solucion[i]);
  }
}
```

####  Comentario 

Se presentan en este programa algunos pasos típicos de manejo de matrices que son muy similares en todos los lenguajes de programación. En cuanto al algoritmo, es ya conocida la forma de multiplicar una matriz por un vector columna: cada elemento del vector producto es el producto escalar (la suma de los productos elemento a elemento) de la fila correspondiente de la matriz por el vector columna. Para ello hacen falta dos bucles: uno recorre las filas de la matriz y el otro realiza el sumatorio propio del producto escalar. Observa que, para realizar el sumatorio, se inicializa cada vez la variable sum a cero.