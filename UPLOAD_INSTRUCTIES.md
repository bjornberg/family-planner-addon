# 🚀 GitHub Upload Instructies

Alles staat klaar! Je hoeft alleen maar te uploaden naar GitHub.

## 📁 Wat zit in deze Folder?

```
github-upload/
├── family_planner/          ← De add-on (alle bestanden)
│   ├── config.yaml
│   ├── Dockerfile
│   ├── run.sh
│   ├── server.py
│   ├── family-planner.html
│   ├── README.md
│   └── CHANGELOG.md
├── repository.json          ← Repository configuratie
├── README.md               ← Repository homepage
├── LICENSE                 ← MIT License
├── .gitignore             ← Git ignore file
└── UPLOAD_INSTRUCTIES.md   ← Dit bestand
```

**Dit is PRECIES de structuur die GitHub nodig heeft!** ✅

---

## 🎯 Optie 1: Via GitHub Web (Makkelijkst - Aanbevolen)

### Stap 1: Maak GitHub Account (Als je die nog niet hebt)

1. Ga naar https://github.com
2. Klik **Sign up**
3. Vul email, wachtwoord, username in
4. Verifieer je email

### Stap 2: Nieuwe Repository Maken

1. Log in op GitHub
2. Klik rechtsboven op **"+"** → **"New repository"**
3. Vul in:
   - **Repository name:** `family-planner-addon`
   - **Description:** `Home Assistant add-on voor family planning`
   - **Public** (aangevinkt)
   - **Add a README file** (NIET aanvinken - we uploaden onze eigen)
4. Klik **"Create repository"**

### Stap 3: Upload Bestanden

GitHub toont nu een lege repository. Scroll naar beneden naar **"uploading an existing file"**.

**Upload ALLE bestanden uit `D:\Claude\Family-Planner\github-upload\`:**

#### Methode A: Sleep & Drop (Aanbevolen)

1. Klik op **"uploading an existing file"** link
2. Open **`D:\Claude\Family-Planner\github-upload\`** in Windows Verkenner
3. **Selecteer ALLES** in die folder (CTRL+A)
4. **Sleep** naar het GitHub upload veld
5. Wacht tot alles geüpload is
6. Scroll naar beneden
7. Typ commit message: `Initial commit: Family Planner add-on v1.0.0`
8. Klik **"Commit changes"**

#### Methode B: Handmatig Per Bestand

Als slepen niet werkt:

1. Klik **"Add file"** → **"Upload files"**
2. **Klik "choose your files"**
3. Selecteer alle bestanden en folders uit `github-upload`
4. Upload
5. Commit message: `Initial commit: Family Planner add-on v1.0.0`
6. **"Commit changes"**

### Stap 4: Verifieer Upload

Je repository moet er nu zo uitzien:

```
family-planner-addon/
├── family_planner/
├── .gitignore
├── LICENSE
├── README.md
└── repository.json
```

**Controleer of `family_planner` folder bestaat en bestanden bevat!**

### Stap 5: Pas URL aan in repository.json

1. Klik op **`repository.json`**
2. Klik op het **potlood icoon** (Edit)
3. Vervang `JOUW-USERNAME` met je echte GitHub username
   ```json
   "url": "https://github.com/jouw-echte-username/family-planner-addon"
   ```
4. Scroll naar beneden
5. **"Commit changes"** → **"Commit directly to the main branch"** → **"Commit changes"**

### Stap 6: Pas URL aan in README.md

1. Klik op **`README.md`**
2. Klik **potlood icoon** (Edit)
3. Zoek alle `JOUW-USERNAME` teksten
4. Vervang met je echte username (Er zijn er meerdere!)
5. **"Commit changes"**

---

## ✅ Stap 7: Toevoegen aan Home Assistant

1. **Kopieer je repository URL:**
   ```
   https://github.com/jouw-username/family-planner-addon
   ```

2. **In Home Assistant:**
   - Settings → Add-ons → Add-on Store
   - Klik ⋮ (rechtsboven) → **Repositories**
   - Plak je URL
   - Klik **Add**
   - Sluit het venster

3. **Installeer de add-on:**
   - Scroll in de Add-on Store
   - Je ziet nu jouw repository naam
   - Klik op **"Family Planner"**
   - Klik **"Install"**
   - Wacht 2-5 minuten
   - Klik **"Start"**
   - Schakel **"Start on boot"** in
   - Klik **"OPEN WEB UI"**

🎉 **Klaar! De add-on werkt nu!**

---

## 🎯 Optie 2: Via GitHub Desktop (Gebruiksvriendelijk)

Als je Git wilt leren gebruiken:

### Stap 1: Download GitHub Desktop

1. https://desktop.github.com
2. Installeer
3. Log in met je GitHub account

### Stap 2: Nieuwe Repository

1. **File** → **New Repository**
2. Name: `family-planner-addon`
3. Local path: Kies een locatie
4. **Create Repository**

### Stap 3: Bestanden Kopiëren

1. Open de repository folder (via GitHub Desktop: **Repository** → **Show in Explorer**)
2. Kopieer ALLE bestanden uit `D:\Claude\Family-Planner\github-upload\` naar deze folder
3. Ga terug naar GitHub Desktop
4. Je ziet alle files in de "Changes" lijst

### Stap 4: Commit & Push

1. Links onder: Summary: `Initial commit`
2. Description: `Family Planner add-on v1.0.0`
3. Klik **"Commit to main"**
4. Klik **"Publish repository"**
5. Vink **"Keep this code private"** UIT (voor public)
6. **"Publish repository"**

### Stap 5: Pas URLs aan (zie Optie 1, Stap 5-6)

---

## 🎯 Optie 3: Via Command Line (Geavanceerd)

Als je Git al kent:

```bash
cd "D:\Claude\Family-Planner\github-upload"

# Initialiseer Git
git init
git add .
git commit -m "Initial commit: Family Planner add-on v1.0.0"

# Maak repository op GitHub (via web, zie Optie 1)
# Dan:
git remote add origin https://github.com/jouw-username/family-planner-addon.git
git branch -M main
git push -u origin main
```

Vergeet niet `repository.json` en `README.md` aan te passen!

---

## ✅ Checklist

- [ ] GitHub account gemaakt
- [ ] Repository `family-planner-addon` aangemaakt
- [ ] Alle bestanden uit `github-upload` folder geüpload
- [ ] `repository.json` aangepast met jouw username
- [ ] `README.md` aangepast met jouw username
- [ ] Repository URL toegevoegd in Home Assistant
- [ ] Add-on geïnstalleerd
- [ ] Add-on gestart
- [ ] Getest in browser

---

## 🆘 Hulp Nodig?

### Upload werkt niet?

- Probeer kleinere batches (eerst repository.json, dan LICENSE, etc.)
- Check internet verbinding
- Probeer GitHub Desktop (Optie 2)

### Kan bestanden niet selecteren?

- Zorg dat je ALLE bestanden selecteert inclusief `.gitignore` (hidden file!)
- In Windows: View → Show hidden files

### Add-on verschijnt niet in HA?

- Check of repository.json de goede URL heeft
- Reload de add-on store (⋮ → Reload)
- Check of je repository Public is (niet Private)

---

## 🎉 Succes!

Als je vast zit, laat het me weten! Maar deze instructies zouden je door het hele proces moeten leiden.

**Veel plezier met je Family Planner! 👨‍👩‍👧‍👦**
