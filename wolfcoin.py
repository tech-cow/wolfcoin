"""
Origin Code Base: Gerald Nash
Modifier: Yu Zhou

Algorithm Used.

Mini Blockchain using SHA-256: [Secure Hashing Algorithm 256]
Giving SHA-256 a hash key, it would generated a non-sense value that represents
the key.

Algorithm Explained.

How does SHA works?
Feeding in a 512 bits binary at a time, randomize in SHA's internal receptors, repeat the process
for 80+ times, generate a temporary result and then receive another 512 bits binary to repeat the process
again. Until there is no more data feeds in, then output the final results.

More on here: https://www.youtube.com/watch?v=DMtFhACPnTY

"""

import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """
        Function Explain.

        hash.update(arg) :Update the hash object with the string arg.

        hash.hexdigest(arg) : Return the digest of the strings passed to the
        update() method so far containing only hexadecimal digits.

        """
        sha = hasher.sha256()
        sha.update(str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash))
        return sha.hexdigest()



def create_genesis_block():
    """
    Manually create the first block with
    index zero and arbitary previous hash
    """
    return Block(0, date.datetime.now(), "Genesis Block", "0")



def new_block(last_block):
    """
    Create new block based on previous block
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Yo! I am block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)



# Create the genesis within Blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Upper Bound of blocks
blocks_num = 20

# Loop and create 20 subsequent blocks
for i in xrange(0, blocks_num):
    next_block = new_block(previous_block)
    blockchain.append(next_block)
    previous_block = next_block
    print "Block #{} has been added to the blockchain!".format(next_block.index)
    print "Hash: {}\n".format(next_block.hash)
