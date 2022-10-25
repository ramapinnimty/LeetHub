class RandomizedSet:
    def __init__(self):
        '''
            Create :
            - a HashMap to store {val: index_in_array}
            - an Array to save all the unique elements
            - a variable to keep track of the last index in the array
        '''
        self.num2idx_map = {}
        self.arr = []
        self.curr_idx = 0

    def insert(self, val: int) -> bool:
        # Insert if the value doesn't already exist
        if val not in self.num2idx_map:
            self.num2idx_map[val] = self.curr_idx # insert into HashMap
            self.arr.append(val) # add the value to the array
            self.curr_idx += 1 # increment the latest index
            return True
        return False

    def remove(self, val: int) -> bool:
        # Remove the value if present
        if val in self.num2idx_map:
            # Replace the num to be removed with the num at the last index
            self.arr[self.num2idx_map[val]] = self.arr[-1]
            # Update the index of the last element in the HashMap
            self.num2idx_map[self.arr[-1]] = self.num2idx_map[val]
            self.arr.pop() # delete the value from the array
            self.curr_idx -= 1 # decrement the latest index in the array
            del self.num2idx_map[val] # delete the value from the HashMap
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr) # randomly choose a value from array


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()