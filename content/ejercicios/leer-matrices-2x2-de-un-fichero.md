---
title: "Leer matrices 2x2 de un fichero"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Leer matrices 2x2 de un fichero

##  Enunciado

Un archivo de texto almacena matrices de dos por dos con el siguiente formato: 
```text

NúmeroDeMatrices
Fila1Col1Mat1  Fila1Col2Mat1  Fila2Col1Mat1  Fila2Col2Mat1
Fila1Col1Mat2  Fila1Col2Mat2  Fila2Col1Mat2  Fila2Col2Mat2
...

```
Por ejemplo, dado el archivo: 
```text

3
1 2 3 4
1 1 2 2
7 8 6 4

```
El archivo almacena las matrices: 
```text

1 2      1 1      7 8
3 4      2 2      6 4

```
Realiza una función que tome como parámetro un nombre de archivo con el formato especificado y una posición y devuelva la matriz 2x2 que ocupa la posición indicada en el archivo. Si el archivo tiene menos matrices que la posición indicada debe devolver una matriz vacía. Por ejemplo, si para el archivo de ejemplo se indica la posición 2 entonces se debe devolver la matriz: 
```text

1 1
2 2

```
##  Soluciones 

###  Programa en Matlab 
```matlab

function matriz = LeerMatriz2x2(nombre, posicion)
% Funcion matriz = LeerMatriz2x2(nombre, posicion)
% Descripción: Extrae de un fichero de texto una matriz 2x2
% Parámetros de entrada:
%    nombre: CADENA DE CARACTERES; nombre del fichero de texto que 
%          contiene las matrices 2x2 según el formato especificado 
%          en el enunciado
%    posicion: ENTERO; posición en el fichero de la matriz a extraer
% Parámetros de salida:
%    matriz: ARRAY (2,2) DE REALES; la matriz que ocupaba la posición
%          indicada en el fichero de matrices de nombre nombre. Si no
%          se pudo abrir el fichero o no existe una matriz en dicha
%          posición se devuelve una matriz vacía
matriz = [];
idf = fopen (nombre, 'r');
if idf ~= -1
   nmatrices = fscanf(idf, '%d', 1);
   if posicion <= nmatrices
      for x = 1:posicion
         matriz = fscanf(idf,'%f', [2,2]);
      end
      matriz = matriz';
   end
end
```