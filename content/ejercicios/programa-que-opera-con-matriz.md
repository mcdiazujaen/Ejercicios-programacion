---
title: "Programa que opera con matriz"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---


# Programa que opera con matriz

##  Enunciado 

Suponemos una matriz MxN elementos, la cual se ha rellenado con reales exceptuando la última fila y la última columna. Realizar un programa en el que se ofrezca un menú con las siguientes opciones: 

  1. Dados los índices de dos filas intercambiar dichas filas en la matriz. 
  2. Dado un entero que representa un código de operación (0 suma, 1 producto), realizar la operación que representa con cada fila de la matriz, poniendo el resultado en la última columna. Igual para las columnas poniendo el resultado en la última fila. 
  3. En el elemento de la última fila y la última columna poner el resultado de sumar todos los elementos de la matriz. 

##  Soluciones 

###  Pseudocódigo 

####  Apartado 1 
```text


Procedimiento IntercambiaFilas (Var A, m, n, fila1, fila2)
Entradas:
   A: Array (1..1000,1..1000) de Reales  _(matriz que queremos modificar)_
   m, n: Enteros                         _(número de filas y columnas de la matriz )_
   fila1, fila2: Enteros                 _(filas que queremos intercambiar)_
Salidas:
   A: Array (1..1000,1..1000) de Reales  _(matriz modificada)_
Variables:
   aux: Real
   i, j: Enteros
Inicio
   Para i <--1 hasta m hacer
        aux <-- A(fila1,i)
        A(fila1,i) <-- A(fila2,i)
        A(fila2,i) <-- aux
   Fin_Para
Fin


```
####  Apartado 2 
```text


Procedimiento SumaProducto (Var A, m, n, ope)
Entradas:
   A: Array (1..1000,1..1000) de Reales  _(Matriz que solo rellenamos hasta m-1 y n-1)_
   m, n: Enteros                         _(número de filas y columnas)_
   ope: Entero                           _(operador, 0 para sumar y 1 para multiplicar)_
Salidas:
   A: Array (1..1000,1..1000) de Reales  _(matriz con última fila y columna rellena según la operación dada)_
Variables:
   i, j: Enteros
   aux: Real 
Inicio
   _(Sumar filas y columnas)_
   Si ( ope = 0 ) Entonces 
      _(Sumar filas)_
      Para i <-- 1 hasta ( m – 1 ) hacer
         aux <-- 0
         Para j <-- 1 hasta ( n – 1 ) hacer
            aux <-- aux + A(i,j)
         Fin_Para
         A(i,n) <-- aux
      Fin_Para
      _(Sumar columnas)_
      Para i <-- 1 hasta ( n – 1 ) hacer
         aux <-- 0
         Para j <-- 1 hasta ( m – 1 ) hacer
            aux <-- aux + A(j,i)
         Fin_Para
         A(m,i) <-- aux
      Fin_Para
   Fin_Si
   _(Multiplicar filas y columnas)_
   Si ( ope = 1 ) Entonces 
     _(Multiplicar filas)_
      Para i <-- 1 hasta ( m – 1 ) hacer
         aux <-- 1
         Para j <-- 1 hasta ( n – 1 ) hacer
            aux <-- aux * A(i,j)
         Fin_Para
         A(i,n) <-- aux
      Fin_Para
     _(Multiplicar columnas)_
      Para i <-- 1 hasta ( n – 1 ) hacer
         aux <-- 1
         Para j <-- 1 hasta ( m – 1 ) hacer
            aux <-- aux * A(j,i)
         Fin_Para
         A(m,i) <-- aux
      Fin_Para
   Fin_Si
Fin


```
####  Apartado 3 
```text


Procedimiento SumaUltimaFilaColumna (Var A, m, n)
Entradas:
   A: Array (1..1000,1..1000) de Reales  _(matriz bidimensional)_
   m, n: Enteros                         _(número de filas y columnas de la matriz)_
Salidas:
   A: Array (1..1000,1..1000) de Reales  _(la última fila y columna contiene la suma de los elementos de la matriz)_
Variables:
   i, j: Enteros
   aux, sum: Reales
Inicio
   sum <-- 0
   A(m,n) <-- 0
   Para i <-- 1 hasta m hacer
      Para j <-- 1 hasta n hacer
         sum <-- sum + A(i,j)
      Fin_Para
   Fin_Para
   A(m,n) <-- sum
Fin


```
####  Algoritmo principal 
```text


Procedimiento RellenaMatriz (Var A, m, n)
Entradas:
   m, n: Enteros   _(número de filas y de columnas de la matriz)_
Salidas:
   A: Array (1..1000,1..1000) de Reales  _(matriz bidimensional)_
Variables:
   i, j: Enteros
   b: Real
Inicio
   Para i <-- 1 hasta m hacer                      
      Para j <-- 1 hasta n hacer
         Escribir "Introduzca el elemento ",i," , ",j," de la matriz: "
         Leer A(i,j)
      Fin_Para
   Fin_Para
Fin



Procedimiento MuestraMatriz (A, m, n)
Entradas:
   A: Array (1..1000,1..1000) de Reales  _(matriz bidimensional)_
   m, n: Enteros  _(número de filas y de columnas de la matriz)_
Salidas:
   _(Muestra al usuario el contenido de la matriz)_
Variables:
   i, j: Enteros
   b: Real
Inicio
   Para i <-- 1 hasta m hacer
      Para j <-- 1 hasta n hacer
         Escribir "Elemento ",i," , ",j,": ", A(i,j)
      Fin_Para
   Fin_Para
Fin



Algoritmo Matrices
Entradas:
   matriz: Array (1..1000,1..1000) de Reales  _(matriz bidimensional)_
   filas, columnas: Enteros                   _(número de filas y columnas de la matriz)_
Salidas:
   matriz: Array (1..1000,1..1000) de Reales  _(matriz modificada)_
Variables:
   f1, f2, opcion: Enteros
Inicio
   opcion <--1 
   Mientras ( opcion = 0 ) hacer
      _(Mostrar menú al usuario)_
      Escribir " 1. para lectura de la matriz "
      Escribir " 2. para intercambiar filas de la matriz "
      Escribir " 3. para sumar filas y columnas de la matriz "
      Escribir " 4. para multiplicar filas y columnas de la matriz "
      Escribir " 5. pata sumar todos los elementos de la matriz "
      Escribir " 0. para salir "
      Leer opcion 

      _(Realizar acción según la opción elegida)_
      En Caso De Que opcion Valga
         1: _(Leer la matriz)_
            Escribir " Introduzca numero de filas y de columnas "
            Leer filas, columnas
            RellenaMatriz (matriz, filas, columnas)

         2: _(Intercambiar filas)_
            Escribir " Introduce filas que quieres intercambiar "
            Leer f1, f2
            IntercambiaFilas (matriz, filas, columnas, f1,f2)
            MuestraMatriz (matriz, filas, columnas)

         3: _(Sumar filas y columnas)_
            SumaProducto (matriz, filas, columnas, 0)
            MuestraMatriz (matriz, filas, columnas)

         4: _(Multiplicar filas y columnas)_
            SumaProducto (matriz, filas, columnas, 1)
            MuestraMatriz (matriz, filas, columnas)

         5: _(Sumar todos los elementos de la matriz)_
            SumaUltimaFilaColumna (matriz, filas, columnas)
            MuestraMatriz (matriz, filas, columnas)

         0: _(Salir del programa)_
            Escribir "Gracias por utilizar este programa. Adios"

         En otro caso:
            Escribir " Opción no válida. Pulse una opción entre 0 y 5 "
       Fin_Casos
    Fin_Mientras
Fin
```