import requests
import zipfile
import os
import pandas as pd
from data_information import *

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

    records = []
    row = df.iloc[0]

    for hour in range(1, 25):
        h_col = f'H{hour:02d}'      
        value = row[h_col]
        
        if hour < 24:
            timestamp = pd.Timestamp(year=row['ANO'], month=row['MES'], day=row['DIA'], hour=hour)
        else:
            base_date = pd.Timestamp(year=row['ANO'], month=row['MES'], day=row['DIA'])
            timestamp = base_date + pd.Timedelta(days=1)

        records.append({
            'timestamp': timestamp,
            'value': value,
            'PROVINCIA': row['PROVINCIA'],
            'MUNICIPIO': row['MUNICIPIO'],
            'ESTACION': row['ESTACION'],
            'MAGNITUD': row['MAGNITUD'],
            'PUNTO_MUESTREO': row['PUNTO_MUESTREO']
        })

    df_long = pd.DataFrame(records)

    print(df_long.iloc[23])



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