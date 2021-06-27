class Key:
    def __init__(self, key):
        self.key = key

    def getHash(self, maxSize):
        hash = 0
        R = 64 
        for i, char in enumerate(self.key):
            hash = (R * hash + i) % maxSize 
        return hash

    def get(self):
        return self.key