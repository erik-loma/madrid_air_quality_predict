CURRENT_DIR = './'

download_map = {
    "2024": "https://datos.madrid.es/egob/catalogo/201200-10306320-calidad-aire-horario.zip",
    "2023": "https://datos.madrid.es/egob/catalogo/201200-10306319-calidad-aire-horario.zip",
    "2022": "https://datos.madrid.es/egob/catalogo/201200-10306318-calidad-aire-horario.zip",
    "2021": "https://datos.madrid.es/egob/catalogo/201200-10306317-calidad-aire-horario.zip",
    "2020": "https://datos.madrid.es/egob/catalogo/201200-10306316-calidad-aire-horario.zip",
    "2019": "https://datos.madrid.es/egob/catalogo/201200-42-calidad-aire-horario.zip",
    "2018": "https://datos.madrid.es/egob/catalogo/201200-10306314-calidad-aire-horario.zip",
    "2017": "https://datos.madrid.es/egob/catalogo/201200-10306313-calidad-aire-horario.zip",
    "2016": "https://datos.madrid.es/egob/catalogo/201200-28-calidad-aire-horario.zip",
    "2015": "https://datos.madrid.es/egob/catalogo/201200-27-calidad-aire-horario.zip",
    "2014": "https://datos.madrid.es/egob/catalogo/201200-26-calidad-aire-horario.zip",
    "2013": "https://datos.madrid.es/egob/catalogo/201200-23-calidad-aire-horario.zip",
    "2012": "https://datos.madrid.es/egob/catalogo/201200-22-calidad-aire-horario.zip",
    "2011": "https://datos.madrid.es/egob/catalogo/201200-21-calidad-aire-horario.zip",
    "2010": "https://datos.madrid.es/egob/catalogo/201200-20-calidad-aire-horario.zip",
    "2009": "https://datos.madrid.es/egob/catalogo/201200-19-calidad-aire-horario.zip",
    "2008": "https://datos.madrid.es/egob/catalogo/201200-18-calidad-aire-horario.zip",
    "2007": "https://datos.madrid.es/egob/catalogo/201200-17-calidad-aire-horario.zip",
    "2006": "https://datos.madrid.es/egob/catalogo/201200-16-calidad-aire-horario.zip",
    "2005": "https://datos.madrid.es/egob/catalogo/201200-15-calidad-aire-horario.zip",
    "2004": "https://datos.madrid.es/egob/catalogo/201200-14-calidad-aire-horario.zip",
    "2003": "https://datos.madrid.es/egob/catalogo/201200-13-calidad-aire-horario.zip",
    "2002": "https://datos.madrid.es/egob/catalogo/201200-30-calidad-aire-horario.zip",
    "2001": "https://datos.madrid.es/egob/catalogo/201200-29-calidad-aire-horario.zip"
}

magnitudes_map = {
    1: { "name": "Sulfur Dioxide", "abbreviation": "SO₂", "unit": "µg/m³", "method": "Ultraviolet Fluorescence" },
    6: { "name": "Carbon Monoxide", "abbreviation": "CO", "unit": "mg/m³", "method": "Infrared Absorption" },
    7: { "name": "Nitric Oxide", "abbreviation": "NO", "unit": "µg/m³", "method": "Chemiluminescence" },
    8: { "name": "Nitrogen Dioxide", "abbreviation": "NO₂", "unit": "µg/m³", "method": "Chemiluminescence" },
    9: { "name": "Particles < 2.5 µm", "abbreviation": "PM2.5", "unit": "µg/m³", "method": "Microbalance / Spectrometry" },
    10: { "name": "Particles < 10 µm", "abbreviation": "PM10", "unit": "µg/m³", "method": "Microbalance / Spectrometry" },
    12: { "name": "Nitrogen Oxides", "abbreviation": "NOx", "unit": "µg/m³", "method": "Chemiluminescence" },
    14: { "name": "Ozone", "abbreviation": "O₃", "unit": "µg/m³", "method": "Ultraviolet Absorption" },
    20: { "name": "Toluene", "abbreviation": "TOL", "unit": "µg/m³", "method": "Gas Chromatography" },
    30: { "name": "Benzene", "abbreviation": "BEN", "unit": "µg/m³", "method": "Gas Chromatography" },
    35: { "name": "Ethylbenzene", "abbreviation": "EBE", "unit": "µg/m³", "method": "Gas Chromatography" },
    37: { "name": "Metaxylene", "abbreviation": "MXY", "unit": "µg/m³", "method": "Gas Chromatography" },
    38: { "name": "Paraxylene", "abbreviation": "PXY", "unit": "µg/m³", "method": "Gas Chromatography" },
    39: { "name": "Orthoxylene", "abbreviation": "OXY", "unit": "µg/m³", "method": "Gas Chromatography" },
    42: { "name": "Total Hydrocarbons", "abbreviation": "TCH", "unit": "mg/m³", "method": "Gas Chromatography" },
    43: { "name": "Methane", "abbreviation": "CH₄", "unit": "mg/m³", "method": "Gas Chromatography" },
    44: { "name": "Non-methane Hydrocarbons", "abbreviation": "NMHC", "unit": "mg/m³", "method": "Gas Chromatography" },
    431: { "name": "Meta-Paraxylene", "abbreviation": "MPX", "unit": "mg/m³", "method": "Gas Chromatography" },
}

