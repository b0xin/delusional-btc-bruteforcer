from bit import Key
from time import sleep
from requests import get


with open('btcaddress.txt', 'r') as file:
    wallets = set(file.read().split('\n'))
    if '' in wallets:
        wallets.remove('')


def match_keys():
    while True:
        key = Key()
        if key.address in wallets:
            print(
                f'Match found: Public Adddress: {key.address}, Private Key: {key.to_wif()}')
            with open('cracked.txt', 'a') as cracked:
                cracked.write(f'{key.to_wif()}')
                cracked.write("\n")


match_keys()
