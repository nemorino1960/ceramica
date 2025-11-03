# Guida Rapida a Jinja2 per Template

Questa guida copre le funzionalità di Jinja2 usate nei nostri template.

## 📌 Cos'è Jinja2?

Jinja2 è un motore di template per Python che permette di inserire logica e variabili in file HTML.

## 🔤 Sintassi Base

### 1. Variabili - `{{ }}`

Stampa il valore di una variabile:

```html
<!-- Variabile semplice -->
<h1>{{ page.title }}</h1>
<!-- Output: <h1>Il Mio Titolo</h1> -->

<!-- Variabile annidata (oggetto/dict) -->
<p>{{ site.author }}</p>
<!-- Output: <p>Nome Autore</p> -->

<!-- Accesso con notazione punto -->
{{ page.description }}

<!-- Accesso con notazione dizionario (alternativa) -->
{{ page['description'] }}
```

### 2. Condizioni - `{% if %}`

Mostra contenuto condizionalmente:

```html
<!-- If semplice -->
{% if page.author %}
<span class="author">di {{ page.author }}</span>
{% endif %}

<!-- If/Else -->
{% if page.status == 'attivo' %}
<span class="badge-green">Attivo</span>
{% else %}
<span class="badge-gray">Non attivo</span>
{% endif %}

<!-- If/Elif/Else -->
{% if page.status == 'attivo' %}
<span class="badge-green">Attivo</span>
{% elif page.status == 'completato' %}
<span class="badge-blue">Completato</span>
{% else %}
<span class="badge-orange">In sviluppo</span>
{% endif %}

<!-- Operatori logici -->
{% if page.featured and page.published %}
<div class="featured">In evidenza!</div>
{% endif %}

{% if page.draft or page.private %}
<div class="notice">Non pubblico</div>
{% endif %}
```

### 3. Loop - `{% for %}`

Itera su liste/array:

```html
<!-- Loop base -->
{% for tag in page.tags %}
<span class="tag">{{ tag }}</span>
{% endfor %}
<!-- 
Input: tags: python, html, css
Output: 
<span class="tag">python</span>
<span class="tag">html</span>
<span class="tag">css</span>
-->

<!-- Loop con else (se lista vuota) -->
{% for item in page.gallery %}
<img src="{{ item }}" alt="Gallery">
{% else %}
<p>Nessuna immagine disponibile</p>
{% endfor %}

<!-- Variabili speciali nel loop -->
{% for post in blog.posts %}
<div class="post">
    {{ loop.index }}. {{ post.title }}
    {% if loop.first %}<span>Primo!</span>{% endif %}
    {% if loop.last %}<span>Ultimo!</span>{% endif %}
</div>
{% endfor %}
```

**Variabili loop speciali:**
- `loop.index` - Iterazione corrente (parte da 1)
- `loop.index0` - Iterazione corrente (parte da 0)
- `loop.first` - True se primo elemento
- `loop.last` - True se ultimo elemento
- `loop.length` - Numero totale di elementi

### 4. Filtri - `|`

Trasformano i valori:

```html
<!-- Uppercase -->
{{ page.title | upper }}
<!-- "ciao" → "CIAO" -->

<!-- Lowercase -->
{{ page.title | lower }}
<!-- "CIAO" → "ciao" -->

<!-- Capitalize -->
{{ page.title | capitalize }}
<!-- "ciao mondo" → "Ciao mondo" -->

<!-- Title case -->
{{ page.title | title }}
<!-- "ciao mondo" → "Ciao Mondo" -->

<!-- Replace -->
{{ page.slug | replace("-", " ") }}
<!-- "my-post" → "my post" -->

<!-- Default (valore se variabile è None/vuota) -->
{{ page.description | default("Nessuna descrizione") }}

<!-- Length -->
{{ page.tags | length }} tag disponibili

<!-- Join (unisce array) -->
{{ page.tags | join(", ") }}
<!-- ["python", "html"] → "python, html" -->

<!-- Trim (rimuove spazi) -->
{{ page.content | trim }}

<!-- Truncate (taglia testo) -->
{{ page.description | truncate(100) }}

<!-- Safe (non escape HTML) -->
{{ page.html_content | safe }}
```

