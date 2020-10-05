import pprint
import binascii
import mnemonic
from mnemonic import Mnemonic
import bip32utils
import blockcypher

def generator():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    seed = mnemo.to_seed(words, passphrase="")
    entropy = mnemo.to_entropy(words)
    return(words)
def bal_check():
    print(adress)
    bal = blockcypher.get_total_balance(adress)
    bal1 = str(bal)
    print("balance:"+bal1+"\n")


def bip39(mnemonic_words):
    mobj = mnemonic.Mnemonic("english")
    seed = mobj.to_seed(mnemonic_words)

    bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
    bip32_child_key_obj = bip32_root_key_obj.ChildKey(
        44 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(
        0 + bip32utils.BIP32_HARDEN
    ).ChildKey(0).ChildKey(0)
    global adress
    adress = bip32_child_key_obj.Address()

    # return {
    #     'mnemonic_words': mnemonic_words,
    #     'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
    #     'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
    #     'bip32_derivation_path': "m/44'/0'/0'/0",
    #     'bip32_derivation_addr': bip32_child_key_obj.Address(),
    #     'coin': 'BTC'
    # }

    return {
        'mnemonic_words': mnemonic_words,
        # 'bip32_root_key': bip32_root_key_obj.ExtendedKey(),
        # 'bip32_extended_private_key': bip32_child_key_obj.ExtendedKey(),
        # 'path': "m/44'/0'/0'/0",
        'addr': bip32_child_key_obj.Address(),
        'publickey': binascii.hexlify(bip32_child_key_obj.PublicKey()).decode(),
        'privatekey': bip32_child_key_obj.WalletImportFormat(),
        'coin': 'BTC'
    }


if __name__ == '__main__':
    while True:
        mnemonic_words = generator()
        pprint.pprint(bip39(mnemonic_words))
        bal_check()
