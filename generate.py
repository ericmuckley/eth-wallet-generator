from mnemonic import Mnemonic
from web3 import Web3
import datetime
import json


def generate_wallets(n=1, save_details=True, verbose=True):
    """
    Generate *n* wallets and optionally save their details to a JSON file.
    """

    MAINNET_ENDPOINT = "https://mainnet.infura.io/v3/...my_endpoint_id_here"
    w3 = Web3(Web3.HTTPProvider(MAINNET_ENDPOINT))

    wallets = []
    for i in range(n):
        mnemo = Mnemonic("english")
        words = mnemo.generate(strength=256)
        seed = mnemo.to_seed(words, passphrase="")
        account = w3.eth.account.privateKeyToAccount(seed[:32])

        wallets.append({
            "index": i,
            "words": words,
            "private_key": account.privateKey.hex(),
            "address": account.address,
        })


        if verbose:
            print(f"generated {account.address}")


    wallet_info = {
        "generated_by": "user",
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "wallets": wallets,
    }


    if save_details:
        with open("wallet_info.json", "w", encoding="utf-8") as f:
            json.dump(wallet_info, f, ensure_ascii=False, indent=4)




if __name__ == "__main__":

    generate_wallets(n=5, save_details=True, verbose=True)