---
title: "Losas de tres colores"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['revisar', 'sin_matlab']
---


# Losas de tres colores

##  Enunciado

A un albañil le encargan hacer un suelo poniendo losas de tres colores. Realizar un algoritmo que le permita al albañil conocer cómo quiere el cliente el suelo teniendo en cuenta que: 

  * Se debe utilizar una matriz de NxM losas para representar dicho suelo. 
  * Los colores de las losas se representan con números, así el 1: Azul, el 2: Rojo, el 3: Amarillo. 

El programa se dividirá en los siguientes apartados: 

  1. Subalgoritmo que pida al usuario un color y si es válido lo devuelva y si no devuelva -1. 
  2. Subalgoritmo que rellene la matriz de losas pidiendo los colores utilizando el subalgortmo del apartado a. 
  3. Subalgoritmo al que se le de un color de entrada y devuelva el número de losas de ese color. 
  4. Subalgoritmo que calcule el precio del suelo. Para ello le pedirá al usuario el precio para las losas de cada color (utilizar el subalgoritmo anterior). 
  5. Algoritmo principal que tendrá que rellenar la matriz de colores, y mostrar al usuario el precio final del suelo. 

  

##  Soluciones 

###  Diseño en Pseudocódigo

####  Subalgoritmo 1
```text


FUNCION Lee_color():ENTERO
ENTRADAS:
  (* Se pedirá por teclado *)
SALIDAS:
  c: ENTERO (* valdrá 1,2,3 o devolvera -1 *)
VARIABLES:
  (* No son necesarias *)
INICIO
  ESCRIBIR "Introduce color"
  LEER c
  SI c<1 O c>3
     c <-- -1
  FIN_SI
  DEVOLVER c
FIN

```
####  Subalgoritmo 2
```text


PROCEDIMIENTO Rellena_suelo(VAR suelo, n, m)
ENTRADAS:
  n: ENTERO   (* Número de filas de la matriz *)                 
  m: ENTERO   (* Número de columnas de la matriz *)
SALIDAS:
  suelo: ARRAY(n,m) DE ENTEROS (* Matriz donde se almacenan los colores de las losas *) 
VARIABLES:
  i,j: ENTEROS
INICIO
  PARA i=1 HASTA n HACER
    PARA j=1 HASTA m HACER
       REPETIR
          ESCRIBIR "Losa (", i, ",", j, "):"
          c=Lee_color()
       HASTA c<>-1
       suelo(i,j) <-- c
    FIN_PARA
  FIN_PARA
FIN

```
####  Subalgoritmo 3
```text


FUNCION Cuenta_losas(suelo, n, m, color): ENTERO
ENTRADAS:
  suelo: ARRAY(n,m) DE ENTEROS  (* Array con información de las baldosas *)
  n, m:  ENTEROS    (* Número de filas y columnas del array suelo *)
  color: ENTERO     (* Color de las baldosas que se van a contar *)
SALIDAS:
  cont: ENTERO (* Número de baldosas del color dado *)
VARIABLES:
  i, j: ENTEROS
INICIO
  cont<--0
  PARA i<--1 HASTA n HACER
    PARA j<--1 HASTA m HACER
      SI suelo(i,j)=color ENTONCES
        cont=cont+1
      FIN_SI
    FIN_PARA
  FIN_PARA
  DEVOLVER cont
FIN

```
####  Subalgoritmo 4
```text


FUNCION Precio_suelo(suelo, n, m):REAL
ENTRADAS:
  suelo: ARRAY(n,m) DE ENTEROS (* Array con información de las baldosas *)
  n, m:  ENTEROS      (* Número de filas y columnas del array suelo *)
SALIDAS:
  precio: REAL  (* Precio del suelo según la distribución de losas dada *)
VARIABLES:
  pr_color: ARRAY(3) DE REALES (* Precio de las losas de colores *)
  i, j, color: ENTERO
  suma: REAL
INICIO
  (* Leer precios de las losas *)
  PARA i<--1 HASTA 3 HACER
    ESCRIBIR "Introduzca el precio de la losa de color", i, ":"
    LEER pr_color(i)
  FIN_PARA
 
  (*Calcular precio del suelo *)
  suma<--0
  PARA i<--1 HASTA n HACER
    PARA j<--1 HASTA m HACER
      color=suelo(i,j)
      suma = suma + pr_color( color )
    FIN_PARA
  FIN_PARA
  DEVOLVER suma
FIN

```
####  Algoritmo principal

![Icono de revisar](images/4/44/Icono_revisar.png)

**Este ejercicio no está revisado y puede contener errores.**  
Cuando el ejercicio esté corregido, no aparecerá este mensaje. 
```text


ALGORITMO LosasDeTresColores
ENTRADAS:
  (* ... *)
SALIDAS:
  (* ... *)
VARIABLES:
  (* ... *)
INICIO
  (* ... *)
FIN
```