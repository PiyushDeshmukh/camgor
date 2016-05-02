from camgor.camgor import *

"""
Tests whether Camgor can generate the api url corresponding to the
mentioned git url
"""

def test_fetch_user_names_for_contributors():
    """
    checks if number of usernames are fetched are as the one desired in the input
    """

    query_numbers = [-100, -10, -1, 0, 1, 10, 42, 99, 100, 101, 199, 200]
    expected_numbers = [0, 0, 0, 0, 1, 10, 42, 99, 100, 101, 199, 200]
    category = ["contributors", "stargazers", "watchers"]

    for person in category:
        for index, number in enumerate(query_numbers):
            user_names = fetch_user_names("https://api.github.com/repos/angular/angular/" + person, number)
            assert  len(user_names) == expected_numbers[index]
            user_names = fetch_user_names("https://api.github.com/repos/facebook/react/" + person, number)
            assert  len(user_names) == expected_numbers[index]
