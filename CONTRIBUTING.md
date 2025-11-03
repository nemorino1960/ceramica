# Contributing to Ceramica

Prima di tutto, grazie per il tuo interesse nel contribuire a Ceramica! 🏺

## 📋 Come Contribuire

### 🐛 Segnalare Bug

Se trovi un bug, apri una [Issue](https://github.com/nemorino60/ceramica/issues) con:

- **Titolo chiaro** che descrive il problema
- **Descrizione dettagliata** del bug
- **Passi per riprodurre** il problema
- **Comportamento atteso** vs comportamento attuale
- **Versione** di Ceramica (`python build.py --version`)
- **Sistema operativo** e versione Python

### ✨ Proporre Nuove Funzionalità

Per proporre una nuova funzionalità:

1. Apri una [Issue](https://github.com/nemorino60/ceramica/issues)
2. Usa il tag `enhancement`
3. Descrivi la funzionalità e il caso d'uso
4. Discuti l'implementazione con i maintainer

### 🔧 Inviare Pull Request

1. **Fork** il repository
2. **Crea un branch** per la tua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** le modifiche (`git commit -m 'Add some AmazingFeature'`)
4. **Push** al branch (`git push origin feature/AmazingFeature`)
5. **Apri una Pull Request**

#### Linee Guida per Pull Request

- ✅ Codice pulito e ben commentato
- ✅ Segui lo stile Python PEP 8
- ✅ Testa le modifiche (debug e deploy build)
- ✅ Aggiorna la documentazione se necessario
- ✅ Descrizione chiara della PR

### 📝 Migliorare la Documentazione

La documentazione è importante! Se trovi:
- Errori di battitura
- Spiegazioni poco chiare
- Sezioni mancanti
- Esempi migliorabili

Sentiti libero di inviare una PR con miglioramenti.

### 🎨 Template e Temi

Contributi di template sono benvenuti:
- Nuovi template HTML/CSS
- Variazioni di stile
- Template specializzati (e-commerce, landing page, etc.)

## 🧪 Testing

Prima di inviare una PR, assicurati che:

```bash
# Build test
python3 build.py debug
python3 build.py deploy

# Test locale
cd debug
python3 -m http.server 8000
# Verifica che tutto funzioni
```

## 📐 Code Style

- Usa **4 spazi** per indentazione
- Segui **PEP 8** per Python
- Commenta il codice complesso
- Usa **nomi descrittivi** per variabili e funzioni
- Mantieni le linee sotto **100 caratteri** quando possibile

## 🏗️ Struttura Commit

Usa commit messages chiari:

```
tipo: Breve descrizione (max 50 caratteri)

Descrizione dettagliata se necessaria.
- Punto 1
- Punto 2

Fixes #123
```

**Tipi:**
- `feat`: Nuova funzionalità
- `fix`: Bug fix
- `docs`: Documentazione
- `style`: Formattazione, mancano punti e virgola, etc.
- `refactor`: Refactoring del codice
- `test`: Aggiunta test
- `chore`: Manutenzione

## 🎯 Aree di Contributo

Cerchiamo contributi in:

- 🔧 **Core Features**: Miglioramenti al generatore
- 🎨 **Template**: Nuovi template e temi
- 📚 **Documentazione**: Guide, tutorial, esempi
- 🌍 **Localizzazione**: Traduzioni
- 🐛 **Bug Fixes**: Correzioni
- ⚡ **Performance**: Ottimizzazioni
- 🧪 **Testing**: Unit test, integration test

## 💬 Comunicazione

- Per domande generali, usa le [Discussions](https://github.com/nemorino60/ceramica/discussions)
- Per bug e feature, usa le [Issues](https://github.com/nemorino60/ceramica/issues)
- Sii rispettoso e costruttivo

## 📄 Licenza

Contribuendo a Ceramica, accetti che i tuoi contributi saranno rilasciati sotto la [licenza MIT](LICENSE).

## 🙏 Grazie!

Ogni contributo, grande o piccolo, è apprezzato! Grazie per aiutare a rendere Ceramica migliore! 🏺✨

---

**Domande?** Apri una [Discussion](https://github.com/nemorino60/ceramica/discussions) o contatta [@nemorino60](https://github.com/nemorino60)
