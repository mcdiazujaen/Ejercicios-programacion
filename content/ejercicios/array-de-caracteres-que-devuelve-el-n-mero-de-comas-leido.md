---
title: "Array de caracteres que devuelve el número de comas leido"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo', 'matlab']
categories: ['enunciado']
---

# Array de caracteres que devuelve el número de comas leido

##  Enunciado 

Diseña un algoritmo que lea un array de caracteres hasta que se introduzca un punto, y que de cómo salida el número de comas encontradas, y el número de caracteres leídos. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text

  ALGORITMO ContarComas
  ENTRADAS: 
    V: ARRAY DE CARACTERES   (*Array donde contaremos el número de comas. La primera poscion del array es 1*)
  SALIDAS:
    n: ENTERO                (*Número de elementos que contiene el array*)
    coma: ENTERO             (*Número de comas que contiene el array*)
  VARIBLES:
    (*No son necesarias*)
  INICIO
    coma <-- 0
    n <-- 0
    ESCRIBIR "Introduzca los caracteres: "
    REPETIR
      n <-- n+1
      LEER V(n)
      SI V(n)=',' ENTONCES
        coma <-- coma+1
      FIN_SI
    HASTA ( V(n)='.' )
    ESCRIBIR "Se han leido ", n, " caracteres" 
    ESCRIBIR "El número de comas es:",coma 
  FIN

```
###  Programa en C
```c

 #include <stdio.h>
 #include <stdlib.h>
 #define TAMA 1000
 
 int main(void){
   //ENTRADAS:
   char V[TAMA]; //Array donde contaremos el numero de comas
   //SALIDAS:
   int n;        //Número de elementos que contiene el array
   int coma;     //Número de comas que contiene el array
   //VARIABLES:
     //No hay variables
 
   //Inicializar variables
   coma=0;
   n=0;
 
   printf("Introduzca los caracteres: ");
   do{
       n=n+1;
       scanf("%c",&V[n]);
       if(V[n]==','){
             coma=coma+1;
       }
    }while( V[n]!='.' );
    printf("Se han leído %i caracteres.\n",n);
    printf("El número de comas es:%i \n",coma);
 }

```
###  Programa en Matlab 
```matlab

%PROGRAMA LeerCaracteres
%DESCRIPCION: Algoritmo que lea un array de caracteres hasta que se introduzca un punto.
%ENTRADAS:
%   Array de caracteres.
%SALIDAS:
%   El número de comas y el número de caracteres.
%VARIABLES:
%   leido, comas, caracter: CARÁCTER
%   texto:CADENA DE CARACTERES
 
caracter=0;
comas=0;
leido='a';
while leido~='.',
   leido=input('Introduce un caracter:','s');
   if leido==',';
        comas=comas+1;
   end
   caracter=caracter+1;
end
texto=['Se han introducido', num2str(caracter), 'caracteres'];
disp(texto);
texto=['Se han introducido', num2str(comas), 'comas'];
disp(texto);
```