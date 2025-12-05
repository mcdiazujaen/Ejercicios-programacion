---
title: "Operación con cadena de caracteres"
date: 2024-01-01
draft: false
languages: ['c', 'pseudocódigo', 'matlab']
categories: ['enunciado']
---

# Operación con cadena de caracteres

##  Enunciado 

Realizar un subalgoritmo que dada una cadena de caracteres obtenga otra cadena de caracteres en la que se han eliminado todas las subcadenas formadas por más de un espacio en blanco. Por ejemplo, la cadena “la-----asignatura---de---fundamentos----de----informática---es---interesante” debe quedar “la-asignatura-de-fundamentos-de-informática-es-interesante”, donde hemos representado el espacio en blanco con el guión “-”. 

##  Soluciones 

###  Pseudocódigo 
```text
PROCEDIMIENTO Blancos(Ent, VAR Sal, tam1, VAR tam2)
ENTRADAS:
   Ent: ARRAY [1..1000] DE CARACTERES  _(frase con varios espacios entre palabras)_
   tam1: ENTERO   _(el tamaño de Ent)_
SALIDAS:
   Sal: ARRAY [1..1000] DE CARACTERES  _(frase de entrada con un solo espacio entre palabras)_
   tam2: ENTERO   _(el tamaño de Sal)_
VARIABLES:
   i: ENTERO
INICIO
   tam2<--0
   i<--1
   MIENTRAS i<=tam1 HACER
      tam2<--tam2+1
      Sal(tam2)<--Ent(i)
      SI Ent(i)=' ' ENTONCES
         MIENTRAS Ent(i)=' ' HACER
             i<--i+1
         FIN_MIENTRAS
      SI NO 
         i<--i+1
      FIN_SI
   FIN_MIENTRAS
FIN
```