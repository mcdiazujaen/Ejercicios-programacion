---
title: "Gestionar lotes de sutura"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Gestionar lotes de sutura

##  Enunciado

Se quiere realizar un programa para gestionar lotes de sutura. Se dispone de un archivo que contiene información sobre los lotes que han sido rechazados durante un período de un mes. Cada línea del archivo contiene el número de lote, la temperatura, la presión y el tiempo de permanencia de cada uno de los lotes rechazados. Un lote se rechaza por temperatura si el valor es superior a 155, por presión si es superior a 60 y por tiempo si es menor que 2.10. 

Un ingeniero de control de calidad quiere analizar esta información para determinar el porcentaje mensual de los lotes rechazados por temperatura, por presión y por tiempo de permanencia. Si un lote específico se rechaza por más de una razón, se debe contar en todos los totales aplicables. 

Ejemplo de archivo: 
```text

51	145.5	62.3	2.23
82	153.7	63.2	2.52
53	160.3	58.9	2.51
23	159.5	58.9	2.01
42	160.3	61.2	1.98

```
Escribe un programa en Matlab que pida al usuario el nombre de un archivo con los datos sobre los lotes de sutura, calcule los tres porcentajes comentados y escriba los resultados en un archivo de texto con el siguiente formato (para el ejemplo anterior): 

  * Porcentaje de lotes rechazados por temperatura: 60 
  * Porcentaje de lotes rechazados por presión: 60 
  * Porcentaje de lotes rechazados por tiempo: 40 

El nombre del archivo de salida es un dato que se le debe pedir al usuario. 

##  Soluciones

###  Programa en Matlab 
```matlab

%Programa LotesDefectuosos
%Entrada:
%   nombre de un fichero con los datos, el fichero contiene por cada lote
%   rechazado su temperatura, presión y tiempo
%Salida:
%   escribe en un fichero el porcentaje de lotes rechazados por cada una 
%    de las causas (temperatura, presión y tiempo) 
 
nombre=input('Introduce el nombre del fichero con los datos: ','s'); 
 
%una opción para leer el fichero
f=fopen(nombre,'r');
if (f==-1)
    disp('Error al abrir el fichero de entrada');
else
    mat=fscanf(f,'%f',[4,inf]);
    mat=mat';
    fclose(f);
end
 
%mat=load(nombre); % otra opción para leer el fichero
% fin de la lectura
 
% Calculamos los porcentajes
[nf,~]=size(mat);
contTemp=0;
contPres=0;
contTiempo=0;
for i=1:nf
    if (mat(i,2)>155) % se rechaza por temperatura
        contTemp=contTemp+1;
    end
    if (mat(i,3)>60) % se rechaza por presión
        contPres=contPres+1;
    end
    if (mat(i,4)<2.1) % se rechaza por tiempo
        contTiempo=contTiempo+1;
    end
end
salida=input('Introduce el nombre del fichero de salida: ','s');
fsal=fopen(salida,'w');
if(fsal==-1)
    disp('Error al abrir el fichero de salida');
else
    fprintf(fsal,'Porcentaje de lotes rechazados por temperatura: %0.2f\n',contTemp*100/nf);
    fprintf(fsal,'Porcentaje de lotes rechazados por presión: %0.2f\n',contPres*100/nf);
    fprintf(fsal,'Porcentaje de lotes rechazados por tiempo: %0.2f\n',contTiempo*100/nf);
    fclose(fsal);
end
```