---
title: "Porcentajes de notas"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['sin_c', 'sin_matlab']
---

# Porcentajes de notas

##  Enunciado 

Queremos conocer los datos estadísticos de una asignatura, por lo tanto, necesitamos un algoritmo que lea el número de suspensos, aprobados, notables y sobresalientes de una asignatura, y nos devuelva: 

  * El tanto por ciento de alumnos que han superado la asignatura. 
  * El tanto por ciento de suspensos, aprobados, notables y sobresalientes de la asignatura. 

##  Soluciones 

###  Diseño en pseudocódigo 
```text
ALGORITMO Estadisticas
ENTRADAS:
   suspensos: ENTERO      (* Número de suspensos de la asignatura *)
   aprobados: ENTERO      (* Número de aprobados de la asignatura *)
   notables: ENTERO       (* Número de notables de la asignatura *)
   sobresalientes: ENTERO (* Número de sobresalientes de la asignatura *)
SALIDAS:
   aptos: REAL (* Porcentaje de alumnos que han superado la asignatura *)
   p_sus: REAL (* Porcentaje de suspensos *)
   p_apr: REAL (* Porcentaje de aprobados *)
   p_not: REAL (* Porcentaje de notables *)
   p_sob: REAL (* Porcentaje de sobresalientes *)
VARIABLES:
   alumnos: ENTERO
INICIO
   ESCRIBIR "¿Cuántos alumnos suspensos?: "
   LEER suspensos
   ESCRIBIR "¿Cuántos alumnos aprobados?: "
   LEER aprobados
   ESCRIBIR "¿Cuántos alumnos notables?: "
   LEER notables
   ESCRIBIR "¿Cuántos alumnos sobresalientes?: "
   LEER sobresalientes
 
   alumnos <-- suspensos + aprobados + notables + sobresalientes
   aptos <-- (aprobados + notables + sobresalientes) * 100 / alumnos
   ESCRIBIR "El ", aptos, "% de alumnos ha superado la asignatura."
 
   p_sus <-- suspensos * 100 / alumnos
   p_apr <-- aprobados * 100 / alumnos
   p_not <-- notables * 100 / alumnos
   p_sob <-- sobresalientes * 100 / alumnos
 
   ESCRIBIR "Hay un ", p_sus, "% de alumnos suspensos."
   ESCRIBIR "Hay un ", p_apr, "% de alumnos aprobados."
   ESCRIBIR "Hay un ", p_not, "% de alumnos notables."
   ESCRIBIR "Hay un ", p_sob, "% de alumnos sobresalientes."
FIN
```