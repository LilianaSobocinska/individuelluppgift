# Importerar requests för att kunna hämta data från ett API.
import requests

# Adressen till Open-Meteos väder-API.
API_ADRESS = "https://api.open-meteo.com/v1/forecast"


# Eget fel som används när väderdata inte kan hämtas.
class VäderApiFel(Exception):
    pass


# Hämtar väderdata för en stad med hjälp av koordinater.
def hamta_väderdata(latitud, longitud):

    # Parametrar som skickas till väder-API:et.
    parametrar = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m",
        "daily": ("temperature_2m_max,temperature_2m_min,precipitation_sum"),
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:
        # Skickar en förfrågan till API:et med en tidsgräns.
        svar = requests.get(
            API_ADRESS,
            params=parametrar,
            timeout=10,
        )

        # Kontrollerar om API:et svarade med ett HTTP-fel.
        svar.raise_for_status()

        # Gör om API-svaret från JSON till Python-data.
        return svar.json()

    except requests.RequestException as fel:
        # Gör om API-felet till ett eget felmeddelande.
        raise VäderApiFel("Det gick inte att hämta väderdata just nu.") from fel
