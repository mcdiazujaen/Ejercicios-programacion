---
title: "Leer una frase y escribirla al reves"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Pseudocódigo']
---

# Leer una frase y escribirla al reves

##  Enunciado 

Realiza un programa que lea una línea de texto y a continuación la escriba al revés. Tener en cuenta que en una línea puede contener varias palabras, es decir caracteres en blanco. La función **scanf()** sólo lee la primera palabra de la frase, pues la lectura se detiene al llegar al primer carácter en blanco. Se sugieren dos formas de leer líneas completas, una con la función **scanf()** y otra con la macro **getchar()**. Puedes utilizar cualquiera de las dos. Te sugerimos que pruebes el programa con una de las siguientes frases, que se leen igual de derecha a izquierda y de izquierda a derecha (llamadas palíndromos): "dabale arroz a la zorra el abad"; "a ti no bonita". Si utilizas la macro **getchar()** guarda el programa con el nombre **frase.c** y si utilizas **scanf()** guárdalo como **frase2.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 

/* fichero frase.c */ 
```c

#include <stdio.h>
void main(void) {
  char c, frase[100];
  int i, n;
  printf("Introduce una frase de menos de 100 letras.\n");
  printf("Para finalizar pulsa ^Z:\n");
  i=0;
  while((c=getchar())!=EOF) {
    frase[i]=c;
    i++;
  }
  frase[i]='\0';
  printf("\n");
  for (n=i; n>=0; n--)
  putchar(frase[n]);
  printf("\n");
}

/* fichero frase2.c */
#include <stdio.h>
#include <string.h>
void main(void) {
  char frase[100];
  int i, n;
  printf("Introduce una frase de menos de 100 letras.\n");
  printf("Para finalizar pulsa Intro:\n");
  i=0;
  scanf(" %[^\n]", frase);
  printf("\n");
  for (n=strlen(frase)-1; n>=0; n--)
    putchar(frase[n]);
  printf("\n");
}
```

####  Comentario 

En este caso, la lectura del array se realiza mediante un bucle while cuya condición de ejecución es la de encontrar un carácter distinto del carácter fin de fichero (EOF). Cuando en vez de leer la frase desde un fichero, ésta se introduce desde teclado, el carácter equivalente al EOF es control-z, que también se suele denotar como ^z. Una solución más sencilla a este ejercicio consiste en sustituir la línea scanf(" %s", palabra); del programa alreves.c por scanf(" %[^\n]", frase); El fichero frase2.c muestra esta nueva versión del programa. Una vez almacenada la frase en el array, se procede a escribirla al revés de la misma forma que se hacía en el programa anterior. En este caso se ha utilizado la macro de librería putchar(c); en lugar de printf(), de modo que la frase se escribe carácter a carácter con dicha macro.