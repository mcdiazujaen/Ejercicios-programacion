---
title: "Letra del DNI"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Letra del DNI

##  Enunciado 

Escribe una función que calcule la letra del DNI a partir del número. La letra se obtiene calculando el resto de la división del número del DNI por 23. A cada resultado le corresponde una letra: 0=T; 1=R; 2=W; 3=A; 4=G; 5=M; 6=Y; 7=F; 8=P; 9=D; 10=X; 11=B; 12=N; 13=J; 14=Z; 15=S; 16=Q; 17=V; 18=H; 19=L; 20=C; 21=K; 22=E. 

##  Soluciones 

###  Programa en Matlab 

####  Solución con arrays 
```matlab


function letra = LetraDNI( dni )
% FUNCION letra = LetraDNI( dni )
% DESCRIPCIÓN: Calcula la letra correspondiente a un número de DNI
% PARÁMETROS DE ENTRADA:
%    dni: ENTERO; número del DNI
% PARÁMETROS DE SALIDA:
%    letra: CARÁCTER; letra correspondiente al dni dado
 
% VARIABLES INTERNAS:
%    lista: ARRAY(23) DE CARACTERES (o cadena de caracteres)
%    pos: ENTERO
 
lista ='TRWAGMYFPDXBNJZSQVHLCKE';
 
pos = rem(dni,23);
letra = lista( pos+1 );
```