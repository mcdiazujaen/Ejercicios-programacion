---
title: "Operaciones con vectores"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Operaciones con vectores

##  Enunciado 

Realiza un programa, que lea dos vectores de 3 componentes, y luego los sume, reste y multiplique, tanto escalar como vectorialmente, imprimiendo después todos estos resultados. Para ello crearás las funciones **suma( )** , **resta( )** , **productoEscalar( )** y **productoVectorial( )**. Guárdalo con el nombre **vectores.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero vectores.c */
#include <stdio.h>
/* declaracion de funciones */
void suma( double*, double*, double*);
void resta( double*, double*, double*);
void productoVectorial(double*, double*, double*);
double productoEscalar(double*, double*);
void main(void) {
  double vector1[3], vector2[3], vecsum[3], vecres[3];
  double escalar, prodvect[3];
  int i;
  printf("Introduce los valores del primer vector:\n");
  for (i=0; i<3; i++) {
     printf("\nElmento %d: ", i+1);
     scanf("%lf", &vector1[i]);
  }
  printf("\n");
  printf("Introduce los valores del segundo vector:\n");
  for (i=0; i<3; i++) {
     printf("\nElemento %d: ", i+1);
     scanf("%lf", &vector2[i]);
  }
  printf("\n");
  suma(vector1, vector2, vecsum);
  resta(vector1, vector2, vecres);
  productoVectorial(vector1, vector2, prodvect);
  printf("\nImprimo los resultados: \n\n");
  printf("%10s %10s %20s\n", "Suma", "Resta", "Producto Vectorial");
  for (i=1; i<=50; i++)
     printf("-");
  printf("\n"); 
  for (i=0; i<3; i++){
    printf("%10.2lf %10.2lf %10.2lf\n", vecsum[i], vecres[i], prodvect[i]);
    printf("\n");
  }
  printf("Producto escalar = %5.2lf\n",
  productoEscalar(vector1,vector2));
  printf("----------------\n");
}
void suma(double* vec1, double* vec2, double* sum) {
  int i;
  for (i=0; i<3; i++)
     sum[i]=vec1[i]+vec2[i];
  return;
}
void resta(double* vec1, double* vec2, double* res) {
  int i;
  for (i=0; i<3; i++)
    res[i]=vec1[i]-vec2[i];
  return;
}
void productoVectorial(double* vec1, double* vec2, double* vectorial) {
   vectorial[0] = vec1[1]*vec2[2]-vec2[1]*vec1[2];
   vectorial[1] = vec1[2]*vec2[0]-vec2[2]*vec1[0];
   vectorial[2] = vec1[0]*vec2[1]-vec2[0]*vec1[1];
   return;
}
double productoEscalar(double* vec1, double* vec2) {
  double escalar = 0.0;
  int i;
  for (i=0; i<3; i++)
    escalar+=vec1[i]*vec2[i];
  return (escalar);
}
```

####  Comentario 

Este ejercicio es similar al anterior, pero con algunas diferencias interesantes. La más importante es que el resultado de algunas operaciones con vectores (como la suma, la diferencia o el producto vectorial), son también vectores. Por tanto el resultado de dichas operaciones no es un valor único y no se devuelve como valor de retorno. Lo que se hace es pasar todos los vectores como argumentos por referencia. Como el nombre de un vector es la dirección de su primer elemento, la función es capaz de recibir datos y devolver resultados leyendo y escribiendo en las zonas de memoria adecuadas. En el momento de imprimir resultados, se puede hacer que los letreros de suma, resta y producto vectorial, sean colocados a la hora de imprimir con cierto espacio, lo cual mejora la presentación de los resultados. Esto se hace con instrucciones de cadenas de caracteres reservando los espacios que consideramos necesarios (p.ej: %10s, reserva un espacio mínimo de 10 caracteres para imprimir el letrero correspondiente). Se ha incluido un bucle for que imprime una línea discontinua para subrayar los títulos. Luego, a los resultados se le da el formato indicado para que ocupen un número de espacios acorde con los títulos.