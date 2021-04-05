import sys
import urllib.request
import re
import json

def remove_spaces(str):
    return re.sub(' ', '%20', str)

artist, title = sys.argv[1:]

artist = remove_spaces(artist)
title = remove_spaces(title)

url = f'https://api.lyrics.ovh/v1/{artist}/{title}'
print(url)

with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])
