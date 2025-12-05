---
title: "Producto de matrices"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---

# Producto de matrices

##  Enunciado 

Basándote en el producto de matriz por vector anterior, haz un programa que multiplique dos matrices cuadradas y llámalo bimatriz.c. Si no quieres perder el tiempo introduciendo datos con el teclado, también puedes asignar desde el programa unos valores arbitrarios a las matrices factores. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

 /* fichero bimatriz.c */
 #include <stdio.h>
 #define SIZE 5
 void main(void) {
   double matriz1[SIZE][SIZE], matriz2[SIZE][SIZE]; 
   double solucion[SIZE][SIZE], sum;
   int dimension, i, j, k;
   printf("Introduce la dimension de las matrices:\n");
   printf("Dimension: ");
   scanf("%d", &dimension);
   printf("Introduce los elementos de la primera matriz:\n");
   for (i=0; i<dimension; i++) {
      for (j=0; j<dimension; j++) {
          printf("a(%d,%d): ", i+1, j+1);
          scanf("%lf", &matriz1[i][j] );
      }
   }
   printf("\n");
   printf("Introduce los elementos de la segunda matriz:\n");
   for (i=0; i<dimension; i++) {
      for (j=0; j<dimension; j++) {
         printf("b(%d,%d): ", i+1, j+1);
         scanf("%lf", &matriz2[i][j] );
      }
   }
   printf("\n");
   for (i=0; i<dimension; i++) { 
       for (j=0; j<dimension ; j++) {
          sum=0.0;
          for (k=0; k<dimension; k++)
              sum+=matriz1[i][k]*matriz2[k][j];
              solucion[i][j]=sum;
          }
       }
   printf("Solucion:\n\n\n");
   for (i=0; i<dimension; i++) {
      for (j=0; j<dimension; j++)
          printf("%5.2lf ", solucion[i][j]);
      printf("\n");
   }
 }

```
####  Comentario 

Tal vez el aspecto más interesante de este programa es la necesidad de utilizar 3 bulces for para la multiplicación de dos matrices. Para verlo más claramente, sea **a ij** un elemento de la primera matriz, **b ij** un elemento de la segunda y **c ij** un elemento de la matriz solución. Pensemos por un momento cómo se obtiene un elemento cualquiera de la matriz solución. El elemento **c 23**, por ejemplo, se obtiene multiplicando los elementos de la fila 2 de la primera matriz, por los elementos de la columna 3 de la segunda matriz. Suponiendo que las matrices son de dimensión 3 tendremos: 
```text

c23 = a21*b13+a22*b23+a23*b33 y en general:
cij = ai1*b1j+ai2*b2j+ai3*b3j

```
Por lo tanto, para poder acceder a los elementos de la fila i de la primera matriz y a los elementos de la columna j de la segunda matriz, y para realizar el sumatorio son necesarios tres bucles, para los que se han utilizado las variables **i** , **j** y **k**.