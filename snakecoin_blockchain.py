from snakecoin_genesis import create_genesis_block
from snakecoin_new_block import next_block

# create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# how many blocks should we add to the chain
# after the genesis block
number_of_blocks_to_add = 20

# add blocks to the chain
for i in range(0, number_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # tell everyone about it!
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}\n".format(block_to_add.hash)