### 5. Operatore OR - `or`

Valore di fallback:

```html
<!-- Se page.description è vuoto, usa site.description -->
<meta name="description" content="{{ page.description or site.description }}">

<!-- Equivale a: -->
{% if page.description %}
<meta name="description" content="{{ page.description }}">
{% else %}
<meta name="description" content="{{ site.description }}">
{% endif %}
```

### 6. Commenti - `{# #}`

Non vengono renderizzati nell'output:

```html
{# Questo è un commento, non apparirà nell'HTML finale #}
<h1>{{ page.title }}</h1>

{#
Commento
multi-riga
#}
```

## 🎯 Esempi Pratici dai Nostri Template

### Esempio 1: Metadata del Post (blog.html)

```html
<div class="post-meta">
    <!-- Mostra data solo se presente -->
    {% if page.date %}
    <time datetime="{{ page.date }}">{{ page.date }}</time>
    {% endif %}
    
    <!-- Mostra autore solo se presente -->
    {% if page.author %}
    <span class="author">di {{ page.author }}</span>
    {% endif %}
    
    <!-- Loop sui tag se presenti -->
    {% if page.tags %}
    <div class="tags">
        {% for tag in page.tags %}
        <span class="tag">{{ tag }}</span>
        {% endfor %}
    </div>
    {% endif %}
</div>
```

**Input (frontmatter):**
```yaml
date: 2025-11-03
author: Mario Rossi
tags: python, tutorial, markdown
```

**Output HTML:**
```html
<div class="post-meta">
    <time datetime="2025-11-03">2025-11-03</time>
    <span class="author">di Mario Rossi</span>
    <div class="tags">
        <span class="tag">python</span>
        <span class="tag">tutorial</span>
        <span class="tag">markdown</span>
    </div>
</div>
```

### Esempio 2: Badge di Stato (project.html)

```html
{% if page.status %}
<span class="badge badge-{{ page.status }}">{{ page.status }}</span>
{% endif %}
```

**Input:**
```yaml
status: attivo
```

**Output:**
```html
<span class="badge badge-attivo">attivo</span>
```

### Esempio 3: Link Condizionali (project.html)

```html
<div class="project-info">
    {% if page.github %}
    <a href="{{ page.github }}" target="_blank">GitHub</a>
    {% endif %}
    
    {% if page.demo %}
    <a href="{{ page.demo }}" target="_blank">Demo</a>
    {% endif %}
</div>
```

### Esempio 4: Meta Tag con Fallback (base.html)

```html
<!-- Usa description della pagina, o quella del sito se mancante -->
<meta name="description" content="{{ page.description or site.description }}">

<!-- Usa lingua della pagina, o quella del sito -->
<html lang="{{ page.language or site.language }}">
```

## 🔧 Operatori di Confronto

```html
{% if page.views > 100 %}
<span>Post popolare!</span>
{% endif %}

{% if page.status == 'pubblicato' %}
<span>Pubblicato</span>
{% endif %}

{% if page.status != 'bozza' %}
<span>Visibile</span>
{% endif %}

{% if page.rating >= 4 %}
<span>⭐ Consigliato</span>
{% endif %}
```

Operatori disponibili:
- `==` - Uguale
- `!=` - Diverso
- `>` - Maggiore
- `<` - Minore
- `>=` - Maggiore o uguale
- `<=` - Minore o uguale
- `in` - Contenuto in
- `not in` - Non contenuto in

## 📚 Test Utili

```html
<!-- Verifica se definito -->
{% if page.author is defined %}
<span>{{ page.author }}</span>
{% endif %}

<!-- Verifica se None -->
{% if page.description is none %}
<p>Nessuna descrizione</p>
{% endif %}

<!-- Verifica tipo -->
{% if page.tags is iterable %}
{% for tag in page.tags %}...{% endfor %}
{% endif %}
```

