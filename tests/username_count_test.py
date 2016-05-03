from camgor.camgor import *

"""
Tests whether Camgor fetches usernames till the limited number
"""

def test_fetch_user_names():
    """
    checks if number of usernames fetched are as the one desired in the input
    """
    # For short tests - takes less time
    query_numbers = [-100, -10, -1, 0, 1, 10]
    expected_numbers = [0, 0, 0, 0, 1, 10]

    # For long tests - takes more time
    # query_numbers = [-100, -10, -1, 0, 1, 10, 42, 99, 100, 101, 199, 200]
    # expected_numbers = [0, 0, 0, 0, 1, 10, 42, 99, 100, 101, 199, 200]

    category = ["contributors", "stargazers", "watchers"]
    access_token = open("camgor/token.txt", 'r').read().strip()

    for person in category:
        print("Checking for " + person)
        for index, number in enumerate(query_numbers):
            user_names = fetch_user_names("https://api.github.com/repos/angular/angular/" + person + "?access_token=" + access_token, number)
            assert  len(user_names) == expected_numbers[index]
            user_names = fetch_user_names("https://api.github.com/repos/facebook/react/" + person + "?access_token=" + access_token, number)
            assert  len(user_names) == expected_numbers[index]
