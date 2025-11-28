---
title: "Operación aritmetica"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---


# Operación aritmetica

##  Enunciado 

UNA PEQUEÑA OPERACIÓN ARITMÉTICA. 

Estarás pensando que C ha de servir para algo más que mantener una aburrida conversación con tu PC (¿verdadero y fiel amigo?). En el siguiente programa te presentamos un avance de las "complicadas" operaciones que puede realizar el lenguaje C. 

Escribe el programa y sálvalo como **marathon.c**. 

Compila el programa y ejecútalo; apuntando el resultado. Después modifica el programa sustituyendo 1760.0 por 1760 en la línea que calcula el número de kilómetros. Vuelve a compilar y a ejecutar. ¿Sale lo mismo que antes? ¿Qué ha podido pasar? 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio 
```c


/* fichero marathon.c */
/* Un marathon tiene 26 millas y 385 yardas. */
/* Una milla tiene 1760 yardas. */
/* Calcula la distancia del marathon en kilómetros. */
#include <stdio.h>
void main(void) {
  int millas, yardas;
  float kilometros;
  millas=26;
  yardas=385;
  kilometros=1.609*(millas+yardas/1760.0);
  printf("\nUn marathon tiene %f kilometros.\n\n", kilometros);
}


```
####  Comentario 

En C las constantes que incluyen un punto decimal son de tipo double. La variable yardas es de tipo int. Si en el denominador se pone sólo **1760** , el resultado de **yardas/1760** es entero y por tanto incorrecto. Basta poner **1760.0** para que yardas sea promovido a double y todas las operaciones aritméticas de esa sentencia se realicen con precision double.