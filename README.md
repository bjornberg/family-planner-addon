# Family Planner - Home Assistant Add-on

[![Home Assistant Add-on](https://img.shields.io/badge/Home%20Assistant-Add--on-blue.svg)](https://www.home-assistant.io/)

Een complete family planning applicatie voor Home Assistant met kalender, taken, routines en weekoverzicht.

![Family Planner Screenshot](https://via.placeholder.com/800x400.png?text=Family+Planner+Screenshot)

## ✨ Features

- 📅 **Gezinskalender** - Afspraken voor het hele gezin
- ✅ **Takenbeheer** - Eenmalige en dagelijks terugkerende taken
- 🌅 **Ochtendroutine** - Standaard taken voor kinderen
- 🌙 **Avondroutine** - Bedtijd routine template
- 📊 **Weekoverzicht** - Zie voltooide taken per dag
- 🏆 **Puntensysteem** - Leaderboard met medailles om kinderen te motiveren
- 🌓 **Dark mode** - Licht en donker thema
- 👨‍👩‍👧‍👦 **Kleurcodering** - Elke persoon heeft eigen kleur
- 💾 **Automatisch opslaan** - Alle data wordt direct opgeslagen

## 📥 Installatie

### Stap 1: Add-on Repository Toevoegen

Klik op deze knop om de repository toe te voegen:

[![Add Repository](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fbjornberg%2Ffamily-planner-addon)

Of voeg handmatig toe:

1. Ga in Home Assistant naar **Settings** → **Add-ons** → **Add-on Store**
2. Klik rechtsboven op **⋮** → **Repositories**
3. Voeg toe: `https://github.com/bjornberg/family-planner-addon`
4. Klik **Add**

### Stap 2: Add-on Installeren

1. Zoek **"Family Planner"** in de Add-on Store
2. Klik **Install**
3. Wacht tot installatie voltooid is
4. Klik **Start**
5. Schakel **"Start on boot"** in
6. Klik **"OPEN WEB UI"**

## ⚙️ Configuratie

```yaml
port: 5000  # Wijzig als poort 5000 al in gebruik is
```

## 🚀 Gebruik

### Kalender
Voeg afspraken toe voor gezinsleden met datum en tijd.

### Taken
- **Eenmalige taken:** Voor specifieke taken die één keer gedaan moeten worden
- **Terugkerende taken:** Dagelijkse taken die elke dag terugkomen

### Routines
Gebruik de snelkeuze knoppen om een complete routine toe te voegen:
- **🌅 Ochtendroutine:** Aankleden, tanden poetsen, ontbijten, tas inpakken
- **🌙 Avondroutine:** Pyjama aan, tanden poetsen, boekje lezen

### Weekoverzicht
Bekijk per dag welke taken zijn voltooid en wie hoeveel punten heeft verdiend.

## 📊 Puntensysteem

Elke voltooide taak levert 1 punt op. Het leaderboard toont:
- 🥇 Goud voor #1
- 🥈 Zilver voor #2
- 🥉 Brons voor #3
- 🏅 Medaille voor #4

## 🎨 Personalisatie

Pas de gezinsleden aan in de code (`family_planner/family-planner.html`):
```javascript
const familyMembers = ['Papa', 'Mama', 'Kind 1', 'Kind 2', 'Iedereen'];
```

## 💾 Data Opslag

Alle data wordt opgeslagen in `/data/data.json` binnen de add-on container. Dit wordt automatisch meegenomen in Home Assistant backups.

## 🌐 Toegang

De Family Planner is toegankelijk vanaf:
- Home Assistant Web UI (via "OPEN WEB UI" knop)
- Direct via poort: `http://homeassistant.local:5000`
- Vanaf elk apparaat op je netwerk: `http://[HA-IP]:5000`

## 🔧 Technische Details

- **Backend:** Python 3 + Flask
- **Frontend:** React 18 (CDN) + Tailwind CSS
- **Database:** JSON bestand
- **Poort:** 5000 (configureerbaar)
- **Architecturen:** armhf, armv7, aarch64, amd64, i386

## 📚 Documentatie

Voor meer informatie, zie de [volledige documentatie](family_planner/README.md).

## 🐛 Problemen Melden

Heb je een bug gevonden of een feature request?
[Open een issue](https://github.com/bjornberg/family-planner-addon/issues)

## 🤝 Bijdragen

Pull requests zijn welkom! Voor grote wijzigingen, open eerst een issue om te bespreken wat je wilt wijzigen.

## 📄 Licentie

[MIT License](LICENSE)

## 👨‍💻 Credits

Ontwikkeld met ❤️ voor gezinnen die hun dagelijkse planning willen vereenvoudigen.

---

**Veel plezier met je Family Planner! 👨‍👩‍👧‍👦**
