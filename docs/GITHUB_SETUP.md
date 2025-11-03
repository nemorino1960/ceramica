# Guida Pubblicazione su GitHub

Questa guida ti aiuta a pubblicare Ceramica su GitHub.

## 📋 Prerequisiti

1. Account GitHub (https://github.com)
2. Git installato localmente
3. Repository locale di Ceramica pronto

## 🚀 Passaggi per la Pubblicazione

### 1. Crea il Repository su GitHub

1. Vai su https://github.com/new
2. Imposta:
   - **Repository name:** `ceramica`
   - **Description:** "🏺 Static Site Generator - Un generatore di siti statici minimale scritto in Python"
   - **Visibility:** Public (o Private se preferisci)
   - **NON** inizializzare con README, .gitignore o license (li abbiamo già)

### 2. Inizializza Git Locale (se non già fatto)

```bash
cd /Users/nemorino/MEGA/IPERNOTES/WEBDEV/ceramica

# Inizializza repository
git init

# Aggiungi tutti i file
git add .

# Primo commit
git commit -m "Initial commit: Ceramica v1.0.0

- Static site generator in Python
- Template system con Jinja2
- Markdown to HTML conversion
- Nested folder structure support
- Comprehensive documentation
- MIT License"
```

### 3. Collega al Repository Remoto

```bash
# Aggiungi remote (sostituisci se necessario)
git remote add origin https://github.com/nemorino60/ceramica.git

# Verifica remote
git remote -v

# Rinomina branch a main (se necessario)
git branch -M main

# Push iniziale
git push -u origin main
```

### 4. Verifica su GitHub

Vai su https://github.com/nemorino60/ceramica e verifica che:
- ✅ Tutti i file siano presenti
- ✅ README.md sia visualizzato correttamente
- ✅ Licenza sia riconosciuta
- ✅ Badge funzionino (potrebbero richiedere qualche minuto)

### 5. Configura GitHub Pages (Opzionale)

Per pubblicare automaticamente il sito:

1. Vai su **Settings** > **Pages**
2. Source: **GitHub Actions**
3. Il workflow `.github/workflows/pages.yml` farà il deploy automatico
4. Il sito sarà disponibile su: `https://nemorino60.github.io/ceramica`

### 6. Crea il Primo Release

1. Vai su **Releases** > **Create a new release**
2. Imposta:
   - **Tag version:** `v1.0.0`
   - **Release title:** `Ceramica v1.0.0 - Prima Release Stabile`
   - **Description:** Copia da `RELEASE_NOTES.md`
   - **Assets:** GitHub li creerà automaticamente
3. **Publish release**

### 7. Configura Protezioni Branch (Consigliato)

1. Vai su **Settings** > **Branches**
2. **Add branch protection rule**
3. Branch name pattern: `main`
4. Abilita:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging

### 8. Abilita Discussions (Opzionale)

1. Vai su **Settings** > **General**
2. Features > **Discussions** > Check
3. Questo abiliterà le discussioni community

### 9. Aggiungi Topics

1. Vai sulla home del repository
2. Clicca su ⚙️ (Settings) vicino ad "About"
3. Aggiungi topics:
   - `static-site-generator`
   - `python`
   - `markdown`
   - `jinja2`
   - `website-builder`
   - `html-generator`

## 📊 Comandi Git Utili

### Workflow Quotidiano

```bash
# Verifica stato
git status

# Aggiungi modifiche
git add .

# Commit
git commit -m "feat: descrizione modifica"

# Push
git push

# Pull (aggiornamenti)
git pull
```

### Lavorare con Branch

```bash
# Crea nuovo branch per feature
git checkout -b feature/nome-feature

# Lavora sulla feature...
git add .
git commit -m "feat: nuova feature"

# Push del branch
git push -u origin feature/nome-feature

# Torna a main
git checkout main

# Merge (dopo PR su GitHub)
git pull
```

### Tag e Release

```bash
# Crea tag
git tag -a v1.0.1 -m "Release 1.0.1"

# Push tag
git push origin v1.0.1

# Lista tag
git tag -l
```

## 🔄 Aggiornamenti Futuri

Quando rilasci una nuova versione:

1. Aggiorna `VERSION` file
2. Aggiorna `__version__` in `build.py`
3. Aggiorna `CHANGELOG.md`
4. Commit e push
5. Crea nuovo tag e release su GitHub

## 🐛 Risoluzione Problemi

### Errore: remote origin already exists
```bash
git remote remove origin
git remote add origin https://github.com/nemorino60/ceramica.git
```

### Errore: rejected (non-fast-forward)
```bash
git pull --rebase origin main
git push
```

### File troppo grandi
Aggiungi al `.gitignore` e rimuovi dalla cache:
```bash
echo "file-grande.zip" >> .gitignore
git rm --cached file-grande.zip
git commit -m "Remove large file"
```

## ✅ Checklist Finale

Prima di pubblicare, verifica:

- [ ] Tutti i file sensibili sono in `.gitignore`
- [ ] README.md è completo e formattato
- [ ] CHANGELOG.md è aggiornato
- [ ] LICENSE è presente
- [ ] Link GitHub nella documentazione sono corretti
- [ ] Version è corretta in tutti i file
- [ ] Build test funziona (`python build.py debug`)
- [ ] Nessuna informazione personale/sensibile nel codice

## 📞 Supporto

Se hai problemi:
- [Documentazione Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [GitHub Community](https://github.community/)

---

**Buona pubblicazione! 🚀**

Una volta pubblicato, condividi il link: https://github.com/nemorino60/ceramica
