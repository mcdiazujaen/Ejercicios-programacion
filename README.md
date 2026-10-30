# WikiEjercicios - Sitio Hugo

Este directorio contiene el sitio WikiEjercicios convertido al framework Hugo.

## Estructura del Proyecto

```text
hugo_deploy/
├── config.toml              # Configuración de Hugo
├── content/
│   └── ejercicios/          # 185 ejercicios en formato Markdown
├── static/
│   └── images/              # Imágenes de los ejercicios
├── themes/
│   └── wikiejercicios/      # Tema personalizado
│       └── layouts/
│           ├── _default/
│           │   ├── baseof.html   # Plantilla base
│           │   ├── single.html   # Página individual de ejercicio
│           │   └── list.html     # Lista de ejercicios
│           └── index.html        # Página de inicio
└── README.md                # Este archivo
```

## Características

### Taxonomías Configuradas

El sitio utiliza las siguientes taxonomías para organizar los ejercicios:

- **Languages** (Lenguajes): C, Matlab, Pascal, Pseudocódigo
- **Professors** (Profesores): mcdiaz, lperez, angel
- **Categories** (Categorías): Enunciado, Análisis, Comentario
- **Tags** (Etiquetas): Otras etiquetas como "sin_matlab", "sin_c", etc.

### Frontmatter de Ejercicios

Cada ejercicio tiene un frontmatter YAML con la siguiente estructura:

```yaml
---
title: "Título del Ejercicio"
date: 2024-01-01
draft: false
languages: ['c', 'matlab', 'pseudocódigo']
professors: ['mcdiaz']
categories: ['enunciado']
tags: ['sin_matlab']
---
```

## Instalación de Hugo

Para usar este sitio, necesitas instalar Hugo:

### Ubuntu/Debian

```bash
# Opción 1: Snap (versión más reciente)
sudo snap install hugo

# Opción 2: APT
sudo apt install hugo
```

### macOS

```bash
brew install hugo
```

### Windows

```bash
choco install hugo-extended
```

## Uso

### Servidor de Desarrollo

Para iniciar el servidor de desarrollo:

```bash
cd hugo_deploy
hugo server
```

Luego abre tu navegador en `http://localhost:1313`

### Generar Sitio Estático

Para generar el sitio estático en la carpeta `public/`:

```bash
cd hugo_deploy
hugo
```

Los archivos generados estarán en `hugo_deploy/public/` listos para ser desplegados.

## Soporte

Para más información sobre Hugo, visita [Hugo Documentation](https://gohugo.io/documentation/).
