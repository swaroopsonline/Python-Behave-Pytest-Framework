import pytest

def test_validate_titles():

    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"

    # if actual_title == expected_title:
    #     print("Test case passed")
    # else:
    #     print("Test case failed")

    print("Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmails" in title, "Gmail does not exists in the titles"
    assert False, "Forcefully failing the test"
    print("Ending")