
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext


class linkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count +1
            current = current.getNext()
        return count;

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current is None:
            print("item not found")
            return

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def display(self):
        list = []
        current = self.head
        while current is not None:
            list.append(current.getData())
            current = current.getNext()

        return list

    def replace(self, item, replaceItem):
        current = self.head
        while current is not None:
            if current.getData() == item:
                current.setData(replaceItem)
            current = current.getNext()

    def appendAfter(self, item, newItem):
        current = self.head
        while current is not None:
            if current.getData() == item:
                newNode = node(newItem)
                temp = current.getNext()
                current.setNext(newNode)
                newNode.setNext(temp)
            current = current.getNext()

    def appendBefor(self, item,newItem):
        current = self.head
        previous = None
        found = False
        newNode = node(newItem)
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current is None:
            newNode.setNext(current)
            return

        if previous is None:
            newNode.setNext(current)
            self.head = newNode

        else:
            previous.setNext(newNode)
            newNode.setNext(current)


obj = linkedList()

obj.add(5)
obj.add(6)
obj.add(7)
obj.add(8)
obj.add(9)
obj.add(10)
obj.add(11)
obj.add(12)
obj.add(13)
# obj.replace(13, 16)
obj.appendAfter(10,100)
obj.appendBefor(0,100)

print(obj.display())











