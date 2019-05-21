#A linked list class.

class LinkedListNode:
    
    def __init__(self,newElement=None,newNext=None,newPrevious=None):
        self.element = newElement
        self.next = newNext
        self.previous = newPrevious
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext
        
    def getPrevious(self):
        return self.previous
    
    def setPrevious(self, newPrevious):
        self.previous = newPrevious
        
    def getElement(self):
        return self.element
    
    def setElement(self, newElement):
        self.element = newElement
        
class LinkedList:
    
    def __init__(self,element=None):
        if element != None:
            self.firstNode = LinkedListNode(element)
            self.size = 1
        else:
            self.firstNode = None
            self.size = 0
            
    def __len__(self):
        return self.size
    
    def getFirst(self):
        return self.firstNode
    
    def add(self, element):
        newnode = LinkedListNode(element,self.firstNode)
        if self.firstNode != None:
            self.firstNode.setPrevious(newnode)
        self.firstNode = newnode
        self.size = self.size + 1
        
    def remove(self, element):
        node = self.firstNode
        while node != None:
            if node.getElement() == element:
                if self.size == 1:
                    self.firstNode = None
                elif node.getNext() == None:
                    node.getPrevious().setNext(None)
                elif node.getPrevious() == None:
                    node.getNext().setPrevious(None)
                    self.firstNode = node.getNext()
                elif node.getNext() != None:
                    previous = node.getPrevious()
                    next = node.getNext()
                    previous.setNext(next)
                    next.setPrevious(previous)
                self.size = self.size - 1
                break
            else:
                node = node.getNext()