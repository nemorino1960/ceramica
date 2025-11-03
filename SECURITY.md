# Security Policy

## 🔒 Segnalare una Vulnerabilità

La sicurezza di Ceramica è importante. Se scopri una vulnerabilità di sicurezza, ti preghiamo di NON aprire una issue pubblica.

### Come Segnalare

Invia un'email a: **nemorino60@[tua-email]** con:

- Descrizione della vulnerabilità
- Passi per riprodurla
- Possibile impatto
- Suggerimenti per risolverla (se disponibili)

### Cosa Aspettarsi

- **Conferma iniziale** entro 48 ore
- **Valutazione** della vulnerabilità entro 7 giorni
- **Fix e release** in base alla gravità
- **Credito** nella release notes (se desiderato)

## ✅ Versioni Supportate

| Versione | Supportata          |
| -------- | ------------------- |
| 1.0.x    | :white_check_mark:  |
| < 1.0    | :x:                 |

## 🛡️ Politiche di Sicurezza

- Ceramica è un generatore statico e non esegue codice arbitrario dall'input
- L'output HTML è sicuro per default (Jinja2 auto-escape)
- Tutte le dipendenze sono aggiornate e verificate
- I file Markdown sono trattati come contenuto trusted

## 🔍 Ambito

Consideriamo vulnerabilità di sicurezza:
- Esecuzione di codice arbitrario
- XSS nell'output generato
- Path traversal
- Dipendenze vulnerabili

Non consideriamo vulnerabilità:
- Social engineering
- DoS locale (è un tool locale)
- Problemi nei siti generati dagli utenti

## 📝 Divulgazione

Seguiamo la **responsible disclosure**:
1. La vulnerabilità viene segnalata privatamente
2. Viene verificata e corretta
3. Viene rilasciata una patch
4. Viene pubblicato un advisory
5. Il ricercatore riceve credito (se desidera)

Grazie per aiutare a mantenere Ceramica sicuro! 🏺🔒
