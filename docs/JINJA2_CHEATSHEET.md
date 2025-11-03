# Jinja2 Cheat Sheet - Riferimento Rapido

## 🔤 Sintassi

| Sintassi | Uso | Esempio |
|----------|-----|---------|
| `{{ var }}` | Stampa variabile | `{{ page.title }}` |
| `{% statement %}` | Logica/controllo | `{% if page.author %}` |
| `{# comment #}` | Commento | `{# TODO: aggiungere #}` |
| `{{ var \| filter }}` | Filtro | `{{ text \| upper }}` |

## 🎯 Variabili

```html
{{ page.title }}                    <!-- Variabile semplice -->
{{ site.config.name }}              <!-- Annidata -->
{{ page['description'] }}           <!-- Notazione dizionario -->
{{ page.author or 'Anonimo' }}      <!-- Con default -->
{{ page.description | default("N/A") }}  <!-- Con filtro default -->
```

## 🔀 Condizioni

```html
<!-- If -->
{% if page.published %}
<span>Pubblicato</span>
{% endif %}

<!-- If/Else -->
{% if page.featured %}
<div class="featured">In evidenza</div>
{% else %}
<div class="normal">Standard</div>
{% endif %}

<!-- If/Elif/Else -->
{% if status == 'new' %}
<span class="badge-green">Nuovo</span>
{% elif status == 'active' %}
<span class="badge-blue">Attivo</span>
{% else %}
<span class="badge-gray">Altro</span>
{% endif %}

<!-- Operatori logici -->
{% if published and not draft %}
{% if featured or promoted %}
```

## 🔁 Loop

```html
<!-- Loop base -->
{% for item in items %}
<li>{{ item }}</li>
{% endfor %}

<!-- Con else (se vuoto) -->
{% for item in items %}
<li>{{ item }}</li>
{% else %}
<p>Nessun elemento</p>
{% endfor %}

<!-- Con variabili loop -->
{% for post in posts %}
{{ loop.index }}. {{ post.title }}
{% if loop.first %}<span>Primo</span>{% endif %}
{% if loop.last %}<span>Ultimo</span>{% endif %}
{% endfor %}
```

### Variabili Loop

| Variabile | Descrizione |
|-----------|-------------|
| `loop.index` | Iterazione (da 1) |
| `loop.index0` | Iterazione (da 0) |
| `loop.first` | True se primo |
| `loop.last` | True se ultimo |
| `loop.length` | Numero totale |

## 🎨 Filtri Comuni

| Filtro | Esempio | Output |
|--------|---------|--------|
| `upper` | `{{ "ciao" \| upper }}` | CIAO |
| `lower` | `{{ "CIAO" \| lower }}` | ciao |
| `capitalize` | `{{ "ciao" \| capitalize }}` | Ciao |
| `title` | `{{ "ciao mondo" \| title }}` | Ciao Mondo |
| `trim` | `{{ "  ciao  " \| trim }}` | ciao |
| `length` | `{{ items \| length }}` | 5 |
| `join` | `{{ list \| join(", ") }}` | a, b, c |
| `replace` | `{{ "a-b" \| replace("-", " ") }}` | a b |
| `default` | `{{ var \| default("N/A") }}` | N/A (se vuoto) |
| `truncate` | `{{ text \| truncate(10) }}` | testo... |
| `safe` | `{{ html \| safe }}` | (no escape) |

### Concatenare Filtri

```html
{{ page.title | lower | replace(" ", "-") }}
<!-- "Hello World" → "hello-world" -->

{{ description | trim | truncate(100) | upper }}
```

## 🔍 Operatori

### Confronto

| Operatore | Esempio |
|-----------|---------|
| `==` | `{% if x == 5 %}` |
| `!=` | `{% if x != 0 %}` |
| `>` | `{% if x > 10 %}` |
| `<` | `{% if x < 5 %}` |
| `>=` | `{% if x >= 3 %}` |
| `<=` | `{% if x <= 7 %}` |
| `in` | `{% if 'python' in tags %}` |
| `not in` | `{% if x not in list %}` |

### Logici

| Operatore | Esempio |
|-----------|---------|
| `and` | `{% if a and b %}` |
| `or` | `{% if a or b %}` |
| `not` | `{% if not x %}` |

## ✅ Test

```html
{% if variable is defined %}      <!-- Definito -->
{% if variable is none %}         <!-- None/Null -->
{% if items is iterable %}        <!-- Iterabile -->
{% if num is even %}              <!-- Pari -->
{% if num is odd %}               <!-- Dispari -->
{% if text is string %}           <!-- Stringa -->
```

## 💡 Pattern Comuni

### Menu di Navigazione

```html
<nav>
    <a href="{{ page.base_path }}index.html">Home</a>
    <a href="{{ page.base_path }}blog/index.html">Blog</a>
    <a href="{{ page.base_path }}about.html">About</a>
</nav>
```

### Metadata Condizionale

```html
{% if page.date %}
<time>{{ page.date }}</time>
{% endif %}

{% if page.author %}
<span>di {{ page.author }}</span>
{% endif %}
```

### Loop con Tags

```html
{% if page.tags %}
<div class="tags">
    {% for tag in page.tags %}
    <span class="tag">{{ tag }}</span>
    {% endfor %}
</div>
{% endif %}
```

### Badge Dinamico

```html
{% if page.status %}
<span class="badge badge-{{ page.status }}">
    {{ page.status | upper }}
</span>
{% endif %}
```

### Descrizione con Fallback

```html
<meta name="description" 
      content="{{ page.description or site.description }}">
```

### Lista Numerata

```html
{% for item in items %}
<div class="item-{{ loop.index }}">
    {{ loop.index }}. {{ item.name }}
    {% if loop.first %}<span class="new">Nuovo!</span>{% endif %}
</div>
{% endfor %}
```

### Breadcrumb

```html
<nav>
    <a href="{{ page.base_path }}index.html">Home</a>
    {% if page.category %}
    → <a href="{{ page.base_path }}{{ page.category }}/">
        {{ page.category | title }}
    </a>
    {% endif %}
    → <span>{{ page.title }}</span>
</nav>
```

## 🎓 Tips Veloci

1. **OR per default:** `{{ var or 'default' }}`
2. **Filtra prima:** `{{ text | trim | lower }}`
3. **Test esistenza:** `{% if var is defined %}`
4. **Loop vuoto:** `{% for x in y %}...{% else %}vuoto{% endfor %}`
5. **Commenta:** `{# descrizione #}`

## 🔗 Link Utili

- [Docs Jinja2](https://jinja.palletsprojects.com/)
- [Filtri Builtin](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters)
- [Test Builtin](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-tests)

---

**Stampa questa pagina per averla sempre a portata di mano! 📄**
