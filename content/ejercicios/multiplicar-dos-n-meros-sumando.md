---
title: "Multiplicar dos números sumando"
date: 2024-01-01
draft: false
languages: ['matlab']
categories: ['enunciado']
---

# Multiplicar dos números sumando

##  Enunciado

Implementa un programa que obtenga el producto de dos números enteros a base de sumas. Se ha de tener en cuenta los signos. 

##  Soluciones

###  Programa en Matlab 
```matlab

%Programa ProductoSumas
%Entrada: 
%  a,b: dos números enteros
%Salida:
%  res: resultado de a*b hecho a base de sumas
 
a=input('Introduce el primer número: ');
b=input('Introduce el segundo número: ');
res=0;
if (b>0)
    signo=1;
else
    b=-b;
    signo=-1;
end
 
for x=1:b
    res=res+a;
end
 
res=res*signo;
disp(['a*b=',num2str(res)])
```