### Coinpayments Verify TXID

Created for Astral Discord bot
A simple way to create a request to the coinpayment API with a valid HMAC using your private key and command
______________________



Create request get buyers IP address
```py
txid = 'CPFL0ZDXJQM432TKKS34ZSBBX3'

print(
    createRequest(txid)['results']['sender_ip']
)
```
