import json
import os

from web3 import Web3
from dotenv import load_dotenv

load_dotenv("../.env")

web3 = Web3(Web3.HTTPProvider(os.environ.get("PROVIDER_URL")))

contract_block = 12358926
timestamp = web3.eth.get_block(contract_block)["timestamp"]
prev_hash = web3.eth.get_block(contract_block-1)["hash"]

hash = Web3.solidityKeccak(["bytes32", "uint256"],[prev_hash, timestamp])

print(hash[len(hash)-1], len(hash))