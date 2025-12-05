---
title: "Tabla de multiplicar"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---

# Tabla de multiplicar

##  Enunciado 

Te proponemos este programa que imprime los 21 primeros números y sus repectivos cuadrados de tres formas distintas. Para ejecutar de forma pausada el programa hemos introducido la función **getchar( )** que espera que pulses cualquier tecla para capturar el carácter correspondiente (en este caso no se hace nada con dicho carácter, que está disponible como valor de retorno; es un simple truco para que el ordenador espere hasta que pulsemos una tecla cualquiera) y continuar ejecutando el programa. Guarda el programa como **cuadrados.c**. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero cuadrados.c */
# include <stdio.h>
void main(void) {
  int num=1; 
  while (num<21) {
     printf("%10d %10d\n", num, num*num);
     num=num+1;
  }
  getchar();
  num=1;
  while (num<21) {
     printf("%10d %10d\n", num, num*num);
     num+=1;
  }
  getchar();
  num=1;
  while (num<21) {
     printf("%10d %10d\n", num, num*num);
     num++;
  }
}
```

####  Comentario 

En este programa las instrucciones: num=num+1, num+=1 y num++, las podrás utilizar de la forma que más te convenga, es decir, que la mayor o menor utilidad de una sobre otra se dará en la medida que quieras simplificar tus programas que realizarás más adelante. Como ya hemos dicho, la macro getchar() espera a que el usario teclee un valor cualquiera para continuar ejecutando el programa. Es una forma de esperar una señal del usario para continuar con la solución del programa. Se puede observar que si se pulza un carácter cualquiera seguido de un Intro, en realidad se han pulsado dos caracteres y el programa tiene suficiente para llegar hasta el final. Si se pulsa sólo el Intro hay que pulsarlo dos veces. 

###  Solucion en Pseudocódigo
```text
ALGORITMO cuadrados
ENTRADAS:
   _(No tiene entradas)_
SALIDAS:
   _(El cuadrado de los 21 primeros números)_
VARIABLES:
   num: ENTERO
INICIO
           
   num<--1
   MIENTRAS num<21 HACER
     ESCRIBIR  num, num*num
     ESCRIBIR SaltoDeLinea
     num<--num+1
   FIN_MIENTRAS
                 
   num<--1
   REPETIR    
     ESCRIBIR  num, num*num
     ESCRIBIR SaltoDeLinea
     num<--num+1
   HASTA num>=21
                 
   PARA num<--1 HASTA 20 HACER
     ESCRIBIR  num, num*num
     ESCRIBIR SaltoDeLinea
     num<--num+1
   FIN_PARA
                 
FIN
```

####  Comentario 

En pseudocódigo no existe las diferentes formas de realizar el incremento como en C. Por lo tanto, se han realizado 3 bucles distintos para mostrar 3 formas de calcular el cuadrado de los 20 primeros números enteros.