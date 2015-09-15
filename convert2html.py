import os, urllib2, sys
import json
from pprint import pprint

pwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(pwd)

def convertJsonToHtml(jsonFile):
    tkdArray = jsonFile
    print("print json format: ")
    for tkdItem in tkdArray:
        title = tkdItem["title"]
        # for keywords in tkdItem["keywords"]:
        #     print(keywords)
        keywordsA = tkdItem["keywords"][0]
        keywordsB = tkdItem["keywords"][1]
        keywordsC = tkdItem["keywords"][2]
        desc = tkdItem["desc"]

        f = open(title, 'w')
        msg = """
            <html>
                <head>
                   <meta name="keywords" content="%s, %s, %s">
                   <meta name="description" content="%s">
                </head>
                <body>
                    <pre>%s<pre>
                </body>
            </html>
        """%(keywordsA, keywordsB, keywordsC, desc, desc)
        f.write(msg)
        f.close()

def readJson(jsonFile):
    getFile = jsonFile
    with open(getFile) as data_file:
        data = json.load(data_file)
    convertJsonToHtml(data)

if __name__ == '__main__':
    readJson(sys.argv[1])
