import requests
import zipfile
import os
import shutil
import pandas as pd
from data_information import *

records = []

def download_zip_year(output_name: str) -> int:
    ret = -1
    response = requests.get(url)
    with open(zip_name, 'wb') as f:
        print(f'Downloading {output_name}')
        ret = f.write(response.content)
    return ret

def unzip_year_file(zip_name: str, unziped_folder: str) -> int:
    ret = 1
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        print("Unziping " + zip_name)
        zip_ref.extractall(CURRENT_DIR)

    if not os.path.isdir(unziped_folder):
        source_folder = './'
        destination_folder = unziped_folder
        file_extension = ['.txt', '.csv', '.xml']

        os.makedirs(destination_folder, exist_ok=True)

        for filename in os.listdir(source_folder):
            for ext in file_extension:
                if filename.endswith(ext):
                    src_path = os.path.join(source_folder, filename)
                    dest_path = os.path.join(destination_folder, filename)
                    shutil.move(src_path, dest_path)


    return ret

def read_all_csv(path: str) -> int:
    ret = 1

    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
        
    for file in csv_files:
        file_path = path + '/' + file
        format_csv_file(file_path)

    return ret

def remove_files(zip:str, path: str) -> int:
    ret = -1

    try:
        os.remove(zip)
        shutil.rmtree(path)
        ret = 0
    except Exception as e:
        ret = -2

    return ret 

def save_data_to_csv() -> int:
    ret = 1

    output_folder = './output_files/'
    os.makedirs(output_folder, exist_ok=True)

    for k,v in sampling_points_map.items():
        file_name = 'data_' + str(k) + '.csv'
        df = pd.DataFrame(v["list"])
        df.to_csv(output_folder + file_name, index=False)

    return ret  

def format_csv_file(file: str) -> int:
    df = pd.read_csv(file, sep=';')

    # Iterate using iterrows
    for index, row in df.iterrows():
        for hour in range(1, 25):
            h_col = f'H{hour:02d}'      
            value = row[h_col]

            #Magnitudes variables to store
            magnitude_code = row['MAGNITUD']
            magnitude_name = magnitudes_map[row['MAGNITUD']]["name"]
            magnitude_abbr = magnitudes_map[row['MAGNITUD']]["abbreviation"]
            magnitude_unit = magnitudes_map[row['MAGNITUD']]["unit"]
            magnitude_method = magnitudes_map[row['MAGNITUD']]["method"]

            #Sampling point variables to store
            sampling_point_code = int(str(row['PUNTO_MUESTREO']).split("_")[0])
            sampling_point_name = sampling_points_map[sampling_point_code]["name"]


            if hour < 24:
                timestamp = pd.Timestamp(year=row['ANO'], month=row['MES'], day=row['DIA'], hour=hour)
            else:
                base_date = pd.Timestamp(year=row['ANO'], month=row['MES'], day=row['DIA'])
                timestamp = base_date + pd.Timedelta(days=1)

            sampling_points_map[sampling_point_code]["list"].append({
                'timestamp': timestamp,
                'magnitude_code': magnitude_code,
                'magnitude_name': magnitude_name,
                'magnitude_abbr': magnitude_abbr,
                'magnitude_unit': magnitude_unit,
                'magnitude_method': magnitude_method,
                'sampling_point_code': sampling_point_code,
                'sampling_point_name': sampling_point_name,
                'value': value,
            })
            
    print(f"Added {file} to each station dataframe")



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

        if remove_files(zip_name, path) < 0:
            print(f"Error removing files")
            break

    if save_data_to_csv() < 0:
        print(f"Error creating csv")