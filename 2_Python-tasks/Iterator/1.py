class LargeDatasetIterator:
    def __init__(self,start,end):
        self.store_start = start
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopIteration
        # Makes the iterator loops around
        # else:
        #     self.start = self.store_start+1
        #     return self.start


# I actually prefer using __len__ and __getitem__
x = list(range(1000,3000)) # The supposed unloaded dataset as if it is loaded on hard storage
data = LargeDatasetIterator(0,1000)
iterator = iter(data)
while True:
    print(x[next(iterator)])