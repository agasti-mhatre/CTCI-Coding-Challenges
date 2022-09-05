class BinaryMinHeapPQ:
    def __init__(self, list_of_values = []):
        self.pq = []
        for val in list_of_values:
            self.add_val(val)

    def get_parent(self, i):
        return (i - 1) // 2

    def get_leftchild(self, i):
        return (2 * i) + 1

    def get_rightchild(self, i):
        return (2 * i) + 2

    def add_val(self, val):
        if len(self.pq) == 0:
            self.pq.append(val)
        else:
            self.pq.append(val)
            curr = len(self.pq) - 1
            parent = self.get_parent(curr)
            while (self.pq[parent] > self.pq[curr]) and (parent > 0):
                self.pq[parent], self.pq[curr] = self.pq[curr], self.pq[parent] 
                curr = parent
                parent = self.get_parent(parent)

                if (parent == 0) and (self.pq[parent] > self.pq[curr]):
                    self.pq[parent], self.pq[curr] = self.pq[curr], self.pq[parent]


    def remove_min(self):
        if len(self.pq) == 0:
            raise Exception("Cannot pop from empty heap!")
        elif len(self.pq) == 1:
            return self.pq.pop()

        min_ = self.pq[0]
        self.pq[0] = self.pq.pop()
        
        curr = 0
        left = self.get_leftchild(curr)
        right = self.get_rightchild(curr)
        left_exist = True
        right_exist = True

        if (left > len(self.pq) - 1):
            left_exist = False

        if (right > len(self.pq) - 1):
            right_exist = False

        while (left_exist or right_exist):
            if left_exist and right_exist:
                if self.pq[left] < self.pq[right]:
                    i = left
                else:
                    i = right
                
                if self.pq[curr] > self.pq[i]:
                    self.pq[curr], self.pq[i] = self.pq[i], self.pq[curr]
                    curr = i
                    left = self.get_leftchild(curr)
                    right = self.get_rightchild(curr)

                else:
                    break
       
            elif left_exist:
                i = left

                if self.pq[curr] > self.pq[i]:
                    self.pq[curr], self.pq[i] = self.pq[i], self.pq[curr]
                    curr = i
                    left = self.get_leftchild(curr)
                else:
                    break
            
            elif right_exist:
                i = right

                if self.pq[curr] > self.pq[i]:
                    self.pq[curr], self.pq[i] = self.pq[i], self.pq[curr]
                    curr = i
                    left = self.get_rightchild(curr)
                else:
                    break

            if (left > len(self.pq) - 1):
                left_exist = False

            if (right > len(self.pq) - 1):
                right_exist = False


        return min_


    def peek_min(self):
        return self.pq[0]




if __name__ == "__main__":
    heap = BinaryMinHeapPQ([5, 4, 2, 3, 1, 6])


    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
    print(heap.remove_min())
    print(heap.pq)
    print()
