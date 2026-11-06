# Importerar pytest för att kunna testa Flask-applikationen.
import pytest

# Importerar Flask-applikationen och dess API-fel.
import app


# Skapar en testklient som kan besöka webbappens sidor.
@pytest.fixture
def client():
    app.app.config["TESTING"] = True

    with app.app.test_client() as testklient:
        yield testklient


# Testar att startsidan fungerar.
def test_startsida(client):
    svar = client.get("/")

    assert svar.status_code == 200
    assert b"Stockholm" in svar.data


# Testar att vädersidan visar väderdata.
def test_vadersida(client, monkeypatch):
    testdata = {
        "current": {
            "temperature_2m": 8.5,
            "wind_speed_10m": 12.0,
        },
        "daily": {
            "time": [
                "2026-11-06",
                "2026-11-07",
                "2026-11-08",
            ],
            "temperature_2m_max": [8, 9, 7],
            "temperature_2m_min": [3, 4, 2],
            "precipitation_sum": [1.5, 0.0, 2.5],
        },
    }

    # Ersätter det riktiga API-anropet med testdata.
    monkeypatch.setattr(
        app,
        "hamta_väderdata",
        lambda latitud, longitud: testdata,
    )

    svar = client.get("/väder?stad=Stockholm")

    assert svar.status_code == 200
    assert "8.5" in svar.get_data(as_text=True)
    assert "Stockholm" in svar.get_data(as_text=True)


# Testar att en stad som inte finns avvisas.
def test_ogiltig_stad(client):
    svar = client.get("/väder?stad=Uppsala")

    assert svar.status_code == 400
    assert "Ogiltig stad" in svar.get_data(as_text=True)


# Testar att ett API-fel visas på ett vänligt sätt.
def test_api_fel(client, monkeypatch):
    def simulera_api_fel(latitud, longitud):
        raise app.VäderApiFel("API fungerar inte")

    monkeypatch.setattr(
        app,
        "hamta_väderdata",
        simulera_api_fel,
    )

    svar = client.get("/väder?stad=Stockholm")

    assert svar.status_code == 503
    assert "inte tillgänglig" in svar.get_data(as_text=True)


# Testar att en okänd webbadress ger en egen 404-sida.
def test_sidan_hittas_inte(client):
    svar = client.get("/sida-som-inte-finns")

    assert svar.status_code == 404
    assert "Sidan hittades inte" in svar.get_data(as_text=True)