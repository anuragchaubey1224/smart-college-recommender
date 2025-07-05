import pandas as pd
import os

input_folder = 'data'
output_folder = 'data'

files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx') or f.endswith('.xls')]

for file in files:
    file_path = os.path.join(input_folder, file)
    print(f"📥 Reading: {file_path}")

    try:
        df = pd.read_excel(file_path)
        df.dropna(how='all', inplace=True)
        df.dropna(axis=1, how='all', inplace=True)

        base_name = os.path.splitext(file)[0]
        output_path = os.path.join(output_folder, f"{base_name}.csv")

        df.to_csv(output_path, index=False)
        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Error reading {file}: {e}")
