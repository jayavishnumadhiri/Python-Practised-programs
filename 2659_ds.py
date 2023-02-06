class node :
    def __init__ (self,data):
        self.data  = data
        self.next = None

class llist :
    def __init__ (self):
        self.head  = None

    def inserbefore(self,data,x=None):
        #insert before firts node
        n= node(data)
        if self.head is None :
            self.head = n
        elif self.head.data == x:
            n.next = self.head
            self.head = n
        else :
            ptr = self.head
            while (ptr.next != None):
                if ptr.next.data == x:
                    break
                ptr = ptr.next

            n.next = ptr.next
            ptr.next = n

    def insertafter(self,data ,x):
        n= node(data)
        ptr = self.head
        if self.head is None :
            self.head = n
        else:

            while (ptr != None):
                if ptr.data == x:
                    break
                ptr = ptr.next
            n.next = ptr.next
            ptr.next = n

    def pri(self):
        ptr = self.head

        while (ptr != None):
            print(ptr.data,"-->",end=' ')
            ptr=ptr.next
        print()

    def replacee(self,data,vi):
        ptr=self.head
        n=node(data)
        if self.head.data == vi :
            #self.head.data = data
                   #(OR)
            n.next = self.head.next
            self.head = n
        elif self.head.next == None:
            if self.head.data==vi:
                self.head = n
        else :
            while ptr.next != None:
                if ptr.next.data == vi :
                    break
                ptr = ptr.next
            n.next = ptr.next.next
            ptr.next = n
        



l=llist()
l.inserbefore(30)
l.pri()
'''
#l.pri()
l.inserbefore(20,30)
l.inserbefore(10,20)
l.inserbefore(2659,30)

l.insertafter(59,30)
l.pri()
'''
l.replacee(6,30)
l.pri()







































        
