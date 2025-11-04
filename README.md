# Ceramica 🏺

**Version 1.0.0** | Static Site Generator

Un generatore di siti statici minimale scritto in Python che converte file Markdown in HTML usando template Jinja2.

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/nemorino60/ceramica/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-yellow.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/nemorino60/ceramica)](https://github.com/nemorino60/ceramica/issues)
[![GitHub stars](https://img.shields.io/github/stars/nemorino60/ceramica)](https://github.com/nemorino60/ceramica/stargazers)

> 🏺 Come un artigiano trasforma l'argilla in ceramica, Ceramica trasforma il Markdown in siti web eleganti.

## 📁 Struttura del Progetto

```
ceramica/
├── pages/              # File Markdown con i contenuti delle pagine
│   ├── index.md
│   └── about.md
├── config/             # File di configurazione
│   └── config.json
├── template/           # Template HTML Jinja2
│   └── base.html
├── assets/             # File statici (CSS, JS, immagini)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── resources/          # Risorse aggiuntive (es. file da copiare direttamente)
├── deploy/             # Output per produzione (generato)
├── debug/              # Output per debug locale (generato)
├── build.py            # Script principale di generazione
└── requirements.txt    # Dipendenze Python
```

## 🚀 Installazione

1. **Clona o crea il progetto**
   ```bash
   cd /Users/nemorino/webdev/ceramica
   ```

2. **Crea un ambiente virtuale (opzionale ma raccomandato)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Su macOS/Linux
   ```

3. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Utilizzo

### Build per Debug Locale

Genera il sito nella cartella `debug/` per test locali:

```bash
python build.py debug
```

Poi avvia un server locale:

```bash
cd debug
python -m http.server 8000
```

Apri il browser su http://localhost:8000

### Build per Deploy/Produzione

Genera il sito nella cartella `deploy/` pronto per essere caricato su un host:

```bash
python build.py deploy
```

Il contenuto della cartella `deploy/` può essere caricato direttamente sul tuo server web.

### Test Locale della Build di Deploy

Puoi testare in locale anche la build di produzione prima del caricamento:

```bash
cd deploy
python -m http.server 8000
```

Apri il browser su http://localhost:8000 per verificare che tutto funzioni correttamente.

## ✍️ Creare Nuove Pagine

1. **Crea un nuovo file Markdown** nella cartella `pages/` o in una sottocartella:

   ```markdown
   ---
   title: Il Mio Titolo
   description: Descrizione della pagina
   template: base.html
   ---

   # Contenuto della Pagina

   Il tuo contenuto in Markdown qui...
   ```

2. **Frontmatter supportato**:
   - `title`: Titolo della pagina (obbligatorio)
   - `description`: Meta description per SEO
   - `template`: Template da usare (default: base.html)

3. **Genera il sito**:
   ```bash
   python build.py
   ```

### 📂 Struttura Annidata

Puoi organizzare le pagine in sottocartelle annidate:

```
pages/
├── index.md
├── about.md
├── blog/
│   ├── primo-post.md
│   ├── secondo-post.md
│   └── 2025/
│       └── novembre.md
├── progetti/
│   ├── progetto-1.md
│   └── progetto-2.md
└── contatti/
    └── form.md
```

Il generatore:
- **Mantiene la struttura** nel sito generato
- **Calcola automaticamente** i path relativi per CSS/JS
- **Crea le sottocartelle** necessarie nell'output

Esempio: `pages/blog/primo-post.md` → `debug/blog/primo-post.html`

## 🎨 Personalizzazione

### Template

Il generatore supporta **template multipli**. Template disponibili:

- **`base.html`** - Template generico per pagine standard
- **`blog.html`** - Template per post del blog con metadata e sidebar
- **`project.html`** - Template per progetti con badge e link

Per usare un template, specificalo nel frontmatter:

```markdown
---
title: Il Mio Post
template: blog.html
date: 2025-11-03
author: Nome Autore
tags: python, tutorial
---
```

**Creare nuovi template:**

1. Crea un file `.html` in `template/` (es. `portfolio.html`)
2. Usa la sintassi Jinja2 con variabili come:
   - `{{ site.* }}` - Variabili da config.json
   - `{{ page.* }}` - Variabili dal frontmatter
   - `{{ content }}` - Contenuto HTML generato
   - `{{ page.base_path }}` - Path relativo (calcolato automaticamente)
3. Specifica `template: portfolio.html` nelle pagine

**Nessuna configurazione richiesta!** Il sistema trova automaticamente tutti i template.

Vedi `template/README.md` per la guida completa ai template.

### Stili CSS

Modifica `assets/css/style.css` per personalizzare l'aspetto del sito.

Ogni template può avere CSS specifico - vedi le sezioni commentate nel file CSS.

### JavaScript

Aggiungi funzionalità in `assets/js/main.js`.

### Configurazione

Modifica `config/config.json` per:
- Titolo e descrizione del sito
- URL base
- Opzioni di build

## 🔧 Configurazione

Esempio di `config/config.json`:

```json
{
  "site": {
    "title": "Il Mio Sito",
    "description": "Un sito statico generato con Python",
    "author": "Nome Autore",
    "base_url": "http://localhost:8000",
    "language": "it"
  },
  "paths": {
    "pages": "pages",
    "templates": "template",
    "assets": "assets",
    "resources": "resources",
    "deploy": "deploy",
    "debug": "debug"
  },
  "build": {
    "copy_assets": true,
    "minify": false,
    "generate_sitemap": true
  }
}
```

## 📦 Caratteristiche

- ✅ Conversione Markdown → HTML
- ✅ Template Jinja2 personalizzabili
- ✅ Frontmatter per metadata delle pagine
- ✅ CSS e JavaScript inclusi
- ✅ Build separate per debug e deploy
- ✅ Copia automatica di assets e resources
- ✅ Supporto per code highlighting
- ✅ Supporto per tabelle e liste
- ✅ Design responsive

## 🚀 Sviluppi Futuri

Possibili estensioni:
- [ ] Generazione automatica sitemap.xml
- [ ] Supporto per blog con pagination
- [ ] Minificazione CSS/JS
- [ ] Ottimizzazione immagini
- [ ] RSS feed
- [ ] Sistema di plugin
- [ ] Watch mode per rigenerazione automatica
- [ ] Deploy automatico (FTP/SFTP/Git)
- [ ] Supporto per PHP dinamico

## 📚 Documentazione

- **[Guida Jinja2](docs/JINJA2_GUIDA.md)** - Tutorial completo sulla sintassi Jinja2
- **[Jinja2 Cheat Sheet](docs/JINJA2_CHEATSHEET.md)** - Riferimento rapido stampabile
- **[Template System](template/README.md)** - Come creare e usare template
- **[Changelog](CHANGELOG.md)** - Storia delle versioni e modifiche

## 🤖 Sviluppo Assistito da AI

Ceramica è stato sviluppato con l'assistenza di GitHub Copilot e AI (Claude 3.5 Sonnet) per accelerare l'implementazione e la documentazione. 

**Tuttavia:**
- L'architettura e il design sono di **nemorino60**
- Tutte le decisioni funzionali sono state prese dall'autore
- Il progetto è stato concepito, diretto e validato dall'autore
- Il nome "Ceramica" e la filosofia del progetto sono originali

L'AI è stata utilizzata come **strumento avanzato di sviluppo**, similmente a come un IDE moderno o un framework assistono il programmatore. Il risultato finale riflette la visione e le scelte dell'autore.

Questo approccio rappresenta il moderno workflow di sviluppo dove AI e sviluppatore collaborano: l'umano fornisce creatività, visione e decisioni strategiche; l'AI fornisce implementazione rapida e documentazione strutturata.

## 📋 Versione

**Ceramica v1.0.0** - Rilasciato il 03 novembre 2025

Vedi il [CHANGELOG](CHANGELOG.md) per la lista completa delle funzionalità.

```bash
# Mostra versione
python build.py --version
```

## 📄 Licenza

Questo progetto è rilasciato sotto licenza [MIT](LICENSE).

Copyright (c) 2025 nemorino60

## 🤝 Contributi

I contributi sono benvenuti! Leggi la [guida per contribuire](CONTRIBUTING.md).

- 🐛 [Segnala un bug](https://github.com/nemorino60/ceramica/issues/new?template=bug_report.md)
- ✨ [Richiedi una feature](https://github.com/nemorino60/ceramica/issues/new?template=feature_request.md)
- 💬 [Discussioni](https://github.com/nemorino60/ceramica/discussions)
- ⭐ [Metti una stella](https://github.com/nemorino60/ceramica) se ti piace il progetto!

## 🔗 Link Utili

- 📦 [Repository GitHub](https://github.com/nemorino60/ceramica)
- 📋 [Releases](https://github.com/nemorino60/ceramica/releases)
- 📚 [Documentazione](https://github.com/nemorino60/ceramica/tree/main/docs)
- 🐛 [Issues](https://github.com/nemorino60/ceramica/issues)
- 💬 [Discussions](https://github.com/nemorino60/ceramica/discussions)
- 👤 [Profilo Autore](https://github.com/nemorino60)

## 📞 Supporto

Se hai bisogno di aiuto:
1. Consulta la [documentazione](docs/README.md)
2. Cerca nelle [issues esistenti](https://github.com/nemorino60/ceramica/issues)
3. Apri una [nuova issue](https://github.com/nemorino60/ceramica/issues/new)
4. Partecipa alle [discussions](https://github.com/nemorino60/ceramica/discussions)

---

<div align="center">

**Ceramica** 🏺

*Modella il tuo sito con eleganza*

Fatto con ❤️ da [nemorino60](https://github.com/nemorino60)

[⬆ Torna su](#ceramica-)

</div>
