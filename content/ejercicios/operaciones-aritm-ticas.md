---
title: "Operaciones aritméticas"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['Sin Matlab']
---

# Operaciones aritméticas

##  Enunciado 

Diseñar un algoritmo que lea dos valores reales y nos muestre los resultados de sumar, restar, dividir y multiplicar dichos números. 

##  Soluciones 

###  Pseudocódigo por mcdiaz 
```text
ALGORITMO Operaciones
ENTRADAS:
	i, j: REAL;           _(Valores sobre los que se realizan las operaciones aritméticas)_
SALIDAS:
	suma: REAL;           _(Resultado de sumar “i” mas “j”)_
	resta: REAL;          _(Resultado de restar “i” menos “j”)_ 
	division: REAL;       _(Resultado de dividir “i” entre “j”)_ 
	multiplicacion: REAL; _(Resultado de multiplicar “i” por “j”)_
VARIABLES: 

INICIO
	ESCRIBIR “Introduzca el primer valor: ”
	LEER i
	ESCRIBIR “Introduzca el segundo valor: ”
	LEER j
	
	suma <- i + j
	resta <- i - j
	division <- i / j
	multiplicacion <- i * j
	
	ESCRIBIR i, “ + ”, j, “ = ”, suma
	ESCRIBIR i, “ - ”, j, “ = ”, resta
	ESCRIBIR i, “ / ”, j, “ = ”, division
	ESCRIBIR i, “ * ”, j, “ = ”, multiplicacion
FIN
```

###  Solución en C 
```c

#include <stdio.h>
#include <stdlib.h>
                                                                              
int main(void){
   //ENTRADAS
   float a;
   float b;
   //SALIDAS
   float suma, resta, producto, cociente; 
                                                                    
   //Leer entradas
   printf("Introduzca un entero:");
   scanf("%f",&a);
   printf("Introduzca un real: ");
   scanf("%f",&b);
                                                                     
   //Realizar operaciones
   suma    = a+b;
   resta   = a-b;
   cociente= a/b;
   producto= a*b;
                                                                                  
   //Mostrar salidas
   printf("La suma es: %f + %f = %f\n",a,b,suma);
   printf("La resta de los numeros real y entero es: %f - %f = %f\n",a,b, resta);
   printf("El producto de ambos numeros es: %f * %f = %f\n",a,b, producto);
   printf("El cociente entre estos dos numeros es: %f /%f = %f\n",a,b, cociente);
}
```