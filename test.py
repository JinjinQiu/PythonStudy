import urllib
import sys

#import urllib3 as urllib3
#from pip._vendor.requests.packages import urllib3

urlToRead = 'www.google.com'
crawledWebLinks = {}

while urlToRead != '':
    try:
        urlToRead = input("Please enter the url\n")
        if urlToRead == "":
            print("OK, exit loop")
            break

        shortName = input("please input the name of the url:\n " + urlToRead)

        webFile = urllib.request.urlopen(urlToRead).read()

        crawledWebLinks[shortName] = webFile

    except:
        print("******************\n Unexpected Error *******", sys.exc_info()[0])
        stopOrProceed = input("Stop? 1, continue? 0 \n")
        if stopOrProceed == "1":
            print("Stopping")
            break

        else:
            print("let's continue")
            continue
    print("This is the inside while loop")

print("This is outside while loop")

print(crawledWebLinks)
print(str(len(crawledWebLinks.values())))
delete = input ("delete one page in the dic \n")
crawledWebLinks.pop(delete)
print (len(crawledWebLinks))