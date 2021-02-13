class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class List:
	def __init__(self):
		self.head=None
	def PrintList(self):
		temp=self.head
		while(temp):
			print(int(temp.data))
			temp=temp.next
first=List()
first.head=Node(1)
second=Node(2)
third=Node(3)
first.head.next=second
second.next=third
first.PrintList()


