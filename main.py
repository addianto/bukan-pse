#!/usr/bin/env python
from requests import Response
from time import sleep
from random import randint
import requests

BASE_URL = "https://pse.kominfo.go.id"
API_DOMESTIK = "/static/json-static/LOKAL_TERDAFTAR"

_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

_num_of_files = 872

for i in range(_num_of_files):
    url: str = f"{BASE_URL}/{API_DOMESTIK}/{i}.json"
    response: Response = requests.get(url, headers=_headers)

    if response.status_code == 200:
        with open(f"DOMESTIK_{i}.json", mode="w") as f:
            f.write(response.text)
    else:
        print(f"{response.status_code} | There was a problem downloading {url}")
    
    sleep(randint(5,10))
