import datetime
import hashlib
import time
from binascii import hexlify, unhexlify


class Block:
    def __init__(self, prev_hash, transaction, amount):
        self.next = None
        self.__data = {
            'prev_hash': prev_hash,
            'transaction': transaction,
            'amount': amount,
            'time': datetime.datetime.now().time()
        }

        self.__data['hash'] = self.make_hash()

    def get_data(self):
        return self.__data

    def make_hash(self):
        # start = time.time()
        test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()['prev_hash'])).digest()).decode('utf-8')
        while test_hash[:5] != '00000':
            test_hash = hexlify(hashlib.sha256(unhexlify(test_hash)).digest()).decode('utf-8')
        # finish = time.time() - start
        # print(finish)
        # print(test_hash)
        return test_hash

    def append(self, transaction, amount):
        n = self
        while n.next:
            n = n.next
        prev_hash = n.get_data()['hash']
        end = Block(prev_hash, transaction, amount)
        n.next = end


def print_blocks(block):
    node = block
    # print(node.get_data())
    while node.next:
        node = node.next
        print(node.get_data())


test = Block('000000a8d2e9efbd5d7cf1bb6587b0c102bf446a8494641a2bb3a3955dd2346f', 'bob', 10)
test.append('ivan', 1022)
test.append('alex', 122)

print(test.get_data())
print_blocks(test)
