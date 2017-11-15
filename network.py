import requests
import time
import sys
import getopt

def usage():
    print('usage: network.py -l <url> [-d <delay in seconds>]')
    sys.exit()

def main(argv):
    # setup
    url = ''
    delay = 30

    # parameters
    try:
        opts, args = getopt.getopt(argv,"l:d:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-l"):
            url = arg
        elif opt in ("-d"):
            try:
                delay = int(arg)
            except ValueError:
                usage()

    # check input
    if (url == '' or delay < 1):
        usage()

    # start monitoring
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        try:             
            r = requests.get(url,timeout=1.0)
            if (r.status_code == requests.codes.ok):
                print(localtime, " - OK")
            else:
                print(localtime, " - WEBSITE ERROR: ", r.status_code)
        except:
            print(localtime, " - NETWORK ERROR")
        time.sleep(delay)



if __name__ == "__main__":
   main(sys.argv[1:])
