from constants import ENDPOINT_REST_CONTRIES
from app import get_country_by_region
import pytest
import numpy as np
import json
import os


@pytest.fixture
def countries():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/response-mocks/countries.json', encoding='utf-8') as data_file:
        return json.loads(data_file.read())


@pytest.fixture
def country():
    return {
        "name": "Colombia",
        "languages": [
            {
                "name": "Spanish",
            }
        ]
    }


def test_is_should_get_country_by_region(requests_mock, country, mocker, countries):
    region_name = "americas"
    mocker.patch('numpy.random.choice', return_value=country)
    url = f"{ENDPOINT_REST_CONTRIES}{region_name}"
    requests_mock.get(url,
                      json=countries,
                      status_code=200)

    country_name, _ = get_country_by_region(region_name)
    assert country_name == "Colombia"
    np.random.choice.assert_called_once()
