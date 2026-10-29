---
title: "Preguntas indiscretas"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
---

# Preguntas indiscretas

##  Enunciado 

En este programa vas a utilizar la función scanf() con distintos tipos de variables. De paso podrás contestar a algunas preguntas indiscretas, pero de indudable interés estadístico y social. El siguiente programa debe ser almacenado en un fichero llamado **mascota.c**. Si tu mascota favorita es una boa, una ardilla o una gacela, tendrás que cambiar el artículo "un" por "una", para respetar la concordancia. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero mascota.c */
#include <stdio.h>
void main(void)
{
 int edad;
 float sueldo;
 char cachorro[30];
 printf("Confiesa tu edad, sueldo y mascota favorita.\n");
 scanf("%d %f",&edad, &sueldo);
 scanf("%s", cachorro);
 printf("%d %.0f pts. %s\n",edad, sueldo, cachorro);
 printf("Un %s!!", cachorro);
 printf(" Como te puede gustar un %s?\n", cachorro);
}
```

####  Comentario 

En la función scanf(), se incluye el operador dirección (&) delante de las variables escalares para pasar a la función las direcciones de dichas variables (paso de argumentos por referencia). De esta forma la función scanf() puede depositar en las direcciones de memoria correctas los valores que lee desde teclado. Recordemos que para leer cadenas de caracteres basta poner el nombre de la cadena, que de por sí ya es una dirección. 

###  Solucion en Pseudocódigo
```text
ALGORITMO mascota
ENTRADAS
   edad: ENTERO
   sueldo: REAL
   cachorro: CADENA DE CARACTERES
SALIDAS
   _(No tiene salidas)_
VARIABLES
   _(No tiene variables)_
INICIO      
    
  ESCRIBIR "Confiesa tu edad, sueldo y mascota favorita."
  ESCRIBIR **SaltoDeLinea**
  LEER edad, sueldo
  LEER cachorro
  ESCRIBIR edad, sueldo, cachorro
  ESCRIBIR **SaltoDeLinea**
  ESCRIBIR "Un ", cachorro, "!!!!"
  ESCRIBIR "¿Como te puede gustar un ", cachorro, "?"
  ESCRIBIR **SaltoDeLinea**
  
FIN
```

####  Comentario 

Suponemos que la orden `LEER` permite leer desde el dispositivo de entrada una cadena de caracteres.