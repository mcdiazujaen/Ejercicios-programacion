---
title: "Leer una palabra y escribirla al reves"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['análisis', 'comentario', 'enunciado']
---

# Leer una palabra y escribirla al reves

##  Enunciado 

Para leer una palabra, contar las letras y escribirla al revés, lo primero que hay que hacer es pedir la palabra y almacenarla. Una vez que tenemos la palabra en un array, para contar el número de letras se chequea letra por letra (bucle while) sumando 1 cada vez. Este bucle finaliza cuando el carácter leído es el carácter '\0' que indica el final de la palabra. Este carácter, como ya se ha dicho antes, es introducido por la función `scanf( )` de manera automática. Para escribir la palabra al revés, basta con leerla empleando un bucle que cuente hacia atrás. Guarda este programa como **alreves.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada del Ejercicio: 
```c

/* fichero alreves.c */
/* Este programa lee una palabra y la escribe al revés */
#include <stdio.h>
void main (void) {
  palabra[21];
  int i;
  printf("Teclea una palabra de menos de 20 letras:\n");
  scanf("%s", palabra);
  i=0;
  while (palabra[i++]!='\0')
  ;
  printf("%s tiene %d letras.\n", palabra, i-1);
  printf("%s escrita al reves es: ", palabra);
  while (i>0)
    printf("%c", palabra[--i]);
  printf("\n");
}
```

####  Comentario 

La forma de almacenar el array leyéndolo del teclado es mediante la función scanf(). Luego, mediante un bucle while se determina el número de letras. La forma de chequear la condición de final del bucle es por reconocimiento del carácter '\0' que tienen todas las cadenas de caracteres al final. El contador incluye el carácter de fin de la cadena. La cadena se podría haber rellenado de otra manera, como se verá en el Ejercicio siguiente. También el número de caracteres de la cadena se puede determinar mediante otra forma: llamando a la función de libreria strlen(char*). Una vez que conocemos el número de caracteres de la cadena, se puede escribir el array al revés mediante un bucle con un contador decreciente. Conviene utilizar el operador --i para que decrezca antes de ser utilizado. 

###  Soucion en Pseudocódigo
```text
ALGORITMO AlReves
ENTRADAS:
    palabra:ARRAY (0...20)DE CARACTERES _(Palabra que vamos a mostrar al revés, terminada en punto)_
SALIDAS:
    _(El contenido de**palabra** mostrado al revés)_
VARIABLES:
    i: ENTERO
INICIO
    _(Leer la palabra caracter a caracter hasta que se introduzca un punto)_
    ESCRIBIR "Teclea una palabra de menos de 20 letras: "
    i <-- -1
    REPETIR
       i <--i+1
       LEER palabra(i)
    MIENTRAS palabra(i)<>'.' HACER
 
    _(Mostrar el número de letras de la palabra)_
    ESCRIBIR palabra, "tiene", i-1, "letras"

    _(Mostrar la palabra al revés)_
    ESCRIBIR palabra, "escrita al revés es: "

    MIENTRAS i>0 HACER
       ESCRIBIR palabra(i)
       i <-- i-1
    FIN_MIENTRAS
                    
FIN
```

####  Comentario 

En en lenguaje C las cadenas de caracteres terminan con el carácter especial `'\0'`. Debido a que en el pseudocódigo hemos leído la cadena de caracteres como un `ARRAY DE CARACTERES` se ha modificado la solución para que el final de la palabra introducida quede marcada por un punto (`.`) en lugar de por el carácter especial `'\0'`.