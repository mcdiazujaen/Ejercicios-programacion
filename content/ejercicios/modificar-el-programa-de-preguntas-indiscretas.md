---
title: "Modificar el programa de Preguntas indiscretas"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---


# Modificar el programa de Preguntas indiscretas

  

##  Enunciado 

MODIFICA EL PROGRAMA [**MASCOTA.C**](/ejercicios/preguntas-indiscretas/). 

En este ejercicio se te pide una modificación del programa del Ejercicio [**mascota.c**](/ejercicios/preguntas-indiscretas/). Edita el programa [**mascota.c**](/ejercicios/preguntas-indiscretas/) y guardado con el nombre **pregunta.c** , modificándolo de manera que al ejecutarse nos pregunte el número de calzado, peso y color favorito. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio 
```c


/* fichero pregunta.c */
#include <stdio.h>
void main(void) {
  int calzado;
  float peso;
  char color[20];
  printf("Confiesa tu calzado, peso y color favorito:\n");
  printf("\n Calzado: ");
  scanf("%d", &calzado);
  printf("\n Peso: ");
  scanf("%f", &peso);
  printf("\nColor favorito: ");
  scanf("%s", color);
  printf("El %s!\n", color);
  printf("Como puede gustarte el %s,\n", color);
  printf("calzando un %d y pesando %6.2f Kg.?\n", calzado, peso);
}


```
####  Comentario 

En la función **printf()** hay que utilizar diferentes formatos de salida para las variables que deseamos imprimir en pantalla. Así, el formato **%6.2f** mostrará peso en 6 espacios, de los cuales dos serán para los decimales y uno para el punto decimal. Observa cómo se pide el peso, calzado y color favorito de forma que los dos puntos (:) queden alineados en la pantalla.