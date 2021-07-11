import requests
import os
url=input()
file = requests.get(url, allow_redirects=True)
path=os.chdir(path=input())
filename=str(input())

def testResponse():
    # to test if http response returns 200
    assert file.status_code==200

def testLinkerror():
    # to test if http response is not unauthorised
    assert not file.status_code==401

def testInternalServererror():
    # to test if http response is not Server Error
    assert not file.status_code==500

def fileFound():
    # to test if downloaded file exist in the directory
    entries = os.scandir(path)
    for items in list(entries):
        if items.name==filename:
            assert items.name==filename

def wrongPath():
    # to test if the path given is correct
    assert file.status_code<=200



if __name__ == "__main__":
    testResponse()
    testLinkerror()
    fileFound()
    wrongPath()
    print("Everything passed")