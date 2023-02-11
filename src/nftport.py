# get all the nfts owned by an account

import requests
import json


class cfg:
    wallet = "0x942878558bC523777fE11e6d725AF93c86458050"  # sample wallet address
    auth = """YOUR APIKEY HERE"""


i = 0
li = []
while True:

    headers = {
        "accept": "application/json",
        "Authorization": cfg.auth
    }

    url = f"https://api.nftport.xyz/v0/accounts/{cfg.wallet}?chain=ethereum&page_size=50&include=metadata"
    if i != 0:
        url += f"&continuation={cont}"

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    li.extend([[value['name'], value['contract_address']]
               for value in data['nfts']])

    if data['continuation'] == None:
        break
    else:
        cont = data['continuation']
        i += 1

print(f"Number of NFT held : {len(li)}")
# print(li)
