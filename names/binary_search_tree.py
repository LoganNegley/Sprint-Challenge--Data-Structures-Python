class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)

        if value < self.value:
            if self.left == None:
                self.left = new_node
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is equal to the root value than its in the tree
        if target == self.value:
            return True
        # if the root value is more than the target we check the left side
        if self.value >= target:
            # check to see if left side has a value or is none
            if self.left == None:
                return False

            elif self.left.contains(target):
                return True
        
        if self.value <= target:
            if self.right == None:
                return False

            elif self.right.contains(target):
                return True 

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        maxNode = False
        if self.right:
            maxNode = self.right.get_max()
            return maxNode
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Call on root value first
        fn(self.value)
        # Is there a left node? If so run fn on it
        if self.left is not None:
            self.left.for_each(fn)
        # Is there a node on the left side if so run fn on it?
        if self.right is not None:
            self.right.for_each(fn)

