
# camgor

[camgor](https://github.com/PiyushDeshmukh/camgor) helps you visualize the geographical distribution of contributors of any repository.
It plots the locations of those users on the world map. It uses github's API and Google Maps' Geocoding API. It also allows you to
plot stargazers, and watchers of a particular repo.

## Pre-requisites

camgor expects you to have the [github's API token](https://github.com/settings/tokens/new), and store it in token.txt file in the
root directory.

## Usage
camgor is built on python 2.7

    python camgor.py -u https://github.com/facebook/react.git

![reactjs map](/images/reactmap.png)

Additional functionality can be achieved by passing some flags, see help menu or read the docs for additional information.

    python camgor.py -h
    Usage: camgor.py [options] git_url

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -n MAX_NUMBER, --number=MAX_NUMBER
                            Specify the number of users to be searched for. The
                            default value is 42.
      -u GIT_URL, --url=GIT_URL
                            Specify the url of git repository. The default points
                            to https://github.com/python/pythondotorg.git.
      -c, --contributors    Use this flag if you want to display contributors on
                            the map, this is the default choice.
      -s, --stargazers      Use this flag if you want to display stargazers on the
                            map.
      -w, --watchers        Use this flag if you want to display watchers on the
                            map.
      -d, --keep-database   This option disables the deletion of intermediate
                            database file.
      -l, --keep-location-files
                            This option disables the deletion of intermediate
                            location file.


 ## License
MIT License.
