startTemperatur = -5  # grader c
sluttTemperatur = 106

smeltepunkt = 0  # c
fordampningspunkt = 100  # c

vannSmeltevarme = 334000  # J/kg
vannFordampningsvarme = 2260000  # J/kg

isSpesVarmekapasitet = 2100  # J/kgK
vannSpesVarmekapasitet = 4180  # J/kgK
dampSpesVarmekapasitet = 1900  # J/kgK

vannMasse = 1  # kg

faseskifte = {
    smeltepunkt: vannSmeltevarme,
    fordampningspunkt: vannFordampningsvarme
}


def faseskifteEnergi(masse, temperatur):  # regner spesifikk (smelte/fordapnings)varme
    return masse * faseskifte[temperatur]
    # Q = q m        ^ henter smelte eller fordamnignsvarmen til stoffet,
    # basert på om det går fra fast til flytende, eller flytende til gass


def tempØkeEnergi(spesVarmekapasitet, masse):
    return spesVarmekapasitet * masse * 1
    # Q = C M delta T
    # delta t er 1 her.


for temperatur in range(startTemperatur, sluttTemperatur, 5):
    krevetEnergi = 0

    if temperatur in faseskifte.keys():
        krevetEnergi = faseskifteEnergi(vannMasse, temperatur)

    else:
        if temperatur < 0:
            spesVarmekapasitet = isSpesVarmekapasitet
        if temperatur > 0 and temperatur < 100:
            spesVarmekapasitet = vannSpesVarmekapasitet
        if temperatur > 100:
            spesVarmekapasitet = dampSpesVarmekapasitet

        krevetEnergi = tempØkeEnergi(spesVarmekapasitet, vannMasse)

    print(f"temperatur: {temperatur}. energi: {krevetEnergi / 1000}kJ for å øke stoffed med 1°C")
