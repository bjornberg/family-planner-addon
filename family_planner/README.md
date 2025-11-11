# Family Planner - Home Assistant Add-on

Family planning app met kalender, taken, dagelijkse routines en weekoverzicht.

## Features

- 📅 **Kalender** - Afspraken voor het hele gezin
- ✅ **Taken** - Eenmalige en terugkerende taken
- 🌅 **Ochtendroutine** - Standaard taken voor kinderen
- 🌙 **Avondroutine** - Bedtijd routine
- 📊 **Weekoverzicht** - Zie voltooide taken per dag
- 🏆 **Puntensysteem** - Leaderboard met medailles
- 🌓 **Dark mode** - Licht en donker thema
- 💾 **Automatisch opslaan** - Alle data wordt direct opgeslagen

## Installatie

### Stap 1: Add-on Repository Toevoegen

Er zijn twee manieren om deze add-on te installeren:

#### Optie A: Via Local Add-on (Makkelijkst)

1. Kopieer de hele `addon` folder naar je Home Assistant:
   - Via File Editor, Samba share, of SSH
   - Plaats in: `/addon/family_planner/`
   - De volledige pad wordt: `/addon/family_planner/config.yaml`

2. Ga in Home Assistant naar:
   - **Settings** → **Add-ons** → **Add-on Store**
   - Klik rechtsboven op de **3 puntjes** (⋮)
   - Klik op **"Check for updates"**

3. De add-on verschijnt nu onder **"Local add-ons"**

#### Optie B: Via GitHub Repository (Gevorderd)

1. Upload de `addon` folder naar een GitHub repository

2. Voeg de repository toe in Home Assistant:
   - **Settings** → **Add-ons** → **Add-on Store**
   - Klik rechtsboven op de **3 puntjes** (⋮)
   - **Repositories**
   - Voeg toe: `https://github.com/jouw-gebruikersnaam/jouw-repo`

### Stap 2: Installeer de Add-on

1. Zoek **"Family Planner"** in de Add-on Store
2. Klik erop en klik **"Install"**
3. Wacht tot installatie voltooid is (kan enkele minuten duren)

### Stap 3: Start de Add-on

1. Ga naar de **Configuration** tab (optioneel, default poort is 5000)
2. Ga terug naar **Info** tab
3. Klik **"Start"**
4. Schakel **"Start on boot"** aan (optioneel maar aanbevolen)
5. Schakel **"Watchdog"** aan (optioneel, herstart add-on bij crash)

### Stap 4: Open Family Planner

Klik op **"OPEN WEB UI"** of ga naar:

```
http://homeassistant.local:5000
```

Of vanaf andere apparaten:
```
http://[HOMEASSISTANT_IP]:5000
```

## Configuratie

De add-on heeft minimale configuratie nodig.

### Opties

- **port**: Poort waarop de web interface draait (default: 5000)

Voorbeeld configuratie:
```yaml
port: 5000
```

## Data Opslag

Alle data wordt opgeslagen in `/data/data.json` binnen de add-on.

Deze data is **persistent** - blijft bewaard zelfs na:
- Add-on herstart
- Home Assistant herstart
- Add-on updates

### Backup

De data wordt automatisch meegenomen in Home Assistant backups.

Je kunt ook handmatig backuppen via File Editor of SSH:
- Data bestand: `/addon_configs/[addon-slug]/data.json`

## Toevoegen aan Dashboard

Voeg Family Planner toe aan je Home Assistant dashboard:

1. **Edit Dashboard** → **Add Card** → **Webpage Card**
2. URL: `/api/hassio_ingress/[addon-slug]`

Of als iFrame:
1. **Edit Dashboard** → **Add Card** → **Manual Card**
2. Voeg toe:
```yaml
type: iframe
url: http://homeassistant.local:5000
aspect_ratio: 100%
```

## Netwerktoegang

De Family Planner is toegankelijk vanaf:
- ✅ Home Assistant web interface
- ✅ Alle apparaten op je lokale netwerk
- ✅ Via Home Assistant Ingress (beveiligd)
- ❌ Internet (tenzij je port forwarding instelt)

## Troubleshooting

### Add-on start niet

1. Check de logs:
   - Open add-on → **Log** tab
2. Veelvoorkomende problemen:
   - Poort 5000 al in gebruik → Wijzig poort in configuratie
   - Fout in configuratie → Check YAML syntax

### Kan niet verbinden

1. Controleer of add-on draait (groen)
2. Probeer: `http://[HOMEASSISTANT_IP]:5000`
3. Check firewall instellingen

### Data verdwijnt

1. Check of add-on nog draait
2. Check logs voor errors
3. Herstel via Home Assistant backup

### Performance problemen

De add-on is zeer licht en zou geen performance problemen moeten geven.
Als het toch traag is:
- Check Home Assistant system resources
- Overweeg hardware upgrade als systeem overbelast is

## Support

Voor vragen of problemen:
- Open een issue op GitHub
- Check Home Assistant community forum

## Credits

Gebouwd met:
- Python 3
- Flask
- React (via CDN)
- Tailwind CSS (via CDN)

## Licentie

MIT License - Vrij te gebruiken en aan te passen
