# Importerar pytest för att kunna testa flera olika städer.
import pytest

# Importerar funktionen som vi ska skapa.
from väder_logic import kontrollera_stad, skapa_prognos


# Testar att de fem tillåtna städerna godkänns.
@pytest.mark.parametrize(
    "stad",
    ["Stockholm", "Göteborg", "Malmö", "Umeå", "Kiruna"],
)
def test_giltiga_städer(stad):
    assert kontrollera_stad(stad) is True


# Testar att en stad som inte finns i listan avvisas.
def test_ogiltig_stad():
    assert kontrollera_stad("Uppsala") is False


# Testar att väderdata omvandlas till en prognos för tre dagar.
def test_skapa_prognos():
    väderdata = {
        "daily": {
            "time": [
                "2026-11-06",
                "2026-11-07",
                "2026-11-08",
            ],
            "temperature_2m_max": [8.5, 9.0, 7.0],
            "temperature_2m_min": [3.0, 4.0, 2.0],
            "precipitation_sum": [0.0, 2.5, 1.0],
        }
    }

    resultat = skapa_prognos(väderdata)

    assert len(resultat) == 3
    assert resultat[0]["datum"] == "2026-11-06"
    assert resultat[0]["max_temp"] == 8.5
    assert resultat[0]["min_temp"] == 3.0
    assert resultat[0]["nederbörd"] == 0.0
