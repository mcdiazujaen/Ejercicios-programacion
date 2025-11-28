---
title: "Giro de una barra extensible"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---


# Giro de una barra extensible

  

##  Enunciado 

En la siguiente figura se muestra una barra AB extensible, es decir, de longitud variable, que gira alrededor de su extremo fijo A. Las coordenadas (xi, yi) de su extremo móvil B son conocidas en diez instantes del movimiento. 

![imagen:Giro.JPG](images/8/8d/Giro.JPG)

Las coordenadas del extremo B son las siguientes: (2, 0), (1.5, 3), (-1, 3), (-1.5, 2), (-2.5, 0), (-2.5, -1), (-1.5, -1.5), (0, -1), (1, -2), (1.5, -1.5). Estas coordenadas se almacenarán en el fichero **datos.d**. Realiza un programa que calcule el ángulo formado por la barra con la horizontal y su longitud, en cada uno de los diez instantes de tiempo. El ángulo se calculará leyendo los datos del fichero **datos.d** , y utilizando la función arcotangente. La librería matemática de C dispone de dos funciones para calcular el arcotangente: atan() y atan2(), cuyos prototipos son: 

  * double atan(double a) que calcula el arcotangente de a entre (-π/2, π/2) 
  * double atan2(double b, double a) que calcula el arcotangente de un ángulo cuyo seno es proporcional a b y cuyo coseno es proporcional a a. De esta forma puede detectarse el cuadrante y devolver un ángulo entre –π y π radianes. 

Te pedimos que programes una función similar a atan2() y que llamarás atan2a() (empleando para ello atan()), de manera que el ángulo que devuelva esté comprendido entre (-π, π). 

La salida del programa deberá ser similar a la siguiente: 

En el instante 1 la barra tiene una longitud de 2 y forma un angulo de 0 radianes o de 0 grados con la horizontal. En el instante 2 la barra tiene una longitud de 1.765 y forma un angulo de 0.17823 radianes o 10.21 grados con la horizontal. En el instante 3 ... 

(Los valores que se muestran son inventados y no han de concidir con los que calcules). 

Guarda el programa como **barra.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c


/* fichero barra.c */
#include <stdio.h>
#include <math.h>
#define PI 3.141592654
void main(void) {
  int i;
  FILE *fi;
  double x, y;
  double radianes, grados, longitud;
  double calculaLongitud(double, double);
  double atan2a(double, double);
  fi = fopen("datos.d", "r");
  for (i=1; i<=10; i++) {
    fscanf(fi, "%lf", &x);
    fscanf(fi, "%lf", &y);
    longitud=calculaLongitud(x,y);
    radianes=atan2a(x,y);
    grados=radianes*180.0/PI;
    printf("En el instante %d la barra tiene una longitud de %lf\n", i, longitud);
    printf("y forma un angulo de %lf radianes ", radianes);
    printf("o %lf grados con la horizontal.\n", grados);
    getchar();
  }
  fclose(fi);
}
double calculaLongitud(double x, double y) {
  double resul;
  resul=sqrt(x*x+y*y);
  return(resul);
}
double atan2a(double x, double y) {
  double resul, aux;
  if (x==0.0)
     if (y>0.0)
         resul=PI/2;
       else
         resul=-PI/2;
    else
     aux=atan(y/x);
  if ((x<0.0)&&(x!=0.0))
     if (y>=0.0) /*si el angulo esta en el segundo cuadrante */
         resul=aux+PI;
       else
         resul=aux-PI; /* si el angulo esta en el tercer cuadrante */
   else if (x!=0.0) 
           resul=aux; /* si el angulo esta en el primer o cuarto cuadrante */
 return resul;
}


```
####  Comentario 

Este programa va leyendo las coordenadas x e y para cada posición de la barra y llama **calculaLongitud()** y **atan2a()** respectivamente a las funciones que calculan la longitud de la barra y que devuelve el ángulo que forma la barra en radianes. En cuanto a la función **atan2a()** , queremos que devuelva un ángulo comprendido entre -π y π radianes basándonos en la función **atan()** que devulve un ángulo comprendido entre −π/2 y π/2. Para ello hay que tener en cuenta que: 

  * Si x>0 e y>0: el ángulo pertenece al primer cuadrante, por lo tanto atan2a()=atan(). 
  * Si x>0 e y<0: el ángulo pertenece al cuarto cuadrante, por lo tanto atan2a()=atan(). 
  * Si x<0 e y>0: el ángulo pertenece al segundo cuadrante, por lo tanto atan2a()=atan()+ π. 
  * Si x<0 e y<0: el ángulo pertenece al tercer cuadrante, por lo tanto atan2a()=-atan()- π. 

Hay que tener cuidado cuando x=0, pues se realiza una división por cero que produce un error al ejecutar el programa. Esto se puede evitar fácimente, ya que en este caso la barra se encuentra en posición vertical, formando un ángulo de π/2 (y>0), o −π/2 (y<0).