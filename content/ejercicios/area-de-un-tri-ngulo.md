---
title: "Area de un triángulo"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---

# Area de un triángulo

##  Enunciado 

Diseñar un algoritmo para leer las longitudes de los tres lados de un triángulo (L1, L2, L3) y calcular el área del mismo de acuerdo con la siguiente fórmula: ![Imagen:FormulaTriangulo.jpg](images/1/12/FormulaTriangulo.jpg)

##  Soluciones 

###  Diseño en pseudocódigo 
```text
 ALGORITMO AreaTriangulo
 ENTRADAS:
 	L1, L2, L3: ENTEROS  (* Longitudes de los lados del triángulo *)
 SALIDAS:
 	area: REAL           (* Área del triángulo definido por L1, L2 y L3 *)
 VARIABLES:
 	SP: REAL
 
 INICIO
 	ESCRIBIR "Introduzca la longitud de lado 1 del triángulo: "
 	LEER L1
 	ESCRIBIR "Introduzca la longitud de lado 2 del triángulo: "
 	LEER L2
 	ESCRIBIR "Introduzca la longitud de lado 3 del triángulo: "
 	LEER L3
 
 	SP <-- (L1 + L2 + L3) / 2
 
 	(* Suponemos que disponemos de una función matemática llamada raiz que realiza la raíz cuadrada de un valor *)
 	area <-- raiz(SP * (SP-L1) * (SP-L2) * (SP-L3))
 
 	ESCRIBIR "El área del triángulo es: ", area
 FIN
```

###  Programa en C 
```c

  #include <stdio.h>
  #include <stdlib.h>
  #include <math.h>
  int main(void){
    /*ENTRADAS*/
     int L1,L2,L3; // Longitudes de los lados del triangulo.
    /*SALIDAS*/
     float area; // Area del triangulo.
    /*VARIABLES*/
     float SP;
 
    /*INICIO*/
     printf ("Introduzca la longitud del lado 1 del triangulo:");
     scanf("%i",&L1);
     printf("Introduzca la longitud del lado 2 del triangulo:");
     scanf("%i", &L2);
     printf("Introduzca la longitud de lado 3 del triangulo:");
     scanf("%i",&L3);
     SP=(L1+L2+L3) /2.0; //Le añadimos el 0 para que la division sea real y no se pierdan decimales siendo una division entera.
     area=sqrt(SP*(SP-L1)*(SP-L2)*(SP-L3));
     printf("El area del triangulo es:%f",area);
 
    system("PAUSE");
 }
```

##  Soluciones 

###  Programa en Matlab 
```matlab

% Programa Area_Triangulo
% Descripcion: calcula el área de un triángulo introduciendo los lados.
% Entradas: Lados del triángulo.
% Salidas: Área del triángulo.
% Variables:
%    L1, L2, L3: ENTEROS
%    SP, Area: REAL
 
% Leemos los lados del triángulo
L1 = input('Introduce el primer lado del triángulo:');
L2 = input('Introduce el segundo lado del triángulo:');
L3 = input('Introduce el tercer lado del triángulo:');
% Calculamos el área del triángulo
SP = (L1+L2+L3)/2;
Area = sqrt(SP*(SP-L1)*(SP-L2)*(SP-L3));
% Mostramos el resultado
disp('El area es:');
disp(Area);
```