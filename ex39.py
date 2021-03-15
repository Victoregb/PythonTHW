comunidades = {
    "Castilla y León": "CYL",
    "Madrid": "MAD",
    "País Vasco": "PV",
    "Andalucía": "AND",
    "Galicia": "GAL"
}

ciudades = {
    "CYL":"Valladolid",
    "PV":"Donostia-San Sebastián",
    "AND":"Granada"
}

ciudades["GAL"] = "Santiago de Compostela"
ciudades["MAD"] = "Madrid"

print("-"*10)

print("La comunidad de Madrid tiene: ", ciudades["MAD"])
print("Castilla y León tiene: ", ciudades["CYL"])

print("-"*10)

print("La abreviatura de Castilla y León es", comunidades["Castilla y León"])
print("La abreviatura de Andalucía es", comunidades["Andalucía"])

print("-"*10)

print("Galicia tiene: ", ciudades[comunidades["Galicia"]])
print("Castilla y León tiene: ", ciudades[comunidades["Castilla y León"]])

print("-"*10)

for comun, abreviatura in list(comunidades.items()):
    print(f"{comun} se abrevia {abreviatura}.")

print("-"*10)

for abreviatura, ciud in list(ciudades.items()):
    print(f"{abreviatura} tiene {ciud}.")

print('-' * 10)
for comun, abreviatura in list(comunidades.items()):
    print(f"{comun} es abreviado {abreviatura}")
    print(f"y tiene la ciudad {ciudades[abreviatura]}")

print('-' * 10)
comunidad = comunidades.get('Texas')

if not comunidad:
    print("Lo siento, no hay Texas.")

   # get a city with a default value
ciudad = ciudades.get('TX', 'No existe')
print(f"La ciudad para el estado 'TX': {ciudad}.")
