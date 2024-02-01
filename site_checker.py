# inport urllib
# use urllib.request to get the data from the url

import urllib.request as urllib


def main(url):
    print("Checking connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to ",url,"successfully")
    print("The response was: ", response.getcode())

print("This is a site connectivity checker program")
input_url = input("Enter the url of this site: ")

main(input_url)
# gives the user a response for connectivity and the value 200 which means successful