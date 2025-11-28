---
title: "Suma de los cuadrados de los 100 primeros números enteros"
date: 2024-01-01
draft: false
languages: ['c']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---


# Suma de los cuadrados de los 100 primeros números enteros

##  Enunciado 

Diseñar un algoritmo para imprimir la suma de los cuadrados de los 100 primeros números enteros. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text


  ALGORITMO suma100
  ENTRADAS: 
    (* No hay, porque cogemos directamente los primeros 100 números enteros *)
  SALIDAS: 
    suma: ENTERO
  VARIABLES: 
    i: ENTERO
  INICIO
    suma <-- 0
    PARA i <-- 1 HASTA  100 CON INCREMENTO DE 1 HACER
      suma <-- suma+(i*i)
    FIN_PARA
    ESCRIBIR "La suma vale:", suma 
  FIN

```
###  Solución en C
```c


  #include <stdio.h>
  #include <stdlib.h>
  int main (void){
    /*ENTRADAS: no tiene.*/
    /*SALIDAS*/
    int suma;
    /*VARIABLES*/
    int i;
    /*INICIO*/
    suma=0;
    for(i=1;i<=100; i++){
                    suma=suma+(i*i);
    }
    printf("La suma es %i \n",suma);
  }
```