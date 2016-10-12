class Graph():

	def __init__(self,n):
		self.n = n
		self.matrix = self.inputAdjacencyMatrix(n)

	def inputAdjacencyMatrix(self,n):
		matrix = [ [0]*n for i in range(n)]
		
		i=0
		while i<n:
			j=i+1
			while j<n:
				matrix[i][j] = input("Is node %d adjacent to %d (0 or cost) : " % (i,j) )
				j+=1
			i+=1		

		return matrix

	def printAdjacencyMatrix(self):
		print "Entered Adjecency Matrix ::"
		print "-"*((4*self.n)+5)
		print "  n  | ",
		print '   '.join([str(i) for i in range(self.n)])
		print "-"*((4*self.n)+5)
		for i,row in enumerate(self.matrix):
			print " ",i," | ",
			for elem in row:
				print elem,' ',
			print ''
		print "-"*((4*self.n)+5)

	
	def aStar(self, s, g, h):
		"Best First Search"
		# s - start node indexing from 0
		# g - goal node indexing from 0
		# h - huerestic values

		openList = {str(s):0+h[0]}

		i=0
		while openList:
			minIndex = self.getMin(openList)

			if minIndex[-1] == str(g):
				return minIndex
			
			del openList[minIndex]

			children =  self.getChildren(minIndex[-1])
			for node in children:
				newIndex = minIndex+str(node)
				openList[newIndex] = self.getG(newIndex) + h[node]
		return []

	def getG(self,node):
		cost,firstNode = 0, int(node[0])

		for i in node[1:]:
			secondNode = int(i)
			cost += self.matrix[firstNode][secondNode]
			firstNode = secondNode
		return cost

	def getChildren(self,node):
		return [i for i,value in enumerate(self.matrix[int(node)]) if value!=0]

	def getMin(self,openList):
		# returns tuple (index,minimum)
		index = openList.keys()[0]		
		minimum = openList[index]

		for key,value in openList.iteritems():
			if value < minimum:
				minimum = value
				index = key
		return index
		

if __name__ == '__main__':
	n = input("Enter number of nodes : ")
	graph = Graph(n)
	graph.printAdjacencyMatrix()

	while True:
		start = input("\nEnter start node : ")
		goal = input("Enter Goal node : ")
		h = input("Enter huerestic list : ")
		path = graph.aStar(start,goal, h)

		if path:
			print 'Path : ',' - '.join(map(str,path))
		else:
			print 'Path : Not Found'

		isExit = raw_input("do you want to exit ([y]/n) : ")
		if isExit in ('y','Y',''):
			print "Bye"
			break