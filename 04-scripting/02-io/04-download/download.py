import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as input:
    webContent = input.read()
    print(webContent)