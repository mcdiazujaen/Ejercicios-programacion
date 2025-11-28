---
title: "Elecciones de rector"
date: 2024-01-01
draft: false
categories: ['enunciado']
tags: ['sin_matlab', 'sin_solución']
---


# Elecciones de rector

##  Enunciado

En la universidad se realizan las elecciones de rector y se presentan _**M**_ candidatos. Los votos se realizan adscribiéndolos a cuatro sectores: PAS, alumnos, PDI permanente y PDI no permanente. Los resultados de las elecciones se recogen en una matriz que tiene _**M**_ filas (en cada fila están los resultados obtenidos por cada candidato en los 4 sectores) y 4 columnas los 4 sectores mencionados. 

Diseña un algoritmo que dada la matriz de resultados muestre en un diagrama de sectores el porcentaje de votos obtenidos por parte de cada sector por el candidato que ha obtenido más votos. 

Para la realización del algoritmo se pueden usar los siguientes módulos que ya están diseñados: 
```text


PROCEDIMIENTO Recuento(VAR votos)
ENTRADAS:
  (* Ninguna *)
SALIDAS:
   votos: ARRAY(1..M, 1..4) DE ENTEROS (* matriz con los votos de los candidatos, 
               los votos de cada candidato están en una fila y las columnas son 
               los votos obtenidos en cada sector: PAS, %alumnos, PDI permanente y PDI no permanente *)


PROCEDIMIENTO pie(x)
(* Descripción: la función dibuja un diagrama de sectores con los datos contenidos en el array x *)
ENTRADAS:
   x: ARRAY (1..4) DE REALES (* array con los porcentajes para dibujar un diagrama de sectores *)
SALIDAS:
   (* Ninguna *)

```
##  Soluciones