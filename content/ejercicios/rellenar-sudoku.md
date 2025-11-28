---
title: "Rellenar sudoku"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo']
categories: ['enunciado']
tags: ['sin_matlab']
---


# Rellenar sudoku

##  Enunciado 

Realizar un subalgoritmo con todos los subalgoritmos necesarios para rellenar un [sudoku](http://es.wikipedia.org/wiki/Sudoku "http://es.wikipedia.org/wiki/Sudoku") casilla por casilla. El algoritmo mostrará en pantalla el sudoku parcialmente relleno, teniendo en cuenta que: 

  * Aquellas casillas que estén rellenas mostrarán el número introducido. 
  * Las casillas vacías mostrarán los posibles valores que pueden introducirse. 

El algoritmo solicitará al usuario la casilla que desea rellenar (fila y columna) y el valor que desea introducir. El valor se guardará en la casilla si éste es un valor válido para la posición (véase las normas del [sudoku](http://es.wikipedia.org/wiki/Sudoku "http://es.wikipedia.org/wiki/Sudoku")) y se mostrará al usuario el estado actual del sudoku. 

##  Soluciones 

###  Diseño en Pseudocódigo 
```text


PROCEDIMIENTO Inicializa( VAR m )
ENTRADAS:
   (*Ninguna*)
SALIDAS:
   m: ARRAY (0..8,0..8,0..9) DE ENTEROS (*Matriz con los valores a 0 y los posibles valores a 1*)
VARIABLES:
   i,j,k: ENTEROS
INICIO 
   PARA i<--0 HASTA 8 HACER
      PARA j<--0 HASTA 8 HACER
         m(i,j,0) <-- 0
         PARA k<--1 HASTA 9 HACER
            m(i,j,k) <-- 1
         FIN_PARA
      FIN_PARA
   FIN_PARA
FIN_PARA
 
//----------------------------------
 
PROCEDIMIENTO Pinta( m )
ENTRADAS:
   m: ARRAY (0..8,0..8,0..9) DE ENTEROS (*Matriz con los valores y los posibles valores*)
SALIDAS:
   (*Muestra por pantalla la matriz del sudoku, mostrando los valores disponibles en
   aquellas casillas donde no se ha introducido aún ningún valor*)
VARIABLES:
    p: ARRAY (0..36,0..36) DE CARACTERES
    i, j, k, x, y: ENTEROS
INICIO    
   (*Inicializar la matriz p que se mostrará en pantalla*)
   PARA i<--0 HASTA 36 HACER
      PARA j<--0 HASTA 36 HACER
         p(i,j) <-- ' '
      FIN_PARA
   FIN_PARA
 
   (*Colocar bordes*)
   PARA i<--0 HASTA 36 HACER
      p(0,i)  <-- GRUESO
      p(36,i) <-- GRUESO
      p(i,0)  <-- GRUESO
      p(i,36) <-- GRUESO
   FIN_PARA
   PARA i<--1 HASTA 35 HACER
      PARA j<--4  HASTA 35 CON INCREMENTO 4 HACER
         p(j,i) <-- FINO
         p(i,j) <-- FINO
      FIN_PARA
   FIN_PARA
   PARA i<--1 HASTA 35 HACER
      PARA j<--12 HASTA 35 CON INCREMENTO 12 HACER
         p(j,i) <-- GRUESO
         p(i,j) <-- GRUESO
      FIN_PARA
   FIN_PARA
 
   (*Volcar matriz de enteros en matriz de caracteres*)
   PARA i<--0 HASTA 8 HACER
      PARA j<--0 HASTA 8 HACER
         SI m(i,j,0)<>0 ENTONCES
            x <-- 2+(4*i)
            y <-- 2+(4*j)
            p(x,y) <-- CHR(ORD('0')+m(i,j,0))
         SI_NO
            PARA k<--1 HASTA 9 HACER
              x <-- 1+(4*i)+((k-1) DIV 3)
              y <-- 1+(4*j)+((k-1) MOD 3)
              SI m(i,j,k)<>0 ENTONCES
                 p(x,y) <-- CHR(ORD('0')+k)
              FIN_SI
            FIN_PARA
         FIN_SI
      FIN_PARA
   FIN_PARA
 
   (*Pintar pantalla*)
   PARA i<--0 HASTA 36 HACER
      PARA j<--0 HASTA 36 HACER
         ESCRIBIR p(i,j)
      FIN_PARA
      ESCRIBIR SaltoDeLinea
   FIN_PARA
   ESCRIBIR SaltoDeLinea
FIN
 
//----------------------------------
 
FUNCION LeerEntero(min, max): ENTERO
ENTRADAS:
   min: ENTERO (*Valor mínimo que se puede leer*)
   max: ENTERO (*Valor máximo que se puede leer*)
SALIDAS:
   (*Un valor entero comprendido entre min y max*)
VARIABLES:
   valor: ENTERO
INICIO    
   REPETIR
      LEER valor
      SI valor<min O valor>max ENTONCES
         ESCRIBIR "El valor debe estar entre", min, " y ", max, ". Vuelva a Introducirlo."
      FIN_SI
   HASTA valor>=min Y valor<=max
 
   DEVOLVER valor
FIN
 
//----------------------------------
 
PROCEDIMIENTO QuitarOpcion( VAR m, x, y, v )
ENTRADAS:
   m: ARRAY (0..8,0..8,0..9) DE ENTEROS (*Matriz con valores y posibles valores*)
   x,y: ENTEROS (*Coordenadas donde se ha introducido el valor*)
   v: ENTERO    (*Valor introducido*)
SALIDAS:
   m: ARRAY (0..8,0..8,0..9) DE ENTEROS (*Matriz donde se han eliminado v como posible valor en las celdas correspondientes*)
VARIABLES:
   i,j,f,c: ENTEROS
 
   PARA i<--0 HASTA 8 HACER
      m(x,i,v) <-- 0  (*Quitar opción en fila*)
      m(i,y,v) <-- 0  (*Quitar opición en columna*)
   FIN_PARA
 
   (*Quitar opición en submatriz*)
   f <-- (x DIV 3)*3
   c <-- (y DIV 3)*3
   PARA i<--f HASTA f+2 HACER
      PARA j<--c HASTA c+2 HACER
         m(i,j,v) <-- 0
      FIN_PARA
   FIN_PARA
FIN
 
//----------------------------------
 
ALGORITMO CreaSudoku
ENTRADAS:
   x, y: ENTEROS (*Coordenadas de una casilla del sudoku*)
   valor: ENTERO (*Valor a Introducir en la casilla x,y*)
SALIDAS:
   (*Valores fijos y posibles de cada casilla del sudoku*)
   sudoku: ARRAY (0..8,0..8,0..9) DE ENTEROS
VARIABLES:
   (*No son necesarias*)   
CONSTANTES:
   GRUESO='*' 
   FINO=' ' 
INICIO
   Inicializa( sudoku )
   Pinta( sudoku )
   ESCRIBIR "Introduzca el valor de la casilla (0 para salir): "
   valor <-- LeerEntero(0,9)
   MIENTRAS valor <> 0 HACER
       ESCRIBIR "Introduzca la fila (0-8): "
       x <-- LeerEntero(0,8)
       ESCRIBIR "Introduzca la columna (0-8): "
       y <-- LeerEntero(0,8)
       SI sudoku(x,y,valor) = 0 ENTONCES
           ESCRIBIR "Ese valor no se puede poner en la casilla. Elija uno nuevo."
       SI_NO
          SI sudoku(x,y,0) <> 0 ENTONCES
             ESCRIBIR "La casilla ya tiene un valor. Elija otra casilla."
          SI_NO
             sudoku(x,y,0) <-- valor
             QuitarOpcion( sudoku, x, y, valor )
          FIN_SI
       FIN_SI
 
       Pinta( sudoku )
       ESCRIBIR "Introduzca el valor de la casilla (0 para salir): "
       valor <-- LeerEntero(0,9)
    FIN_MIENTRAS
FIN

```
###  Programa en C 
```c


#include <stdio.h>
#include <stdlib.h>
 
#define GRUESO  '*'
//#define GRUESO  219
#define FINO ' '
 
//----------------------------------
void Inicializa( int m[9][9][10] ){
   int i,j,k;
 
   for(i=0; i<=8; i++){
      for(j=0; j<=8; j++){
         m[i][j][0]=0;
         for(k=1; k<=9; k++){
            m[i][j][k]=1;
         }
      }
   }
}
//----------------------------------
void Pinta( int m[9][9][10] ){
    char p[37][37];
    int i, j, k, x, y;
 
    //Inicializar
   for(i=0; i<=36; i++){
      for(j=0; j<=36; j++){
         p[i][j]=' ';
      }
   }
   //Colocar bordes
   for(i=0;i<=36;i++){
      p[0][i]=GRUESO;
      p[36][i]=GRUESO;
      p[i][0]=GRUESO;
      p[i][36]=GRUESO;
   }
   for(i=1; i<=35; i++){
      for(j=4; j<=35; j+=4){
         p[j][i]=FINO;
         p[i][j]=FINO;
      }
   }
   for(i=1; i<=35; i++){
      for(j=12; j<=35; j+=12){
         p[j][i]=GRUESO;
         p[i][j]=GRUESO;
      }
   }
   //Volcar matriz de enteros en matriz de caracteres
   for(i=0; i<=8; i++){
      for(j=0; j<=8; j++){
         if(m[i][j][0]!=0){
            x=2+(4*i);
            y=2+(4*j);
            p[x][y]='0'+m[i][j][0];
         }else{
            for(k=1; k<=9; k++){
              x=1+(4*i)+((k-1)/3);
              y=1+(4*j)+((k-1)%3);
              if(m[i][j][k]!=0){
                 p[x][y]='0'+k;
              }
            }
         }
      }
   }
   //Pintar pantalla
   for(i=0; i<=36; i++){
      for(j=0; j<=36; j++){
         printf("%c", p[i][j]);
      }
      printf("\n");
   }
   printf("\n");
}
//----------------------------------
int LeerEntero(int min, int max){
    int entero;
 
    do{
        scanf("%i", &entero);
        if(entero<min || entero>max){
           printf("El valor debe estar entre %i y %i. Vuelva a introducirlo.\n", min, max);
        }
    }while(entero<min || entero>max);
 
    return( entero );
}
//----------------------------------
void QuitarOpcion( int m[9][9][10], int x, int y, int v ){
   int i,j,f,c;
 
   for (i=0; i<=8; i++){
      m[x][i][v]=0;  //Quitar en fila
      m[i][y][v]=0;  //Quitar en columna
   }
   //Quitar en submatriz
   f=(x/3)*3;
   c=(y/3)*3;
   for(i=f; i<=f+2; i++){
      for(j=c; j<=c+2; j++){
         m[i][j][v]=0;
      }
   }
 
}
//----------------------------------
 
int main( void ){
    int sudoku[9][9][10];
    int x, y, valor;
 
    Inicializa( sudoku );
    Pinta( sudoku );
    printf("Introduzca el valor de la casilla (0 para salir): ");
    valor=LeerEntero(0,9);
    while(valor!=0){
       printf("Introduzca la fila (0-8): ");
       x=LeerEntero(0,8);
       printf("Introduzca la columna (0-8): ");
       y=LeerEntero(0,8);
       if(sudoku[x][y][valor]==0){
           printf("Ese valor no se puede poner en la casilla. Elija uno nuevo.\n");
       }else{
          if(sudoku[x][y][0]!=0){
             printf("La casilla ya tiene un valor. Elija otra casilla.\n");
          }else{
             sudoku[x][y][0]=valor;
             QuitarOpcion( sudoku, x, y, valor );
          }
       }
 
       Pinta( sudoku );
       printf("Introduzca el valor de la casilla (0 para salir): ");
       valor=LeerEntero(0,9);
    }
 
    system("PAUSE");
}
```