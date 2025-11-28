---
title: "Busca del número mayor y menor"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['enunciado', 'análisis']
tags: ['sin_pseudocódigo']
---


# Busca del número mayor y menor

  

##  Enunciado 

Escribir un programa que pida por teclado una serie de números enteros, los almacene en una tabla estática y posteriormente escriba por pantalla todos los números introducidos indicando además cual es el mayor y el menor. 

##  Análisis 

Lo primero que debe hacer el programa es preguntar al usuario cuantos números se van a introducir y comprobar que dicha cantidad es menor que la dimensión de la tabla. Para dicha dimensión debe definirse una constante (por ejemplo MAX_DIMENSION) a la cual se puede asignar un valor razonable (por ejemplo, 100). 

Funciones C a utilizar: 

• scanf: para leer números introducidos por el teclado. 

• printf: para imprimir por pantalla. 

Ejemplo de ejecución: lo que se vería por pantalla debe ser algo así como 
```text


Introduce la cantidad de números:
3
Introduce los números:
5
7
2
Los números introducidos son:
5
7
2
El mayor es el 7.
El menor es el 2.


```
##  Soluciones 

###  Programa en C por **Angel**
```c


 /**********************************************************/
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #define OK 1
 #define ERR -10001
 #define MAX_DIM 100
 int enteros[MAX_DIM]; /* Array para guardar los enteros */
 int num_total;
 int lectura(void);
 int sacarpantalla(int max, int min, int num_total);
 int calcular(int *max, int *min, int total);
 int es_digito(char caracter[]);
 int main()
 {
   int menor; /* Numero menor */
   int mayor; /* Numero mayor */
   if (lectura() == ERR)
    {
     printf("Error al leer el numero de terminos.\n");
     return ERR;
    }
   if (calcular(&mayor, &menor, num_total) == ERR)
    {
     printf("Error al intentar calcular el mayor y el menor");
     return ERR;
    }
  if (sacarpantalla(mayor, menor, num_total) == ERR)
   {
    printf("Error al mostrar por pantalla.\n");
    return ERR;
   }
  return OK;
 }
 /*********************************************************
 * Funcion: int lectura(int *total)
 *
 * IN: Toma una variable tipo int.
 * OUT: Devuelve OK si se ha leido correctamente, ERR si hay algun  fallo.
 * MAKE: Obtiene los numeros que introduce el usuario y los guarda
 * en un array de enteros
 **********************************************************/
 int lectura(void)
 {
  int continuar = OK;
  int n;
  char numeros[MAX_DIM];
  for (n = 0; n < (int) strlen(numeros); n++)
  numeros[n] = '0';
  printf("\nCuantos numeros va a introducir? --> ");
  do {
       gets(numeros);
       continuar = OK;
       if ((num_total = es_digito(numeros)) == ERR)
            continuar = ERR;
       if (num_total <= 0)
        {
          printf("Debe introducir un numero positivo.\n");
          continuar = ERR;
        }
     } while (continuar != OK);
  printf("\nIntroduzca los numeros: \n");
  for (n = 0; n < num_total; n++)
   {
    gets(numeros);
    if ((enteros[n] = es_digito(numeros)) == ERR)
     {
      printf("Error al leer el numero, por favor repita introduccion.\n");
      n--; 
     }
  }
 return OK;
 }
 /*********************************************************
 * Funcion: int calcular(int *max, int *min, int num_total)
 *
 * IN: *max y *min que acumulan el numero mayor y menor. num_total
 * acumula la cantidad de numeros que se van a introducir.
 * OUT: OK si se ha realizado correctamente o ERR si hay fallos.
 * MAKE: Encuentra el minimo y el maximo de los numeros introducidos
 *
 **********************************************************/
 int calcular(int *max, int *min, int total)
 {
  int n;
  *min = *max = enteros[0]; /* Lo inicializamos */
  for (n = 1; n < total; n++)
  {
   if (*min > enteros[n])
      *min = enteros[n];
   if (*max < enteros[n])
      *max = enteros[n];
  } 
  return OK;
 }
 /*********************************************************
 * Funcion: int sacarpantalla(int max, int min, int num_total)
 *
 * IN: toma el valor maximo,minimo y total de elementos
 * OUT: devuelde ERR si no puede y OK si puede 
 * MAKE: Nada
 *
 **********************************************************/
 int sacarpantalla(int max, int min, int num_total)
 {
  int n;
  printf("Los numeros introducidos son: ");
  for (n = 0; n < num_total; n++)
  printf("%d, ", enteros[n]);
  printf("\nMinimo: %d", min);
  printf("\nMaximo: %d\n", max);
  return OK;
 }
 /*********************************************************
 * Funcion: int es_digito(char caracter)
 *
 * IN: Se le da una serie de caracteres para que se pasen a numero
 * OUT: Nos devolvera ERR si se produce un eroor
 * MAKE: Comprueba la integridad de los datos
 *
 **********************************************************/
 int es_digito(char caracter[])
 {
  int i;
  int num = 0;
  int rango;
  /* Si la cadena esta vacia */
  if (caracter[0] == 0)
  return ERR;
  if (caracter[0] == '-') /* Si se ha introducido un numero negativo */
  {
   i = 1;
   /* Empezamos el bucle para ver si es caracter desde el siguiente caracter */
   rango = 5;
  }
  else /* Debe ser un numero positivo o hay algun error */
   {
    i = 0;
    rango = 4; 
   }
  /* Comprobamos que todos los elementos sean digitos */
  /* El mayor numero que permitimos es 9999 */
  if ((int) strlen(caracter) > rango)
  {
    printf("No puede introducir esa cantidad de numeros!!!\n");
    printf("Es demasiado grande. Introduzca numeros entre -9999 y 9999\n");
    return ERR;
  }
  for (i = i; i < (int) strlen(caracter); i++)
    if (caracter[i] < '0' || caracter[i] > '9')
     {
      printf("\nIntroduzca unicamente digitos, por favor.\n");
      return ERR;
     }
  /* Si solo se ha introducido un caracter */
  if (strlen(caracter) == 1)
  return num = caracter[0] - '0'; /* Devolvemos el digito */
  /* Si hay mas de un caracter */
  for (i = 0; i != (int) strlen(caracter); i++)
  num = (num * 10) + (caracter[i] - '0');
  return num;
 }

```
###  Programa en Matlab 
```matlab


%PROGRAMA BuscaMayorMenor
%DESCRIPCION: Escribir un programa que pida por teclado una serie de números enteros, 
%   los almacene en un array y posteriormente escriba por pantalla todos los números 
%   introducidos indicando además cual es el mayor y el menor.
%ENTRADAS: números enteros
%SALIDAS: El vector, el valor máximo y el valor mínimo.
%VARIABLES:
%   dim, max, min: ENTEROS
%   v:ARRAY(dim) DE ENTEROS
 
% Leer los datos de entrada
dim=input('Introduce la dimensión: ');
v=zeros(1,dim);
for pos=1:dim
   v(pos)=input('Introduce un número: ');
end
 
%Buscar máximo y mínimo
max=v(1);
min=v(1);
for pos=2:dim
   if v(pos)>max
      max=v(pos);
   end
   if v(pos)<min
      min=v(pos);
   end
end
 
% Mostrar el vector
disp('El vector es:');
for pos=1:dim
   disp(v(pos));
end
% Mostrar máximo y mínimo
disp('El máximo es:');
disp(max);
disp('El mínimo es:');
disp(min);
```