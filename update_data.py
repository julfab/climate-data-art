import pandas as pd
import requests
from io import StringIO

# 🌍 Source : Our World In Data CO₂ dataset
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

print("Fetching CO₂ data from Our World in Data...")
response = requests.get(url)
response.raise_for_status()

# Charger dans un DataFrame
df = pd.read_csv(StringIO(response.text))

# Sélectionner les dernières données disponibles pour chaque pays
latest_year = df["year"].max()
df_latest = df[df["year"] == latest_year][["country", "iso_code", "co2_per_capita"]]

# Nettoyage : retirer les entrées globales
df_latest = df_latest[df_latest["iso_code"].apply(lambda x: isinstance(x, str) and len(x) == 3)]

# Sauvegarde dans data/
output_path = "data/co2_latest.csv"
df_latest.to_csv(output_path, index=False)

print(f"✅ Updated {len(df_latest)} rows for {latest_year} and saved to {output_path}")
