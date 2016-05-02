from camgor.camgor import *

"""
Tests whether Camgor can generate the api url corresponding to the
mentioned git url
"""

def test_accepts_contributors():
    """
    checks if contributor urls are generated
    """
    api_url = get_api_url("https://github.com/python/pythondotorg.git", "contributors")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/python/pythondotorg/contributors"

    api_url = get_api_url("https://github.com/facebook/react.git", "contributors")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/facebook/react/contributors"

    api_url = get_api_url("https://github.com/torvalds/linux.git", "contributors")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/torvalds/linux/contributors"

    api_url = get_api_url("https://github.com/PiyushDeshmukh/camgor.git", "contributors")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/PiyushDeshmukh/camgor/contributors"

def test_accepts_stargazers():
    """
    checks if stargazers urls are generated
    """
    api_url = get_api_url("https://github.com/python/pythondotorg.git", "stargazers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/python/pythondotorg/stargazers"

    api_url = get_api_url("https://github.com/facebook/react.git", "stargazers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/facebook/react/stargazers"

    api_url = get_api_url("https://github.com/torvalds/linux.git", "stargazers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/torvalds/linux/stargazers"

    api_url = get_api_url("https://github.com/PiyushDeshmukh/camgor.git", "stargazers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/PiyushDeshmukh/camgor/stargazers"

def test_accepts_watchers():
    """
    checks if stargazers urls are generated
    """
    api_url = get_api_url("https://github.com/python/pythondotorg.git", "watchers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/python/pythondotorg/watchers"

    api_url = get_api_url("https://github.com/facebook/react.git", "watchers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/facebook/react/watchers"

    api_url = get_api_url("https://github.com/torvalds/linux.git", "watchers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/torvalds/linux/watchers"

    api_url = get_api_url("https://github.com/PiyushDeshmukh/camgor.git", "watchers")
    api_url_without_key = api_url[:len(api_url)-(40+14)]
    assert  api_url_without_key == "https://api.github.com/repos/PiyushDeshmukh/camgor/watchers"
