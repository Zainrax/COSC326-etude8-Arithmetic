class Node:
    def __init__(self,val):
        self.value = val
        self.additionNode = None
        self.multiplicationNode = None


class ArthmeticLR:
    def __init__(self,n,t):
        self.numbers = n
        self.target = t
        self.root = Node(self.numbers.pop(0))
        self.create_node(self.root,0)

    def add_node(self,node,p):
        if(p == len(self.numbers)): return
        print("plus - {}:{}".format(node.value,self.numbers[p]))
        if(node.value+self.numbers[p] > self.target): return
        if(node.value*self.numbers[p] == self.target): print("found")
        node.additionNode = Node(node.value+self.numbers[p])
        self.create_node(node.additionNode,p+1)
        
        
    
    def multiple_node(self,node,p):
        if(p == len(self.numbers)): return
        print("multiple - {}:{}".format(node.value,self.numbers[p]))
        if(node.value*self.numbers[p] > self.target): return
        if(node.value*self.numbers[p] == self.target): print("found")
        node.multiplicationNode = Node(node.value*self.numbers[p])
        self.create_node(node.multiplicationNode,p+1)
        
        

    def create_node(self,node,p):
        self.add_node(node,p)
        self.multiple_node(node,p)

ArthmeticLR([1,2,3],9)