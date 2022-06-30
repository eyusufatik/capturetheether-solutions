import rlp
from eth_utils.address import to_normalized_address
from web3 import Web3

def get_contract_address(sender, nonce):
    return Web3.sha3(rlp.encode([to_normalized_address(sender), nonce]))[12:]

address = "0x66f68692c03eB9C0656D676f2F4bD13eba40D1B7"

if __name__ == "__main__":
    nonce = 0
    while True:
        
        contract_address = get_contract_address(address, nonce).hex()
        
        if nonce%1000 == 0:
            print(nonce, contract_address)

        if "badc0de" in contract_address:
            print("found", nonce, contract_address)
            break
        else:
            nonce += 1
