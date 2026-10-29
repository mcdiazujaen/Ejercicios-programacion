---
title: "Calculo del número E"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['análisis', 'enunciado']
tags: ['Sin Pseudocódigo']
---

# Calculo del número E

##  Enunciado 

El número **e** (2.7183...) se puede aproximar mediante la suma: 

![Imagen:Numero_e.GIF](images/0/05/Numero_e.GIF)

Sumatorio de 1/n! desde n=0 hasta n=N 

En esta expresión la precisión queda determinada por el valor N. El valor n! representa el factorial de n (1·2·...·(n -1)·n). Recordemos que, por definición, 0!=1. 

Escribir un programa que permita calcular la aproximación al número e dada por N (valor preguntado al usuario). Debe crearse una función recursiva que calcule el factorial, puesto que n!=n·(n-1)!. 

##  Soluciones 

###  Programa en C por **angel**
```c

 /*********************************************************
 *
 * MAKE: Este programa realiza la aproximacion al numero e.
 * Lo hemos realizado de 2 maneras:
 * - Recursivamente.
 * - Forma mas eficiente (sin usar recursividad).
 *
 * Un ejemplo: (introduciendo 10000 terminos)
 * - Recursividad: 12 segundos aproximadamente
 * - Eficientemente: Se obtiene el resultado instantaneamente.
 *
 **********************************************************/
 #include <stdio.h>
 #include <string.h>
 #define OK 1
 #define ERR -10001
 #define NO 0
 #define MAX_TERM 1000000
 float n_term;
 int eficiente;
 int lectura(int *eficiente, float *n_term);
 float calcular(float n_term);
 int sacarpantalla(float numeroe);
 float factorial(int n);
 int es_digito(char caracter[]);
 int main()
  {
   if (lectura(&eficiente, &n_term) == ERR)
    {
     printf("Error al leer el numero de terminos\n");
     return ERR;
    }
   if (sacarpantalla(calcular(n_term)) == ERR)
    {
     printf("Error al sacar por pantalla/calcular el numero\n");
     return ERR;
    }
   return OK;
  }
 /*********************************************************
 * Funcion: int sacarpantalla(float numeroe)
 *
 * IN: Toma la variable numeroe de tipo float.
 * OUT: Devuelve OK si lo consigue, ERR si hay algun
 * MAKE: Saca por pantalla el resultado. No modifica ninguna  variable.
 *
 **********************************************************/
 int sacarpantalla(float numeroe)
 {
  printf("\nEl valor de la aproximacion al numero e es: %f\n\n", numeroe);
  return OK;
 }
 /*********************************************************
 * Funcion: int lectura(int *eficiente, float *n_term)
 *
 * IN: Toma la direccion de la variable eficiente, y el numero de  términos
 * OUT: Nos devuelve OK si lo consigue ERR si hay algun fallo.
 * MAKE: Se encarga de leer el numero de terminos a calcular.  Modifica
 * n_term y eficiente.
 *
 **********************************************************/
 int lectura(int *eficiente, float *n_term)
 {
  char numero[5];
  char temp = 0;
  int continuar = NO;
  do {
      printf("\nIntroduzca el numero de terminos a calcular del numero e: ");
      gets(numero);
  } while ((*n_term = es_digito(numero)) == ERR || (*n_term < 1));
  do {
      printf("Desea usar el modo de calculo rapido? [S,N]:\t");
      fflush(stdin);
      fflush(stdout);
      scanf("%c", &temp);
      fflush(stdin);
      if ((temp == 'S') || (temp == 'N') || (temp == 's') || (temp == 'n'))
       {
         continuar = OK;
         if ((temp == 'S') || (temp == 's'))
         *eficiente = OK;
        else
         {
          *eficiente = NO;
          if (strlen(numero) > 4) /* Permitimos hasta el numero 9999 */
          {
             printf("\nSi desea calcular este numero con recursividad puede ocasionar problemas."); 
 printf("\nIntentelo con la manera eficiente.\n");
 return ERR;
 }
 }
 }
  else
  {
   continuar = NO;
   printf("Por favor introduzca un valor valido!!! \n");
  }
  } while (continuar != OK);
  return OK;
 }
 /*********************************************************
 * Funcion: float calcular(float terminos)
 *
 * IN: Numero de terminos para realizar la aproximacion.
 * OUT: La aproximacion al numero e si es correcto o ERR si ha habido un
 * fallo.
 * MAKE: Calcula la serie: 1 entre el factorial de un numero dado.
 *
 **********************************************************/
 float calcular(float terminos)
 {
  float e = 0;
  float facto = 1; /* Va a ir acumulando el valor del factorial cuando se haya seleccionado "eficiente" */
  int n;
  if (eficiente == OK)
   {
    printf("\nSe esta calculando el numero e de la manera mas eficiente.");
    e = 1;
    for (n = 1; n < (int) terminos; ++n)
     {
      facto *= n;
      e += 1 / facto;
     }
    return e;
   }
   else /* Calculamos la serie usando recursividad */
    {
     do {
          e += (1 / factorial((int) terminos--));
         } while (terminos >= 0);
     printf("\nSe esta calculando el numero e usando recursividad.");
    }
    return e;
   }
 /*********************************************************
 * Funcion: float factorial (int n)
 *
 * IN: Numero de terminos de los que se calcularan sucesivos   factoriales
 * OUT: El factorial del numero o ERR si ha habido algun error.
 * MAKE: Calcula el factorial de un numero dado.
 *
 **********************************************************/
 float factorial(int n)
 {
 if (n == 0)
      return 1;
  else
     return (n * factorial(n - 1));
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
   /* Si la cadena esta vacía */
   if (caracter[0] == 0)
        return ERR;
   if (caracter[0] == '-') /* Si se ha introducido un numero negativo */
     {
      i = 1;
      /* Empezamos el bucle para ver si es caracter desde el siguiente caracter */
      rango = 7;
     }
    else /* Debe un numero positivo o hay algun error */
     {
      i = 0;
      rango = 7;
     }
 /* Comprobamos que todos los elementos sean digitos */
 /* El mayor numero permitido es 9999999 */
 if ((int) strlen(caracter) > rango)
 {
  printf("No puede introducir esa cantidad de numeros!!!\n");
  printf("Es demasiado grande. Rango: -9999999 y 9999999\n");
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

function res=factorial_recursivo(n)
% FUNCIÓN res=factorial_recursivo(n)
% DESCRIPCIÓN: Calcula el factorial de n de forma recursiva
% ENTRADAS:
%    n: ENTERO;  valor para calcular el factorial
% SALIDAS:
%    res: ENTERO; factorial de n
% VARIABLES:
%    No son necesarias
 
if n==0||n==1,
    res=1;
else
    res=n*factorial_recursivo(n-1);
end
```

* * *
```matlab

%Programa Calcular_e
%Descripción: Aproxima el valor del número e
%Entradas: Número de iteraciones
%Salidas: El valor de e aproximado
%Variables:
%    N,n: ENTEROS;
%    aprox: REAL.
 
%Pedir el factor de aproximacion (iteraciones)
N=input('Introduzca el número de términos (<170):');
aprox=0;
%Calcular e
for n=0:N,
    aprox=aprox+(1/factorial_recursivo(n));
end
%Mostrar resultado
disp(aprox);
```