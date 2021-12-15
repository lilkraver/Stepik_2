import requests
import json

headers = {"X-Xapp-Token" : '...'}
lst =[]
with open('dataset_24476_4.txt', 'r') as file_object:
    for line in file_object:
        r = requests.get("https://api.artsy.net/api/artists/{}".format(line.strip()), headers=headers)
        j = json.loads(r.text)
        bn = j['birthday'] + ' ' + j['sortable_name']
        lst.append(bn)
        lst.sort()
        with open('names.txt', 'w', encoding='utf8') as f:
            f.write("\n".join(i[5:] for i in lst))
