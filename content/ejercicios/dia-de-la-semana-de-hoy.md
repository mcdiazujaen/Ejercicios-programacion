---
title: "Dia de la semana de hoy"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---


# Dia de la semana de hoy

##  Enunciado

Realiza un programa que pida al usuario el día del mes en el que estamos y en qué día empezó dicho mes, es decir que diga si fue lunes, martes, miércoles, jueves, viernes, sábado o domingo. Entonces devolverá el día de la semana en que estamos. 

Por ejemplo, si el usuario dice que hoy es día 10 y el mes empezó en lunes, entonces el sistema devolverá: Miércoles. Si el usuario dice que hoy es día 23 y el mes empezó en jueves, entonces el sistema devolverá que hoy es viernes. 

Observación: En este ejercicio se requiere usar dos estructuras switch, una para decidir el desplazamiento dependiendo del día de la semana, y otra para devolver la respuesta dependiendo del resto. 

##  Soluciones 

###  Programa en Matlab 
```matlab


% Programa DiaSemana
% Entradas:
%   - Día de la semana del primer día del mes
%   - Número del día para saber su día de la semana
% Salidas:
%   Mensaje con el día de la semana del número indicado
% Variables:
 
clear all
%Leer datos de entrada.
dia1 = input('¿En qué día de la semana empezó el mes?: ','s');
num_hoy = input ('¿Qué día es hoy?: ');
 
%Calcular acumulador según el primer dia del mes.
switch dia1
    case {'l','L','lunes','Lunes','LUNES'}
        acum=0;
    case {'m','M','martes','Martes','MARTES'}
        acum=1;
    case {'x','X','miercoles','Miercoles','MIERCOLES','miércoles','Miércoles'}
        acum=2;
    case {'j','J','jueves','Jueves','JUEVES'}
        acum=3;
    case {'v','V','viernes','Viernes','VIERNES'}
        acum=4;
    case {'s','S','sabado','Sabado','SABADO','sábado','Sábado'}
        acum=5;
    case {'d','D','domingo','Domingo','DOMINGO'}
        acum=6;
    otherwise
        disp('Día de la semana incorrecto')
        acum=-1;
end
if acum>=0
    %Calcular valor del día de la semana actual.
    dia_hoy = mod(num_hoy+acum,7);
    %Mostrar dia de la semana.
    switch dia_hoy
        case 0
            disp('Hoy es DOMINGO');
        case 1
            disp('Hoy es LUNES');
        case 2
            disp('Hoy es MARTES');
        case 3
            disp('Hoy es MIERCOLES');
        case 4
            disp('Hoy es JUEVES');
        case 5
            disp('Hoy es VIERNES');
        case 6
            disp('Hoy es SABADO');
    end
end
```