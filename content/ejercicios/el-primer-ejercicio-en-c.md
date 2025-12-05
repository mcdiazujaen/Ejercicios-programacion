---
title: "El primer ejercicio en C"
date: 2024-01-01
draft: false
languages: ['pascal', 'pseudocódigo']
professors: ['lperez']
categories: ['enunciado', 'comentario']
tags: ['sin_c', 'sin_matlab']
---

# El primer ejercicio en C

##  Enunciado 

EL PRIMER PROGRAMA. Para que tu debut como programador en C sea todo un éxito, te hemos preparado un sencillo programa de bienvenida. Tecléalo en un fichero al que puedes poner por nombre hola.c. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio 
```c

 /* fichero hola.c */
 /* Este programa saluda desenfadadamente. */
 #include <stdio.h>
 void main(void) {
     printf("Hola! Que tal estas, futuro programador?\n");
 }

```
####  Comentario 

La primera línea de este programa es un comentario, y es ignorado por el compilador. 

La directiva #include permite utilizar la librería stdio, indispensable para diferentes instrucciones de entrada/salida del lenguaje C. 

El fichero stdio.h contiene las declaraciones de las funciones de entrada/salida, así como definiciones de constantes simbólicas y algunas otras definiciones de utilidad. La palabra void es opcional; indica que la función main() no tiene valor de retorno ni argumentos.