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
    }

    url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{cfg.auth}/getNFTs?owner={cfg.wallet}&pageSize=100&withMetadata=true"
    if i != 0:
        url += f"&pageKey={pagekey}"

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    li.extend([[value['metadata']['name'], value['contract']['address']]
               for value in data['ownedNfts']])

    if 'pageKey' not in data.keys():
        break
    else:
        pagekey = data['pageKey']
        i += 1

print(f"Number of NFT held : {len(li)}")
# print(li)
