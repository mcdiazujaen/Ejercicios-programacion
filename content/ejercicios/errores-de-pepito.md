---
title: "Errores de pepito"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['Sin C', 'Sin Matlab']
---

# Errores de pepito

##  Enunciado 

Pepito esta descontento con su rendimiento en la clase de fundamentos de informática. En su primer programa cometió un error, en el segundo cometió dos, en el tercero, cuatro, y asi sucesivamente. Resulta que siempre comete el doble de errores en cada nuevo programa que hace. Las clases duran trece semanas y deben realizar dos problemas por semana. Diseñar un algoritmo que calcule el número de errores que Pepito debe esperar cometer en su programa principal final, si se mantiene su rendimiento. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text
 ALGORITMO ErroresPepito
 ENTRADAS:
    _(Ninguna, ya el el número de semanas, errores e incremento de errores es fijo)_
 SALIDAS:
    _(Número total de errores que cometerá en el último ejercicio)_
 VARIABLES:
    errores: ENTERO
    i: ENTERO
 INICIO
    _(Inicializar con los errores de la primera semana)_
    errores <-- 2

    _(Simular el paso de las semanas)_
    PARA i <-- 2 HASTA 13 HACER
       errores <-- errores*2  _(errores en el primer problema de la semana)_
       errores <-- errores*2  _(errores en el segundo problema de la semana)_
    FIN_PARA

    ESCRIBIR("Pepito cometerá ", errores," en su programa final")
 FIN
```