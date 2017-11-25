from snakecoin_block import SnakeBlock


def originblock():
    return SnakeBlock(0, 'Origin Block', 0)


def nextblock(last_block):
    index = last_block.index + 1
    data = "Ledger " + str(index)
    last_hash = last_block.hash
    return SnakeBlock(index, data, last_hash)

"""
def createBlock():
    n = 1
    previous_hash = None

    def block():
        nonlocal n, previous_hash
        b = SnakeBlock(n, 'Ledger {}'.format(n), previous_hash)
        previous_hash = b.hash
        n = b.index + 1
        return b
    return block

createblock = createblock()

for i in range(1, 11):
    b = createblock()
    print('create block %s' % i)
    print(b.hash)
    print()
"""

# Create a blockchain and add first block
blockchain = [originblock()]
previous_block = blockchain[0]

# Number of blocks we add to the chain
NO_OF_BLOCKS_TO_ADD = 20


# Add block to chain
for i in range(0, NO_OF_BLOCKS_TO_ADD):
    block = nextblock(previous_block)
    blockchain.append(block)
    previous_block = block

    print("Block #{} has been added to the blockchain.".format(block.index))
    print("Hash: {}\n".format(block.hash))
