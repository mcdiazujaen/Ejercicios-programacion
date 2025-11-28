---
title: "Función sin argumentos"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'análisis']
---


# Función sin argumentos

##  Enunciado 

El siguiente programa calcula la diferencia en minutos entre dos horas distintas. La función **minutos()** acepta el tiempo que el usuario introduce en horas y minutos y lo convierte a minutos devolviendo este valor entero. La función presenta la particularidad de no tener argumentos. Guarda el programa como **tiempo.c**. 

Otra novedad de este programa es la existencia del carácter dos puntos (**:**) entre los dos especificadores de formato, **%d** y **%d** , de la instrucción **scanf()**. Esto hace que el usuario deba introducir los dos puntos entre los números que conforman el formato del tiempo. Estos números son capturados por la función mediante los especificadores **%d**. Los dos puntos sustituyen a los caracteres de espaciado tradicionales (espacio, tabulador, nueva línea). Así el usuario puede introducir el tiempo en el formato estándar de horas:minutos, utilizando los dos puntos para separarlos. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c


/* fichero tiempo.c */
/* calcula la diferencia entre dos horas distintas */
#include <stdio.h>
void main(void) {
  int minutos1, minutos2;
  int minutos(void);
  printf("Escribe la primera hora (formato 3:22): ");
  minutos1=minutos(); /* obtiene los minutos */
  printf("Escribe la segunda hora (posterior): ");
  minutos2=minutos(); /* obtiene los minutos*/
  printf("La diferencia es %d minutos.\n", minutos2-minutos1);
}
int minutos(void) {
  int horas, mins;
  scanf("%d:%d", &horas, &mins);
  return (horas*60+mins); 
}


```
###  Diseño en Pseudocódigo
```text


 FUNCION Minutos():ENTERO
 ENTRADAS:
    _(no tiene, las lee de teclado)_
 SALIDAS:
    _(no tiene, las muestra por pantalla)_
 VARIABLES:
    horas: ENTERO
    mins:  ENTERO
 INICIO
    LEER horas
    LEER mins
    DEVOLVER (horas*60)+mins
 FIN



 _(Programa Principal)_
              
 ALGORITMO tiempo
 ENTRADAS:
     _(Dos datos horarios dados con horas y minutos)_
 SALIDAS:
     _(Mensaje mostrando la diferencia entre las dos horas)_
 VARIABLES:
     minutos1:ENTERO
     minutos2:ENTERO
 INICIO
     ESCRIBIR "Escribe la primera hora (formato 3:22): "
     minutos1<--Minutos()
     ESCRIBIR "Escribe la segunda hora (posterior): "
     minutos2<--Minutos()
     ESCRIBIR "La diferencia es", minutos2-minutos1
 FIN
```