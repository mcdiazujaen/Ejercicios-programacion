---
title: "Tabla de conversión de grados centigrados a fahrenheit"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---

# Tabla de conversión de grados centigrados a fahrenheit

##  Enunciado 

Realiza un programa en C que escriba una tabla de dos columnas para la conversión entre las temperaturas en grados Fahrenheit −comprendidas entre 0 ºF y 300 ºF, según incrementos de 20 ºF− y su equivalente en grados centígrados. Se realizarán dos versiones de este programa: una llamada temp1.c que empleará un bucle while. La otra versión se llamará temp2.c y utilizará un bucle for. La conversión entre grados Centígrados y grados Fahrenheit obedece a la fórmula: 

![imagen:Fahrenheit.JPG](images/9/95/Fahrenheit.JPG)

siendo ºC la temperatura en grados Centígrados y ºF en grados Fahrenheit. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

 /* fichero temp1.c */
 #include <stdio.h>
 void main(void) {
 double gradosFahr, gradosCent;
 printf("grados Fahrenheit grados Centigrados\n");
 printf("----------------- ------------------\n\n");
 gradosFahr = 0.0;
 while (gradosFahr<=300.0) {
   gradosCent=(5*(gradosFahr-32.0))/9.0;
   printf("%17.2lf%17.2lf\n", gradosFahr, gradosCent);
   gradosFahr+=20.0;
  }
 }

 /* fichero temp2.c */
 #include <stdio.h>
 Ejercicios Resueltos de Programación en ANSI C pág. 10
 void main(void) {
 double gradosFahr, gradosCent;
 printf("grados Fahrenheit grados Centigrados\n");
 printf("----------------- ----------------\n\n");
 for (gradosFahr=0.0; gradosFahr<=300.0; gradosFahr+=20.0) {
    gradosCent = (5*(gradosFahr-32.0))/9.0;
    printf("%17.2lf%17.2lf\n", gradosFahr, gradosCent);
  }
 }

```
####  Comentario 

Como podrás observar la diferencia entre los dos programas está fundamentalmente en la forma de utilizar los bucles respectivos, a diferencia del while, en los parámetros del bucle for está incluidas todas las condiciones necesarias para su ejecución, es decir se encuentran: la inicialización, la condición a cumplir y además el incremento del contador, lo cual simplifica mucho el programa.