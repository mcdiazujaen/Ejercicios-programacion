---
title: "Decodificar clave de acceso"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Decodificar clave de acceso

##  Enunciado

Se necesita implementar un programa para decodificar una clave de acceso a un sistema, para ello se han de implementar las siguientes funciones: 

###  Función de lectura 

Función que tome como parámetro de entrada el nombre de un fichero y devuelva un vector con los elementos válidos del fichero, si el fichero no puede abrirse, sus elementos no son válidos o no hay un número correcto de datos, devolverá el array vacío. El formato del fichero es el siguiente: en la primer línea un entero que indica un tamaño N, las NxN siguientes líneas están formadas por tres dígitos enteros separados por espacios, la última línea está formada por un entero. Los elementos que deben devolverse en el vector son los almacenados en las NxN líneas anteriormente descritas y son válidos si el valor almacenado en la última fila es un -1. 

Ejemplo fichero: 
```text

3
3 1 5
2 3 6
1 1 3
3 2 4
1 3 7
2 2 3
1 1 1
3 3 5
2 1 2
-1

```
Vector de Salida: 
```text

[3 1 5 2 3 6 1 1 3 3 2 4 1 3 7 2 2 3 1 1 1 3 3 5 2 1 2]

```
###  Función de decodificación 

Función que reciba como parámetro de entrada un vector de enteros positivos de tamaño NxNx3 y devuelva como salida dos valores: un valor lógico indicando si la decodificación se ha realizado con éxito y un entero que es la clave decodificada. La forma de realizar la decodificación es la siguiente: a partir del vector de entrada se ha de construir una matriz cuadrada de tamaño NxN. Cada elemento de la matriz se obtiene a partir de tres elementos del vector que informan de una posición de fila, una posición de columna y el valor que se va a situar en dicha posición. Si todo ha sido correcto la clave se obtiene formando un número entero con los dígitos situados en la primera fila de la matriz. 

Ejemplo: 
```text

Vector=[3 1 5 2 3 6 1 1 3 3 2 4 1 3 7 2 2 3 1 2 1 3 3 5 2 1 2]

```
La matriz quedaría: 

3 |  1 |  7   
---|---|---  
2 |  3 |  6   
5 |  4 |  5   
  
La función devolvería verdadero en el valor lógico como clave el número 317. 

En cada momento la función debe controlar que las posiciones de fila y columna son correctas y que no se hace más de un acceso a una posición (si ocurre algo de ésto la función acaba y devuelve falso en el valor lógico). 

###  Programa principal 

Programa principal que lea desde el teclado el nombre de un fichero donde están los datos y utilizando las funciones anteriores devuelva la clave de acceso si todo se ha realizado con éxito, en caso contrario debe especificar que no ha habido éxito y el por qué. 

##  Soluciones 

###  Programa en Matlab 

####  Función de lectura 
```matlab

function v=Lectura(nombre)
%Parámetros de Entrada: 
%  nombre: CADENA DE CARACTERES, nombre del fichero donde están los datos.
%      Formato del fichero: en la primer línea un entero que indica un 
%      tamaño N, las NxN siguientes líneas están formadas por tres dígitos 
%      enteros separados por espacios, la última línea está formada por un 
%      entero. 
%Parámetros de Salida:
%  v: ARRAY DE ENTEROS, Vector con los elementos válidos. Vector vacío si 
%      el fichero no puede abrirse, sus elementos no son válidos (último 
%      dígito distinto a -1) o no hay un número correcto de datos (debe 
%      haber NxNx3 datos)
 
fich=fopen(nombre,'r');
if (fich==-1)
    v=[];
else
    N=fscanf(fich,'%d',1); % obtenemos el tamaño del array 
    v=fscanf(fich,'%d',inf); % obtenemos el resto de datos
    fclose(fich);
    t=length(v);
    ultimo=v(t); % nos quedamos con le último elemento ó ultimo=m(end)
    v(t)=[] % eliminamos el último elemento
    % vector correcto si el último es -1 y su dimensión N*N*3, si no se 
    % devuelve vector vacío
    if (ultimo~=-1 || t-1~=N*N*3)
        v=[];
    end
end

```
####  Función de decodificación 
```text

function [exito,clave]=Decodifica(v)
%Parámetros de Entrada: 
%  v: vector de N*N*3 elementos
%Parámetros de Salida:
%  exito: true, si la clave se puede conseguir (las posiciones de fila 
%      y columna son correctas y no se hace más de un acceso a una 
%      posición) false en otro caso
%  clave: clave conseguida a partir de v, formando una matriz N*N y
%      tomando un entero con los dígitos de la primera fila. Cada 3 
%      elementos en v indican una posición de fila, una de columna y el 
%      valor a colocar en dicha posición (los valores a colocar son 
%      enteros positivos)
 
N=length(v);
dim=sqrt(N/3); % no de filas y columnas
m=zeros(dim);
m=m-1; % construímos una matriz de -1s
 
% ahora se contruye la matriz a partir de los datos del vector
exito=true;
i=1;
while (i<N && exito) % recorremos todos los elementos del vector
    fil=v(i); % indica el número de fila
    col=v(i+1); % indica el número de columna
    valor=v(i+2); % indica el valor (que es positivo)
    % todo es correcto si la fila y columna no se pasan de los límites
    % y la matriz contenía en esa posición un -1 (indica que no se ha accedido antes)
    if (1<=fil && fil<=dim && 1<=col && col<=dim && m(fil,col)==-1)
        m(fil,col)=valor;
    else 
        exito=false;
    end
    i=i+3; % se avanza a la posición fila del siguiente elemento 
end
 
% se forma la clave a partir de los dígitos de la primera fila
clave=0;
pot=dim-1;
for i=1:dim
    clave=clave+m(1,i)*(10^pot);
    pot=pot-1;
end

```
####  Programa principal 
```matlab

%Programa Decodificar_clave
%Entradas: el nombre de un fichero
%Salidas: clave contenida si el proceso de decodificación ha ido bien
%Variables: 
%    fich: CADENA DE CARACTERES
%    vec, clave: ARRAY DE ENTEROS
%    bien: LOGICO
 
fich=input('Introduce el nombre del fichero con los datos: ','s');
vec=Lectura(fich);
if (length(vec)==0) % hay error al leer los datos
    disp('Hay error al leer desde el fichero');
else
    [bien,clave]=Decodifica(vec);
    if (bien)
       disp(['La clave es: ',num2str(clave)]);
    else
       disp('La clave no se ha podido decodificar');
    end
end
```