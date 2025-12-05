---
title: "Estación meteorológica"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Estación meteorológica

##  Enunciado

Tenemos una estación meteorológica que nos proporciona los datos de temperaturas a lo largo de una semana completa, empezándose a medir cualquier día entre el lunes y el domingo. Los datos se almacenan en un fichero de 3 líneas: la 1ª almacena el día de la semana en el que se empiezan a tomar medidas, la 2ª para temperaturas mínimas y la 3ª para las máximas. Por ejemplo: 
```text

miércoles
 2    0    4    6    5    7    6		
12    9   10   20   16   18   14		

```
Lo que significa que los datos de este archivo se empiezaron a medir el miércoles, y el viernes (tercer dato de cada fila) hubo una temperatura mínima de 4 y máxima de 10 

```text
**Apartado 1.** Implementa un módulo que dado el nombre de un archivo con el formato anteriormente indicado devuelva en un parámetro el día de la semana de inicio y en otro una matriz con los datos de las temperaturas. 

**Apartado 2.** Implementa un programa que pida al usuario el nombre del archivo con los datos de las temperaturas y calcule y muestre un vector con la diferencia entre temperaturas máxima y mínima de cada día de la semana y el día en el que se obtuvo una mayor diferencia entre ambas. Si hay varios con el mismo valor se puede devolver cualquiera de ellos. 
Para el ejemplo anterior, el vector que debe devolver es 

10	9	6	14	11	11	8

Y el día: sábado (diferencia 14 y cuarto día, empezando desde el miércoles) 

```
##  Soluciones

###  Programa en Matlab 

####  Apartado 1 
```matlab

function [dia,temperaturas]=Lectura(nombre)
%Parámetros de entrada:
%   nombre: nombre del fichero donde están los datos
%Parámetros de salida:
%   dia: día de la semana en que comienzan las mediciones (1ª fila 
%         fichero)
%   temperaturas: matriz con 2 filas (temperatura máxima y mínima de 
%   los días de la semana)
 
fich=fopen(nombre,'r');
if (fich==-1)
    dia=' ';
    temperaturas=[];
else
    dia=fscanf(fich,'%s',1);
    temperaturas=fscanf(fich,'%d',[7,2]);
    fclose(fich);
    temperaturas=temperaturas';
end

```
####  Apartado 2 
```matlab

%Programa Temperaturas
%Entradas:
%   nombre: nombre del fichero donde están los datos,
%       día de la semana en que comienzan las mediciones y 
%       temperaturas máxima y mínima de los días de la semana)
%Salidas:la diferencia entre temperaturas máxima y mínima de cada día de la
%       semana y el día en el que se obtuvo una mayor diferencia entre ambas
 
nombrefich=input('Introduce el nombre del fichero: ','s');
[inicio,temp]=Lectura(nombrefich); 
if (inicio==' ')
    disp('Error al abrir el fichero');
else
    diferencias=temp(2,:)-temp(1,:);
    [mayor,pmayor]=max(diferencias);
    switch (inicio)
        case 'lunes'
            pos=1;
        case 'martes'
            pos=2;
        case 'miércoles'
            pos=3;
        case 'jueves'
            pos=4;
        case 'viernes'
            pos=5;
        case 'sábado'
            pos=6;
        case 'domingo'
            pos=7;
    end
    dias=[pos:1:7,1:1:pos-1];
    switch (dias(pmayor))
        case 1
            diamayor='lunes';
        case 2
            diamayor='martes';
        case 3
            diamayor='miércoles';
        case 4
            diamayor='jueves';
        case 5
            diamayor='viernes';
        case 6
            diamayor='sábado';
        case 7
            diamayor='domingo';
    end
    disp('Las diferencias de temperatura en los días han sido: ');
    disp(diferencias);
    disp(['La diferencia máxima se alcanzó el ',diamayor,' con ',num2str(mayor),' grados']);
end
```