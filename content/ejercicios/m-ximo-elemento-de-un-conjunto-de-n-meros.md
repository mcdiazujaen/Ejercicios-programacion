---
title: "Máximo elemento de un conjunto de números"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Máximo elemento de un conjunto de números

##  Enunciado 

Este programa calcula el máximo entre un conjunto de números enteros. Para ello se sigue el siguiente algoritmo: se crea una variable llamada **max** , a la que se da inicialmente el valor de **conjunto[0]**. Luego se recorren paso a paso todos los elementos del vector, comparando el valor almacenado en la posición considerada del vector con el valor de la variable **max**. Si el valor de la posición considerada del vector es mayor que **max** , entonces se copia (se sustituye el valor) en la variable **max** este valor. De esta forma, una vez recorrido todo el vector, la variable **max** contendrá el máximo valor. Guarda este programa con el nombre **maximo.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero maximo.c */
/* Programa para calcular el máximo de un conjunto de números */
#include <stdio.h>
#define SIZE 5
void main(void) {
  int i, max, imax;
  int conjunto[SIZE];
  printf("Introduce %d valores:\n", SIZE);
  for (i=0; i<SIZE; i++) {
     printf("%d: ", i+1);
     scanf("%d", &conjunto[i] );
     printf("\n");
  }
  max=conjunto[0];
  imax=0;
  for (i=0; i<SIZE; i++) {
     if (conjunto[i]>max) {
          max=conjunto[i];
          imax=i;
       }
  }
  printf("\nEl maximo valor del conjunto es: %d.\n", max);
  printf("\ny esta en la posicion %d.\n", imax+1);
}

```
####  Comentario 

Este programa es muy sencillo, si se entiende el algoritmo. La variable `max` acabará siendo igual al elemento mayor del conjunto, e `imax` indicará la posición del máximo. 

###  Diseño en pseudocódigo
```text
ALGORITMO Maximo
ENTRADAS:
    conjunto: ARRAY (0...SIZE-1) DE ENTEROS  _(Elementos donde buscar el máximo)_
SALIDAS:
    max:  ENTERO  _(Valor del máximo)_
    imax: ENTERO  _(Posición del máximo)_
VARIABLES:
    i: ENTERO
CONSTANTES:
    SIZE=5
INICIO
    _(Pedir los valores al usuario)_            
    ESCRIBIR "Introduce ", SIZE, " valores: "
    PARA i<--0 HASTA SIZE-1 C.I +1 HACER
        ESCRIBIR i+1
        LEER conjunto(i)
    FIN_PARA
    
    _(Buscar el máximo)_
    max<--conjunto(0)
    imax<--0
    PARA i<--0 HASTA SIZE-1 C.I +1 HACER
       SI conjunto(i)>max ENTONCES
          max<--conjunto(i)
          imax<--i
       FIN_SI
    FIN_PARA
                         
    _(Mostrar los resultados)_
    ESCRIBIR "El maximo valor del conjunto es: ", max
    ESCRIBIR "y está en la posicion: ", imax+1
FIN
```