# Aim: Implementation of hash DataStructure to solve collision in Hashtable using close Chaining method.

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Hash:
    def __init__(self, n):
        self.hashmap = [[] for i in range(n)]
        self.m = len(self.hashmap)
      
    # function to insert data into hash
    def insert(self, data):
        remainder = data % self.m
        if self.hashmap[remainder]:
            update = self.hashmap[remainder][0]
            while update.next != None:
                update = update.next
            update.next = ListNode(data)
        else:
            self.hashmap[remainder] = [ListNode(data)]
        print(f"Inserted Successfully : {data}")
      
    # Function to search element into hash
    def search(self, data):
        remainder = data % self.m
        if self.hashmap[remainder]:
            find = self.hashmap[remainder][0]
            index = 0
            if find.data == data:
                print(f"slot : {remainder} index: {index}")
                return
            else:
                while find.next != None:
                    find = find.next
                    index += 1
                    if find.data == data:
                        print(f"Slot : {remainder} index: {index}")
                        return
        print("Not Found")
        return None
      
    # Function to delete data from hash
    def delete(self, data):
        remainder = data % self.m
        if self.hashmap[remainder]: 
            prev = None
            current = self.hashmap[remainder][0]
            while current:
                if current.data == data:
                    if prev:
                        prev.next = current.next
                    else:
                        self.hashmap[remainder][0] = current.next
                        current.next = None
                    print(f"Data: {data} is successfully deleted")
                    return data
                prev = current
                current = current.next
        print(f"Data: {data} is not found")
        return None

# Driver code for test
if __name__ == "__main__":

  # Insertion of data
    h = Hash(10)
    h.insert(12)
    h.insert(22)
    h.insert(31)
    h.insert(7)
    h.insert(16)
    h.insert(13)
    h.insert(25)
    h.insert(37)
    h.insert(17)
    h.insert(18)
    h.insert(14)
    h.insert(29)
    h.insert(10)
    h.insert(70)
    h.insert(169)

    # To verify that data is inserted or not
    print("Hash Table:")
    for i, slot in enumerate(h.hashmap):
        print(f"Slot {i}: ", end="")
        if slot:
            current = slot[0]
            while current:
                print(current.data, end=" -> ")
                current = current.next
        print("None")
      
   # Search for data
    print("\nSearch results:")
    h.search(22)
    h.search(18)

  
    # Deletion of data
    h.delete(17)
    h.delete(19)
