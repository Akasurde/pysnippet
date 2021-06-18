from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return False

        self.cache.move_to_end(key)
        return True

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def refer(self, value):
        if not self.get(value[0]):
            self.put(value[0], value[1])

lru = LRUCache(5)
lru.put(1,2)
print(lru.cache)
lru.put(2,2)
print(lru.cache)
lru.put(3,2)
print(lru.cache)
lru.put(4,2)
print(lru.cache)
lru.put(5,2)
print(lru.cache)
lru.refer((5, 2))
print(lru.cache)
lru.refer((4, 2))
print(lru.cache)
lru.put(6, 7)
print(lru.cache)
lru.refer((9, 8))
print(lru.cache)
lru.refer((4, 2))
print(lru.cache)

