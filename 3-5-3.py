import requests
with open("input.txt") as f:
    for i in f:
        api_url = "http://numbersapi.com/{}/math".format(int(i))
        params = {"json" : True }
        res = requests.get(api_url,params)
        data = res.json()
        if data["found"]:
            print("Interesting")
        else:
            print("Boring")
