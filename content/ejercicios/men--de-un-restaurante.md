---
title: "Menú de un restaurante"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
tags: ['Sin C', 'Sin Matlab']
---

# Menú de un restaurante

##  Enunciado 

El siguiente es el menú de un restaurante de bocadillos. Diseñar un algoritmo capaz de leer el número de unidades consumidas de cada alimento ordenado y calcular la cuenta total. 

  * Bocadillo de jamón (250 pts) 
  * Bocadillo de queso (200 pts) 
  * Patatas fritas (100 pts) 
  * Refresco (175 pts) 
  * Cerveza (125 pts) 

##  Soluciones 

###  Diseño en pseudocódigo 
```text
ALGORITMO Menu
ENTRADAS:
	jamon: ENTERO; Cantidad de bocadillos de jamón
	queso: ENTERO; Cantidad de bocadillos de queso
	patatas: ENTERO; Cantidad de patatas fritas
	refrescos: ENTERO; Cantidad de refrescos
	cervezas: ENTERO; Cantidad de cervezas
SALIDAS:
	total: ENTERO; La cuenta total
VARIABLES:

INICIO
	ESCRIBIR “Introduzca la cantidad servida de ...”
	ESCRIBIR “... bocadillos de jamón: ”
	LEER jamon
	ESCRIBIR “... bocadillos de queso: ”
	LEER queso
	ESCRIBIR “... patatas fritas: ”
	LEER patatas
	ESCRIBIR “... refrescos: ”
	LEER refrescos
	ESCRIBIR “... cervezas: ”
	LEER cervezas

	total <-- jamon*250 + queso*200 + patatas*100 + refrescos*175 + cerveza*125 

	ESCRIBIR “El total de la factura es: ”, total,“ pesetas.”
FIN
```