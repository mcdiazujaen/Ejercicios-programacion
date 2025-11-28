---
title: "Invertir contenido de un archivo"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Invertir contenido de un archivo

##  Enunciado 

Escribe un programa que lea una lista de números reales a partir de un archivo. El programa los almacena en un vector, y presenta la lista en pantalla en orden inverso al que tienen en el archivo. 

##  Soluciones 

###  Programa en Matlab 
```matlab


% Se lee una lista de números reales a partir de un archivo. El programa los almacena
% en un vector, y presenta la lista en pantalla en orden inverso al que tienen en el archivo.
clc; %Borra la pantalla
 
%pedimos al usuario el nombre del archivo
nombre1=input('Nombre del archivo origen: ', 's');
 
% abrimos el archivo
orig = fopen(nombre1, 'r');
 
% si se ha abierto correctamente leemos el vector de reales
if (orig ~= -1)
   v = fscanf(orig,'%f',[1,inf]);
   fclose(orig);
else
   disp ('Error al abrir el fichero');
end
 
% mostramos el vector leído para comprobar que todo está correcto
disp('Vector original');
disp(v);
long =length(v);
 
% calculamos el inverso
for i=1:(long/2)
   temp = v(i);
   v(i) = v(long-i+1);
   v(long-i+1) = temp;
end
% mostramos el vector invertido
disp('Vector inverso:');
disp(v);
```