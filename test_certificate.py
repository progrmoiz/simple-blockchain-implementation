from certificate_block import CertificateBlock

DIR_PATH = 'ledger/'


def originblock():
    return CertificateBlock(0, DIR_PATH + 'startissue.xyz', 0)


def nextblock(last_block):
    index = last_block.index + 1
    path = DIR_PATH + 'student{}.xyz'.format(index)
    last_hash = last_block.hash
    return CertificateBlock(index, path, last_hash)


# Create blockchain and add genesis block
blockchain = [originblock()]
previous_block = blockchain[0]

# Number of blocks we add to the chain
NO_OF_BLOCKS_TO_ADD = 7

# Add block to chain
for i in range(0, NO_OF_BLOCKS_TO_ADD):
    block = nextblock(previous_block)
    blockchain.append(block)
    previous_block = block

    print("Student #%s certificate block has been added to the blockchain." %
          block.index)
    print("Hash: {}\n".format(block.hash[:7]))
