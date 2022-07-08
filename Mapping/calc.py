import binascii
from Crypto.Hash import keccak
# Convert a number to 32 bytes array.
def bytes32(i):
    return binascii.unhexlify('%064x' % i)
# Calculate the keccak256 hash of a 32 bytes array.
def keccak256(x):
    return keccak.new(digest_bits=512).update(x).hexdigest()



desired_pos = 0
array_pos = 1

array_start_pos = keccak256(bytes32(0))
print(array_start_pos)