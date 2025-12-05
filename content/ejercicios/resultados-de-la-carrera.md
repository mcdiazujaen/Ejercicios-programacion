---
title: "Resultados de la carrera"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Resultados de la carrera

##  Enunciado

A la salida de una carrera se anotan en un fichero el número total de corredores que participan, así como los dorsales de los mismos en el orden en el que efectúan la salida. A medida que éstos van llegando a la meta se anota en una nueva línea de ese mismo fichero el número de dorsal, en el orden de llegada. 

Implementa las siguientes funciones: 

```text
**Apartado 1.** Función a la que se le pase como entrada el nombre del fichero con los datos, lea su contenido y devuelva dos vectores: uno con los dorsales en el orden de salida y otro con los dorsales en el orden de llegada. 

**Apartado 2.** Función que reciba como entrada un número y un vector, y devuelva la posición en la que está (si el número está en el vector) o -1 en caso contrario. 

**Apartado 3.** Función a la que se le pasen como parámetros de entrada los dos vectores con los dorsales de salida y llegada, y devuelva en un nuevo vector los números de los dorsales de los corredores que hayan abandonado la carrera sin llegar a la meta. 

**Apartado 4.** Programa principal que pida al usuario el nombre del fichero con los datos de entrada, lo lea, averigüe los corredores que han abandonado y por último guarde en un fichero (su nombre se pedirá también al usuario) los dorsales de dichos corredores. 

Por ejemplo si el fichero de entrada es el siguiente: 

  8
  10 20 30 40 50 60 70 80
  70 40 50 20 80

el programa escribiría en el fichero de salida: 

  Los dorsales de los corredores que han abandonado son: 10 30 60.

```
##  Soluciones

###  Programa en Matlab 

####  Apartado 1 
```matlab

function [salida,llegada]=Lectura(nombre)
%Parámetros de entrada:
%  nombre: nombre del fichero donde están los datos.
%     Formato --> línea1 - número total de corredores que participan,
%                 línea2 - dorsales de los mismos en el orden en el que efectúan la salida
%                 línea3 - dorsales en el orden de llegada
%Parámetros de salida:
%  salida: vector con los dorsales de los corredores en la salida
%  llegada: vector con los dorsales de los corredores que llegan a meta
fich=fopen(nombre,'r');
if (fich~=-1)
  n=fscanf(fich,'%d',1);
  salida=fscanf(fich,'%d',n);
  salida=salida';
  llegada=fscanf(fich,'%d',inf);
  llegada=llegada';
  fclose(fich);
else
  salida=[];
  llegada=[];
end

```
####  Apartado 2 
```text
function posicion=Busca(v,x)
%Parámetros de entrada:
%  v: vector de números
%  x: elemento a buscar en v
%Parámetros de salida
%  posicion: posición que ocupa x en v, -1 si no está
posicion=-1;
t=length(v);
h=1;
while (h<=t && posicion==-1)
  if (x==v(h))
    posicion=h;
  else
    h=h+1;
  end
end

```
####  Apartado 3 
```text
function vabandonos=Abandono(salida,llegada)
%Parámetros de entrada:
%  salida: vector con los dorsales de los corredores en la salida
%  llegada: vector con los dorsales de los corredores que llegan a meta
%Parámetros de salida:
%  vabandonos: vector con los dorsales de los corredores que abandonan la carrera
tsalida=length(salida);
tllega=length(llegada);
vabandonos=[];
if (tsalida~=tllega) % si son iguales no ha habido ningún abandono
  for x=1:tsalida
    p=Busca(llegada,salida(x)); %Utilizamos el módulo del apartado 2
    if p==-1
      %corredor que sale y no llega a meta
      vabandonos=[vabandonos salida(x)];
    end
  end
end

```
####  Apartado 4 
```matlab

%Programa Principal
%Entradas:
%  Nombre fichero con los datos dorsales de los corredores en la salida y los dorsales de los corredores que llegan a meta.
%  Nombre fichero donde guardar la salida
%Salida:
%  Guarda en un fichero los dorsales de los corredores que abandonan la carrera
 
fichE=input('Nombre del fichero con los datos de entrada: ','s');
[vS,vLl]=Lectura(fichE);
if (length(vS)==0 || length(vLl)==0)
  disp('Error en el fichero de entrada');
else
  fichS=input('Nombre del fichero de salida: ','s');
  fich=fopen(fichS,'w');
  if fich==-1
    disp('Error en el fichero de salida');
  else
    vA=Abandono(vS,vLl);
    t=length(vA);
    fprintf(fich,'Los dorsales de los corredores que han abandonado la carrera son: ');
    if t==0
      fprintf(fich,'Ninguno');
    else
      fprintf(fich,'%d ',vA);
    end
    fclose(fich);
  end
end
```