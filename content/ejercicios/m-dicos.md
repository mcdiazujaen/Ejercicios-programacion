---
title: "Médicos"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Médicos

##  Enunciado

Queremos conocer los datos estadísticos de una consulta médica de varios doctores. Para ello crea un programa principal que pregunte cuántos doctores tiene la clínica, cuántos pacientes han pedido cita para cada doctor, y cuál es el precio de la consulta para cada doctor. Crear u utilizar módulos para realizar las siguientes operaciones: 

  * **Módulo 1:** Pedir los datos de citas al usuario y devolverlos en un array. 
  * **Módulo 2:** Pedir el precio de la consulta de cada doctor y devolverlos en un array. 
  * **Módulo 3** : Calcular el tanto por ciento de pacientes que han ido a un doctor determinado, dado el array de citas. 
  * **Módulo 4** : La cantidad de dinero que ha ganado cada doctor, dadas las citas y el precio de las consultas. 
  * **Módulo 5** : La media de dinero que se gana por paciente en la clínica en general. 

##  Soluciones

###  Programa en Matlab 

####  Módulo 1 
```matlab


function c = PedirCitas( num )
% FUNCIÓN c = PedirCitas( num )
% Descripción: Pedir el numero de citas de los 3 médicos
% Parámetros de entrada:
%   num: ENTERO; número de médicos de la clínica
% Parámetros de salida:
%   c: ARRAY(num) DE ENTEROS; Citas de cada médico.
 
% Variables (internas):
%   x: ENTERO
 
c = zeros(1,num);
for x=1:num
    fprintf('Introduzca citas del medico %d',x);
    c(x) = input(': ');
end

```
####  Módulo 2 
```matlab


function c = PedirPrecios( num )
% FUNCION c = PedirPrecios( num )
% Descripción: Pedir el precio por cita de cada médico
% Parámetros de entrada:
%   num: ENTERO; número de médicos de la clínica
% Parámetros de salida:
%   c: ARRAY DE REALES; Precio de cada médico.
 
% Variables (internas):
%   num, x: ENTERO
 
c = zeros(1,num);
for x=1:num
    fprintf('Introduzca precio por cita del medico %d',x);
    c(x) = input(': ');
end

```
####  Módulo 3 
```matlab


function valor = PorcentajeDr( c, n )
% FUNCIÓN valor = PorcentajeDr( c, n )
% Descripción: Devuelve el porcentaje de pacientes que han tenido cita con
% el doctor n
% Parámetros de entrada:
%   c: ARRAY DE ENTEROS; citas de todos los doctores
%   n: ENTERO; Doctor para calcular el porcentaje
% Parámetros de salida:
%   valor: REAL; Porcentaje del medico n
 
% Variables (internas): Ninguna
 
valor = (c(n)/sum(c))*100;

```
####  Módulo 4 
```text


function ganado = GananciaDr( c, p )
% FUNCIÓN ganado = GananciaDr( c, p )
% Descripción: Devuelve la cantidad de dinero que ha ganado cada doctor
% Parámetros de entrada:
%   c: ARRAY DE ENTEROS; citas de todos los doctores
%   p: ARRAY DE REALES;  precios de todos los doctores
% Parámetros de salida:
%   ganado: ARRAY DE REALES; lo que ha ganado cada doctor
 
% Variables (internas):
%   tama, x: ENTERO
 
tama = length( c );
ganado = zeros(1,tama);
for x=1:tama
    ganado(x) = c(x)*p(x);
end

```
####  Módulo 5 
```text


function media = MediaPaciente( c, p )
% FUNCIÓN media = MediaPaciente( c, p )
% Descripción: Devuelve la media de dinero que se gana por paciente en la clínica en general
% Parámetros de entrada:
%   c: ARRAY DE ENTEROS; citas de todos los doctores
%   p: ARRAY DE REALES;  precios de todos los doctores
% Parámetros de salida:
%   media: REAL; la media de dinero por paciente en la clínica
 
% Variables (internas):
%   gana: ARRAY DE REALES
 
gana = GananciaDr( c, p );
media = sum(gana) / sum(c);

```
####  Programa principal 
```matlab


% Programa Medicos
% Entradas: Citas de los médicos y precios de los médicos
% Salidas: Ganancias, porcentajes de pacientes y ganancia de la clínica
% Variables: 
clear all;
num = input('¿Cuántos médicos hay en la clínica?: ');
citas = PedirCitas( num );
precios = PedirPrecios( num );
 
disp('Porcentajes:');
for doctor=1:num
    porcen = PorcentajeDr( citas, doctor );
    fprintf('Doctor %d: %f%%\n',doctor,porcen);
end
 
disp('Cada Doctor ha ganado:');
ganado = GananciaDr( citas, precios );
for doctor=1:num
    fprintf( 'Doctor %d: %f euros\n', ganado(doctor) );
end
 
disp('La clinica gana por paciente:');
fprintf(' %f euros\n', MediaPaciente( citas, precios );
```