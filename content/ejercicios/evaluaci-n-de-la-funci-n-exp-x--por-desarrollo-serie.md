---
title: "Evaluación de la función Exp(x) por desarrollo serie"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab']
---


# Evaluación de la función Exp(x) por desarrollo serie

##  Enunciado 

Según la fórmula de Taylor, podemos expresar la función exponencial **e x** mediante la siguiente serie de potencias de x: 

![imagen:Taylor1.JPG](images/6/6a/Taylor1.JPG)

En el programa que te presentamos a continuación, las variables z y numero, argumentos formales de la función, reciben respectivamente una copia de x y terminos, que son los argumentos actuales. La variable **frac** va almacenando la fracción a sumar en cada término del sumatorio. Así para cada nuevo sumando no hay más que multiplicar el anterior valor por **z/i** : 

![imagen:Taylor2.JPG](images/3/37/Taylor2.JPG)

Guarda el programa en un fichero con el nombre **serie.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c


/* fichero serie.c */
#include <stdio.h>
#include <math.h>
void main(void) {
  int terminos;
  double x;
  double serie(double ,int );
  printf("%s%s", "Este programa calcula \"e\" elevado a \"x\" por desarrollo ",
         "en serie\ncon el numero de terminos que quieras\n");
  printf("Teclea x: ");
  scanf("%lf",&x);
  printf("Teclea el numero de terminos: ");
  scanf("%d", &terminos);
  printf("%s%lf con %d %s%16.6lf\n",
         "El resultado de e elevado a ", x, terminos, "terminos es ",
         serie(x, terminos));
  printf("Error cometido: %16.6lf\n", serie(x, terminos)-exp(x));
}



double serie(double z, int numero) {
  double miserie=1, frac;
  int i;
  frac=z;
  miserie+=frac;
  i=2;
  if (numero==1) {
     miserie=1;
     return miserie;
    }
  while (i<=numero) { 
     frac=frac*z/i++;
     miserie+=frac;
  }
  return miserie;
}


```
####  Comentario 

La complejidad de este tipo de programas reside en el algoritmo concreto que se utilice. En este caso, la condición que tiene el bucle para finalizar la iteración es el número de términos, que se ha introducido por el teclado como dato. La forma de calcular la serie es añadiendo una nueva fracción a la serie. Para el cálculo de esta nueva fracción utilizamos el valor que tenía la fracción en la iteración anterior, según explica el enunciado del ejercicio. En este tipo de sumas los errores son más pequeños sumando primero los términos más pequeños y luego los más grandes, pues al sumar un número pequeño a uno grande unas cuantas cifras del número pequeño se pierden de modo irremediable. Además, es posible que un número pequeño sea despreciable frente a uno grade, pero la suma de muchos números pequeños puede no ser tan insignificante. Si cada número pequeño se suma al número grande individualmente, el resultado puede ser diferente que si todos los número pequeños se suman entre sí primero, y luego el resultado se suma al número grande.