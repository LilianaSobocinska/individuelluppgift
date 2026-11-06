# Importerar Flask-funktioner för att skapa webbappen och visa HTML-sidor.
from flask import Flask, render_template, request

# Importerar funktionerna som hämtar och bearbetar väderdata.
from väder_api import VäderApiFel, hamta_väderdata
from väder_logic import STÄDER, kontrollera_stad, skapa_prognos

# Skapar Flask-applikationen.
app = Flask(__name__)


# Koordinaterna för de fem städerna.
STAD_KOORDINATER = {
    "Stockholm": (59.33, 18.07),
    "Göteborg": (57.71, 11.97),
    "Malmö": (55.61, 13.00),
    "Umeå": (63.83, 20.26),
    "Kiruna": (67.86, 20.23),
}


# Eget filter som visar temperatur med en decimal.
@app.template_filter("temperatur")
def temperatur_filter(värde):
    return f"{värde:.1f} °C"


# Startsidan där användaren väljer stad.
@app.route("/")
def index():
    return render_template(
        "index.html",
        städer=STÄDER,
    )


# Visar väderinformation för den valda staden.
@app.route("/väder")
def visa_väder():

    # Hämtar vald stad från webbadressens parametrar.
    stad = request.args.get("stad", "")

    # Kontrollerar att staden är tillåten.
    if not kontrollera_stad(stad):
        return render_template(
            "fel.html",
            meddelande="Ogiltig stad. Välj en stad i listan.",
        ), 400

    # Hämtar stadens koordinater.
    latitud, longitud = STAD_KOORDINATER[stad]

    try:
        # Hämtar väderdata från API:et.
        väderdata = hamta_väderdata(latitud, longitud)

        # Hämtar den aktuella väderinformationen.
        aktuellt = väderdata["current"]

        # Omvandlar API-data till en prognos för tre dagar.
        prognos = skapa_prognos(väderdata)

        return render_template(
            "väder.html",
            stad=stad,
            aktuellt=aktuellt,
            prognos=prognos,
        )

    except (VäderApiFel, KeyError, TypeError):
        return render_template(
            "fel.html",
            meddelande=(
                "Väderinformationen är inte tillgänglig just nu. Försök igen senare."
            ),
        ), 503


# En egen sida för adresser som inte finns.
@app.errorhandler(404)
def sidan_hittas_inte(fel):
    return render_template(
        "fel.html",
        meddelande="Sidan hittades inte.",
    ), 404


# Startar webbservern när programmet körs direkt.
if __name__ == "__main__":
    app.run(debug=True)
