---
title: "Calculo del determenante de una matriz 3x3"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['enunciado', 'comentario', 'análisis']
tags: ['sin_pseudocódigo']
---

# Calculo del determenante de una matriz 3x3

##  Enunciado 

Realiza un programa que calcule el determinante de una matriz 3×3. En el caso de que la matriz sea singular, el programa deberá advertirlo con un mensaje. Recuerda que la fórmula para el cálculo del determinante es la siguiente: 

![Imagen:Determinante.JPG](images/5/57/Determinante.JPG)

En vez de tener que introducir la matriz tecleándola cada vez, utiliza un fichero llamado **matriz.d** que contiene una matriz 3×3 cualquiera. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

/* fichero determin.c */
#include <stdio.h>
#define SIZE 3
void main(void) {
  double matriz[SIZE][SIZE];
  double determinante;
  int i, j;
  FILE *fi;
  /* printf("Introduzca los elementos de la matriz 3x3:\n"); */
  fi = fopen("matriz.d", "r+");
  for (i=0; i<SIZE; i++)
     for (j=0; j<SIZE; j++) {
         fscanf(fi, "%lf", &matriz[i][j]);
     }
  fclose(fi);
  printf("\n");
  determinante = matriz[0][0]*matriz[1][1]*matriz[2][2];
  determinante += matriz[0][1]*matriz[1][2]*matriz[2][0];
  determinante += matriz[1][0]*matriz[2][1]*matriz[0][2];
  determinante -= matriz[0][2]*matriz[1][1]*matriz[2][0];
  determinante -= matriz[0][1]*matriz[1][0]*matriz[2][2];
  determinante -= matriz[0][0]*matriz[2][1]*matriz[1][2];
  printf("La matriz introducida es:\n");
  for (i=0; i<SIZE; i++) {
     for (j=0; j<SIZE; j++)
        printf("%8.2lf", matriz[i][j]);
     printf("\n");
  }
  printf("\nY su determinante es: %12.4lf\n", determinante);
}
```

####  Comentario 

En principio este programa no existe ninguna dificultad respecto al manejo de las matrices (ya se ha visto en programas anteriores). Lo único que es importante comentar es el algoritmo: tenemos siempre una matriz 3x3 y, por ello, podemos realizar las operaciones **“a mano”** (sin más complejidades en el algoritmo, es decir, sin introducir bucles o bifurcaciones). Si quisiéramos calcular el determinante de una matriz cualquiera, tendríamos que triangularizar la matriz y, una vez triangularizada, el determinante sería el producto de los elementos de la diagonal. La matriz se lee de un fichero de disco. Para ello es necesario abrir el fichero mediante la función **fopen()** , que devuelve un puntero a FILE. Después se van leyendo los datos de dicho fichero mediante la función **fscanf()** a la que se pasa como primer argumento el puntero al fichero abierto; excepto en que lee de fichero, esta función es completamente análoga a **scanf()**. Al acabar de leer la matriz se debe cerrar el fichero con la función **fclose()**. Es interesante observar como se ha dividido una expresión muy larga en seis expresiones más cortas, utilizando los operadores de suma y diferencia acumulativas (+= y -=). 

###  Programa en Matlab 

####  Solución con programación básica 

El siguiente programa en MatLab utiliza funciones similares a las utilizadas en lenguaje C. 
```matlab

% Programa Calcular_Determinante
% Descripción: Calcula el determinante de una matriz 3×3
% Entradas: Nombre del fichero donde está la matriz.
% Salidas: El determinante.
% Variables:
%    nombre: CADENA DE CARACTERES
%    fichero: ENTERO
%    matriz: ARRAY (3,3) DE REALES
%    deter: REAL
 
% Leer fichero
nombre=input('Introduce nombre del fichero:');
fichero=fopen(nombre,'r');
matriz=fscanf(fichero,'%f',[3,3]);
fclose(fichero);
matriz = matriz';
 
% Calcular determinante
deter=matriz(1,1)*matriz(2,2)*matriz(3,3);
deter=deter+matriz(1,2)*matriz(2,3)*matriz(3,1);
deter=deter+matriz(1,3)*matriz(2,1)*matriz(3,2);
deter=deter-matriz(2,1)*matriz(1,2)*matriz(3,3);
deter=deter-matriz(3,1)*matriz(2,2)*matriz(1,3);
deter=deter-matriz(1,1)*matriz(3,2)*matriz(2,3);
 
% Mostrar el resultado
disp('El determinante es:');
disp(deter);
```

####  Solución con programación Matlab avanzada 
```matlab

% Programa Calcular_Determinante
% Descripción: Calcula el determinante de una matriz 3×3
% Entradas: Nombre del fichero donde está la matriz.
% Salidas: El determinante.
% Variables:
%    nombre: CADENA DE CARACTERES
%    matriz: ARRAY (3,3) DE REALES
%    deter: REAL
 
% Leer fichero
nombre=input('Introduce nombre del fichero:');
matriz=load(nombre);
 
% Calcular determinante
deter=det(matriz);
 
% Mostrar el resultado
disp('El determinante es:');
disp(deter);
```