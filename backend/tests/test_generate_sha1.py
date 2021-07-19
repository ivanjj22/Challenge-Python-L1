from app import generage_sha1


def test_it_should_generate_sha1():
    expected_hash = "8df7f1b361b2af42d36011e00d22c0f9891ec0b0"
    result_hash = generage_sha1(
        "Spanish")
    assert expected_hash == result_hash
