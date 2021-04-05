import sys
import urllib.request
import json
from PIL import Image

def get_comic(nr):
    if nr:
        url = f'http://xkcd.com/{nr}/info.0.json'
    else:
        url = f'http://xkcd.com/info.0.json '
    
    with urllib.request.urlopen(url) as input:
        data = json.loads(input.read())

    return data

def get_fototje(url):
    with urllib.request.urlopen(url) as input:
        return Image.open(input)

if len(sys.argv) == 1:
    nr = None
else:
    nr = sys.argv[1]

data = get_comic(nr)

for key, value in data.items():
    print(f'{key}: {value}')

fototje = get_fototje(data['img'])
fototje.show()