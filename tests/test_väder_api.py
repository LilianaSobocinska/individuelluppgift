# Importerar mock för att simulera API-anrop.
from unittest.mock import Mock, patch

import pytest
import requests

# Importerar vår egen API-modul.
from väder_api import VäderApiFel, hamta_väderdata


# Testar att API-data hämtas korrekt.
@patch("väder_api.requests.get")
def test_hamta_väderdata(mock_get):
    # Skapar ett simulerat svar från API:et.
    mock_svar = Mock()
    mock_svar.json.return_value = {
        "current": {
            "temperature_2m": 8.5,
            "wind_speed_10m": 12.0,
        }
    }

    mock_get.return_value = mock_svar

    resultat = hamta_väderdata(59.33, 18.07)

    assert resultat["current"]["temperature_2m"] == 8.5
    mock_get.assert_called_once()


# Testar att ett nätverksfel hanteras.
@patch("väder_api.requests.get")
def test_nätverksfel(mock_get):
    mock_get.side_effect = requests.Timeout

    with pytest.raises(VäderApiFel):
        hamta_väderdata(59.33, 18.07)


# Testar att ett HTTP-fel hanteras.
@patch("väder_api.requests.get")
def test_http_fel(mock_get):
    mock_get.side_effect = requests.HTTPError

    with pytest.raises(VäderApiFel):
        hamta_väderdata(59.33, 18.07)
