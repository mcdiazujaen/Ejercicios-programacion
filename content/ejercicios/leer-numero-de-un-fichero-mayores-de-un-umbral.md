---
title: "Leer numero de un fichero mayores de un umbral"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Leer numero de un fichero mayores de un umbral

##  Enunciado

Implementa una función que reciba como parámetros de entrada los nombres de dos ficheros de texto y un valor entero que indica un umbral. El primero de los ficheros contendrá una lista de números enteros. La función debe introducir en el segundo fichero los números del primer fichero que sean mayores que el umbral establecido. La función debe devolver dos valores: un valor lógico que indique si lo dos ficheros se han abierto correctamente y un valor entero que indique el número de elementos que se han copiado en el segundo fichero. 

##  Soluciones

###  Programa en Matlab 
```matlab

function [exito, ncopias]=CopiaMayor(nfichero1, nfichero2, umbral)
% FUNCION [exito, ncopias]=CopiaMayor(nfichero1, nfichero2, umbral)
% Descripción: se copian en el segundo fichero (nfichero2) los valores del 
%    primero (nfichero1) que son mayores que la cota dada en el parámetro umbral
% Parámetros de entrada:
%   nfichero1, nfichero2: ARRAY DE CARACTERES, los nombres de dos ficheros
%   umbral: ENTERO, umbral para realizar la copia
% Parámetros de salida:
%   exito: LÓGICO, verdadero si los ficheros se han abierto correctamente,
%     falso en otro caso
%   ncopias: ENTERO, número de valores que se han copiado del primer 
%     fichero en el segundo
f1=fopen(nfichero1, 'r');
if (f1==-1)
    exito=false;
    ncopias=0;
else
    f2=fopen(nfichero2, 'w');
    if (f2==-1)
        exito=false;
        ncopias=0;
    else
        exito=true;
        ncopias=0;
        todos=fscanf(f1,'%d',inf);
        tam=length(todos);
        for p=1:tam
            if (todos(p)>umbral)
                fprintf(f2,'%d \n',todos(p));
                ncopias=ncopias+1;
            end
        end
        fclose(f2);
    end
    fclose(f1);
end
```