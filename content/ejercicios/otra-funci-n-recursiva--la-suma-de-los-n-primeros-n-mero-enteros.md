---
title: "Otra función recursiva: La suma de los N primeros número enteros"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---

# Otra función recursiva: La suma de los N primeros número enteros

##  Enunciado 

Seguro que con la experiencia adquirida en el ejercicio [**factor2.c**](/ejercicios/una-función-que-se-llama-a-sí-misma-función-recursiva/) no tienes ninguna dificultad en desarrollar tu propia función recursiva para hallar la suma de los n primeros números enteros impares. Llama **sum2.c** al fichero correspondiente. En este caso, la función se puede basar en la fórmula recursiva siguiente: 

**suma(n) = (2*n−1) + suma(n−1)**

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero sum2.c */
#include <stdio.h>
void main(void) {
  int n;
  double suma(int);
  printf("Teclea un numero entero positivo: \n");
  scanf("%d", &n);
  printf("La suma de los %d primeros impares es %lf\n", n, suma(n));
}
double suma(int n) {
  if(n<=1)
      return 1.0;
  return ((2*n-1)+suma(n-1));
}
```

####  Comentario 

Sólo reseñar que no se trata de la suma de los impares hasta el número n que se teclea, sino que es la suma de los n primeros números impares, es decir, si por ejemplo tecleamos 3, el resultado será 9 que es la suma de 1 más 3 más 5.