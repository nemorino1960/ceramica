# Template System - Guida

Questa guida spiega come creare e utilizzare template personalizzati.

## 📋 Template Disponibili

### 1. base.html
Template generico per pagine standard.

**Quando usarlo:** Pagine semplici come About, Contatti, ecc.

**Variabili disponibili:**
- `{{ site.title }}` - Titolo del sito
- `{{ site.description }}` - Descrizione del sito
- `{{ site.author }}` - Autore
- `{{ site.language }}` - Lingua
- `{{ page.title }}` - Titolo della pagina
- `{{ page.description }}` - Descrizione della pagina
- `{{ page.base_path }}` - Path relativo alla root
- `{{ content }}` - Contenuto HTML generato dal Markdown

**Esempio frontmatter:**
```markdown
---
title: Chi Siamo
description: Informazioni sul progetto
template: base.html
---
```

### 2. blog.html
Template specializzato per post del blog con sidebar e metadata.

**Quando usarlo:** Articoli del blog, tutorial, post

**Variabili aggiuntive:**
- `{{ page.date }}` - Data di pubblicazione
- `{{ page.author }}` - Autore del post
- `{{ page.tags }}` - Array di tag

**Esempio frontmatter:**
```markdown
---
title: Titolo del Post
description: Descrizione breve
template: blog.html
date: 2025-11-03
author: Nome Autore
tags: python, tutorial, markdown
---
```

**Note:** I tag devono essere separati da virgole

### 3. project.html
Template per pagine di progetto con badge di stato e link.

**Quando usarlo:** Portfolio, showcase progetti

**Variabili aggiuntive:**
- `{{ page.status }}` - Stato del progetto (attivo, completato, in-sviluppo)
- `{{ page.tech }}` - Tecnologie utilizzate
- `{{ page.github }}` - URL repository GitHub
- `{{ page.demo }}` - URL demo live

**Esempio frontmatter:**
```markdown
---
title: Nome Progetto
description: Descrizione del progetto
template: project.html
status: attivo
tech: Python, JavaScript, React
github: https://github.com/user/repo
demo: https://demo.example.com
---
```

## 🎨 Creare un Nuovo Template

### Step 1: Crea il file HTML

Crea un nuovo file nella cartella `template/`, es. `template/portfolio.html`:

```html
<!DOCTYPE html>
<html lang="{{ site.language }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} - {{ site.title }}</title>
    <link rel="stylesheet" href="{{ page.base_path }}assets/css/style.css">
</head>
<body>
    <header>
        <nav>
            <h1>{{ site.title }}</h1>
            <!-- Navigazione -->
        </nav>
    </header>

    <main>
        <h1>{{ page.title }}</h1>
        
        <!-- Accedi a variabili custom del frontmatter -->
        {% if page.subtitle %}
        <h2>{{ page.subtitle }}</h2>
        {% endif %}
        
        <!-- Contenuto Markdown convertito -->
        <div class="content">
            {{ content }}
        </div>
    </main>

    <footer>
        <p>&copy; 2025 {{ site.author }}</p>
    </footer>

    <script src="{{ page.base_path }}assets/js/main.js"></script>
</body>
</html>
```

### Step 2: Usa Jinja2

Puoi usare tutte le funzionalità di Jinja2:

**Condizioni:**
```html
{% if page.featured %}
<div class="featured">In evidenza!</div>
{% endif %}
```

**Loop:**
```html
{% if page.gallery %}
<div class="gallery">
    {% for image in page.gallery %}
    <img src="{{ image }}" alt="Gallery">
    {% endfor %}
</div>
{% endif %}
```

**Filtri:**
```html
<p>{{ page.description | upper }}</p>
<p>{{ page.title | lower | replace(" ", "-") }}</p>
```

### Step 3: Aggiungi CSS Specifico

In `assets/css/style.css`:

```css
/* Portfolio Template */
.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}
```

### Step 4: Usa il Template

Nel file Markdown, specifica il template:

```markdown
---
title: Mio Portfolio
template: portfolio.html
subtitle: I miei lavori migliori
featured: true
gallery:
  - /assets/img1.jpg
  - /assets/img2.jpg
---

# Contenuto della pagina...
```

## ⚙️ Variabili Sempre Disponibili

### Variabili Site (da config.json)
- `{{ site.title }}`
- `{{ site.description }}`
- `{{ site.author }}`
- `{{ site.base_url }}`
- `{{ site.language }}`

### Variabili Page (da frontmatter + automatiche)
- `{{ page.title }}`
- `{{ page.description }}`
- `{{ page.base_path }}` - Path relativo calcolato automaticamente
- `{{ page.* }}` - Qualsiasi variabile custom dal frontmatter

### Variabile Content
- `{{ content }}` - HTML generato dal Markdown

## 🔧 Nessuna Configurazione Richiesta!

**Non serve modificare `config.json`** o `build.py` per aggiungere template.

Il sistema:
1. ✅ Legge automaticamente tutti i file `.html` da `template/`
2. ✅ Usa il template specificato nel frontmatter
3. ✅ Se non specificato, usa `base.html` come default

## 📚 Best Practices

1. **Mantieni i template DRY**: Usa include/extends di Jinja2 per parti comuni
2. **Usa nomi descrittivi**: `blog.html`, `project.html`, non `template1.html`
3. **Documenta le variabili**: Aggiungi commenti nei template
4. **Testa con vari depth**: Verifica che `base_path` funzioni in sottocartelle
5. **Valida HTML**: Usa strumenti di validazione HTML5

## 🎯 Esempi Avanzati

### Template con Breadcrumb
```html
<nav class="breadcrumb">
    <a href="{{ page.base_path }}index.html">Home</a>
    {% if page.category %}
    → <a href="{{ page.base_path }}{{ page.category }}/index.html">{{ page.category }}</a>
    {% endif %}
    → <span>{{ page.title }}</span>
</nav>
```

### Template con TOC
```html
{% if page.show_toc %}
<aside class="toc">
    <h3>Indice</h3>
    {{ toc }}
</aside>
{% endif %}
```

### Template Multilingua
```html
<html lang="{{ page.language or site.language }}">
```

---

**Domande?** Consulta la [documentazione Jinja2](https://jinja.palletsprojects.com/)
