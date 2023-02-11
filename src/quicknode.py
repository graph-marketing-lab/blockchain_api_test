from web3 import Web3, HTTPProvider


class cfg:
    wallet = "0x942878558bC523777fE11e6d725AF93c86458050"
    auth = "358bb9f1a03f6ed3eaa527bb68bbbd09d50859a9"


OPTIONS = {
    'headers':
    {
        'x-qn-api-version': '1'
    }
}
w3 = Web3(HTTPProvider(
    f'https://twilight-empty-county.discover.quiknode.pro/{cfg.auth}/', request_kwargs=OPTIONS))
resp = w3.provider.make_request('qn_getWalletTokenBalance', {
    "wallet": cfg.wallet
})
print(resp)
