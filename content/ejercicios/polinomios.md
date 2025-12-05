---
title: "Polinomios"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Polinomios

##  Enunciado

Una posible representación para un polinomio P es un vector en el que en cada celda se encuentra almacenado el coeficiente con grado igual a la `posición-1` que ocupa en dicho vector. Un ejemplo sería el polinomio de grado 6, **`P(x)=9x6-5x5+4x3-18x+1`** que vendría representado mediante un vector de la forma: 

```text
 1 |  -18 |  0 |  4 |  0 |  -5 |  9   
```
---|---|---|---|---|---|---  
  
Utilizando dicha representación, realizar en Matlab los siguientes apartados: 

```text
**Apartado 1.** Implementar una función que dados un polinomio P y un valor de x, devuelva P(x), es decir, el resultado de evaluar el polinomio para el valor x. 

**Apartado 2.** Implementar una función que dado un polinomio cualquiera devuelva la derivada de dicho polinomio. Para el ejemplo anterior: 

 -18 |  0 |  12 |  0 |  -25 |  54   
```
---|---|---|---|---|---  
  
```text
**Apartado 3.** Implementar un programa que pida al usuario que introduzca un polinomio y un valor y, utilizando las funciones anteriores, muestre por pantalla el resultado de evaluar el polinomio para ese valor así como su derivada, siguiendo el formato (para el ejemplo): 

**`P’(x)= 54.0x^5 - 25.0x^4 + 12.0x^2 - 18.0**`

```
##  Soluciones

###  Programa en Matlab 

####  Apartado 1 
```matlab

function valor=Evalua(p,x)
%Parámetros de entrada:
%   p: un vector que representa un polinomio. El primer elemento
%     del vector es el coeficiente independiente
%   x: valor para evaluar p
%Parámetros de salida:
%   el resultado de evaluar p en x
 
t=length(p);
valor=0;
for g=1:t
    valor=valor+p(g)*(x^(g-1));
end

```
####  Apartado 2 
```text
function pd=Derivada(p)
%Parámetros de entrada:
%   p: un vector que representa un polinomio. El primer elemento
%     del vector es el coeficiente independiente
%Parámetros de salida:
%   pd: polinomio derivada de p
 
pd=[];
t=length(p);
for g=2:t
    pd=[pd (p(g)*(g-1))];
end

```
####  Apartado 3 
```matlab

%Programa Polinomio
%Entradas:
%   un polinomio (representado como vector, empieza con el término 
%        independiente en la primera posición)
%   un valor 
%Salidas:
%   el resultado de evaluar el polinomio con el valor dado
%   el polinomio derivado del dado
 
poli=input('Introduce entre corchetes los coeficientes del polinomio, empieza por el menor grado: ');
x=input('Introduce el punto donde evaluarlo: ');
y=Evalua(poli,x);
polider=Derivada(poli);
disp(['Resultado evaluación: ',num2str(y)]);
disp('Polinonimo derivada: ');
t=length(polider);
if (t==0)
    disp('No hay polinomio: ');
else
    for g=t:-1:1
        if(polider(g)~=0)  % lo mostramos si es distinto de cero
            if(g==1)  % término independiente no va multiplicado
                fprintf('%0.1f',polider(g))
            else
                if (polider(g)>=0 && g~=t) % coef. positivo y no es el primer escrito
                    fprintf('+%0.1f*x^%d',polider(g),g-1);
                else % coeficiente negativo, ya tiene el signo o el primero que no lleva
                    fprintf('%0.1f*x^%d',polider(g),g-1);
                end
            end
        end
    end
    fprintf('\n');
end
```