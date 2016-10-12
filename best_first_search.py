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

	def bfs(self, s, g, h):
		"Best First Search"
		# s - start node indexing from 0
		# g - goal node indexing from 0

		openList = {s:0}
		closeList = []
		while openList:
			minIndex, minValue = self.getMin(openList)
			del openList[minIndex]
			
			closeList.append(minIndex)

			if minIndex == g:
				return closeList

			childs = self.getChildren(minIndex)
			
			for key,value in childs.iteritems():
				childs[key] = h[key]

			openList = self.appendDict(openList,childs)

		return []
		
	def getChildren(self,r):
		return { i:value for i,value in enumerate(self.matrix[r]) if value!=0}

	def appendDict(self,dict1, dict2):
		for key,value in dict1.iteritems():
			if dict2.has_key(key):
				if dict1[key]>dict2[key]:
					dict1[key]=dict2[key]
				del dict2[key]
		dict1.update(dict2)
		return dict1

	def getMin(self,openList):
		# returns tuple (index,minimum)

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
		h = input("Enter huerestic list : ")
		path = graph.bfs(start,goal, h)

		if path:
			print 'Path : ',' - '.join(map(str,path))
		else:
			print 'Path : Not Found'

		isExit = raw_input("do you want to exit ([y]/n) : ")
		if isExit in ('y','Y',''):
			print "Bye"
			break


'''
======================
--------OUTPUT--------
======================

Enter number of nodes : 5

Is node 0 adjacent to 1 (0 or cost) : 1
Is node 0 adjacent to 2 (0 or cost) : 4
Is node 0 adjacent to 3 (0 or cost) : 0
Is node 0 adjacent to 4 (0 or cost) : 0
Is node 1 adjacent to 2 (0 or cost) : 2
Is node 1 adjacent to 3 (0 or cost) : 3
Is node 1 adjacent to 4 (0 or cost) : 12
Is node 2 adjacent to 3 (0 or cost) : 2
Is node 2 adjacent to 4 (0 or cost) : 0
Is node 3 adjacent to 4 (0 or cost) : 0

Entered Adjecency Matrix ::
-------------------------
  n  |  0   1   2   3   4
-------------------------
  0  |  0   1   4   0   0   
  1  |  0   0   2   3   12   
  2  |  0   0   0   2   0   
  3  |  0   0   0   0   0   
  4  |  0   0   0   0   0   
-------------------------

Enter start node : 0
Enter Goal node : 4
Enter huerestic list : [13,12,100,100,0]
Path :  0 - 1 - 4
do you want to exit ([y]/n) : n

Enter start node : 1
Enter Goal node : 4
Enter huerestic list : [13,12,100,100,0]
Path :  1 - 4
do you want to exit ([y]/n) : n

Enter start node : 2
Enter Goal node : 4
Enter huerestic list : [13,12,100,100,0]
Path : Not Found
do you want to exit ([y]/n) : y
Bye

'''
