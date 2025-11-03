---
title: Post di Novembre 2025
description: Un esempio di struttura profonda
template: base.html
---

# Post di Novembre 2025

Questa pagina dimostra come funziona una struttura a **3 livelli** di profondità.

## Path della Pagina

```
pages/blog/2025/novembre.md
→ genera →
blog/2025/novembre.html
```

## Gestione dei Path

Il generatore calcola automaticamente:
- La profondità della pagina
- I path relativi corretti per CSS/JS
- I link di navigazione

## Esempio di Path Relativo

Per tornare alla root da qui, il generatore usa: `../../`

Quindi:
- CSS: `../../assets/css/style.css`
- JS: `../../assets/js/main.js`
- Home: `../../index.html`

Tutto gestito automaticamente! 🎉

---

[Home](../../index.html) | [Blog](../primo-post.html) | [About](../../about.html)
