# Scott Rousseau
# Homework 2
# Question 2

# coding: utf-8
class Sclass:
    def __init__(self):
        self.StackItems = []
    def sEmpty(self):
        return self.StackItems == []
    def sadd(self, item):
        self.StackItems.append(item)
    def sretrieve(self):
        return self.StackItems.pop()
    def sItem(self):
        return self.StackItems[len(self.StackItems)-1]
    def __str__(self):
        return str(self.StackItems)

if __name__ == "__main__":
    myStack = Sclass()
    print myStack
    myStack.sadd(4)
    print myStack
    myStack.sadd(6)
    print myStack
    myStack.sadd(9)
    print myStack
    myStack.sadd(12)
    print myStack
    while not myStack.sEmpty():
        returnedItem = str(myStack.sItem())
        print "Returned item " + returnedItem
        myStack.sretrieve()
        print myStack
        