Pso_Recoletos = []
Glta_de_Carlos_V = []
Pza_del_Carmen = []
Pza_de_Espana = []
Barrio_del_Pilar = []
Pza_Dr_Maranon = []
Pza_M_de_Salamanca = []
Escuelas_Aguirre = []
Pza_Luca_de_Tena = []
Cuatro_Caminos = []
Av_Ramon_y_Cajal = []
Pza_Manuel_Becerra = []
Vallecas = []
Pza_Fdez_Ladreda = []
Pza_Castilla = []
Arturo_Soria = []
Villaverde_Alto = []
C_Farolillo = []
Huerta_Castaneda = []
Moratalaz = []
Pza_Cristo_Rey = []
Pso_Pontones = []
Final_C_Alcala = []
Casa_de_Campo = []
Santa_Eugenia = []
Urb_Embajada_Barajas = []
Barajas = []
Mendez_Alvaro = []
Pso_Castellana = []
Retiro = []
Ensanche_Vallecas = []
Plaza_Eliptica = []
Sanchinarro = []
El_Pardo = []
Parque_Juan_Carlos_I = []
Tres_Olivos = []

sampling_points_map = {
    28079001: {"name": "Pº. Recoletos", "list": Pso_Recoletos},
    28079002: {"name": "Glta. de Carlos V", "list": Glta_de_Carlos_V},
    28079035: {"name": "Pza. del Carmen", "list": Pza_del_Carmen},
    28079003: {"name": "Pza. del Carmen", "list": Pza_del_Carmen},
    28079004: {"name": "Pza. de España", "list": Pza_de_Espana},
    28079039: {"name": "Barrio del Pilar", "list": Barrio_del_Pilar},
    28079005: {"name": "Barrio del Pilar", "list": Barrio_del_Pilar},
    28079006: {"name": "Pza. Dr. Marañón", "list": Pza_Dr_Maranon},
    28079007: {"name": "Pza. M. de Salamanca", "list": Pza_M_de_Salamanca},
    28079008: {"name": "Escuelas Aguirre", "list": Escuelas_Aguirre},
    28079009: {"name": "Pza. Luca de Tena", "list": Pza_Luca_de_Tena},
    28079038: {"name": "Cuatro Caminos", "list": Cuatro_Caminos},
    28079010: {"name": "Cuatro Caminos", "list": Cuatro_Caminos},
    28079011: {"name": "Av. Ramón y Cajal", "list": Av_Ramon_y_Cajal},
    28079012: {"name": "Pza. Manuel Becerra", "list": Pza_Manuel_Becerra},
    28079040: {"name": "Vallecas", "list": Vallecas},
    28079013: {"name": "Vallecas", "list": Vallecas},
    28079014: {"name": "Pza. Fdez. Ladreda", "list": Pza_Fdez_Ladreda},
    28079015: {"name": "Pza. Castilla", "list": Pza_Castilla},
    28079016: {"name": "Arturo Soria", "list": Arturo_Soria},
    28079017: {"name": "Villaverde Alto", "list": Villaverde_Alto},
    28079018: {"name": "C/ Farolillo", "list": C_Farolillo},
    28079019: {"name": "Huerta Castañeda", "list": Huerta_Castaneda},
    28079036: {"name": "Moratalaz", "list": Moratalaz},
    28079020: {"name": "Moratalaz", "list": Moratalaz},
    28079021: {"name": "Pza. Cristo Rey", "list": Pza_Cristo_Rey},
    28079022: {"name": "Pº. Pontones", "list": Pso_Pontones},
    28079023: {"name": "Final C/ Alcalá", "list": Final_C_Alcala},
    28079024: {"name": "Casa de Campo", "list": Casa_de_Campo},
    28079025: {"name": "Santa Eugenia", "list": Santa_Eugenia},
    28079026: {"name": "Urb. Embajada (Barajas)", "list": Urb_Embajada_Barajas},
    28079027: {"name": "Barajas", "list": Barajas},
    28079047: {"name": "Méndez Álvaro", "list": Mendez_Alvaro},
    28079048: {"name": "Pº. Castellana", "list": Pso_Castellana},
    28079049: {"name": "Retiro", "list": Retiro},
    28079050: {"name": "Pza. Castilla", "list": Pza_Castilla},
    28079054: {"name": "Ensanche Vallecas", "list": Ensanche_Vallecas},
    28079055: {"name": "Urb. Embajada (Barajas)", "list": Urb_Embajada_Barajas},
    28079056: {"name": "Plaza Elíptica", "list": Plaza_Eliptica},
    28079057: {"name": "Sanchinarro", "list": Sanchinarro},
    28079058: {"name": "El Pardo", "list": El_Pardo},
    28079059: {"name": "Parque Juan Carlos I", "list": Parque_Juan_Carlos_I},
    28079060: {"name": "Tres Olivos", "list": Tres_Olivos},
}