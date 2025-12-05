---
title: "Ordenación de la burbuja"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---

# Ordenación de la burbuja

##  Enunciado 

ORDENAR UN CONJUNTO DE NÚMEROS ENTEROS. 

El siguiente programa, al que llamarás **ordena.c** , ordena un conjunto de números enteros almacenados en un vector, utilizando el siguiente algoritmo (método de la burbuja): se van recorriendo una a una todas las posiciones del vector, desde la primera hasta la penúltima. Estando en cada una de estas posiciones, se recorren, a su vez, todas las posiciones siguientes y se compara su valor con el de la posición actual. Si se encuentra un valor menor se intercambia con el de esta posición. 

Para implementar este algoritmo son necesarios dos bucles: el primero, bucle i, recorre el vector desde la posición i=0 hasta i=SIZE-1. El segundo bucle, bucle j, recorre el vector desde la posición j=i+1 hasta el final. Para que quede más claro, vamos a ver con un ejemplo como funciona este algoritmo. Supongamos que queremos ordenar los siguientes cinco números: 7,3,5,1,4. Estos números se almacenarán en un vector de la siguiente manera: 

![imagen:burbuja1.JPG](images/8/82/Burbuja1.JPG)

Vamos a recorrer las posiciones del vector desde **i=0** hasta **i=3**. 

**i = 0** {**7** 3 5 1 4} 

Recorremos el vector desde **j=1** hasta **j=4** y comparamos **vector [0]=7** con **vector [j]**. Si **vector [j] <vector [0]** intercambiamos los valores de posición. Vamos a ver cómo quedaría el vector inicial una vez que termina cada bucle **j**. 

**j = 1** {**3** **7** 5 1 4} Se intercambia 3 con 7 **j = 2** {**3** 7 **5** 1 4} No se intercambia 3 con 5 **j = 3** {**1** 7 5 **3** 4} Se intercambia 1 con 3 **j = 4** {**1** 7 5 3 **4**} No se intercambia 1 con 4 

**i = 1** {1 **7** 5 3 4} 

Recorremos el vector desde **j=2** hasta **j=4** y comparamos **vector [1]=7** con **vector [j]**. 

**j = 2** {1 **5** **7** 3 4} Se intercambia 5 con 7 **j = 3** {1 **3** 7 **5** 4} Se intercambia 3 con 5 **j = 4** {1 **3** 7 5 **4**} No se intercambia 3 con 4 

**i = 2** {1 3 **7** 5 4} 

**j = 3** {1 3 **5** **7** 4} Se intercambia 5 con 7 **j = 4** {1 3 **4** 7 **5**} Se intercambia 4 con 5 

**i = 3** {1 3 4 **7** 5} 

**j = 4** {1 3 4 **5** **7**} Se intercambia 5 con 7 ¡Números ordenados! 

Ya se ve que no es necesario que el bucle i llegue hasta el valor 4. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero ordena.c*/
/* Programa para ordenar un conjunto de números enteros*/
#include <stdio.h>
#define SIZE 7
void main(void) {
  int vector[SIZE];
  int j, i, temp;
  printf("Introduce los %d valores para ordenar:\n", SIZE);
  for(i=0; i<SIZE; i++) {
     printf("%d: ", i+1);
     scanf("%d", &vector[i]);
     printf("\n");
  }
  /* se aplica el algoritmo de la burbuja */
  for(i=0; i<(SIZE-1); i++) {
     for (j=i+1; j<SIZE; j++) {
        if(vector[j]<vector[i]) {
            temp=vector[j];
            vector[j]=vector[i];
            vector[i]=temp;
        }
     }
  }
  printf("El vector ordenado es:\n");
  for(i=0; i<SIZE ; i++) {
     printf("%d ", vector[i]);
  }
  printf("\n");
}
```

####  Comentario 

Para intercambiar entre sí los valores de dos variables no se pueden emplear las dos instrucciones siguientes: 
```text
**vector[j]=vector[i];** /* esta instrucción pone en la posición j el valor de la posición i, perdiéndose el valor de la posición j */

**vector[i]=vector[j];** /* esta instrucción pone en la posición i el valor de la posición j, pero no el original, que se ha perdido, sino el nuevo */
```

Por eso es necesaria una variable intermedia, que en este caso hemos llamado temp, que guarda temporalmente el valor de la posición **j**. Por esto se requieren tres instrucciones.