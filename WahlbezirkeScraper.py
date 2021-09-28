#!/usr/bin/env python3

import json
import requests
import re
import pandas as pd
import numpy as np
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


class WahlbezirkeScraper:
    def __init__(self, json_file, parteien, debug=False):
        self.json_file = json_file
        self.parteien = parteien
        self.results = []
        self.debug = debug
        self.invalid = 0

    def _scrape_wahlbezirk(self, bezirk, debug=False):
        bundesland = bezirk["bundesland"]
        stadt = bezirk["stadt"]
        json_url = bezirk["zweitstimme_wahlbezirke_url"]
        r = requests.get(json_url)
        if "Content-Type" not in r.headers or r.headers[
                "Content-Type"] != "application/json":
            if debug:
                print(f"Keine gültige .json für {stadt} ({bundesland}).")
            self.invalid += 1
            return
        js = r.json()
        if not "tabelle" in js:
            if debug:
                print(f"Keine Daten für {stadt} ({bundesland}) vorhanden.")
            self.invalid += 1
            return
        return [{
            **{
                "Bundesland": bundesland,
                "Stadt": stadt,
                'Wahlbezirk': zeile["label"]
            },
            **{
                i["tip"]: float(i["order_value_proz"])
                for i in zeile["felder"] if i["tip"] in self.parteien
            }
        } for zeile in js["tabelle"]["zeilen"]]

    def _pool_func(self, bezirk):
        bundesland = bezirk["bundesland"]
        stadt = bezirk["stadt"]
        if (url := bezirk.get("zweitstimme_wahlbezirke_url")) is None:
            self.invalid += 1
            if self.debug:
                print(f"Keine json URL für {stadt} ({bundesland})")
        else:
            if (erg := self._scrape_wahlbezirk(bezirk)) is not None:
                self.results.extend(erg)
            else:
                self.invalid += 1

    def start(self, num_threads=10):
        pool = ThreadPool(processes=num_threads)
        for r in tqdm(pool.imap_unordered(func=self._pool_func,
                                          iterable=self.json_file),
                      total=len(self.json_file)):
            pass
        print(f"{self.invalid} Wahlbezirke konnten nicht durchsucht werden.")

    def get_dataframe(self):
        # TODO: Kombiniere noch die CSU und CDU Spalten
        df = pd.DataFrame(self.results)
        return df
