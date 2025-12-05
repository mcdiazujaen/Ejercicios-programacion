---
title: "Errores subalgoritmos"
date: 2024-01-01
draft: false
languages: ['pseudocódigo']
categories: ['enunciado']
---

# Errores subalgoritmos

##  Enunciado 

En estos subalgoritmos se han cometido errores, identifique estos errores y diga cómo podrían solucionarse. 

**AVISO:** Las líneas aparecen numeradas para facilitar la referencia a los errores 

###  Subalgoritmo 1 
```text
01 FUNCION FACTORIAL (N:ENTERO)
02 ENTRADA:
03    N, un entero positivo.
04 SALIDA:
05    El factorial de N.
06 VARIABLES:
07    i: ENTERO
08    resultado: ENTERO
09 INICIO
10    resultado <-- 0
11    PARA i = 0 HASTA N HACER
12       resultado <-- resultado + N
13    FIN_PARA
14 FIN
```

###  Subalgoritmo 2 
```text
01 PROCEDIMIENTO PRIMO (N:ENTERO, salida: LOGICO)
02 ENTRADA:
03    N, un entero positivo.
03 SALIDA:
04    salida valdrá VERDAD si N es primo y FALSO si no lo es.
05 VARIABLES:
06    i: ENTERO
07 INICIO
08    i <-- 2
09    Salida <-- FALSO
10    MIENTRAS i<=N HACER
11       SI (N MOD i)=0 ENTONCES
12          Salida<--FALSO
13          i<--N
14       SI NO
15          i<--2*i
16       FIN_SI
17    FIN_MIENTRAS
18 FIN
```

##  Soluciones 

###  Subalgoritmo 1 

###  Subalgoritmo 2