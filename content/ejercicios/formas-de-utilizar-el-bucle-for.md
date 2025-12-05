---
title: "Formas de utilizar el bucle For"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---

# Formas de utilizar el bucle For

##  Enunciado 

VARIAS FORMAS DE UTILIZAR EL BUCLE FOR. 

En el siguiente programa se muestran distintas formas de escribir un bucle for para sumar los enteros del 1 al 5. Escribe el siguiente programa y guárdalo con el nombre **sumaFor2.c**. Compílalo, ejecútalo y observa los resultados. ¿Ves algo raro? 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero sumaFor2.c */
/* Programa para sumar los enteros del 1 al 5 */
#include <stdio.h>
void main(void) {
int i=1, suma=0;
  for ( ; i<=5 ; ) { /* primera forma */
     suma += i;
     ++i;
  }
  printf("suma 1 = %d\n", suma);
  suma=0; /* segunda forma */
 
  for (i=1; i<=5; ++i)
       suma+=i;
  printf("suma 2 = %d\n", suma);
 
  for(i=1, suma=0; i<=5 ; ++i, suma+=i) /* tercera forma */
  ;
  printf("suma 3 = %d\n", suma);
  
  for(i=1, suma=0; i<=5 ; suma+=i, ++i) /* cuarta forma */
  ;
  printf("suma 4 = %d\n", suma);
}
```

####  Comentario 

Para definir un bucle hace falta un contador o variable de control (que casi siempre es un entero y suele nombrarse con las letras típicas de subíndices: i, j, k, ...). Esta variable de control es la que se chequea cada vez que comienza el bucle y la que permite continuar o no realizando las operaciones de dentro del bucle. Por otra parte, en C, el bucle for tiene tres componentes separadas por puntos y comas: la primera es una inicialización de la variable de control (u otras que pudieran afectar al bucle), la segunda es la sentencia de chequeo de la variable de control que siempre es necesaria (véase la primera forma); por último, la tercera son sentencias de actualización que se ejecutan al final del bucle (que también se podrían poner entre las llaves del bucle, detrás de las demás sentencias). Conociendo estas características, la forma más habitual de expresar un bucle es la segunda, ya que el bucle for contiene las instrucciones pertinentes a la variable de control. La forma primera es más asimilable a un bucle while, ya que la instrucción for contiene sólo el chequeo de la variable. La diferencia entre las formas tercera y cuarta es el orden en que se ejecutan las instrucciones: la forma tercera ejecuta antes el incremento de la variable que el chequeo y la suma, por tanto cuando i vale 6 ya se ha sumado a la variable suma y, por eso el resultado sale 20 en lugar de 15.