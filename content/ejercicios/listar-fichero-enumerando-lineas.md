---
title: "Listar fichero enumerando lineas"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Listar fichero enumerando lineas

##  Enunciado 

Realizar un programa que abra un fichero denominado **fich1.txt** , que vaya leyendo línea a línea y muestre las líneas leídas numeradas. También mostrará el total de líneas leídas. 

##  Soluciones 

###  Programa en Matlab 
```matlab

%borro la pantalla
clc;
 
filename = 'fich1.txt';
% abrimos el fichero
fid = fopen (filename, 'r');
 
contLineas = 0;
% mientras no lleguemos al final del fichero
while (~feof(fid))
   % leemos toda la línea con fgetl
   linea = fgetl (fid);
   contLineas = contLineas + 1;
   % vamos mostrando todas las líneas
   disp(['Línea ', num2str(contLineas), ': ', linea]);
end
 
% cerramos el fichero
fclose (fid);
% mostramos el total de líneas leídas
disp(['Número de líneas leídas: ', num2str(contLineas)]);
```