---
title: "Limite peso"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_c', 'sin_matlab']
---

# Limite peso

##  Enunciado 

Los reglamentos de pesca imponen un limite a la cantidad total permitida de kilos en un dia de pesca. Se supone que se planea llevar un computador portátil y se necesita un programa que indique cuando se ha excedido dicho limite. Diseñar un Algoritmo que primero lea el limite diario en kg y que luego lea los valores de entrada uno tras otro (corresponderá a los pesos individuales de las presas pescadas en el orden en que se obtienen) e imprima un mensaje en el momento en que el limite haya sido excedido. Un peso de 0 indica el fin de los datos y, despues de que cada pescado haya sido registrado, el algoritmo deberá imprimir el peso total que se lleva hasta ese momento. 

##  Soluciones 

###  Diseño en Pseudocódigo
```text
ALGORITMO Pesca
ENTRADAS:
   limite:REAL (* limite en kg del peso de toda la pesca del día *)
   peso:REAL   (* peso en kg de una presa pescada *)
SALIDAS:
   total:REAL  (* se refiere al peso total de lo pesado *)
VARIABLES:
INICIO
   ESCRIBIR "Introduzca el límite en Kg de pesca del día:"
   LEER limite
 
   total=0
   REPETIR
       ESCRIBIR "Introduce el peso en Kg de la presa pescada:"
       LEER peso
       total=total+peso
       ESCRIBIR "Total: ",total
   HASTA (peso=0) O (total>=limite)
 
   SI total>=limite ENTONCES
      ESCRIBIR "Límite superado"
   FIN_SI
FIN
```