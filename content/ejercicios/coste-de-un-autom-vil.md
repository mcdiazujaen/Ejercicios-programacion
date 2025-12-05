---
title: "Coste de un automóvil"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Coste de un automóvil

##  Enunciado 

El coste de un automóvil nuevo para un comprador es la suma total del coste del vehículo, del porcentaje de la ganancia del vendedor y de los impuestos locales o estatales aplicables (sobre el precio de venta). Suponer una ganancia del vendedor del 12% en todas las unidades y un impuesto del 6% y diseñar un algoritmo para leer el coste total del automóvil e imprimir el coste para el consumidor. 

##  Soluciones 

###  Pseudocódigo 
```text

ALGORITMO ComprarAuto
ENTRADAS:
	coste_total: REAL; Coste del vehículo en euros
SALIDAS:
	coste_comprador: REAL; Coste del vehículo nuevo para el comprador (en euros) 
VARIABLES:
	ganancia: REAL
	impuestos: REAL

INICIO
	ESCRIBIR “Introduzca el coste total del vehículo: ”
	LEER coste_total
	
	ganancia <-- coste_total * 0.12
	impuestos <-- coste_total * 0.06
	coste_comprador <-- coste_total + ganancia + impuestos
	
	ESCRIBIR “El coste del vehículo para el comprador es de ”, coste_comprador, “ euros.”
FIN

```
###  Programa en C 
```c

 #include <stdio.h>
 #include<stdlib.h>

 int main (void){
   /*ENTRADAS*/
    float coste_total; //Coste del vehículo en euros
   /*SALIDAS*/
    float coste_comprador; //Coste del vehículo nuevo para el comprador (en euros) 
   /*VARIABLES*/
    float ganancia;
    float impuestos;

   /*INICO*/
    printf("Introduzca el coste total del vehículo: ");
    scanf("%f",&coste_total);
    ganancia=coste_total*0.12;
    impuestos=coste_total*0.06;
    coste_comprador=coste_total+ganancia+impuestos;
    printf("El coste del vehículo para el comprador es de %f euros.",coste_comprador);

    system("PAUSE");
}
```