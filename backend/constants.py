import os

REGION_ENDPOINT = "https://restcountries-v1.p.rapidapi.com/all"
HEADERS_RAPIDAPI = {
    'x-rapidapi-key': os.environ.get('RAPIDAPI_KEY'),
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
}
ENDPOINT_REST_CONTRIES = "https://restcountries.eu/rest/v2/region/"
DATABASE_NAME = "sqlite:///db/regions.sqlite"
