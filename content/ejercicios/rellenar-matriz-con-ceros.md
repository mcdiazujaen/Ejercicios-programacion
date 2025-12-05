---
title: "Rellenar matriz con ceros"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Rellenar matriz con ceros

##  Enunciado 

Implementa un programa que dado como entrada el nombre de un fichero de texto lea desde éste una matriz cuadrada de tamaño **n** de números enteros, la transforme sustituyendo los ceros por un valor que indique el número de valores distintos de cero que hay en la fila y escriba la matriz transformada en otro fichero llamado **resultado.txt**. El fichero de salida ha de tener el mismo formato que el fichero de entrada. 

Haz una descomposición modular del problema de forma que el programa enlace tres funciones: una que lea los dados desde el archivo y devuelva la matriz, otra que transforme la matriz dada y la última que reciba de entrada la matriz resultado y la escriba en el fichero. 

El formato del fichero de entrada es el siguiente: en la primera línea la dimensión de la matriz, y en las siguientes líneas cada una de las filas de la matriz. 

**Ejemplo:** Archivo de entrada 
```text

5				
5	0	7	0	0
4	2	7	0	0
0	0	0	0	9
8	2	6	5	0
1	4	4	8	6

```
**Ejemplo:** Archivo de salida 
```text

5				
5	**2**	7	**2**	**2**
4	2	7	**3**	**3**
**1**	**1**	**1**	**1**	9
8	2	6	5	**4**
1	4	4	8	6

```
##  Soluciones 

###  Programa en Matlab 

####  Función que lee el fichero 
```matlab

function m = leeFich(nombre)
% Función m = leeFich(nombre)
% Descripción: Extrae una matriz cuadrada de enteros almacenada en
%              un fichero de texto
% Parámetros de entrada:
%   nombre: CADENA DE CARACTERES; nombre del fichero de texto 
%      que contiene la matriz. El formato del fichero es el 
%      siguiente. En la primera fila un entero indica la
%      dimensión de la matriz. Cada una de las líneas siguientes 
%      contiene una fila de la matriz, con los elementos
%      separados por espacios en blanco.
% Parámetros de salida:
%   m: ARRAY BIDIMENSIONAL DE REALES; la matriz leída. Si no 
%      se pudo abrir el fichero la matriz estará vacía.
m = [];
idf = fopen (nombre, 'r');
if idf ~= -1
    dim = fscanf(idf, '%d', 1);
    m = fscanf(idf,'%d', [dim,dim]);
    m = m';
    fclose(idf);
end

```
####  Función que transforma la matriz 
```text

function s = transforma(m)
% Función s = transforma(m)
% Descripción: Dada una matriz, construye otra en la que se 
%              sustituyen los ceros por el número de valores
%              distintos de cero en la fila
% Parámetros de entrada:
%   m: ARRAY BIDIMENSIONAL DE REALES; matriz de datos
% Parámetros de salida:
%   s: ARRAY BIDIMENSIONAL DE REALES; matriz transformada
[nf,nc] = size (m);
for f = 1:nf
    nonulos = 0;
    for c = 1:nc
        if m(f,c) ~= 0
            nonulos = nonulos + 1;
        end
    end
    for c = 1:nc
        if m(f,c) == 0
            m(f,c) = nonulos;
        end
    end
end
s = m;

```
####  Función que escribe en el fichero 
```text

function escribeFich(m)
% Función escribeFich(m)
% Descripción: Escribe una matriz de enteros en un fichero llamado
%              'resultado.txt'. El formato del fichero es igual
%              al especificado en la función leeFich
% Parámetros de entrada:
%   m: ARRAY BIDIMENSIONAL DE REALES; la matriz a escribir
idf = fopen ('resultado.txt', 'w');
if idf ~= -1
    [nf,nc] = size (m);
    fprintf(idf,'%d\n',nf);
    for f = 1:nf
        for c = 1:nc
            fprintf(idf,'%d ', m(f,c));
        end
        fprintf(idf,'\n');
    end
    fclose(idf);
end

```
####  Programa principal 
```matlab

% Programa TransformaMatriz
% Entradas:
%    - Nombre del fichero donde se encuentra la matriz a transformar
% Salidas:
%    - Fichero 'resultado.txt' con la matriz transformada
% Variables:
%    nombre: CADENA DE CARACTERES
%    m,t: ARRAYS BIDIMENSIONALES DE REALES
 
nombre = input('Introduzca el nombre del fichero de entrada: ','s');
m = leeFich(nombre);
t = transforma(m);
escribeFich(t);
```