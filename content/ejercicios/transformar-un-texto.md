---
title: "Transformar un texto"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_matlab', 'sin_pseudocódigo']
---

# Transformar un texto

##  Enunciado 

El siguiente programa lee un texto cualquiera y lo escribe al revés transformando las mayúsculas en minúsculas y viceversa. Para esto último basta tener en cuenta que la diferencia entre el código ASCII de una letra mayúscula y el de la misma letra en minúscula es la misma para todas las letras del abecedario. Hay que tener cuidado para no modificar los caracteres de estilo tales como espacio en blanco (' '), tabulador ('\t'), coma (,), ... 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

/* fichero inverso.c */
/* Este programa convierte las mayusculas en minusculas y viceversa */
/* y escribe el texto cambiado al reves */
#include <stdio.h>
void main(void) {
  int ch;
  char texto[101]; /* limite de caracteres del texto */
  int i, n, dif;
  dif='a'-'A';
  printf("Introduce un texto de no mas de 100 caracteres.\n");
  printf("Pulsa ^Z para finalizar:\n");
  i=0;
  while ((ch=getchar())!=EOF) {
    if ((ch>='a')&&(ch<='z')) /* es minúscula */
          ch-=dif;
      else if ((ch>='A')&&(ch<='Z')) /* es mayúscula */
               ch+=dif;
    texto[i++]=ch;
  }
  texto[i]='\0';
  for (n=i; n>=0; n--)
     printf("%c", texto[n]);
  printf("\n");
}
```

####  Comentario 

Como ya se ha visto, en C se utiliza la constante simbólica **EOF** para indicar el final de un fichero (esta constante está definida en el fichero **stdio.h**). Su valor numérico es (−1) y equivale también a <control>z (^z) cuando se introduce el texto desde teclado. 

En este programa se utiliza la forma de introducir la cadena como ya se hizo en el programa [**frase.c**](/ejercicios/leer-una-frase-y-escribirla-al-reves/). Para cambiar las mayúsculas a minúsculas y viceversa hay que chequear el carácter y ver si es alfabético o no. Una vez que se sabe que es un carácter alfabético, hay que tener en cuenta que el código ASCII correspondiente a la "A" es el 65 y el correpondiente a la "a" es el 97, es decir, la diferencia entre ambos es 32. La misma diferencia se mantiene para otras letras entre la minúscula y la mayúscula. En lugar de teclear el texto cada vez, puedes crear un fichero de texto llamado texto1.txt y redireccionar la entrada del programa con el operador (<) si ejecutas el programa desde la línea de comandos, en la forma: **> inverso < texto1.txt**.