from constants import HEADERS_RAPIDAPI, REGION_ENDPOINT
import pytest
import json
import os
import pandas as pd
import db
import app


def test_it_should_run(mocker):
    country_name = "Colombia"
    sha1_hash = "e3d92827c04e8bd003692ed8189f8467b9e58178"
    regions_list = ['Africa', 'Americas',
                    'Asia', 'Europe', 'Oceania', 'Polar']
    d = {'Region': ["Americas"], 'City Name': [country_name], 'Language': [
        sha1_hash], 'Time': ["480 ms"]}
    test_df = pd.DataFrame(data=d)
    mocker.patch("app.get_country_by_region", return_value=(
        country_name, sha1_hash))
    mocker.patch("app.get_regions", return_value=regions_list)
    mocker.patch.object(db, "engine")
    mocker.patch("pandas.DataFrame", return_value=test_df)

    mocker.patch.object(test_df, "to_sql", return_value=None)
    mocker.patch.object(test_df, "to_json", return_value=None)

    result_df = app.run()

    result_df.to_sql.assert_called_once()
    result_df.to_json.assert_called_once()
