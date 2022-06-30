import web3
import os
from dotenv import load_dotenv
from eth_account._utils.signing import extract_chain_id, to_standard_v, serializable_unsigned_transaction_from_dict
from eth_account._utils.legacy_transactions import serializable_unsigned_transaction_from_dict
from eth_account._utils.legacy_transactions import ALLOWED_TRANSACTION_KEYS

load_dotenv("../.env")

tx_hash = 0xabc467bedd1d17462fcc7942d0af7874d6f8bdefee2b299c9168a216d3ff0edb

w3 = web3.Web3(web3.HTTPProvider(os.environ.get("PROVIDER_URL")))

tx = w3.eth.getTransaction(tx_hash)


s = w3.eth.account._keys.Signature(vrs=(
    to_standard_v(extract_chain_id(tx.v)[1]),
    w3.toInt(tx.r),
    w3.toInt(tx.s)
))


tt = {k: tx[k] for k in ALLOWED_TRANSACTION_KEYS - {'chainId', 'data'}}
tt['data'] = tx.input
tt['chainId'] = extract_chain_id(tx.v)[0]


ut = serializable_unsigned_transaction_from_dict(tt)
print(s.recover_public_key_from_msg_hash(ut.hash()))
