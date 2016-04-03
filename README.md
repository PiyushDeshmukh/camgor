
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
