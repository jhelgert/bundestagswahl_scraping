#!/usr/bin/env python3

import json
from BehoerdenScraper import BehoerdenScraper
from WahlbezirkeScraper import WahlbezirkeScraper

if __name__ == "__main__":
    # 1.
    #bs = BehoerdenScraper()
    #bs.start()
    #bs.to_json_file("results.json")

    # 2.
    with open("results.json", "r") as fp:
        json_file = json.load(fp)
    parteien = ["CDU", "CSU", "FDP", "AfD", "SPD", "DIE LINKE", "GRÜNE"]
    ws = WahlbezirkeScraper(json_file, parteien, debug=False)
    ws.start()

    df = ws.get_dataframe()

    # Top Wahlkreise je Partei:
    for partei in parteien:
        print(df.sort_values(by=[partei], ascending=False).head())