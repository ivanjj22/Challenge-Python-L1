from constants import HEADERS_RAPIDAPI, REGION_ENDPOINT
from app import get_regions
import pytest
import json
import os


@pytest.fixture
def countries():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/response-mocks/regions.json', encoding='utf-8') as data_file:
        return json.loads(data_file.read())


def test_it_should_get_regions(requests_mock, countries):
    requests_mock.get(REGION_ENDPOINT,
                      headers=HEADERS_RAPIDAPI,
                      json=countries,
                      status_code=200)
    resp = get_regions()
    expected_value = ['Africa', 'Americas',
                      'Asia', 'Europe', 'Oceania', 'Polar']
    assert resp == expected_value