## 🎨 Filtri Concatenati

Puoi concatenare più filtri:

```html
<!-- Lowercase e poi replace -->
{{ page.title | lower | replace(" ", "-") }}
<!-- "Hello World" → "hello-world" -->

<!-- Trim e poi capitalize -->
{{ page.name | trim | capitalize }}
<!-- "  mario  " → "Mario" -->

<!-- Truncate e poi upper -->
{{ page.description | truncate(50) | upper }}
```

## 💡 Esempi Pratici Completi

### Menu di Navigazione Dinamico

```html
<nav>
    <ul>
        {% for item in menu.items %}
        <li class="{% if item.active %}active{% endif %}">
            <a href="{{ item.url }}">{{ item.label }}</a>
        </li>
        {% endfor %}
    </ul>
</nav>
```

### Lista di Post con Numerazione

```html
{% for post in posts %}
<article>
    <span class="number">{{ loop.index }}</span>
    <h2>{{ post.title }}</h2>
    <p>{{ post.excerpt | truncate(150) }}</p>
    
    {% if loop.first %}
    <span class="badge">Ultimo post</span>
    {% endif %}
</article>
{% else %}
<p>Nessun post disponibile</p>
{% endfor %}
```

### Gallery con Immagini

```html
{% if page.images %}
<div class="gallery">
    {% for image in page.images %}
    <figure>
        <img src="{{ page.base_path }}{{ image.url }}" 
             alt="{{ image.alt | default('Immagine') }}">
        {% if image.caption %}
        <figcaption>{{ image.caption }}</figcaption>
        {% endif %}
    </figure>
    {% endfor %}
</div>
{% endif %}
```

### Breadcrumb Dinamico

```html
<nav class="breadcrumb">
    <a href="{{ page.base_path }}index.html">Home</a>
    
    {% if page.category %}
    →
    <a href="{{ page.base_path }}{{ page.category }}/index.html">
        {{ page.category | title }}
    </a>
    {% endif %}
    
    {% if page.subcategory %}
    →
    <span>{{ page.subcategory | title }}</span>
    {% endif %}
</nav>
```

## 🚀 Tips & Best Practices

### 1. Usa OR per Valori di Default
```html
<!-- ✅ Buono -->
<p>{{ page.author or 'Anonimo' }}</p>

<!-- ❌ Prolisso -->
{% if page.author %}
<p>{{ page.author }}</p>
{% else %}
<p>Anonimo</p>
{% endif %}
```

### 2. Combina Condizioni
```html
<!-- ✅ Buono -->
{% if page.published and not page.draft %}

<!-- ❌ Annidato -->
{% if page.published %}
{% if not page.draft %}
```

### 3. Usa Filtri Default
```html
<!-- ✅ Buono -->
{{ page.description | default("Nessuna descrizione") }}

<!-- ❌ Verboso -->
{% if page.description %}{{ page.description }}{% else %}Nessuna descrizione{% endif %}
```

### 4. Commenta il Codice Complesso
```html
{# Loop attraverso i post recenti, mostra solo i primi 5 #}
{% for post in recent_posts[:5] %}
...
{% endfor %}
```

## 📖 Riferimenti

- [Documentazione Jinja2 Ufficiale](https://jinja.palletsprojects.com/)
- [Lista Completa Filtri](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters)
- [Lista Completa Test](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-tests)

## 🎓 Esercizi Pratici

Prova a creare questi elementi nei tuoi template:

1. ✏️ Menu di navigazione con link attivo evidenziato
2. ✏️ Lista di post ordinata per data
3. ✏️ Sidebar con categorie e conteggio articoli
4. ✏️ Footer con anno dinamico
5. ✏️ Badge colorati basati su categorie

---

**Ricorda:** Jinja2 è potente ma semplice. Queste basi coprono il 90% dei casi d'uso nei nostri template!
