# Lista över de fem städer som användaren får välja.
STÄDER = [
    "Stockholm",
    "Göteborg",
    "Malmö",
    "Umeå",
    "Kiruna",
]


# Kontrollerar om den valda staden finns i listan.
def kontrollera_stad(stad):
    return stad in STÄDER


# Omvandlar väderdata till en lista med tre dagars prognos.
def skapa_prognos(väderdata):

    prognos = []

    # Hämtar informationen för de tre prognosdagarna.
    dagar = väderdata["daily"]

    # Går igenom varje dag och samlar väderinformationen.
    for index in range(len(dagar["time"])):
        dag = {
            "datum": dagar["time"][index],
            "max_temp": dagar["temperature_2m_max"][index],
            "min_temp": dagar["temperature_2m_min"][index],
            "nederbörd": dagar["precipitation_sum"][index],
        }

        prognos.append(dag)

    return prognos

# Kontrollerar om en stad finns i listan över tillåtna städer.
def ar_giltig_stad(stad):
    return stad in STÄDER