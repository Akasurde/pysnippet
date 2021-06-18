class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def get(self, key):
        if key not in self.cache:
            return False
        self.cache.remove(key)
        self.cache.append(key)
        return True

    def add(self, key):
        self.cache.append(key)
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
    
    def refer(self, key):
        if not self.get(key):
            self.add(key)
            

lru = LRUCache(4)
lru.add('banana')
print(lru.cache)
lru.add('apple')
print(lru.cache)
lru.add('pineapple')
print(lru.cache)
lru.refer('banana')
print(lru.cache)