#!/usr/bin/env python3

from block import Block


class SnakeBlock(Block):

    def __init__(self, index, data, previous_hash=None):
        self.index = index
        self.data = data

        # this must be at last line of __init__
        Block.__init__(self, previous_hash)

    def ledger(self):
        return (
            str(self.index) +
            str(self.data)
        ).encode()


if __name__ == '__main__':
    l1 = SnakeBlock(1, "Ledger 1")
    print(l1.hash_block())
    l2 = SnakeBlock(2, "Ledger 2", l1.hash_block())
    print(l2.hash_block())
    l3 = SnakeBlock(3, "Ledger 3", l2.hash_block())
    print(l3.hash_block())
    l4 = SnakeBlock(4, "Ledger 4", l3.hash_block())
    print(l4.hash_block())
