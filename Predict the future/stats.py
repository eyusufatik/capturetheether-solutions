import os

from web3 import Web3
from dotenv import load_dotenv

load_dotenv("../.env")

stats = {}

web3 = Web3(Web3.HTTPProvider(os.environ.get("PROVIDER_URL")))

cur_block = web3.eth.get_block_number()


for i in range(cur_block, 12457317, -1):
    print(i)
    timestamp = web3.eth.get_block(i)["timestamp"]
    prev_hash = web3.eth.get_block(i-1)["hash"]

    hash = Web3.solidityKeccak(["bytes32", "uint256"],[prev_hash, timestamp])

    number = hash[len(hash)-1] % 10

    stats[number] = stats.get(number, 0) + 1


print(stats) # 0 is the most probable number