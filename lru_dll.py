# -----------------------------------------------------------
# LRU cache implemetation using Doubly Linked List
# -----------------------------------------------------------


class Node:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None
		
class LRUCache:
	"""
	Class to represent the LRU cache

	Attributes
	----------
	capapcity : int
			size of the cache
	current_size: int
			what is the current size of the cache
	head : Node
			a node signifying the start of the cache
	tail : Node
			a node signifying the end of the cache
	lookmap: Dict
			dictionary to store the nodes with key as look for O(1) lookup

	Methods
	-------
	remove(node):
	Remove the node from the cache

	insert_at_begining(key, value):
	Any new node is inserted at the begining of the doubly linked list. The first node
	signifies the most recent used item and the last node the least recenlty accessed
	item

	get(key):
	Returns the value found at the key or -1 if not found. Also shift the queried node to 
	the start of the linked list

	put(key, value):
	If capacity is not full then inserts the key,value pair as a node at the start of the
	linked list and increases the current size of the linked list. If capacity full, then
	removes  the item which has been used least recently which is at the end of the list
	and inserts the key,value pair at the start and increases the current size
	"""

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.current_size = 0
		self.head = Node("head", "head")
		self.tail = Node("tail", "tail")
		self.head.next = self.tail
		self.tail.prev = self.head
		self.lookup = {}
	
	def remove(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
		del node
	
	def insert_at_begining(self, node):
		node.next = self.head.next
		node.prev = self.head
		self.head.next.prev = node
		self.head.next = node
		
		
	def get(self, key: int) -> int:
		if key in self.lookup:
			node = self.lookup[key]
			self.remove(node)
			self.insert_at_begining(node)
			return node.val
		else:
			return -1

	def put(self, key: int, value: int) -> None:
		if key in self.lookup:
			node = self.lookup[key]
			node.val = value
			self.remove(node)
			self.insert_at_begining(node)
		else:	
			if self.current_size == self.capacity:
				node = self.tail.prev
				self.remove(node)
				del self.lookup[node.key]
				self.current_size = self.current_size - 1 
			node = Node(key, value)
			self.insert_at_begining(node)
			self.lookup[key] = node
			self.current_size = self.current_size + 1 
			


# Testing with some values
cache = LRUCache(2)
cache.put(1,1)
print(cache.get(1))
cache.put(2,2)
print(cache.get(2))
cache.put(2,4)
print(cache.get(2))
cache.put(3,3)
print(cache.lookup)
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))

		
