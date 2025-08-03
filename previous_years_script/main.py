import requests

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
    "2001": "https://datos.madrid.es/egob/catalogo/201200-29-calidad-aire-horario.zip",
}

if __name__ == "__main__":
    for year, url in download_map.items():
        zip_name = 'air_quality_' + year + '.zip'
        response = requests.get(url)

        with open(zip_name, 'wb') as f:
            f.write(response.content)

        
        break