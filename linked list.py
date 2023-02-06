class node:
        def __init__(self, data):
                self.data = data
                self.next = None

class llist:
        def __init__ (self):
                self.head = None
        def inser(self,index,data):
                n=node(data)
                if index==0:
                        n.next=self.head
                        self.head=n
                else:
                        ptr=self.head
                        c=0

                        while ptr:
                                if c==index-1:
                                        n.next=ptr.next
                                        ptr.next=n
                                        break
                                        
                                ptr=ptr.next
                                c+=1
        def pri(self):
                ptr=self.head
                c=0
                while ptr:
                        print(ptr.data)
                        c=c+1
                        ptr=ptr.next
                        
                print("Count",c)

l=llist()
l.inser(0,0)
l.inser(1,1)
l.inser(2,2)
l.inser(3,3)
l.pri()























                        
