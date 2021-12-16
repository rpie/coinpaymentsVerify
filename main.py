import requests, hashlib, hmac
from collections import OrderedDict
from urllib.parse import urlencode

api_url = 'https://www.coinpayments.net/api.php'
private_key = ''
public_key = ''
txid = ''

def getkey(params):
    privateKey = bytearray(private_key, 'utf-8')
    return hmac.new(privateKey, bytearray(str(params), 'utf-8'), hashlib.sha512).hexdigest()

def getParams(command, txid):
    base_params = [
        ('version', 1),
        ('key', public_key),
        ('cmd', command),
        ('format', 'json'),
        ('txid', str(txid))
    ]

    return urlencode(OrderedDict(base_params))

def createRequest(txid):
    data = getParams('get_tx_info', txid)

    headers = {
        'HMAC': getkey(data),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    resp = requests.post(
        url = api_url,
        data = data,
        headers = headers
    ).json()

    return resp

print(
    createRequest(txid)
)
