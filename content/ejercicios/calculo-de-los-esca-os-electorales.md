---
title: "Calculo de los escaños electorales"
date: 2024-01-01
draft: false
languages: ['c', 'matlab']
professors: ['angel']
categories: ['enunciado', 'análisis']
tags: ['sin_pseudocódigo']
---

# Calculo de los escaños electorales

##  Enunciado 

Vamos a ver como se convierten en escaños los votos de los sufridos ciudadanos siguiendo el método d'Hont. ¿Estas familiarizado con este método? Por si acaso te lo vamos a recordar. 

Supongamos que concurren 3 partidos a las elecciones y que la provincia o distrito electoral dispone de 2 escaños. El primer escaño se lo llevara el partido mas votado. Para el segundo escaño se dividen los votos de cada partido entre el numero de escaños obtenidos mas uno (el partido que no tenga todavía ningún escaño se dividirá entre 1) y se calculan los restos de dichas divisiones. El escaño se asigna al partido que tras esta operación tenga un resto mas elevado. Vamos a verlo con un ejemplo: 

```text

Partido 1: 6000 (Se lleva el escaño 1) <-- restos <-- 6000/(1+1) = 3000
Partido 2: 4000                        <-- restos <-- 4000/(1+0) = 4000 <-- Se lleva el escaño 2.
Partido 3: 2000                        <-- restos <-- 2000/(1+0) = 2000

```
El programa que te presentamos a continuación es para 3 partidos y 2 escaños, pero queda a tu entera disposición para que lo particularices -si dispones de datos-. Ten mucho cuidado porque un fallo en la programación puede hacer caer sobre ti una acusación de fraude electoral. 

Lo primero que hace este programa es inicializar a cero el vector **nEsca [ ]**. En este vector se va a almacenar el numero de escaños de cada partido: **nEsca [0]** contendrá el numero de escaños del partido numero 1, **nEsca [1]** los escaños del partido número 2, etc. Este vector se va a ir modificando a lo largo de la ejecución del programa. 

A continuación se almacenan en el vector **nVotos [ ]** los números de votos obtenidos por cada partido, estos datos serán introducidos por el usuario a través del teclado. 

La novedad de este programa es que incluye una función: **nextEsc(long *, int *)**. Esta función tiene como argumentos dos punteros a sendos vectores, es decir, las direcciones de memoria o los nombres de dos vectores. Cuando se llama a la función, **nextEsc(nVotos, nEsca)** se pasa la dirección de memoria de los vectores **nEsca [ ]** y **nVotos [ ]**. El nombre de un vector (como por ejemplo **nEsca**) es un puntero a la dirección del primer elemento. La función devuelve el numero del partido que ha conseguido el escaño y se almacena en la variable **esca**. Este numero sera cero si el escaño corresponde al primer partido, 1 si corresponde al segundo, etc. 

Con esta pequeña explicación ya estas en condiciones de escribir el programa y comprobar como funciona. 

##  Soluciones 

###  Programa en C por **Angel**

Solución comentada al Ejercicio: 
```c

 /* fichero elecciones.c*/
 /* Calculo de escanos por partido (d'Hondt). */
 #include <stdio.h>
 #define NESC 2 /* numero de escanos en liza. */
 #define NPAR 3 /* numero de partidos que concurren */
 void main(void) {
   int i, esca;
   int nEsca[NPAR]; /* nEsca{[NPAR]= no de escanos por partido*/
   long nVotos[NPAR]; /* nVotos[NPAR]=no de votos por partido*/
   int nextEsc(long *, int *); /* declaracion de funcion */
   for(i=0; i<NPAR; ++i)
      nEsca[i]=0;
      printf("Teclea el numero de votos de cada partido.\n");
      for (i=0; i<NPAR; ++i) {
         printf("\nPartido %d: ", i+1);
         scanf("%ld", &nVotos[i]);
      }
      for(i=0; i<NESC; ++i) { /* asignacion de escanos */
         esca = nextEsc(nVotos, nEsca);
         nEsca[esca] = nEsca[esca]+1;
      }
      for (i=0; i<NPAR; ++i)
         printf("\nEl partido %d ha obtenido %d escagnos.", i+1, nEsca[i]);
      printf("\n");
 }
 
 int nextEsc( long nVotos[], int nEsca[]) {
   int imaximo=0, i;
   long maximo=0;
   for( i=0; i<NPAR; ++i) {
      if( maximo<(nVotos[i]/(nEsca[i]+1)) ) {
         maximo=nVotos[i]/(nEsca[i]+1);
         imaximo=i;
      }
   }
   return imaximo;
 }

```
###  Programa en Matlab 
```matlab

%PROGRAMA Elecciones
%DESCRIPCIÓN: Diseñar un algoritmo para asignar escaños a los diferentes 
%    partidos que concurren en unas elecciones.
%ENTRADAS: Número de partidos, Votos que obtiene cada partido y Número de escaños a repartir.
%SALIDAS: Los escaños obtenidos por cada partido.
%VARIABLES:
%    npar, pos, nesc, conta, pmax:ENTEROS
%    votos, esca: ARRAY(npar) DE ENTEROS
 
%Pedir los partidos, sus votos y el número de escaños
npar = input('Introduzca el número de partidos:');
for pos=1:npar
    votos(pos) = input( ['Introduzca los votos para el partido ',num2str(pos),': '] );
end
nesc=input('Introduce el número de escaños:');
 
%Repartir los escaños
esca = zeros(1,npar);
for conta = 1:nesc
    pmax = nextEsc( votos, esca );
    esca(pmax)=esca(pmax)+1;
end
 
%Mostrar los escaños asignados a cada partido
for pos=1:npar
    disp( ['Partido ', num2str(pos) ': ', num2str(esca(pos)),' escaños'] );
end

```
* * *
```matlab

function  p = nextEsc( nVotos, nEsca )
%FUNCION p = nextEsc( nVotos, nEsca )
%DESCRIPCION: Devuelve cual es el partido que debería tener el siguiente escaño
%PARÁMETROS DE ENTRADA:
%    nVotos: ARRRAY DE ENTEROS; número de votos de cada partido
%    nEsca:  ARRRAY DE ENTEROS; número de escaños asignados actualmente a cada partido
%PARÁMETROS DE SALIDA:
%    p: ENTERO; partido al que le correspondería el siguiente escaño
 
%VARIABLES INTERNAS:
%    maximo, pos: ENTEROS
 
p=1;
maximo=nVotos(1);
for pos=2:length(nVotos)
    if maximo<( nVotos(pos)/(nEsca(pos)+1) ) 
        maximo=nVotos(pos)/(nEsca(pos)+1);
        p=pos;
    end
end
```