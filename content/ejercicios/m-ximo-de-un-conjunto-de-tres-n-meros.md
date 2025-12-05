---
title: "Máximo de un conjunto de tres números"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Máximo de un conjunto de tres números

##  Enunciado 

Realiza un programa principal que lea tres números enteros por teclado, los almacene en tres variables (x, y, z) y llame a una función llamada **maximo()** , con tres argumentos, que devuelva el máximo de estos tres valores. Guarda el programa como **maxval.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio 5.4. 
```c

/* fichero maxval.c */
#include <stdio.h>
void main(void) {
  int x, y, z;
  int maximo(int, int, int);
  printf("Introduce tres valores:\n");
  printf("primero: ");
  scanf("%d", &x);
  printf("segundo: ");
  scanf("%d", &y);
  printf("tercero: ");
  scanf("%d", &z);
  printf("El maximo de los tres valores introducidos es: ");
  printf("%d\n", maximo(x, y, z));
}

int maximo(int a, int b, int c) {
  int max;
  max=a;
  if (b>max)
      max=b;
  if (c>max)
      max=c;
  return max;
}
```

####  Comentario 

Como la función maximo() devuelve un valor entero. Las variables a, b, y c, argumentos formales de la función, reciben una copia de los argumentos actuales: x, y, z. La forma de calcular el máximo de una lista de números es ya conocida.