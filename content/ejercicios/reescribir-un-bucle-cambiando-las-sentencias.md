---
title: "Reescribir un bucle cambiando las sentencias"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Reescribir un bucle cambiando las sentencias

##  Enunciado 

Cambiando simplemente el orden de las sentencias (sin cambiar cómo se ha escrito ninguna de ellas), hacer que el bucle siguiente escriba los números del 1 al 10. 
```text
 Numero <-- 1
 MIENTRAS Numero < 11 HACER
        Numero <-- Numero + 1
        ESCRIBIR Numero
 FIN_MIENTRAS
```

##  Soluciones 

Lo único que debemos hacer es cambiar la posición de las sentencias que hay dentro del bucle MIENTRAS. El bucle quedaría: 
```text
 Numero <-- 1
 MIENTRAS Numero < 11 HACER
        **ESCRIBIR Numero**
        **Numero <-- Numero + 1**
 FIN_MIENTRAS
```