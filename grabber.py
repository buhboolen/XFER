import lxml
import pandas as pd
import requests

class Ship:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return f"{self.name}"

    def add_df(self, df):
        self.df = df

allem = [
  OBJ := Ship('OBJ', 'wikipedia url'),
]

for ship in allships:
    df_list = pd.read_html(requests.get(ship.url).content)
    for df in df_list:
        if not df.filter(regex="Pennant").columns.empty and not df.filter(regex="Status").columns.empty:
            df = df.rename(columns={df.filter(regex="SEARCHYPHRASE").columns.to_list()[0]: "NEWNAME"})
            df = df[["Name", "NEWNAME", "Feet"]]
            ship.add_df(df)

for ship in allships:
    print(ship)
    print(ship.df, end="\n\n\n")
