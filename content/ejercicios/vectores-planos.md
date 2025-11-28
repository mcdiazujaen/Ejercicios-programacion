---
title: "Vectores planos"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---


# Vectores planos

##  Enunciado 

Sean dos vectores planos (con 2 componentes cada uno) a[ ] y b[ ]. Si a[ ] y b[ ] son linealmente independientes, cualquier vector plano c[ ] podrá ser expresado como combinación lineal de ellos: 

c[ ] = alfa * a[ ] + beta * b[ ] 

Realizar un programa que lea los vectores a[ ], b[ ] y c[ ] y calcule los coeficientes alfa y beta. El programa deberá distinguir 3 casos: 

1\. a[ ] y b[ ] son linealmente independientes (1 solución). 

2\. a[ ] y b[ ] son linealmente dependientes y c[ ] es colineal con ellos (infinitas soluciones).Elegir la solución de módulo mínimo. 

3\. a[ ] y b[ ] son linealmente dependientes y c[ ] no es colineal con ellos (no hay ninguna solución). 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c


/* fichero vector2d.c */
#include <stdio.h>
void main(void) {
  double a[2], b[2], c[2];
  double alfa, beta, aux;
  printf("Introduce los siguientes datos:\n");
  printf("a1: ");
  scanf("%lf", &a[0]);
  printf("a2: ");
  scanf("%lf", &a[1]);
  printf("b1: ");
  scanf("%lf", &b[0]);
  printf("b2: ");
  scanf("%lf", &b[1]);
  printf("c1: ");
  scanf("%lf", &c[0]);
  printf("c2: ");
  scanf("%lf", &c[1]);
  /* se calcula el determinante */
  aux = a[0]*b[1]-a[1]*b[0];
  if (aux!=0.0) {
      alfa = (c[0]*b[1]-c[1]*b[0])/aux;
      beta = (c[1]*a[0]-c[0]*a[1])/aux;
      printf("El problema tiene solucion:\n");
      printf("alfa=%lf\nbeta=%lf\n", alfa, beta);
    } else {
            printf("a y b son linealmente dependientes.\n");
            if (a[0]*c[1]==c[0]*a[1]){
                 printf("c es colineal con a y b: infinitas soluciones.\n");
                 alfa = (a[0]*c[0])/(a[0]*a[0]+a[1]*a[1]);
                 beta = (a[1]*c[0])/(a[0]*a[0]+a[1]*a[1]);
                 printf("La solucion de modulo minimo es:\n");
                 printf("alfa=%lf\nbeta=%lf\n", alfa, beta);
               } else
                     printf("No hay solucion.\n");
            }
}


```
####  Comentario 

El algoritmo para la resolución de este programa (resolución en C de un sistema de dos ecuaciones lineales con dos incógnitas), se ha basado en la regla de Cramer y se tienen en cuenta los diferentes valores del determinante de la matriz del sistema definido por la variable aux. Respecto a la comparación numérica de variables tipo double hay que decir que es preferible realizar la comparación con números muy pequeños que nos marquen un límite, por ejemplo, la sentencia if(a[0]*c[1]==c[0]*a[1]) sería más recomendable poner if(abs(a[0]*c[1]-c[0]*a[1])<1.0e-10). Esto es debido a que en el manejo de números decimales en el ordenador, siempre existe un error correspondiente al número máximo de cifras significativas que puede almacenar la variable. Por ese motivo, en este caso consideraríamos “cero” los valores absolutos inferiores a 1.0e-10. Para calcular la solución de modulo mínimo en el caso de ser a y b colineales y ser c colineal a su vez con a y b, utilizamos una operación de máximos y mínimos que da como solución: alfa = a[1]*c[1]/(a[1]*a[1] + a[2]*a[2]) beta = a[2]*c[1]/(a[1]*a[1] + a[2]*a[2])