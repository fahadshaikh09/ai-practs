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

	def hillClimb(self, s, g):
		# s - start node indexing from 0
		# g - goal node indexing from 0

		openList = {s:0}
		closeList = []

		while openList:
			popepd = self.getMin(openList)
			closeList.append(popepd[0])
			if popepd[0]==g:
				return closeList
			
			openList = self.getChildren(popepd[0])

		return []

	def getChildren(self, node):
		return { i:value for i,value in enumerate(self.matrix[node]) if value!=0 }

	def getMin(self,openList):
		index = openList.keys()[0]
		minimum = openList[index]

		for key,value in openList.iteritems():
			if value < minimum:
				minimum = value
				index = key
		return (index,minimum)


if __name__ == '__main__':
	n = input("Enter number of nodes : ")
	graph = Graph(n)
	graph.printAdjacencyMatrix()

	while True:
		start = input("\nEnter start node : ")
		goal = input("Enter Goal node : ")
		path = graph.hillClimb(start,goal)

		if path:
			print 'Path : ',' - '.join(map(str,path))
		else:
			print 'Path : Not Found'

		isExit = raw_input("do you want to exit ([y]/n) : ")
		if isExit in ('y','Y',''):
			print "Bye"
			break
