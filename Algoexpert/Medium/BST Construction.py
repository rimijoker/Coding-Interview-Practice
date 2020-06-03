class Bst:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):

        if val < self.val:
            if not self.left:
                self.left = Bst(val)
            else:
                self.insert(self.left, val)
        else:
            if not self.right:
                self.right = Bst(val)
            else:
                self.insert(self.right, val)
        return self
    
    def contains(self, val):

        if self.val == val:
             return True
        elif val < self.val:
            if not self.left:
                self.contains(self.left, val)
            else:
                return False
        elif val > self.val:
            if not self.right:
                self.contains(self.right, val)
            else:
                return False
    
    def remove(self, val):
        
        # Base Case 
        if self is None: 
            return self  
    
        # If the val to be deleted is smaller than the self's 
        # val then it lies in  left subtree 
        if val < self.val: 
            self.left = self.remove(self.left, val) 
    
        # If the kye to be delete is greater than the self's val 
        # then it lies in right subtree 
        elif(val > self.val): 
            self.right = self.remove(self.right, val) 
    
        # If val is same as self's val, then this is the node 
        # to be deleted 
        else: 
            
            # Node with only one child or no child 
            if self.left is None : 
                temp = self.right  
                self = None 
                return temp  
                
            elif self.right is None : 
                temp = self.left  
                self = None
                return temp 
    
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = self.getMinValue(self.right) 
    
            # Copy the inorder successor's content to this node 
            self.val = temp.val 
    
            # Delete the inorder successor 
            self.right = self.remove(self.right , temp.val) 
    
    
        return self  

    def getMinValue(self):
        currentNode = self
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.val