import requests
import numpy as np
import hashlib
import pandas as pd
import time
import db
from constants import REGION_ENDPOINT, HEADERS_RAPIDAPI, ENDPOINT_REST_CONTRIES
import json


def generage_sha1(text: str) -> str:
    """Generate a sha1 hash string

    Args:
        text (str): Text to generate hash

    Returns:
        str: sha1 hash
    """
    hash_object = hashlib.sha1(text.encode('utf-8'))
    hash_str = hash_object.hexdigest()
    return hash_str


def get_regions() -> list:
    """get all the regions

    Returns:
        list: name of the regions
    """
    response = requests.request(
        "GET", REGION_ENDPOINT, headers=HEADERS_RAPIDAPI)
    countries = response.json()
    regions = []
    [regions.append(country['region'])
     for country in countries if country['region'] != '' and country['region'] not in regions]
    regions.sort()
    return regions


def get_country_by_region(region_name: str) -> tuple:
    """Get a country name and its sha1 string hash of the language name

    Args:
        region_name (str): region name

    Returns:
        tuple: name af the country, string hash language name of the country
    """
    url = f"{ENDPOINT_REST_CONTRIES}{region_name}"
    response = requests.request("GET", url)
    countries = response.json()
    selected_country = np.random.choice(countries)
    language = selected_country["languages"][0]
    sha1_language_name = generage_sha1(language["name"])
    return selected_country["name"], sha1_language_name


def run() -> pd.DataFrame:
    """Executes the program

    Returns:
        pd.DataFrame: dataframe instance
    """
    d = {'Region': [], 'City Name': [], 'Language': [], 'Time': []}
    regions = get_regions()
    for region in regions:
        start = time.time()
        country_name, sha1_language_name = get_country_by_region(region)
        end = time.time()
        execution_time = (end - start) * 1000
        execution_time_data = f"{execution_time:.2f} ms"
        d["Region"].append(region)
        d["City Name"].append(country_name)
        d["Language"].append(sha1_language_name)
        d["Time"].append(execution_time_data)

    df = pd.DataFrame(data=d)
    ms = df["Time"].apply(lambda x: float(x.replace('ms', '')))
    sum_ms = f"{ms.sum():.2f} ms"
    avg_ms = f"{ms.mean():.2f} ms"
    max_ms = f"{ms.max()} ms"
    min_ms = f"{ms.min()} ms"
    print(f"Total time: {sum_ms}")
    print(f"Average time: {avg_ms}")
    print(f"Max time: {max_ms}")
    print(f"Min time: {min_ms}")
    metrics = {
        "avg": avg_ms,
        "total": sum_ms,
        "max": max_ms,
        "min": min_ms
    }

    with open('./exports/metrics.json', 'w') as fp:
        json.dump(metrics, fp)

    # Save data to database
    df.to_sql('regions', con=db.engine, if_exists='replace')
    # Export data to JSON file
    df.to_json(
        './exports/data.json', orient='records')
    print("Finish")
    return df


if __name__ == '__main__':
    run()
