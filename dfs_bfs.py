class Graph():
	def __init__(self,n):
		self.n = n
		self.matrix = self.inputAdjacencyMatrix(n)

	def inputAdjacencyMatrix(self,n):
		# method return adjecency Matrix by taking input from user 

		#create empty matrix of n x n 
		matrix = [ [0]*n for i in range(n)]

		i=0
		while i<n:
			j=i+1
			while j<n:
				matrix[i][j] = input("is %d and %d connected ? [0 or 1] : " % (i+1,j+1) )
				j+=1
			i+=1

		return matrix

	def dfs(self, s, g):
		# s - start node
		# g - goal node
		# method returns closed_list

		# init open list with start node
		open_list = [s]
		# create closed list
		close_list = []

		while open_list:
			# pop from stack
			poped = open_list.pop()
			# add poped node to closed list
			close_list.append(poped)

			# if poped is goal then return
			if poped == g:
				return close_list

			# find children of poped node
			child = self.getChildren(poped)

			t=[]
			for i in child:
				# add node in open list if not in closed list
				if i not in close_list:
					t.append(i)

			open_listq.extend(t)

	def bfs(self, s, g):
		# s - start node
		# g - goal node
		# returns closed list

		# init open list with start node
		open_list = [s]
		# crate empty closed list
		close_list = []

		while open_list:
			# pop node from open list
			poped = open_list[0]
			open_list = open_list[1::]

			# add poped node in closed list
			close_list.append(poped)

			# if poped node is goal node then return closed list
			if poped == g:
				return close_list

			# find children of poped node
			child = self.getChildren(poped)

			t=[]
			for i in child:
				# add child node in open list if  not in closed list
				if i not in close_list:
					t.append(i)

			open_list.extend(t)
			
	def getChildren(self,r):
		# r - row (node)
		# returs children of given node
		children = []
		i=0
		while i < self.n:
			if self.matrix[r][i]!=0:
				children.append(i)
			i+=1
		return children

# main function
if __name__ == '__main__':
	n = input("Enter number of nodes : ")
	g = Graph(n)

	while True:
		choice = raw_input("1) BFS\n2) DFS\n3) Exit\n\tEnter your choice :: ")

		if choice not in '123':
			print "Invalid choice"
			continue
		elif choice == '1':
			start = input("\nEnter start node (less than %d): " % n)
			goal = input("Enter Goal node (less than %d): " % n)
			r = g.bfs(start, goal)
			print 'Path : ',' - '.join(map(str,r))

		elif choice=='2':
			start = input("\nEnter start node : ")
			goal = input("Enter Goal node : ")
			r = g.dfs(start, goal)
			print 'Path : ',' - '.join(map(str,r))

		elif choice == '3':
			print "Bye"
			break