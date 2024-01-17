import os
import pandas as pd

def list_csv_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.csv')]

def read_csv(file_path, separators=[';', ',']):
    for separator in separators:
        try:
            return pd.read_csv(file_path, sep=separator, encoding='latin1')
        except pd.errors.ParserError:
            continue
    return None

def process_csv(file_path, output_dir, fill_value='null'):
    df = read_csv(file_path)
    if df is not None:
        df.fillna(fill_value, inplace=True)
        output_file = os.path.join(output_dir, os.path.basename(file_path))
        df.to_csv(output_file, index=False)
        return output_file
    else:
        print(f"Erro ao processar {file_path}")
        return None
