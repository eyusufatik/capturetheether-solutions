from web3 import Web3


n = 0
while n < 600:
    result = Web3.solidityKeccak(["uint8"],[n]).hex()
    if result == "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365":
        print(n)
        break

    n+=1