class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.left_child = None
		self.right_child = None
	def insert_left(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insert_right(self, new_node):
		if self.right_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def get_left_child(self):
		return self.left_child

	def get_right_child(self):
		return self.right_child

	def get_root_val(self):
		return self.key

	def set_root_val(self, obj):
		self.key = obj

# r = BinaryTree('a')
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left('b')
# print(r.get_left_child().get_root_val())