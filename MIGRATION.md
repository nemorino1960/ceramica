# Ceramica - Migration Log

## Rinominazione Progetto

**Data:** 3 novembre 2025  
**Da:** static-site-generator  
**A:** ceramica  

## Modifiche Effettuate

### 1. Cartella Principale
- ✅ Rinominata da `/WEBDEV/static-site-generator/` a `/WEBDEV/ceramica/`

### 2. File Documentazione
- ✅ `README.md` - Titolo e riferimenti aggiornati
- ✅ `docs/README.md` - Documentazione aggiornata
- ✅ `CERAMICA.md` - Nuovo file informativo creato

### 3. File Sorgenti
- ✅ `build.py` - Docstring aggiornata
- ✅ `config/config.json` - Descrizione sito aggiornata
- ✅ `pages/index.md` - Contenuto aggiornato
- ✅ `pages/about.md` - Struttura cartella aggiornata
- ✅ `pages/progetti/progetto-1.md` - Nome progetto aggiornato

### 4. Verifica Dipendenze

#### Path Assoluti
- ✅ Nessun path assoluto trovato nel codice
- ✅ `build.py` usa `base_dir = "."` (path relativo)
- ✅ Tutti i path sono calcolati relativamente

#### Path Relativi
- ✅ `{{ page.base_path }}` calcolato automaticamente
- ✅ Template funzionanti a qualsiasi profondità
- ✅ Asset (CSS/JS) linkati correttamente

#### Build e Output
- ✅ Build test eseguito con successo
- ✅ Tutti i file generati correttamente
- ✅ HTML contiene riferimenti aggiornati

## Stato Finale

✅ **Progetto completamente rinominato e funzionante**

### Struttura Attuale
```
/Users/nemorino/MEGA/IPERNOTES/WEBDEV/
└── ceramica/
    ├── pages/
    ├── config/
    ├── template/
    ├── assets/
    ├── resources/
    ├── docs/
    ├── debug/
    ├── build.py
    ├── requirements.txt
    ├── README.md
    └── CERAMICA.md
```

### Comandi Aggiornati
```bash
# Navigazione
cd /Users/nemorino/MEGA/IPERNOTES/WEBDEV/ceramica

# Build
python3 build.py debug
python3 build.py deploy

# Server locale
cd debug && python3 -m http.server 8000
```

## Note
- Non sono richieste modifiche al codice per utilizzatori
- I path relativi garantiscono portabilità
- Il progetto può essere spostato ovunque senza problemi
- Tutte le funzionalità testate e funzionanti

---

**Ceramica** 🏺 - Static Site Generator
