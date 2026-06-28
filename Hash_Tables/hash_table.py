class HashTable:
    def __init__(self, size: int = 4):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be an positive integer")
        
        if size % 2 != 0:
            raise ValueError("Size must be even")

        self.buckets = [[] for _ in range(size)]
        self.size = 0
        self.input_size = size

    def __len__(self):
        return self.size
    
    def __repr__(self):
        return "{\n    " + ",\n    ".join(f"{key}: {value}" for bucket in self.buckets for key, value in bucket) + "\n}"

    def __setitem__(self, key, value):
        bucket = hash(key) % len(self.buckets)
        for i, stored_key in enumerate(self.buckets[bucket]):
            if stored_key[0] == key:
                self.buckets[bucket][i] = (key, value)
                return
        self.buckets[bucket].append((key, value))
        self.size += 1
        self.__load_handler()

    def __getitem__(self, key):
        bucket =  hash(key) % len(self.buckets)
        for stored_key, stored_value in self.buckets[bucket]:
            if stored_key == key:
                return stored_value
        raise KeyError(key)
    
    def __delitem__(self, key):
        bucket = hash(key) % len(self.buckets)
        for i, stored_key in enumerate(self.buckets[bucket]):
            if stored_key[0] == key:
                del self.buckets[bucket][i]
                self.size -= 1
                self.__load_handler()
                return True
        raise KeyError(key)
                
    def __contains__(self, key):
        bucket = hash(key) % len(self.buckets)
        for stored_key in self.buckets[bucket]:
            if stored_key[0] == key:
                return True
        return False
    
    def __resize(self, new_size):
        carrier_buckets = [[] for _ in range(new_size)]
        for no_bucket in range(len(self.buckets)):
            for (key, value) in self.buckets[no_bucket]:
                bucket = hash(key) % len(carrier_buckets)
                carrier_buckets[bucket].append((key, value))
        self.buckets = carrier_buckets

    def __load_handler(self):
        load_factor = self.size/len(self.buckets)

        if load_factor > 0.75:
            self.__resize(len(self.buckets)*2)

        elif load_factor < 0.375 and len(self.buckets)>self.input_size:
            self.__resize(len(self.buckets)//2)