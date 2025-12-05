---
title: "Ecuación de segundo grado"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---

# Ecuación de segundo grado

##  Enunciado 

SOLUCIÓN DE LA ECUACIÓN DE SEGUNDO GRADO. Dada la ecuación de segundo grado ax2 + bx +c = 0 : se calcula el discriminante discr =b2 −4ac . Se pueden presentar tres casos distintos: 

  * Si discr >0.0 las dos raíces son reales y distintas, y valen: 

![imagen:Ecuacion2grado1.JPG](images/9/9f/Ecuacion2grado1.JPG)

  * Si discr = 0.0 las dos raíces son reales e iguales, y valen: 

![imagen:Ecuacion2grado2.JPG](images/e/ef/Ecuacion2grado2.JPG)

  * Finalmente, si discr<0.0 las dos raíces son complejas conjugadas. 

Las partes real e imaginaria valen: 

![imagen:Ecuacion2grado3.JPG](images/9/9d/Ecuacion2grado3.JPG)

Teclea y compila el siguiente programa para resolver la ecuación de segundo grado. Llámalo **ecuacion2.c.**

Compila y ejecuta este programa cambiando los valores de a, b y c, de modo que se prueben las tres opciones del programa. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero ecuacion2.c */
/* resolución de la ecuación de segundo grado */
#include <stdio.h>
#include <math.h> /* incluye decl. de la función sqrt() */

void main(void) {
  double a, b, c;
  double discr, x1, x2, xr, xi;
  
  printf("Escribe los valores de los coeficientes A, B y C\n");
  scanf("%lf%lf%lf", &a, &b, &c);
  discr=b*b-4.0*a*c;
  if (discr>0.0) {
      x1=(-b+sqrt(discr))/(2.0*a);
      x2=(-b-sqrt(discr))/(2.0*a);
      printf("\nLas dos raices reales son: %12.6e y %12.6e \n",x1, x2);
  } else if (discr<0.0) {
      xr=-b/(2.0*a);
      xi=sqrt(-discr)/(2.0*a);
      printf("\nRaices complejas:\n");
      printf("(%12.6e, %12.6ei) y (%12.6e, %12.6ei)\n", xr, xi, xr, -xi);
  } else {
      x1 = -b/(2.0*a);
      printf("\nLas dos raices son iguales y valen: %12.6e \n", x1);
  }
}

```
####  Comentario 

Incluyendo la librería math.h se pueden usar las funciones matemáticas tales como sqrt() para la raíz cuadrada; cos() para calcular el coseno de un ángulo, etc. La instrucción if...else permite hacer una bifurcación, dependiendo de la cual se realizarán diferentes actividades. Merece la pena observar la forma utilizada para partir en varias líneas las distintas llamadas a la función printf(). La idea fundamental es que, en el fichero *.c la cadena de control (lo que va entre comillas como primer argumento de la función printf()) no se puede partir entre dos o más líneas. 

###  Diseño en pseudocódigo
```text

 ALGORITMO divisonSegundoGrado
 ENTRADAS:
    a,b,c: REALES _(Coeficientes de la ecuación)_
 SALIDAS:
    x1,x2: REALES _(Soluciones reales)_
    xr,xi: REALES _(Soluciones imaginarias)_
 VARIABLES:
    discr: REAL
 INICIO
    ESCRIBIR "Escribe los valores de los coeficientes A, B y C:"
    LEER a,b,c
    discr <-- b*b-4*a*c
    SI discr>0 ENTONCES
       x1 <-- (-b+raiz(discr))/(2*a)
       x2 <-- (-b-raiz(discr))/(2*a)
       ESCRIBIR "Las dos raices reales son ", x1, " y ", x2
    SI_NO
       SI discr<0 ENTONCES
          xr <-- -b/2*a
          xi <-- raiz(-discr)/(2*a)
          ESCRIBIR "Raíces complejas: "
          ESCRIBIR "(", xr, ",", xi, ") y (", xr, ",", -xi, ")"
       SI_NO
          x1 <-- -b/(2*a)
          ESCRIBIR "Las dos raíces son iguales y valen: ", x1
       FIN_SI
    FIN_SI
FIN
```