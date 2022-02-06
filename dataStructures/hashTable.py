# Exercise from Master The Coding Interview: Data Structures + Algorithms on Udemy

class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def __hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        # generate a hash
        address = self.__hash(key)
        # initialize a bucket
        if not self.data[address]:
            self.data[address] = []
        # add a [key, value] pair to the bucket
        self.data[address].append([key, value])

    def get(self, key):
        address = self.__hash(key)
        # if key hash exists
        if self.data[address] != None:
            # look for a key in a list of buckets
            for bucket in self.data[address]:
                if bucket[0] == key:
                    return bucket[1]
        # otherwise return None
        return None

    def keys(self):
        keysArray = []

        for entry in self.data:
            if entry != None:
                for bucket in entry:
                    keysArray.append(bucket[0])
        return keysArray
        


map = HashTable(50)
map.set('grapes', 10000)
map.set('apples', 1000)
map.set('oranges', 1000)
print(map.get('apples'))

print(map.keys())
    