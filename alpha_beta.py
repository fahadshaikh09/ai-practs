from networkx import DiGraph


class AlphaBeta():

	def __init__(self, graph, valueMarix, root=1, infinity=100000):
		self.INFINITY = infinity
		self.closedList = set()
		self.root = root
		self.abvalue = valueMarix  # alpha beta value
		self.graph = graph
		self.pruninedNodes = []

	def getUnvisitedChild(self, node):
		children = self.graph[node].keys()
		unvisitedChildren = filter(
			lambda x: x not in self.closedList,
			sorted(children)
		)
		return unvisitedChildren

	def isHaveChild(self, node):
		children = self.graph[node].keys()
		return children != []

	def setAlpha(self, node, value):
		# assuming node is parent node
		if self.abvalue[node][1] == None:
			self.abvalue[node][1] = value
			return True

		if value > self.abvalue[node][1]:
			self.abvalue[node][1] = value
			return True
		return False

	def setBeta(self, node, value):
		# assuming node is parent node
		if self.abvalue[node][1] == None:
			self.abvalue[node][1] = value
			return True

		if value < self.abvalue[node][1]:
			self.abvalue[node][1] = value
			return True
		return False

	def alphabeta(self):
		# init node with root and player with MAX palyer
		node = self.root
		isMaxPlayer = True
		self.pruninedNodes = []

		while True:
			# append node in closed list
			self.closedList.add(node)
			children = self.getUnvisitedChild(node)

			# if node is not root then only check for pruning
			if node != self.root:
				parent = self.graph.predecessors(node)[0]

				# init values of alpha and beta
				if isMaxPlayer:
					alpha = self.abvalue[node][1]
					beta = self.abvalue[parent][1]
				else:
					beta = self.abvalue[node][1]
					alpha = self.abvalue[parent][1]

				# check if pruning can be done
				if alpha != None and beta != None and alpha >= beta:
					# children = getUnvisitedChild(node)
					if children:
						self.pruninedNodes.append(
							{node: children, 'player': isMaxPlayer})
						node = self.graph.predecessors(node)[0]
						isMaxPlayer = not isMaxPlayer
						continue

			# if node have unvisited children
			if children != []:
				# go to first child
				node = children[0]
			else:
				# if node dont have any unvisited children

				# checking if it had children
				if self.isHaveChild(node):
					# set value of alpha/beta to value of node
					self.abvalue[node][0] = self.abvalue[node][1]

				# if it is root node then complete tree have been traversed
				if node == self.root:
					return

				valueOfNode = self.abvalue[node][0]
				self.setBeta(parent, valueOfNode) if isMaxPlayer else self.setAlpha(
					parent, valueOfNode)
				node = parent

			isMaxPlayer = not isMaxPlayer

	def findPath(self):
		node = self.root
		path = []
		isMaxPlayer = True

		while True:
			path.append(node)
			children = self.graph[node]

			if not children:
				return path

			if isMaxPlayer:
				# MAX player
				# maximum is tuple of (index, node_value)
				maximum = (None, -1 * self.INFINITY)

				for node in children.keys():
					value = self.abvalue[node][0]
					if value != None and maximum[1] < value:
						maximum = (node, self.abvalue[node][0])
				node = maximum[0]
			else:
				# MIN player
				minimum = (None, self.INFINITY)
				for node in children.keys():
					value = self.abvalue[node][0]
					if value != None and minimum[1] > value:
						minimum = (node, self.abvalue[node][0])

				node = minimum[0]
			isMaxPlayer = not isMaxPlayer

if __name__ == '__main__':
	# alpha beta value
	abvalue = {}
	for i in range(1, 28):
		abvalue[i] = [None, None]

	# print abvalue
	values = [2, 2, 1, 1, 3, 4, 4, 3, 7, -1, 1, 0, 3, 5, 4, 2, 5, 6]
	for i, value in zip(range(10, 28), values):
		abvalue[i] = [value, None]

	nodes = range(1, 27)
	edges = [
		(1, 2),		(1, 3),
		(2, 4),		(2, 5),
		(2, 6),		(3, 7),
		(3, 8),		(3, 9),
		(4, 10),	(4, 11),
		(4, 12),	(5, 13),
		(5, 14),	(5, 15),
		(6, 16),	(6, 17),
		(6, 18),	(7, 19),
		(7, 20),	(7, 21),
		(8, 22),	(8, 23),
		(8, 24),	(9, 25),
		(9, 26),	(9, 27),
	]

	g = DiGraph()
	g.add_nodes_from(nodes)
	g.add_edges_from(edges)

	alpha_beta = AlphaBeta(graph=g, valueMarix=abvalue)
	alpha_beta.alphabeta()
	path = alpha_beta.findPath()

	print "Path : ", ' - '.join(map(str, path))
	for i in alpha_beta.pruninedNodes:
		parent = i.keys()[1]
		if i['player']:
			print "Beta cutt off, at parent node", parent, ", Prunied nodes ", i[parent]
		else:
			print "Alpha cutt off, at parent node", parent, ", Prunied nodes ", i[parent]

""" 
=== SAMPLE OUTPUT ===

Path :  1 - 2 - 4 - 10
Beta cutt off, at parent node 5 , Prunied nodes  [15]
Beta cutt off, at parent node 6 , Prunied nodes  [17, 18]
Alpha cutt off, at parent node 3 , Prunied nodes  [8, 9]
[Finished in 0.4s]

"""
