import requests
import zipfile
import os
import pandas as pd

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

def download_zip_year(output_name: str) -> int:
    ret = -1
    response = requests.get(url)
    with open(zip_name, 'wb') as f:
        print(f'Downloading {output_name}')
        ret = f.write(response.content)
    return ret

def unzip_year_file(zip_name: str, unziped_folder: str) -> int:
    ret = -1
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        print("Unziping " + zip_name)
        zip_ref.extractall(CURRENT_DIR)

    if os.path.isdir(unziped_folder):
        ret = 1
    return ret

def read_all_csv(path: str) -> int:
    ret = -1

    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
        
    for file in csv_files:
        file_path = path + '/' + file
        format_csv_file(file_path)

        #temporal
        return -1

    return ret

def format_csv_file(file: str) -> int:
    df = pd.read_csv(file, sep=';')

    print(df.head)



if __name__ == "__main__":
    for year, url in download_map.items():
        zip_name = 'air_quality_' + year + '.zip'
        path = CURRENT_DIR + 'Anio' + year[2:]
    
        #Download the file for the year
        if download_zip_year(zip_name) < 0:
            print(f'Error downloading {zip_name}, skipping this year')
            break

        #Unzip the file and check if the folder exists
        if unzip_year_file(zip_name, path) < 0:
            print(f'Error unziping {zip_name}, skipping this year')
            break

        if read_all_csv(path) < 0:
            print(f'Error reading {path} csv files, skipping this year')
            break


        break