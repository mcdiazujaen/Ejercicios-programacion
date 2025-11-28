---
title: "Sumar vectores y buscar el máximo"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
---


# Sumar vectores y buscar el máximo

##  Enunciado 

Diseñar un algoritmo que lea por teclado dos vectores de números enteros del mismo tamaño, sume las parejas de números que ocupan la misma posición en los dos vectores y los almacene el resultado en otro vector suma. Una vez realizada esta operación el algoritmo deberá devolver el valor y la posición del número mayor dentro del vector suma, si existieran dos o más números mayores iguales el algoritmo devolverá la posición del primero de ellos. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text


ALGORITMO SumarVectoresYMaximo
ENTRADAS:
  v1: ARRAY DE ENTEROS  _(Primer vector)_
  v2: ARRAY DE ENTEROS  _(Segundo vector)_
  tama:   ENTERO        _(Número de elementos de cada vector)_
SALIDAS:
  pos: ENTERO    _(posición de primer valor máximo de la suma de los vectores)_
  max: ENTERO    _(primer valor máximo de la suma de los vectores)_
VARIABLES:
  suma: ARRAY DE ENTEROS  _(Vector que contendrá la suma de v1 y v2)_
  cont: ENTERO
INICIO
  _(Leer vectores y calcular la suma)_
  ESCRIBIR "Introduzca el número de elementos de los vectores:"
  LEER tama
  PARA cont <- 1 HASTA tama HACER 
     ESCRIBIR "Introduzca el elemento ", cont, "del vector 1:"
     LEER v1(cont)
     ESCRIBIR "Introduzca el elemento ", cont, "del vector 2:"
     LEER v2(cont)

     suma(cont) <- v1(cont) + v2(cont)
  FIN_PARA

  _(Encontrar el mayor y su posición)_
  pos <- 1         _(Consideramos el primer elemento como mayor)_
  max <- suma(1)
  PARA cont <- 1 HASTA tama HACER 
     SI max < suma(cont) ENTONCES
        max <- suma(cont)
        pos <- cont
     FIN_SI
  FIN_PARA

  _(Mostrar el mayor y su posición)_
  ESCRIBIR "La mayor de las sumas es:", max
  ESCRIBIR "Y está en la posición:", pos
FIN
```