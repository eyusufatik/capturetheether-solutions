import json
import os

from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

load_dotenv("../.env")

NICKNAME = "ruthless!"
ACC_ADDRESS = "0x66f68692c03eB9C0656D676f2F4bD13eba40D1B7"


private_key = os.environ.get("PRIVATE_KEY")

contract_address = "0x71c46Ed333C35e4E6c62D32dc7C8F00D125b4fee"
abi = json.load(open("abi.json", "r"))


web3 = Web3(Web3.HTTPProvider(os.environ.get("PROVIDER_URL")))
contract = web3.eth.contract(
    address=Web3.toChecksumAddress(contract_address), abi=abi)


nonce = web3.eth.get_transaction_count(ACC_ADDRESS)
print("Nonce:", nonce)
transaction = contract.functions.setNickname(
    bytes(NICKNAME, "utf-8")
).buildTransaction({
    'nonce': nonce,
    'maxFeePerGas': 160,
    'maxPriorityFeePerGas': 5,
    'from': ACC_ADDRESS
}
)
signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)

web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
