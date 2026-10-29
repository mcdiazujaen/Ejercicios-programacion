---
title: "Conversación en C"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
tags: ['Sin Matlab']
---

# Conversación en C

##  Enunciado 

Si has realizado [el primer ejercicio en C](/ejercicios/el-primer-ejercicio-en-c/) seguro que te ha dejado con ganas de responder a la pregunta que aparece en la pantalla. Para ello es necesario utilizar la función scanf(). Esta función permite leer tanto números como cadenas de caracteres, pero cuando encuentra blancos, tabuladores o espacios en blanco, termina de leer. Crea el siguiente programa en un fichero llamado hola2.c. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio 
```c

 /* fichero hola2.c */
 /* Este programa saluda más personalmente */
 #include <stdio.h>
 void main(void) {
   char nombre[30];
   printf("Hola! Como te llamas?\n");
   scanf("%s", nombre);
   printf("Que tal estas, %s?\n", nombre);
 }
```

####  Comentario 

La sentencia char nombre[30], declara una variable llamada nombre que es una cadena de 30 caracteres (tipo char). Estos caracteres se numeran del 0 al 29, y deben incluir la marca de fin de cadena '\0'. Con la función scanf(), se lee lo que será el contenido de dicha cadena por medio del formato %s, que es propio de las cadenas de caracteres. Como la lectura se detiene al encontrar un blanco, un carácter nueva línea o un tabulador, por medio de este programa no se puede leer una frase completa, sino sólo una palabra. 

Observa que a la función scanf() hay que pasarle los argumentos por referencia. Como nombre es de por sí la dirección de nombre[0] no hace falta precederlo por el operador (&).