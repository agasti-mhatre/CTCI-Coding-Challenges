class HashMap:
    def __init__(self, list_of_values = []):
        self.size = 0
        self.dec_thresh = 0
        self.inc_thresh = 4
        self.buckets = [[], []]
        self.modulator = 2

        index = 0
        while index < len(list_of_values):
            self.add_val(list_of_values[index])
            index += 1


    def add_val(self, val):
        if self.size >= self.inc_thresh:
            buckets = []
            self.modulator *= 2
            self.inc_thresh *= 2
            self.dec_thresh = self.size // 2
            
            for num in range(0, self.modulator):
                buckets.append([])

            for list in self.buckets:
                for item in list:
                    num_bucket = abs(hash(item)) % self.modulator
                    buckets[num_bucket].append(item)

            self.buckets = buckets

        num_bucket = abs(hash(val)) % self.modulator
        self.buckets[num_bucket].append(val)


        self.size += 1

    def remove_val(self, val):
        num_bucket = abs(hash(val)) % self.modulator
        index = 0
        found = False
        while index < len(self.buckets[num_bucket]):
            if(self.buckets[num_bucket][index] == val):
                self.buckets[num_bucket].pop(index)
                found = True

            index += 1

        if not found:
            raise Exception("Cannot remove value that does not exist in HashMap!")

        self.size -= 1

        if self.size <= self.dec_thresh:
            buckets = []
            self.modulator = self.modulator // 2
            self.inc_thresh = (self.size // 2) + 1
            self.dec_thresh = self.dec_thresh // 2
            
            for num in range(0, self.modulator):
                buckets.append([])

            for list in self.buckets:
                for item in list:
                    num_bucket = abs(hash(item)) % self.modulator
                    buckets[num_bucket].append(item)

            self.buckets = buckets



if __name__ == "__main__":
    x_map = HashMap([(1, 'a'), (2, 'b'), (3, 'c'), 
                     (4, 'd'), (5, 'e'), (6, 'f'),
                     (7, 'g'), (8, 'h'), (9, 'i')])

    #x_map.remove_val((1, 'a'))
    #x_map.remove_val((2, 'b'))
    #x_map.remove_val((3, 'c'))
    #x_map.remove_val((4, 'd'))
    #x_map.remove_val((5, 'e'))
    #x_map.remove_val((6, 'f'))


    print(x_map.buckets)
    print("Size: ", x_map.size)
    print("Inc: ", x_map.inc_thresh)
    print("Dec: ", x_map.dec_thresh)