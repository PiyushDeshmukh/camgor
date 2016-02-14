import os
import urllib
import sqlite3
import json
import time
import ssl

github_api_token = "0d821d633355841c12195ca0dbd23d05bebe72fb"

def get_input():
    """
    Get input on basis of either
        * Git repo url
        * User and Repository individually
    """

    #if flag:
    url = raw_input('Enter the git repo url : ')
    if len(url) < 5:
        return "https://github.com/torvalds/linux.git"
    return url

def get_api_url(url):
    """
    Return the url corresponding to the api
        url: string
        hit_url: string
    """

    serviceurl = "https://api.github.com/repos/"
    splitted_url = url.split('/')
    user = splitted_url[3]
    repo = splitted_url[4].split('.')[0]
    hit_url = serviceurl + user + '/' + repo + '/contributors' + "?Authorization=" + github_api_token
    return hit_url

def fetch_user_names(hit_url):
    """
    Returns a list of user names who contributed to that repo(not all)
        hit_url: string
        user_names: list of strings
    """

    try:
        handler = urllib.urlopen(hit_url)
        data = handler.read()
        js = json.loads(str(data))
        print(js)
        print("\n\n")
        user_names = []
        for user in js:
            user_names.append(user["login"])
        print("The top contributors are\n")
        for user in user_names:
            print(user.encode('ascii', 'ignore'))
        print("\n")
        return user_names
    except Exception as e:
        print(e)
        if 'Y' == raw_input("Could not fetch urls. Try again? (Y/N) : "):
            return "Try again"
        else:
            return None

def fetch_user_locations(user_names):
    """
    Returns a list of addresses of users who had contributed to that repo(not all)
        user_names: list of strings
        user_locations: list of strings of addresses corresponding to each user in user_names
    """

    serviceurl = "https://api.github.com/users/"
    try:
        user_locations = []
        for user in user_names:
            handler = urllib.urlopen(serviceurl + user + "?Authorization=" + github_api_token)
            data = handler.read()
            js = json.loads(str(data))#[0]
            #print(js)
            user_locations.append(js["location"])
            print(user_locations)
        return user_locations
    except Exception as e:
        if len(user_locations) != 0:
            return user_locations
        print(e)
        if 'Y' == raw_input("Could not fetch locations. Try again? (Y/N) : "):
            return "Try again"
        else:
            return None

def gather_coordinates():
    """
    Gathers coordinates of all the locations that are stored in where.data
    text file using Google Geocode API, and then loads those coordinates into sqlite3 database.
    """

    # Deal with SSL certificate anomalies Python > 2.7
    # scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    scontext = None

    conn = sqlite3.connect('coordinates.db')
    cur = conn.cursor()


    cur.execute('''
    DROP TABLE IF EXISTS Locations;''')

    cur.execute('''
    CREATE TABLE Locations (address TEXT, geodata TEXT);''')

    fh = open("where.data", 'r')

    for line in fh:
        address = line.strip()
        serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
        url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
        uh = urllib.urlopen(url, context=scontext)
        data = uh.read()
        try:
            js = json.loads(str(data))
        except:
            continue

        if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
            print("Failed To Retrieve : url")

        cur.execute('''INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
        conn.commit()
    conn.close()
    fh.close()

if __name__ == '__main__':
    url = get_input()
    hit_url = get_api_url(url)
    print("Attempting to fetch user names\n")
    user_names = fetch_user_names(hit_url)
    while user_names == "Try again":
        user_names = fetch_user_names(hit_url)
    print("Successfully fetched user names!\n")

    print("Attempting to fetch user locations\n")
    user_locations = fetch_user_locations(user_names)
    while user_locations == "Try again":
        user_locations = fetch_user_locations(user_names)
    print("Successfully fetched user locations!\n")

    '''Explicit locations for offine testing'''
    # user_locations = [u'Germany', None, u'Spain', u'Taipei, Taiwan', None, None, u'London', u'Kaunas, Lithuania', u'Czech Republic', u'S\xe3o Paulo, Brazil', u'Lausanne, Switzerland', u'Pakistan', None, None, u'Strasbourg, France', None, None, u'SAN DIEGO', None, None, u'Brooklyn', u'Slovakia', u'London, UK', None, None, None, u'India', None, None, u'London']
    #user_locations = [u'Portland, OR', None, u'Edinburgh, Scotland', u'Nuremberg', None, None, None, None, None, u'Taiwan', u'Basel, Switzerland', None, None, None, None, None, None, None, None, None, None, None, u'Sweden', None, None, u'Canberra', None, u'Mebane, NC', u'San Francisco, CA, U.S.A.', None]

    print("Filering the locations ... ")
    user_loc = []
    for loc in filter(lambda x: x != None, user_locations):
        try:
            # user_loc.append(loc.encode('ascii').decode('cp037'))
            user_loc.append(loc.encode('ascii', 'ignore'))
        except Exception as e:
            print(e , "during", loc)
            pass
    print("Successfully filtered the locations!\n")

    print("Writing to file ...")
    fh = open('where.data', 'w')
    for loc in user_loc:
        fh.write(loc + '\n')
    fh.close()
    print("Successfully written to file!\n")
    print("Data : ", user_loc)

    print("\nGathering coordinates of user locations ... ")
    gather_coordinates()
    print("Successfully gathered coordinates of user locations!\n")
    os.system("python dump.py")
