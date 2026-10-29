---
title: "Plantilla:Revisar"
date: 2024-01-01
draft: false
tags: ['revisar']
---

# Plantilla:Revisar

{{< revisar >}}

Esta plantilla se utiliza para marcar los ejercicios que aún no han sido revisados o que pueden contener errores.

## Uso en Markdown

Para poner este aviso de advertencia en cualquier ejercicio en Markdown de forma fácil, simplemente incluye el shortcode:

```markdown
{{</* revisar */>}}
```

### Opciones y personalización

También puedes personalizar el mensaje si lo deseas:

- Con un texto alternativo:
  ```markdown
  {{</* revisar "Texto de advertencia personalizado" */>}}
  ```

- Especificando título y descripción:
  ```markdown
  {{</* revisar title="Atención" text="Este apartado está pendiente de revisión por el profesor." */>}}
  ```

- O utilizando el shortcode genérico de aviso para cuadros con formato libre:
  ```markdown
  {{</* aviso */>}}
  **Aviso:** Contenido en revisión.
  {{</* /aviso */>}}
  ```