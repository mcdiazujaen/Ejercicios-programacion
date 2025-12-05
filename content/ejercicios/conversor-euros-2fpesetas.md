---
title: "Conversor euros/pesetas"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Conversor euros/pesetas

##  Enunciado 

Diseñar un algoritmo que lea un valor en euros y lo convierta a pesetas (1 euro = 166,386 ptas). 

##  Soluciones 

###  Pseudocódigo 
```text

ALGORITMO Conversor
CONSTANTES:
	UN_EURO=166.386
ENTRADAS:
	euros: REAL; _Valor en euros que queremos convertir_
SALIDAS:
	pesetas: REAL; _Valor en pesetas de la cantidad introducida en euros_
VARIABLES:

INICIO
	ESCRIBIR “Introduzca la cantidad de euros a convertir: ”
	LEER euros

	pesetas <-- euros * UN_EURO

	ESCRIBIR euros, “euros son ”, pesetas, “pesetas.”
FIN

```
###  Programa en C 
```c

#include <stdio.h>
#include <stdlib.h>
#define UN_EURO 166.386

int main (void){
   //Entradas
   float euros;    /* Valor en euros que queremos cambiar */
   //Salidas
   float pesetas;  /* Valor en pesetas de la cantidad introducida en euros*/
   //Variables
   
   //Inicio
   printf("Introduzca la cantidad de euros a convertir: ");
   scanf("%f", &euros);
   
   pesetas=euros*UN_EURO;
   
   printf(" %f euros son %f pesetas \n", euros, pesetas); 
   
   system("PAUSE");   
}
```