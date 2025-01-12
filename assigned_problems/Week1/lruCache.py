class LRUCache:
    # Saman - LRU Cache
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value = self.map[key]
        del self.map[key]
        self.map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.map and len(self.map) == self.capacity:
            del self.map[next(iter(self.map))] # deletes first item
        if key in self.map:
            del self.map[key]
        self.map[key] = value