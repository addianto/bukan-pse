#!/usr/bin/env python
from requests import Response
from time import sleep
from random import randint
from typing import Dict
import requests


def create_api_url(base_url: str, type: str) -> str:
    PSE_TYPES: Dict = {
        "Domestik Terdaftar": "LOKAL_TERDAFTAR",
        "Domestik Dihentikan Sementara": "LOKAL_DIHENTIKAN_SEMENTARA",
        "Domestik Dicabut": "LOKAL_DICABUT",
        "Asing Terdaftar": "ASING_TERDAFTAR",
        "Asing Dihentikan Sementara": "ASING_DIHENTIKAN_SEMENTARA",
        "Asing Dicabut": "ASING_DICABUT",
    }

    if not type in PSE_TYPES:
        raise Exception()

    return f"{base_url}/static/json-static/{PSE_TYPES[type]}"


def main() -> None:
    PSE_TYPE: str = "Domestik Terdaftar"
    BASE_URL: str = "https://pse.kominfo.go.id"
    API_URL: str = create_api_url(BASE_URL, PSE_TYPE)

    headers: Dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    # TODO Get number of entries via browser using Selenium WebDriver
    NUM_OF_ENTRIES: int = 8721
    PAGES: int = NUM_OF_ENTRIES // 10

    print(f"URL: {API_URL}")
    print(f"Pages: {PAGES}")

    for i in range(PAGES):
        call_url: str = f"{API_URL}/{i}.json"
        response: Response = requests.get(call_url, headers=headers)

        if response.status_code == 200:
            file_name: str = f"{PSE_TYPE.replace(' ', '')}_{i}.json"
            with open(file_name, mode="w") as json_file:
                json_file.write(response.text)

            print(f"Created {file_name}")
        else:
            print(f"{response.status_code} | There was a problem downloading {url}")

        sleep(randint(5, 10))


if __name__ == "__main__":
    main()
