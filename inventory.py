class Inventory:
    def __init__(self):
        self.slots = []

        def add_item(self,item):
            self.slots.append(item)
        
        def use_item(self, item):
            self.slots.remove(item)

        def get_item(self, index):
            return self.slots[index]
