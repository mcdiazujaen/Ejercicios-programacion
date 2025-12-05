---
title: "Calcular la varianza"
date: 2024-01-01
draft: false
languages: ['pseudocódigo', 'matlab']
categories: ['enunciado']
---

# Calcular la varianza

##  Enunciado

La siguiente fórmula proporciona la varianza de los valores de un vector _x_ (denota la media de los _n_ valores del vector): 

![imagen:varianza.jpg](images/a/a5/Varianza.jpg)

Diseñar un algoritmo para leer los elementos de un vector _x_ y calcular la media y la varianza de los valores usando la fórmula dada anteriormente. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text

ALGORITMO varianza_medida
ENTRADAS:
  n: REAL  (* número de valores del vector *)
  x: ARRAY (1..n) DE REALES (* Vector con los valores *)
SALIDAS:
  (* La media y la varianza del vector x *)
VARIABLES:
  i: ENTERO
  suma, media, varianza: REALES
INICIO
  (* Pedir al usuario los valores del vector *)
  ESCRIBIR "Introducir tamaño"
  LEER n
  PARA i<--1 HASTA n HACER
      ESCRIBIR "Introducir numero"
      LEER x(i)
  FIN_PARA
 
  (* Calcular la media de los valores de x *)
  suma <-- 0
  PARA i<--1 HASTA n HACER
       suma <-- suma + x(i)
  FIN_PARA
  media <-- suma/n
 
  (* Calcular la varianza de los valores de x *)
  varianza <-- 0
  PARA i <-- 1 HASTA n HACER
      varianza <-- varianza + (x(i) - media)
  FIN_PARA
  varianza <-- varianza/(n-1)
 
  (* Mostrar los resultados *)
  ESCRIBIR "La media es:", media
  ESCRIBIR "La varianza es:", varianza
FIN

```
###  Programa en Matlab 
```matlab

% Programa Varianza_Media
% Entradas: Número de elementos del vector.
% Salidas: La media y la varianza.
% Variables:
%    dim, pos : ENTEROS
%    v: ARRAY DE REALES
%    media, vari: REALES
%    texto: CADENA DE CARACTERES
 
% Rellenar vector con valores aleatorios.
dim=input('Introduce el número de elementos:');
v=randn(1,dim);
 
% Calcular la media
media=0;
for pos=1:dim,
    media=media+v(pos);
end
media=media/dim;
 
% Calcular la varianza
vari=0;
for pos=1:dim,
    vari=vari+(v(pos)-media);
end
varian=vari/(dim-1);
 
% Mostrar el resultado
texto=['La media es:' num2str(media)];
disp(texto);
texto=['La varianza es:' num2str(varian)];
disp(texto);
```