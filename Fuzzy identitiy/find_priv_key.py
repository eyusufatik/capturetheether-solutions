import secrets
import threading
from time import time_ns
import rlp
import os
from eth_account import Account
from eth_utils import keccak, to_checksum_address, to_bytes

def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.

    # https://ethereum.stackexchange.com/a/761/620
    """
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)

def target():
    trial = 0
    while True:
        private_key = "0x"+secrets.token_hex(32)
        address = Account.from_key(private_key).address
        # print(private_key, address, mk_contract_address(address, 0))

        if trial % 100 == 0:
            print(trial, private_key, address)
        should_break = False
        for i in range(1000):
            contract_address = mk_contract_address(address, i)
            
            if "badc0de" in contract_address.lower():
                print("found:", private_key, address, contract_address, "nonce:", i)
                should_break=True
                break

        
        if should_break:
            os._exit(1)


        trial += 1

for i in range(4):
    threading.Thread(target=target).start()

