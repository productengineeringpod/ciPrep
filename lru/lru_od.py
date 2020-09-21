# -----------------------------------------------------------
# LRU cache implemetation using OrderedDict
# -----------------------------------------------------------

from collections import OrderedDict

class LRUCache:
	"""
	Class to represent the LRU cache

	Attributes
	----------
	capapcity : int
			size of the cache
	cache : OrderedDict
			data structure to implement the actual cache to store the values

	Methods
	-------
	get(key):
	Returns the value found at the key or -1 if not found. Also shift the queried key to 
	the end of the OrderedDict

	put(key, value):
	If capacity is not full then inserts the key,value pair in the cache and moves it to
	the end of the OrderedDict. If capacity full, then pops out the item which has been
	used least recently which is at the start of the OrderedDict and inserts the key,value
	pair at the end
	"""

	def __init__(self, capacity:int):
		self.capacity = capacity
		self.cache = OrderedDict()

	def get(self, key:int) -> int:
		if key not in self.cache:
			return -1
		else:
			self.cache.move_to_end(key)
			return self.cache[key]

	def put(self, key:int, value:int) -> None:
		if len(self.cache) == self.capacity:
			self.cache.popitem(last=False)
		self.cache[key] = value
		self.cache.move_to_end(key)

# Testing with 2 values
if __name__ == "__main__":
	cache = LRUCache(2)
	cache.put(1,1)
	cache.put(2,2)
	print(cache.get(1))
	print(cache.get(2))
	cache.put(3,3)
	print(cache.get(2))
	print(cache.get(3))
	cache.put(1,1)
	print(cache.cache)



		
