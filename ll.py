class Node:
	def __init__(self,data):
		self.data= data
		self.next= None
class LinkedList:
	def __init__(self):
		self.head= None
	
	def Printll(self):
		temp=self.head
		while(temp):
			print(temp.data)
			temp=temp.next
		
ll=LinkedList()
ll.head=Node(1)
second=Node(2)
third=Node(3)
ll.head.next= second
second.next= third
ll.Printll()
