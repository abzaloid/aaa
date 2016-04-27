import requests
import json
import os
while 1 > 0:
    os.system('streamer -f jpeg -o image.jpeg')
    filename = "image.jpeg"
    files = {'file': (filename, open('image.jpeg', 'rb'))}
    r = requests.post('http://api.qrserver.com/v1/read-qr-code/', files=files)
    print r.status_code
    t = r.text
    s = json.loads(t)
    s = s[0]['symbol'][0]['data']
    print s
