---
title: "Sopa de letras"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---

# Sopa de letras

##  Enunciado 

Se desea hacer un algoritmo para resolver si se encuentra o no una palabra en una sopa de letras. Para ello habrá que disponer de una matriz de _NxN_ dónde se encontrará la sopa de letras y además un vector de _M_ elementos dónde se encontrará la palabra a buscar. Las estructuras que se necesitan se muestran a continuación: 

  * **sopa** : Array bidimensional de caracteres 

```text
     1   2   3  ... ... ...  n
   +---------------------------
 1 | A   Q   A   Z   P   V   A 
 2 | Z   I   X   N   S   L   B
 3 | X   A   R   T   O   J   F
...| D   I   R   A   R   A   T
...| R   D   Q   Ñ   A   Y   I
...| E   T   T   J   G   N   L
...| D   R   A   H   U   B   X
...| I   N   O   T   A   R   P
...| L   R   W   O   O   Y   T
 n | O   S   N   A   V   N   I

```
  * **buscar** : Array de caracteres 

```text
 1   2   3  ...  m
-------------------
 R   A   T   O   N

```
Para resolver este problema habrá que realizar los siguientes subalgoritmos: 

###  Apartado a 

Realizar un subalgoritmo que lea un array de caracteres. En el subalgoritmo, el usuario irá insertando caracteres y cuando introduzca un punto ('.') se terminará de leer. El resultado será un array como el de la figura (_array buscar_), donde se encuentra una palabra, y un número indicando el tamaño de dicha palabra. El punto no se considera para el tamaño. 

###  Apartado b 

Realizar un subalgoritmo que compruebe si la palabra se encuentra en horizontal. Habrá que comprobar si se encuentra leyendo de izquierda a derecha. Se dará como entrada un array bidimensional con la sopa de letras, su tamaño, el array con la palabra a buscar y el tamaño de la palabra. Si se encuentra la palabra se devolverá _Verdadero_ y sino se devolverá _Falso_. 

###  Apartado c 

Termina de rellenar el código del algoritmo principal que se indica a continuación de forma que se pida al usuario jugar tantas veces como quiera. Utiliza los subalgoritmos que has generado en los apartados anteriores. 
```text
ALGORITMO SopaDeLetras
ENTRADAS:
  sopa: ARRAY (1..100,1..100) DE CARACTERES 
  n: ENTERO  (* tamaño de la sopa *)
  buscar: ARRAY (1..100) DE CARACTERES
  m: ENTERO  (* tamaño de la palabra a buscar *)
SALIDAS:
  (* mensaje de si se encuentra o no las palabras buscadas *)
VARIABLES:
  op: CARACTER  (* valor para saber si deseamos continuar jugando *)
INICIO
  LeerSopa (sopa, n)  (* Aquí ya hemos inicializado una matriz sopa cualquiera *)
  REPETIR
     ESCRIBIR "Introduzca palabra a buscar:"
 
     //PON TU CÓDIGO AQUÍ PARA leer la palabra que queremos buscar
 
     //PON TU CÓDIGO AQUÍ PARA buscar si está la palabra en la sopa en horizontal e indicar por mensaje si esta o no       
 
     ESCRIBIR "¿Desea seguir jugando? (S/N)"
     LEER op
  HASTA ( (*PON TU CÓDIGO AQUÍ*) )
FIN

```
##  Soluciones