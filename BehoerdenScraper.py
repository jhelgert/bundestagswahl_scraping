#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing.pool import ThreadPool
from tqdm import tqdm
import json
import time


class BehoerdenScraper:
    def __init__(self, debug=False):
        self.ts: int = int(time.time() * 1000)  # aktueller timestamp
        self.behoerden: list[dict[str, str]] = []
        self.timeout: float = 3.0
        self.invalid: int = 0
        self.debug = debug
        self.results = []

    def _scrape_behoerden(self) -> None:
        r = requests.get(
            f"https://wahlen.votemanager.de/behoerden.json?_={self.ts}")
        self.behoerden = [{
            'url': BeautifulSoup(url, "lxml").a["href"],
            'bundesland': bl,
            'stadt': stadt
        } for (url, stadt, bl) in r.json()["data"]]

    def _scrape_behoerde(self, behoerde: dict[str, str]) -> None:
        """ Durchsucht die aktuelle Behörde nach der URL zur .json, welche
            die Wahlergebnisse der Bezirke enthält. """
        def logger(bundesland: str, stadt: str) -> None:
            self.invalid += 1
            if self.debug:
                print(f"Ignoriere {stadt} ({bundesland})")

        # 1. Link zu den Bundestagswahlergebnissen der Behörde
        stadt, bundesland = behoerde["stadt"], behoerde["bundesland"]
        url = behoerde["url"].replace("index.html", "api/termine.json")
        try:
            r = requests.get(url)
            if not r.ok or "Content-Type" not in r.headers or r.headers[
                    "Content-Type"] != "application/json":
                logger(bundesland, stadt)
                return
            else:
                # 2. wahl_id der Behörde (wird benötigt für die json url)
                termine = r.json()["termine"]
                item = next((
                    t for t in termine
                    if t["date"] == "26.09.2021" and "Bundestag" in t["name"]),
                            None)
                if item is not None:
                    wahl_url = urljoin(behoerde["url"], item["url"])
                    wahl_id_url = wahl_url.replace(
                        "praesentation/", "api/praesentation/termin.json")
                else:
                    logger(bundesland, stadt)
                    return
        except:
            logger(bundesland, stadt)
            return
        # 3. URL zum json-file mit den Ergebnissen
        r = requests.get(wahl_id_url, timeout=self.timeout)
        wahl_id = r.json()["wahleintraege"][0]["wahl"]["id"]
        api_json_url = f"api/praesentation/wahl_{wahl_id}/uebersicht_ebene_6_1.json?ts={self.ts}"
        ergebnisse_url = wahl_url.replace("praesentation/", api_json_url)
        behoerde["zweitstimme_wahlbezirke_url"] = ergebnisse_url
        self.results.extend(behoerde)

    def start(self, num_threads=1):
        # Besorge die Behördenlinks
        self._scrape_behoerden()
        # Besorge für jede Behörde die Ergebnisse
        pool = ThreadPool(processes=num_threads)
        for r in tqdm(pool.imap_unordered(func=self._scrape_behoerde,
                                          iterable=self.behoerden),
                      total=len(self.behoerden)):
            pass

    def to_json_file(self, filename: str):
        with open(filename, "w") as fp:
            json.dump(self.behoerden, fp)