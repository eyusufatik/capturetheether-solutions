import os

from web3 import Web3
from solcx import compile_source
from dotenv import load_dotenv

load_dotenv("../.env")

web3 = Web3(Web3.HTTPProvider(os.environ.get("PROVIDER_URL")))

ACC_ADDRESS = "0x66f68692c03eB9C0656D676f2F4bD13eba40D1B7"


private_key = os.environ.get("PRIVATE_KEY")

web3.eth.default_account = web3.eth.account.privateKeyToAccount(private_key)

compiled_sol = compile_source("""
    pragma solidity ^0.8.15;

    contract Soln{
        bytes32 _name = bytes32("smarx");
        IFuzzyIdentityChallenge cahallangeContract = IFuzzyIdentityChallenge(0x6deac7236829467a34032dc80C119340bb451e3c);
        
        function solveChallange() public {
            cahallangeContract.authenticate();
        }
        
        function name() external view returns (bytes32){
            return _name;
        }
    }

    interface IFuzzyIdentityChallenge {
        function authenticate() external;
    }
""", output_values=['abi', 'bin'])

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

contract = web3.eth.contract(abi=abi, bytecode=bytecode)

nonce = 3194334

nonce = web3.eth.get_transaction_count(ACC_ADDRESS)
print("Nonce:", nonce)

transaction = contract.constructor().buildTransaction({
    'nonce': nonce,
    'maxFeePerGas': 100,
    'maxPriorityFeePerGas': 10,
    'from': ACC_ADDRESS
}
)

# print(transaction)
signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)

web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

print("done")