---
title: "El sultan y el estudiante"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Matlab']
---

# El sultan y el estudiante

##  Enunciado 

Habrás oído hablar de la historia de un poderoso sultán que deseaba recompensar a un estudiante que le había prestado un gran servicio. Cuando el sultán le preguntó qué recompensa deseaba, éste le señaló un tablero de ajedrez y solicitó simplemente 1 grano de trigo por la primera casilla, 2 por la segunda, 4 por la tercera, 8 por la siguiente, y así sucesivamente. El sultán, que no debía andar muy fuerte en matemáticas, quedó sorprendido por la modestia de la petición, porque estaba dispuesto a otorgarle riquezas muy superiores: al menos, eso pensaba él. En el siguiente programa se calcula el número total de granos de trigo que corresponden a cada casilla y se acumula el total. Como el número de granos no es una cantidad que se maneje habituamente, se compara también con una estimación de la producción anual mundial de trigo expresada en granos. Guarda este programa con el nombre **trigo.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

 /* fichero trigo.c */
 #define CUADRADOS 64 /* cuadrados del tablero */
 #define COSECHA 4E15 /* cosecha mundial en granos */
 #include <stdio.h>
 void main(void) {
    double actual, total;
    int cont=1;
    printf("Cuadro granos sumados granos totales ");
    printf("fraccion de\n");
    printf(" ");
    printf(" cosecha\n");
    total=actual=1.0; /* comenzamos con un grano */
    printf("%4d %15.2e %16.2e %12.2e\n",
    cont, actual, total, total/COSECHA);
    while (cont<CUADRADOS) {
       cont=cont+1;
       actual*=2.0; /* duplica granos en cada cuadro */
       total+=actual; /* actualiza total */
       printf("%4d %15.2e %16.2e %12.2e\n", cont, actual, total, total/COSECHA);
    }
 }
```

####  Comentario 

El interés de este ejercicio está en ver una forma de disponer los resultados de salida en columnas, formando una tabla. Primero se deben imprimir los encabezamientos de las columnas y luego las cifras correspondientes a cada línea o fila de la tabla. 

###  Diseño en Pseudocódigo
```text
 ALGORITMO granos_trigo
 CONSTANTES:
 	CUADRADOS=64
 	COSECHA=4*1015
 ENTRADAS:
 	_(No son necesarias)_
 SALIDAS:
 	actual: REAL
       total: REAL
 	cont: ENTERO
 INICIO
    ESCRIBIR "Cuadros, granos sumados, granos totales, fracción de cosecha"
    ESCRIBIR  SaltoDeLinea
 
    cont <-- 1
    total <-- 1
    actual <-- 1 _(Comenzamos con un grano)_
 
    ESCRIBIR cont, actual, total, total/COSECHA 
    ESCRIBIR SaltoDeLinea
 
    MIENTRAS cont<CUADRADOS HACER
       cont<--cont+1
       actual<--actual*2     _(Duplica granos en cada cuadro)_
       total<--total+actual  _(Actualiza total)_
 
       ESCRIBIR cont, actual, total, total/COSECHA 
       ESCRIBIR SaltoDeLinea
    FIN_MIENTRAS
 
 FIN
```