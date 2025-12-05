---
title: "Ordenar sin olvidar el orden inicial"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Ordenar sin olvidar el orden inicial

##  Enunciado 

Modifica el programa [**ordena.c**](/ejercicios/ordenación-de-la-burbuja/) de manera que, además de mostrar el vector ordenado, muestre también el vector original. Además deberá mostrar la posición que cada número ocupaba en el vector inicial. Guarda este programa con nombre **reordena.c**. 

Una salida posible podría ser: 

El vector inicial es: {7, 23, 5, 1, 8, 3, 12} 

El vector ordenado es: {1, 3, 5, 7, 8, 12, 23} 

que ocupaban los lugares {4, 6, 3, 1, 5, 7, 2}, respectivamente. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

/* fichero reordena.c */
#include <stdio.h>
#define SIZE 7
void main(void) {
  int vector[SIZE], copia[SIZE], orden[SIZE];
  int j, i, temp;
  printf("Introduzca los %d valores para ordenar:\n", SIZE);
  for(i=0; i<SIZE; i++) {
     printf("\n%d: ", i+1);
     scanf("%d", &vector[i]);
     copia[i]=vector[i];
     orden[i]=i+1;
  }
  for (i=0; i<(SIZE-1); i++)
     for (j=i+1; j<SIZE; j++)
       if (vector[j]<vector[i]) {
            temp=vector[j];
           vector[j]=vector[i];
           vector[i]=temp;
           temp=orden[j];
           orden[j]=orden[i];
           orden[i]=temp;
       }
  printf("\nEl vector inicial es: { ");
  for (i=0; i<SIZE; i++)
      printf("%d, ", copia[i]);
  printf("\b\b} \n"); /* se utiliza backspace */
  printf("El vector ordenado es: { ");
  for (i=0; i<SIZE; i++)
      printf("%d, ", vector[i]);
  printf("\b\b} \n");
  printf("que ocupaban los lugares { ");
  for (i=0; i<SIZE; i++)
      printf("%d, ", orden[i]);
  printf("\b\b}, respectivamente.\n");
}

```
####  Comentario 

El funcionamiento del programa de ordenación de los elementos de un vector se vió en la [práctica anterior](/ejercicios/ordenación-de-la-burbuja/). Para evitar perder el vector original con el cambio, lo que se hace es una simple copia del mismo con la instrucción **copia[i] = vector[i]**. 

Para saber en qué posición estaban los elementos en el vector original, se crea un nuevo vector llamado **orden[ ]** , cuyos elementos son los números naturales 1, 2, 3, 4. ... Este vector sufre las mismas permutaciones que el vector inicial, por lo que, al final de la ordenación sus elementos indicarán que posición ocupaban al principio los elementos del vector ordenado. Para obtener exactamente la salida impresa solicitada, hay que imprimir las llaves **{ }** y los blancos y comas que separan los elementos de los vectores. Después de escribir cada elemento de un vector se escribe una coma y un blanco. En realidad esto no hay que hacerlo para el último elemento, que debe ir seguido por el cierre de las llaves. Sin embargo, por simplicidad se escriben también en este caso la coma y el blanco, pero luego se imprimen dos caracteres backspace ('\b', espacio hacia atrás), con lo cual el cierre de las llaves se imprime sobre la coma. 

###  Diseño en Pseudocódigo
```text

ALGORITMO Reordena
CONSTANTES:
    SIZE=7
ENTRADAS:
    vector: ARRAY (0...SIZE-1) DE ENTEROS  _(vector que queremos ordenar)_
SALIDAS:
    copia: ARRAY(0...SIZE-1) DE ENTEROS  _(vector copia con los valores originales)_
    orden: ARRAY(0...SIZE-1) DE ENTEROS  _(posición original de los valores ordenados)_
VARIABLES:
    temp: ENTERO
    i: ENTERO
    j: ENTERO
INICIO
   _(Leer los valores del array)_  
   ESCRIBIR "Introduzca los", SIZE, "valores para ordenar:")
   PARA i<--0 HASTA SIZE-1 HACER
      ESCRIBIR i+1, ": "
      LEER vector(i)
      copia(i)<--vector(i)
      orden(i)<--i+1
   FIN_PARA

   _(Reordenar el vector)_
   PARA i<--0 HASTA SIZE-2 HACER
     PARA j<--i+1 HASTA  SIZE-1 HACER
       SI vector(j)<vector(i) ENTONCES
           _(Cambiar los valores del vector)_
           temp<--vector(j)
           vector(j)<--vector(i)
           vector(i)<--temp
           _(Cambiar las posiciones originales)_
           temp<--orden(j)
           orden(j)<--orden(i)
           orden(i)<--temp
       FIN_SI
     FIN_PARA
  FIN_PARA
  _(Mostrar el array original)_
  ESCRIBIR "El vector inicial es: {" 
  PARA i<--0 HASTA SIZE-1 HACER
      ESCRIBIR copia(i), ", "
  FIN_PARA
  ESCRIBIR "}"
  _(Mostrar el array ordenado)_
  ESCRIBIR "El vector ordenado es: {"
  PARA i<--0 HASTA SIZE-1 HACER
      ESCRIBIR vector(i), ", "
  FIN_PARA
  ESCRIBIR "}"
  _(Mostrar las posiciones originales)_
  ESCRIBIR "que ocupaban los lugares {"
  PARA i<--0 HASTA SIZE-1 HACER
      ESCRIBIR orden(i), ", "
  FIN_PARA
FIN
```