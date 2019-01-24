class Node:
    def __init__(self,val):
        self.value = val
        self.addVal = 0
        self.multiVal = 0
        self.additionNode = None
        self.multiplicationNode = None
        self.endValue = 0


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

class ArthmeticN:
    def __init__(self,n,t):
        self.numbers = n
        self.target = t
        self.root = Node(self.numbers.pop(0))
        self.create_node(self.root,0)
        # self.inOrder(self.root)

    def create_node(self,node,p):
        self.add_node(node,p)
        self.multiple_node(node,p)

    def add_node(self,node,p):
        if(node.addVal == 0): node.addVal = node.value
        if(p == len(self.numbers)-1):
            node.additionNode = Node(self.numbers[p])
            node.additionNode.endValue = node.addVal+self.numbers[p]+node.multiVal
            if(node.additionNode.endValue == self.target):
                print(node.additionNode.endValue)
            return
        elif(node.addVal+self.numbers[p]+node.multiVal > self.target):
            return
            
        value = node.addVal+self.numbers[p]
        node.additionNode = Node(self.numbers[p])
        node.additionNode.addVal = value
        node.additionNode.multiVal = node.multiVal
        self.create_node(node.additionNode,p+1)

    def multiple_node(self,node,p):
        if(node.addVal == 0): node.addVal = node.value
        if(p == len(self.numbers)-1):
            node.multiplicationNode = Node(self.numbers[p])
            node.multiplicationNode.endValue = node.value * self.numbers[p] + node.addVal + node.multiVal
            if(node.multiplicationNode.endValue == self.target):
                print(node.additionNode.endValue)
            return
        elif(node.value * self.numbers[p] + node.addVal + node.multiVal > self.target):
            return
        value = node.value * self.numbers[p]
        node.multiplicationNode = Node(self.numbers[p])
        node.multiplicationNode.addVal = node.addVal
        node.multiplicationNode.multiVal = value
        self.create_node(node.multiplicationNode,p+1)
    
    def inOrder(self,node):
        print("{}-{}".format(node.value,node.addVal+node.multiVal))
        if(node.additionNode!=None):
            self.inOrder(node.additionNode)
        if(node.multiplicationNode!=None):
            self.inOrder(node.multiplicationNode)


ArthmeticN([1,2,3],9)
ArthmeticN([1,2,3,4,5,6,7,8,9],100)