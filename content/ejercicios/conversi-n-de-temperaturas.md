---
title: "Conversión de temperaturas"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
---

# Conversión de temperaturas

##  Enunciado 

Un departamento de climatología ha realizado recientemente su conversión al sistema métrico. Diseñar un algoritmo para realizar las siguientes conversiones: 

  * Leer la temperatura dada en la escala Celsius e imprimir en su equivalente Fahrenheit (la fórmula de conversión es “F=9/5 ºC+32”). 
  * Leer la cantidad de agua en pulgadas e imprimir su equivalente en milímetros (25.5 mm = 1 pulgada). 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text
 ALGORITMO SistemaMetrico
 ENTRADAS:
    grados_C: REAL    (* Temperatura en grados celsius *)
    pulgadas: REAL    (* Cantidad de agua en pulgadas *)
 SALIDAS:
    grados_F: REAL    (* Temperatura en grados Fahrenheit *)
    milimetros: REAL  (* Cantidad de agua en milimetros *)
 VARIABLES:
    (* No son necesarias *)
 INICIO
    ESCRIBIR "Introduzca una temperatura en grados Celsius: "
    LEER grados_C
    grados_F <-- ( 9 / 5 ) * grados_C + 32
    ESCRIBIR grados_C," grados Celsius = ", grados_F, " grados Fahrenheit."
 
    ESCRIBIR "Introduzca una cantidad de agua en pulgadas: "
    LEER pulgadas
    milimetros <-- pulgadas * 25.5
    ESCRIBIR pulgadas, " pulgadas = ", milimetros, " milímetros."
 FIN

```
###  Programa en C 
```c

 #include <stdio.h>
 #include <stdlib.h>
 int main (void){
    //ENTRADAS:
    float grados_C;     /* Temperatura en grado Celsius */
    float pulgadas;     /* Cantidad de agua en pulgadas */
    //SALIDAS:
    float grados_F;     /* Temperatura en grado Farenheit */
    float milimetros;   /* Cantidad de agua en milímetro  */
    //VARIABLES:
    //  No son necesarias.
 
    printf("Introduzca una temperatura en grados Celsius: ");
    scanf("%f", &grados_C);
    grados_F = (9.0/5.0)* grados_C + 32;
    printf("%.2f grados Celsius = %.2f grados Faherheit\n", grados_C, grados_F);
 
    printf("Introduzca una cantidad de agua en pulgadas: ");
    scanf("%f", &pulgadas);
    milimetros = pulgadas * 25.5;
    printf("%.2f pulgadas = %.2f milimetros\n", pulgadas, milimetros);
 
    system("PAUSE");
 }

```
###  Programa en Matlab 
```matlab

%Programa Conversión
%Descripción: Leer la temperatura dada en la escala Celsius e imprimir en su 
%   equivalente Fahrenheit. A continuación lee la cantidad de agua en 
%   pulgadas e imprime su equivalente en milímetros.
%Entradas: 
%   - Valores de temperatura en grados Celsius.
%   - Cantidad de agua en pulgadas.
%Salidas:
%   - Valores de temperatura en grados Fahrenheit.
%   - Cantidad de agua en milímetros.
%Variables:
%   cel,fah: REALES
%   aguaPulgadas,aguaMilimetros: REALES
 
% Convertir temperatura
cel=input('Introduce la temperatura en grados celsius:');
fah=((9/5)*cel)+32;
disp(['La temperatura transformada en grados Fahrenheit es:' num2str(fah)]);
 
% Convertir volumen de agua
aguaPulgadas=input('Introduzca el valor de agua en pulgadas:');
aguaMilimetros=aguaPulgadas*25.5;
disp(['El agua en milímetros es:' num2str(aguaMilimetros) 'mm']);
```