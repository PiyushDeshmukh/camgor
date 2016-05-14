import optparse
import os

from camgor import camgor

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="usage: %prog [options] git_url", version="%prog 1.0")
    parser.add_option("-n", "--number", dest = "max_number", default = 42, help = "Specify the number of users to be searched for. The default value is 42.")
    parser.add_option("-u", "--url", dest = "git_url", default = "https://github.com/python/pythondotorg.git", help = "Specify the url of git repository. The default points to https://github.com/python/pythondotorg.git.")
    parser.add_option("-c", "--contributors", dest = "contributors", default = True, action = "store_true", help = "Use this flag if you want to display contributors on the map, this is the default choice.")
    parser.add_option("-s", "--stargazers", dest = "stargazers", default = False, action = "store_true", help = "Use this flag if you want to display stargazers on the map.")
    parser.add_option("-w", "--watchers", dest = "watchers", default = False, action = "store_true", help = "Use this flag if you want to display watchers on the map.")
    parser.add_option("-d", "--keep-database", dest = "keep_db", default = False, action = "store_true", help = "This option disables the deletion of intermediate database file.")
    parser.add_option("-l", "--keep-location-files", dest = "keep_locations", default = False, action = "store_true", help = "This option disables the deletion of intermediate location file.")
    options, args = parser.parse_args()

    if int(options.max_number) > 200:
        choice = raw_input("Number of usernames specified are significantly more, this may take more time to render!\n Do you want to continue : (Y/N) : ")
        if choice != 'Y' or choice != 'y':
            print("Exiting camgor...")
            exit(0)

    category = "contributors"
    if options.stargazers == True:
        category = "stargazers"
    elif options.watchers == True:
        category = "watchers"
    camgor.main(options.git_url, options.max_number, category)

    os.system("python2 camgor/dump.py")
    camgor.generate_map(options.git_url)
    print "Opening map.html for visualization!"
    os.system("firefox camgor/map.html")

    if not options.keep_db:
        os.system("rm camgor/coordinates.db")
    if not options.keep_locations:
        os.system("rm camgor/where.data")
    os.system("rm camgor/map.html")
