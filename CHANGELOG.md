# Changelog

Tutte le modifiche significative a questo progetto saranno documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/it/1.0.0/),
e questo progetto aderisce al [Semantic Versioning](https://semver.org/lang/it/).

## [1.0.1] - 2025-11-04

### 🐛 Bugfix

#### Correzioni
- **Account GitHub corretto**: Tutti i riferimenti da `nemorino60` a `nemorino1960`
  - URL repository: `https://github.com/nemorino1960/ceramica`
  - Badge nel README
  - Link nella documentazione
  - Issue templates
  - Copyright e licenza
  - Config.json e metadati
- **Versione aggiornata**: Build system ora riporta correttamente v1.0.1
- **Autore corretto**: Tutti i riferimenti all'autore aggiornati

## [1.0.0] - 2025-11-03

### 🎉 Rilascio Iniziale

Prima versione stabile di **Ceramica - Static Site Generator**.

### ✨ Aggiunte

#### Core Features
- **Generatore di siti statici** completo in Python
- Conversione **Markdown → HTML** con supporto estensioni
- Sistema di **template Jinja2** personalizzabili
- **Frontmatter** per metadata delle pagine
- Supporto per **strutture annidate** con sottocartelle
- Calcolo automatico dei **path relativi** in base alla profondità
- **Build separate** per debug e deploy

#### Template System
- Template `base.html` - Layout generico per pagine standard
- Template `blog.html` - Layout specializzato per post del blog con metadata, tags e sidebar
- Template `project.html` - Layout per progetti con badge status e link GitHub/demo
- Template `esempio-commentato.html` - Template didattico con commenti dettagliati
- Supporto **template multipli** senza configurazione aggiuntiva
- Sistema di **variabili** da frontmatter completamente flessibile

#### Struttura Cartelle
- `pages/` - File Markdown sorgente con supporto sottocartelle illimitate
- `config/` - File di configurazione JSON centralizzato
- `template/` - Template HTML Jinja2
- `assets/` - CSS, JavaScript e risorse statiche
- `resources/` - Risorse da copiare direttamente nell'output
- `debug/` - Output per sviluppo locale
- `deploy/` - Output per produzione
- `docs/` - Documentazione completa del progetto

#### Assets e Styling
- **CSS responsive** con variabili CSS
- Stili specifici per ogni template (base, blog, project)
- **JavaScript** con funzionalità interattive:
  - Smooth scrolling per link interni
  - Evidenziazione link attivo nella navigazione
  - Utility per messaggi temporanei

#### Documentazione
- **README.md** completo con guida installazione e utilizzo
- **JINJA2_GUIDA.md** - Tutorial completo sulla sintassi Jinja2 (45+ esempi)
- **JINJA2_CHEATSHEET.md** - Riferimento rapido stampabile
- **template/README.md** - Guida completa al sistema template
- **docs/README.md** - Indice documentazione con percorso apprendimento
- **CERAMICA.md** - Informazioni sul progetto e filosofia del nome
- **MIGRATION.md** - Log della migrazione e rinominazione

#### Pagine di Esempio
- `pages/index.md` - Home page
- `pages/about.md` - Pagina About
- `pages/blog/index.md` - Indice blog
- `pages/blog/primo-post.md` - Esempio post blog
- `pages/blog/secondo-post.md` - Esempio post blog
- `pages/blog/2025/index.md` - Archivio annuale
- `pages/blog/2025/novembre.md` - Post con struttura profonda (3 livelli)
- `pages/progetti/index.md` - Indice progetti
- `pages/progetti/progetto-1.md` - Esempio progetto

### 🔧 Caratteristiche Tecniche

#### Parser e Rendering
- Supporto estensioni Markdown: `extra`, `codehilite`, `toc`, `nl2br`
- Parser frontmatter con formato `key: value`
- Rendering Jinja2 con tutte le funzionalità (loop, condizioni, filtri)

#### Gestione Path
- Calcolo automatico `base_path` in base alla profondità della pagina
- Supporto per strutture annidate a profondità illimitata
- Path relativi che funzionano ovunque nel file system

#### Build System
- Modalità `debug` per sviluppo locale
- Modalità `deploy` per produzione
- Copia automatica di assets e resources
- Pulizia automatica directory output prima della build
- Creazione automatica sottocartelle nell'output

### 📋 Requisiti
- Python 3.7+
- markdown==3.5.1
- jinja2==3.1.2
- pygments==2.17.2

### 🎯 File Principali
- `build.py` - Script principale di generazione (272 righe)
- `requirements.txt` - Dipendenze Python
- `config/config.json` - Configurazione sito centralizzata
- `.gitignore` - File da escludere dal version control

### 👤 Autore
- **nemorino1960**

### 🤖 Sviluppo
Questo progetto è stato sviluppato con l'assistenza di AI (GitHub Copilot + Claude 3.5 Sonnet) 
per accelerare l'implementazione. L'architettura, le decisioni di design e la direzione 
del progetto sono di nemorino1960. L'AI è stata utilizzata come strumento di sviluppo avanzato, 
fornendo codice e documentazione sotto la guida e supervisione dell'autore.

### 📝 Note di Rilascio

Ceramica 1.0.0 rappresenta il primo rilascio stabile del generatore. 
Il progetto è completo, testato e pronto per l'uso in produzione.

Il nome "Ceramica" richiama l'arte della ceramica: come un artigiano trasforma 
l'argilla grezza in opere d'arte, Ceramica trasforma il Markdown in siti web eleganti. 
Questa metafora si estende anche al processo di sviluppo: l'artigiano (nemorino1960) 
usa strumenti moderni (AI) per dare forma alla sua visione.

### 🔗 Link
- Repository: https://github.com/nemorino1960/ceramica
- Documentazione: https://github.com/nemorino1960/ceramica/tree/main/docs
- Issues: https://github.com/nemorino1960/ceramica/issues
- Releases: https://github.com/nemorino1960/ceramica/releases

---

## Formato Versioni

Il progetto segue il [Semantic Versioning](https://semver.org/lang/it/):

- **MAJOR** (1.x.x): Modifiche incompatibili con versioni precedenti
- **MINOR** (x.1.x): Nuove funzionalità mantenendo compatibilità
- **PATCH** (x.x.1): Bug fix e miglioramenti minori

## Tipi di Modifiche

- **Aggiunte** - Nuove funzionalità
- **Modifiche** - Cambiamenti a funzionalità esistenti
- **Deprecate** - Funzionalità che saranno rimosse
- **Rimosse** - Funzionalità rimosse
- **Fix** - Correzione bug
- **Sicurezza** - Vulnerabilità corrette

[1.0.1]: https://github.com/nemorino1960/ceramica/releases/tag/v1.0.1
[1.0.0]: https://github.com/nemorino1960/ceramica/releases/tag/v1.0.0
