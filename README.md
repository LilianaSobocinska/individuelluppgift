# Väderkollen

## Om projektet

Väderkollen är en webbapplikation som jag har byggt med Python och Flask. Applikationen använder Open-Meteo API för att hämta väderinformation.

Användaren kan välja mellan fem svenska städer: Stockholm, Göteborg, Malmö, Umeå och Kiruna.

När användaren väljer en stad visas aktuell temperatur, vindhastighet och en väderprognos för tre dagar. Applikationen har även felhantering om en stad inte är giltig eller om API:et inte fungerar.

## Tekniker och bibliotek

I projektet har jag använt:

- Python – programmeringsspråk.
- Flask – för att skapa webbapplikationen.
- Jinja2 – för att visa dynamisk information i HTML.
- Requests – för att hämta information från Open-Meteo API.
- Pytest – för att testa programmets funktioner.
- Ruff – för att kontrollera och formatera koden.
- Bootstrap 5 – för webbplatsens design.
- HTML och CSS – för att bygga och utforma webbsidorna.

## Installation

För att köra projektet behöver Python vara installerat.

1. Klona projektet från GitHub eller ladda ner projektmappen.
2. Öppna projektmappen i terminalen.
3. Skapa en virtuell miljö:

```powershell
python -m venv venv
```

4. Aktivera den virtuella miljön:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Installera projektets bibliotek:

```powershell
python -m pip install -r requirements.txt
```

6. Installera utvecklingsverktygen:

```powershell
python -m pip install -r requirements-dev.txt
```

## Starta applikationen

Starta webbapplikationen med:

```powershell
python app.py
```

Öppna sedan webbläsaren och gå till:

http://127.0.0.1:5000

## Köra tester

För att köra alla tester använder man:

```powershell
python -m pytest -v
```

Projektet innehåller 15 tester som kontrollerar bland annat startsidan, vädersidan, ogiltiga städer, API-fel och väderlogiken.

För att kontrollera koden med Ruff använder man:

```powershell
python -m ruff check .
```

För att kontrollera formateringen använder man:

```powershell
python -m ruff format --check .
```

## Projektets struktur

```text
individuelluppgift prog2/
│
├── app.py
├── väder_api.py
├── väder_logic.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── bas.html
│   ├── index.html
│   ├── väder.html
│   └── fel.html
│
└── tests/
    ├── test_app.py
    ├── test_väder_api.py
    └── test_väder_logic.py
```

## Frågor att svara på:

### 1. Vad innebär mock och varför används det i tester?

Mock innebär att man ersätter en riktig funktion eller ett riktigt API-anrop med en simulerad version. I mitt projekt använder jag mock för att testa API-funktionen utan att behöva göra riktiga anrop till internet.

Det gör testerna snabbare och mer pålitliga. Jag kan själv bestämma vilket svar som ska komma från API:et och även testa vad som händer när ett fel uppstår.

### 2. Varför används timeout och raise_for_status()?

Timeout används för att bestämma hur länge programmet ska vänta på ett svar från API:et. I mitt projekt har jag satt gränsen till 10 sekunder. Om API:et inte svarar i tid kan programmet fånga felet och visa ett vänligt felmeddelande.

raise_for_status() används för att kontrollera om servern har svarat med ett HTTP-fel. Om ett sådant fel uppstår skapas ett undantag som programmet kan hantera.

### 3. Vad innebär Jinja2 template inheritance?

Template inheritance innebär att flera HTML-sidor kan använda samma grundmall. I mitt projekt heter grundmallen bas.html.

De andra HTML-sidorna använder grundmallen och fyller i sina egna innehållsdelar genom block. Det gör att jag slipper skriva samma kod flera gånger och att sidorna får en enhetlig design.

### 4. Vad är en fixture i Pytest?

En fixture är en funktion som förbereder något som testerna behöver. I mitt projekt använder jag en fixture för att skapa en Flask testklient.

Testklienten gör att jag kan testa webbapplikationens olika sidor utan att behöva starta en riktig webbserver. Flera tester kan använda samma fixture.

## API

Projektet använder Open-Meteo Forecast API:

https://api.open-meteo.com/v1/forecast

API:et används för att hämta aktuell temperatur, vindhastighet och väderprognos. Det behövs ingen API-nyckel.

## Avslutning

Syftet med projektet har varit att skapa en fungerande webbapplikation med Flask, API-hantering, felhantering och automatiserade tester. Jag har även arbetat med HTML, CSS och Bootstrap för att skapa en enkel och användarvänlig design.