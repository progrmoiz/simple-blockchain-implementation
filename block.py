#!/usr/bin/env python3

import hashlib
from abc import ABCMeta, abstractmethod


class Block(metaclass=ABCMeta):

    def __init__(self, previous_hash=None):
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    @abstractmethod
    def ledger(self):
        """
        Return any byte document
        """
        pass

    def hash_block(self):
        m = hashlib.sha256()

        phash = self.previous_hash
        phash = (str(phash) if phash else '').encode()

        m.update(self.ledger() + phash)
        return m.hexdigest()
