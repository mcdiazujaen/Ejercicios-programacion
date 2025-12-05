---
title: "Contar vocales"
date: 2024-01-01
draft: false
languages: ['pseudocódigo', 'matlab']
categories: ['enunciado']
tags: ['sin_c']
---

# Contar vocales

##  Enunciado

Dado un vector de caracteres llamado cadena como el que se indica a continuación, que contiene una frase que termina cuando encuentra un punto (Nota: el tamaño del vector está determinado por el punto). Haz un algoritmo que obtenga en otro vector, denominado resultado, el número de vocales de cada tipo que hay en un vector. Por ejemplo: 
```text
cadena: El saber no ocupa lugar.

           a e i o u
resultado: 3 2 0 2 2
```

El vector resultado significa que en la cadena hay: 3 aes, 2 es, 0 ies, 2 oes, y 2 ues. 

Es importante la eficiencia y claridad a la hora de resolver el algoritmo y fundamentalmente la utilización de las estructuras de control más adecuadas. 

##  Soluciones

###  Diseño en pseudocódigo
```text
ALGORITMO cuentaVocales
ENTRADAS:
   cadena: ARRAY(1..100) DE CARACTERES  (* contiene la frase para contar vocales *)
SALIDAS:
   res: ARRAY(1..5) DE ENTEROS    (* contiene el número de vocales que contiene el array cadena *)
VARIABLES:
   i, n: ENTEROS
INICIO
   (* Leer el array de con la frase *)
   i <-- 0
   REPETIR
     i=i+1;
     ESCRIBIR "Introduce una letra (. para finalizar): "
     LEER cadena(i)
   HASTA cadena(i)='.'
   n <-- i-1
 
   (* Inicializar array con los 5 contadores de las vocales *)
   PARA i=1 HASTA 5 HACER
      res(i) <-- 0
   FIN_PARA
 
   (* Contar las vocales que aparecen en la variable cadena *)
   PARA i=1 HASTA n HACER
       EN CASO DE QUE cadena(i) VALGA
          'a','A': res(1) <-- res(1)+1
          'e','E': res(2) <-- res(2)+1
          'i','I': res(3) <-- res(3)+1
          'o','O': res(4) <-- res(4)+1
          'u','U': res(5) <-- res(5)+1
       FIN_CASO
   FIN_PARA
 
   (* Mostrar resultados *)
   ESCRIBIR res(1), " aes"
   ESCRIBIR res(2), " es"
   ESCRIBIR res(3), " ies"
   ESCRIBIR res(4), " oes"
   ESCRIBIR res(5), " ues"
FIN
```

###  Programa en Matlab 
```matlab

%PROGRAMA CuentaVocales
%DESCRIPCIÓN: Dado un vector de caracteres, se obtiene en otro vector el número de vocales de cada tipo que hay en el primer vector. 
%ENTRADAS: vector de cadena de caracteres.
%SALIDAS: vector resultado.
%VARIABLES:
%   pos: ENTERO
%   texto, vocales, mensa: ARRAY (o CADENA) DE CARACTERES
%   res: ARRAY(5) DE ENTEROS
 
%Pedir el texto al usuario
texto = input('Introduzca un texto: ','s');
disp('El texto a contar es:');
 
%Contar cuantas vocales de cada tipo hay
res=zeros(1,5);
for pos=2:length(texto)
    switch texto(pos)
        case {'A','a'}
            res(1)=res(1)+1;
        case {'E','e'}
            res(2)=res(2)+1;
        case {'I','i'}
            res(3)=res(3)+1; 
        case {'O','o'}
            res(4)=res(4)+1;  
        case {'U','u'}
            res(5)=res(5)+1; 
    end
end
 
%Mostrar los resultados
vocales='AEIOU';
for pos=1:5,
    mensa=;
    disp( ['Hay ', num2str(res(pos)), ' de la vocal ', vocales(pos)] );
end
```