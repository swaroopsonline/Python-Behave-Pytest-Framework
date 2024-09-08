import pytest

def get_data():
    return [

        ("Harry@gmail.com", "asfdsaf"),
        ("Hermione@gmail.com", "wrtewt"),
        ("Ron@gmail.com", "zcvzvv")

    ]

# testdata =  [
#
#         ("Harry@gmail.com", "asfdsaf"),
#         ("Hermione@gmail.com", "wrtewt"),
#         ("Ron@gmail.com", "zcvzvv")
#
#     ]


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password):
    print(username, "---", password)