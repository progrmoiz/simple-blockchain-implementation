#!/usr/bin/env python3

from block import Block


class CertificateBlock(Block):

    def __init__(self, index, path, previous_hash=None):
        self.index = index
        self.path = path

        # this must be at last line of __init__
        Block.__init__(self, previous_hash)

    def ledger(self):
        f = open(self.path, 'r')
        return (str(self.index) +
                f.read()).encode()


if __name__ == '__main__':
    c1 = CertificateBlock(1, 'ledger/student1.xyz')
    print(c1.hash_block())
    c2 = CertificateBlock(2, 'ledger/student2.xyz', c1.hash_block())
    print(c2.hash_block())
