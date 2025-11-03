# Documentazione Ceramica

Benvenuto nella documentazione di Ceramica - Static Site Generator!

## 📖 Guide Disponibili

### 🎓 Per Principianti

1. **[README Principale](../README.md)**
   - Installazione e setup
   - Comandi base
   - Struttura del progetto
   - Quick start

**[CHANGELOG](../CHANGELOG.md)** 📋 - Storia delle versioni
   - Versione corrente: **1.0.0** (03/11/2025)
   - Lista completa delle funzionalità
   - Note di rilascio

### 🎨 Template e Design

2. **[Guida Jinja2](JINJA2_GUIDA.md)** ⭐ INIZIA QUI
   - Tutorial completo sulla sintassi Jinja2
   - Esempi pratici dai nostri template
   - Esercizi e best practices
   - Per chi non conosce Jinja2

3. **[Jinja2 Cheat Sheet](JINJA2_CHEATSHEET.md)** 📄
   - Riferimento rapido
   - Tabelle di consultazione
   - Pattern comuni
   - Stampabile per averlo sempre a portata di mano

4. **[Sistema Template](../template/README.md)**
   - Come creare nuovi template
   - Template disponibili
   - Variabili e personalizzazione
   - Esempi avanzati

### 🎯 Per Funzionalità

5. **[CSS Styles](../assets/css/style.css)**
   - Stili per tutti i template
   - Variabili CSS
   - Classi responsive

6. **[JavaScript](../assets/js/main.js)**
   - Funzionalità interattive
   - Smooth scrolling
   - Link attivi

## 🚀 Percorso di Apprendimento Consigliato

### Livello 1: Uso Base (30 min)
1. Leggi il [README principale](../README.md)
2. Esegui il primo build
3. Crea una nuova pagina Markdown

### Livello 2: Personalizzazione (1-2 ore)
1. Studia la [Guida Jinja2](JINJA2_GUIDA.md)
2. Modifica il template `base.html`
3. Personalizza CSS in `assets/css/style.css`

### Livello 3: Template Avanzati (2-3 ore)
1. Leggi [Sistema Template](../template/README.md)
2. Crea un nuovo template custom
3. Usa variabili avanzate dal frontmatter

### Livello 4: Automazione (opzionale)
1. Script di deploy automatico
2. Watch mode per rigenerazione
3. Ottimizzazione immagini

## 🔍 Riferimenti Rapidi

### Sintassi Jinja2 Base

```html
<!-- Variabili -->
{{ page.title }}

<!-- Condizioni -->
{% if page.author %}
<span>{{ page.author }}</span>
{% endif %}

<!-- Loop -->
{% for tag in page.tags %}
<span>{{ tag }}</span>
{% endfor %}

<!-- Filtri -->
{{ page.title | upper }}
```

### Frontmatter Base

```markdown
---
title: Titolo Pagina
description: Descrizione
template: base.html
---

# Contenuto...
```

### Variabili Disponibili

- `{{ site.* }}` - Da config.json
- `{{ page.* }}` - Da frontmatter
- `{{ content }}` - HTML generato
- `{{ page.base_path }}` - Path relativo

## 🆘 Risoluzione Problemi

### Template non trovato
✅ Verifica che il file esista in `template/`
✅ Controlla il nome nel frontmatter: `template: nome.html`

### CSS/JS non caricano
✅ Usa `{{ page.base_path }}assets/css/style.css`
✅ Verifica path relativi nelle sottocartelle

### Variabile non stampata
✅ Controlla sia definita nel frontmatter
✅ Usa `{% if page.var is defined %}` per testare
✅ Usa `{{ page.var | default("N/A") }}` per fallback

### Directory listing invece di index
✅ Crea file `index.md` nella cartella
✅ Rigenera il sito con `python3 build.py debug`

## 📞 Supporto

Per problemi o domande:
1. Consulta la documentazione pertinente
2. Controlla gli esempi nelle pagine esistenti
3. Verifica la sintassi Jinja2 nel [Cheat Sheet](JINJA2_CHEATSHEET.md)

## 🔗 Link Esterni Utili

- [Jinja2 Official Docs](https://jinja.palletsprojects.com/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Python Markdown Docs](https://python-markdown.github.io/)

---

**Buon lavoro con Ceramica! 🚀**
