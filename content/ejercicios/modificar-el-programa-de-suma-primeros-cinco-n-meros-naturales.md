---
title: "Modificar el programa de Suma primeros cinco números naturales"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---

# Modificar el programa de Suma primeros cinco números naturales

##  Enunciado 

MODIFICA EL PROGRAMA [ SUMAINT.C](/ejercicios/suma-primeros-cinco-números-naturales/). 

Se trata del programa que suma los cinco primeros enteros que se presentó en el Ejercicio [ **sumaint.c**](/ejercicios/suma-primeros-cinco-números-naturales/). En primer lugar se deberá editar este programa y salvarlo con el nombre **sumaFor.c**. Se te pide que modifiques la copia (**sumaFor.c**) para que el programa realice lo mismo(sumar los cinco primeros enteros), pero empleando un bucle for en lugar de un bucle while. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

/* fichero sumaFor.c */
#include <stdio.h>
void main(void) {
  int i, suma=0;
  for(i=0; i<=5; i++)
       suma+=i;
  printf("La suma de los cinco primeros numeros es: %d\n", suma);
}
```

####  Comentario 

En este fichero se ha utilizado la equivalencia directa entre los bucles for y while. Por lo demás, este programa no tiene nada de particular. 

###  Diseño en pseudocódigo

A continuación se presenta la versión en pseudocódigo del algoritmo anterior. 
```text
 ALGORITMO sumaFor
 ENTRADAS:
       _(Este algoritmo no tiene entradas)_
 SALIDAS:
       suma: ENTERO   _(La suma de los cinco primeros números)_
 VARIABLES:
       i: ENTERO
 INICIO:
       suma<--0
       PARA i<--0 HASTA 5 C.I +1 HACER                                                                                        
               suma<--suma+1
               ESCRIBIR "La suma de los cinco numeros es",suma
       FIN_PARA
 FIN
```