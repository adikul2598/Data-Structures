# Data-Structures

Data Structures are a way of organizing data so that it can be accessed more efficiently depending upon the situation. Data Structures are fundamentals of any programming language around which a program is built.  

## Set

Python Set is an ordered collection of data that is mutable and does not allow any duplicate element. Sets are basically used to include membership testing and   eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average.  

>Set = set([1, 2, 'Gks', 4, 'For', 6, 'eks'])  
>print("\nSet with the use of Mixed Values")  
>print(Set)  

>print("\nElements of set: ")  
>for i in Set:  
>	print(i, end =" ")  
>print()   


>print("Teek" in Set)  

## Frozen Sets

Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.  

>normal_set = set(["a", "b","c"])
>print(normal_set)
>frozen_set = frozenset(["e", "f", "g"])
>print("\nFrozen Set")
>print(frozen_set)

## Python Bytearray Operations


>a = bytearray((12, 8, 25, 2))
>print("Creating Bytearray:")
>print(a)
>print("\nAccessing Elements:", a[1])

>a[1] = 3
>print("\nAfter Modifying:")
>print(a)

>a.append(30)
>print("\nAfter Adding Elements:")
>print(a)

## Collection Modules

### Counters

A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents   the element in the iterable and value represents the count of that element in the iterable  

>from collections import Counter
	
>print(Counter(['B','B','A','B','C','A','B','B','A','C']))
	
>count = Counter({'A':3, 'B':5, 'C':2})
>print(count)

>count.update(['A', 1])
>print(count)

### OrderedDict

An OrderedDict is also a sub-class of dictionary but unlike a dictionary, it remembers the order in which the keys were inserted.   

>from collections import OrderedDict

>print("Before deleting:\n")
>od = OrderedDict()
>od['a'] = 1
>od['b'] = 2
>od['c'] = 3
>od['d'] = 4

>for key, value in od.items():
>	print(key, value)

>print("\nAfter deleting:\n")
>od.pop('c')
>for key, value in od.items():
>	print(key, value)
  
>print("\nAfter re-inserting:\n")
>od['c'] = 3
>for key, value in od.items():
>	print(key, value)

### DefaultDict

DefaultDict is used to provide some default values for the key that does not exist and never raises a KeyError. Its objects can be initialized using DefaultDict() method by passing the data type as an argument.  

>from collections import defaultdict
>d = defaultdict(int)	
>L = [1, 2, 3, 4, 2, 4, 1, 2]	
>for i in L:	
>	d[i] += 1		
>print(d)

### ChainMap

A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When a key is needed to be found then all the dictionaries are searched one by one until the key is found.  

>from collections import ChainMap
>d1 = {'a': 1, 'b': 2}
>d2 = {'c': 3, 'd': 4}
>d3 = {'e': 5, 'f': 6}
>c = ChainMap(d1, d2, d3)
>print(c)
>print(c['a'])
>print(c['g'])

### UserDict

UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects.  

>from collections import UserDict

>class MyDict(UserDict):
	
	>def __del__(self):
	>	raise RuntimeError("Deletion not allowed")
	>def pop(self, s = None):
	>	raise RuntimeError("Deletion not allowed")
		>def popitem(self, s = None):
	>	raise RuntimeError("Deletion not allowed")
	>d = MyDict({'a':1,
>	'b': 2,
>	'c': 3})
>print("Original Dictionary")
>print(d)
>d.pop(1)

## Linked List

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.  
A linked list is represented by a pointer to the first node of the linked list. The first node is called the head.  

>class Node:  

	
	def __init__(self, data):  
		self.data = data   
		self.next = None
						  


	class LinkedList:  
	
	def __init__(self):  
		self.head = None  
		
		
		
		
>
class Node:
  
    
    def __init__(self, data):
        self.data = data 
        self.next = None 
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
  

	if __name__=='__main__':
  

    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
  
  
    llist.head.next = second; # Link first node with second
  
    second.next = third;  		
    
## Linked List Traversal

>class Node:
  

    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
  
  

class LinkedList:
  

    def __init__(self):
        self.head = None
  


    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
  
  
	# Code execution starts here
	if __name__=='__main__':
  
    
    	llist = LinkedList()
  
    	llist.head = Node(1)
    	second = Node(2)
    	third = Node(3)
  
 	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node
  
    llist.printList()
    
    
    
## Stack

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only.  

	stack = []

	stack.append('g')
	stack.append('f')
	stack.append('g')

	print('Initial stack')
	print(stack)

	print('\nElements popped from stack:')
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())

	print('\nStack after elements are popped:')
	print(stack)

## QUEUE

As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first  
	
	queue = []

	
	queue.append('g')
	queue.append('f')
	queue.append('g')

	print("Initial queue")
	print(queue)

	# Removing elements from the queue
	print("\nElements dequeued from queue")
	print(queue.pop(0))
	print(queue.pop(0))
	print(queue.pop(0))

	print("\nQueue after removing elements")
	print(queue)

	
Implementation using collections.deque

	from collections import deque

	# Initializing a queue
	q = deque()

	# Adding elements to a queue
	q.append('g')
	q.append('f')
	q.append('g')

	print("Initial queue")
	print(q)

	# Removing elements from a queue
	print("\nElements dequeued from the queue")
	print(q.popleft())
	print(q.popleft())
	print(q.popleft())

	print("\nQueue after removing elements")
	print(q)

	# Uncommenting q.popleft()
	# will raise an IndexError
	# as queue is now empty

## Priority Queue

Priority Queues are abstract data structures where each data/value in the queue has a certain priority.		

	# A simple implementation of Priority Queue
	# using Queue.
	class PriorityQueue(object):
		def __init__(self):
			self.queue = []

		def __str__(self):
			return ' '.join([str(i) for i in self.queue])

		# for checking if the queue is empty
		def isEmpty(self):
			return len(self.queue) == 0

		# for inserting an element in the queue
		def insert(self, data):
			self.queue.append(data)

		# for popping an element based on Priority
		def delete(self):
			try:
				max = 0
				for i in range(len(self.queue)):
					if self.queue[i] > self.queue[max]:
						max = i
				item = self.queue[max]
				del self.queue[max]
				return item
			except IndexError:
				print()
				exit()

	if __name__ == '__main__':
		myQueue = PriorityQueue()
		myQueue.insert(12)
		myQueue.insert(1)
		myQueue.insert(14)
		myQueue.insert(7)
		print(myQueue)			
		while not myQueue.isEmpty():
			print(myQueue.delete())

## Binary Tree

The topmost node of the tree is called the root whereas the bottommost nodes or the nodes with no children are called the leaf nodes. The nodes that are directly under a node are called its children and the nodes that are directly above something are called its parent. 

A binary tree is a tree whose elements can have almost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children.  

	# A Python class that represents an individual node
	# in a Binary Tree
	class Node:
		def __init__(self,key):
			self.left = None
			self.right = None
			self.val = key

Adding Data to Tree

	# Python program to introduce Binary Tree

	# A class that represents an individual node in a
	# Binary Tree
	class Node:
		def __init__(self,key):
			self.left = None
			self.right = None
			self.val = key


	# create root
	root = Node(1)
	''' following is the tree after above statement
			1
		/ \
		None None'''

	root.left	 = Node(2);
	root.right	 = Node(3);

	''' 2 and 3 become left and right children of 1
			1
			/ \
			2	 3
		/ \ / \
	None None None None'''


	root.left.left = Node(4);
	'''4 becomes left child of 2
			1
		/	 \
		2		 3
		/ \	 / \
	4 None None None
	/ \
	None None'''
	
## Tree Traversals

	# Python program to for tree traversals

	# A class that represents an individual node in a
	# Binary Tree
	class Node:
		def __init__(self, key):
			self.left = None
			self.right = None
			self.val = key


	# A function to do inorder tree traversal
	def printInorder(root):

		if root:

			# First recur on left child
			printInorder(root.left)

			# then print the data of node
			print(root.val),

			# now recur on right child
			printInorder(root.right)


	# A function to do postorder tree traversal
	def printPostorder(root):

		if root:

			# First recur on left child
			printPostorder(root.left)

			# the recur on right child
			printPostorder(root.right)

			# now print the data of node
			print(root.val),


	# A function to do preorder tree traversal
	def printPreorder(root):

		if root:

			# First print the data of node
			print(root.val),

			# Then recur on left child
			printPreorder(root.left)

			# Finally recur on right child
			printPreorder(root.right)


	# Driver code
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	print("Preorder traversal of binary tree is")
	printPreorder(root)

	print("\nInorder traversal of binary tree is")
	printInorder(root)

	print("\nPostorder traversal of binary tree is")
	printPostorder(root)

## Graph

A graph is a nonlinear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph  

### Adjacency Matrix  

Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. The adjacency matrix for an undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.

	# A simple representation of graph using Adjacency Matrix
	class Graph:
		def __init__(self,numvertex):
			self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
			self.numvertex = numvertex
			self.vertices = {}
			self.verticeslist =[0]*numvertex

		def set_vertex(self,vtx,id):
			if 0<=vtx<=self.numvertex:
				self.vertices[id] = vtx
				self.verticeslist[vtx] = id

		def set_edge(self,frm,to,cost=0):
			frm = self.vertices[frm]
			to = self.vertices[to]
			self.adjMatrix[frm][to] = cost

			# for directed graph do not add this
			self.adjMatrix[to][frm] = cost

		def get_vertex(self):
			return self.verticeslist

		def get_edges(self):
			edges=[]
			for i in range (self.numvertex):
				for j in range (self.numvertex):
					if (self.adjMatrix[i][j]!=-1):
						edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
			return edges

		def get_matrix(self):
			return self.adjMatrix

	G =Graph(6)
	G.set_vertex(0,'a')
	G.set_vertex(1,'b')
	G.set_vertex(2,'c')
	G.set_vertex(3,'d')
	G.set_vertex(4,'e')
	G.set_vertex(5,'f')
	G.set_edge('a','e',10)
	G.set_edge('a','c',20)
	G.set_edge('c','b',30)
	G.set_edge('b','e',40)
	G.set_edge('e','d',50)
	G.set_edge('f','e',60)

	print("Vertices of Graph")
	print(G.get_vertex())

	print("Edges of Graph")
	print(G.get_edges())

	print("Adjacency Matrix of Graph")
	print(G.get_matrix())

### Adjacency List

An array of lists is used. The size of the array is equal to the number of vertices. Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex.

	# A class to represent the adjacency list of the node
	class AdjNode:
		def __init__(self, data):
			self.vertex = data
			self.next = None


	# A class to represent a graph. A graph
	# is the list of the adjacency lists.
	# Size of the array will be the no. of the
	# vertices "V"
	class Graph:
		def __init__(self, vertices):
			self.V = vertices
			self.graph = [None] * self.V

		# Function to add an edge in an undirected graph
		def add_edge(self, src, dest):

			# Adding the node to the source node
			node = AdjNode(dest)
			node.next = self.graph[src]
			self.graph[src] = node

			# Adding the source node to the destination as
			# it is the undirected graph
			node = AdjNode(src)
			node.next = self.graph[dest]
			self.graph[dest] = node

		# Function to print the graph
		def print_graph(self):
			for i in range(self.V):
				print("Adjacency list of vertex {}\n head".format(i), end="")
				temp = self.graph[i]
				while temp:
					print(" -> {}".format(temp.vertex), end="")
					temp = temp.next
				print(" \n")


	# Driver program to the above graph class
	if __name__ == "__main__":
		V = 5
		graph = Graph(V)
		graph.add_edge(0, 1)
		graph.add_edge(0, 4)
		graph.add_edge(1, 2)
		graph.add_edge(1, 3)
		graph.add_edge(1, 4)
		graph.add_edge(2, 3)
		graph.add_edge(3, 4)

		graph.print_graph()

## Graph Traversals

### BFS

Breadth-First Traversal for a graph is similar to Breadth-First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array  

	# Python3 Program to print BFS traversal
	# from a given source vertex. BFS(int s)
	# traverses vertices reachable from s.
	from collections import defaultdict

	# This class represents a directed graph
	# using adjacency list representation
	class Graph:

		# Constructor
		def __init__(self):

			# default dictionary to store graph
			self.graph = defaultdict(list)

		# function to add an edge to graph
		def addEdge(self,u,v):
			self.graph[u].append(v)

		# Function to print a BFS of graph
		def BFS(self, s):

			# Mark all the vertices as not visited
			visited = [False] * (max(self.graph) + 1)

			# Create a queue for BFS
			queue = []

			# Mark the source node as
			# visited and enqueue it
			queue.append(s)
			visited[s] = True

			while queue:

				# Dequeue a vertex from
				# queue and print it
				s = queue.pop(0)
				print (s, end = " ")

				# Get all adjacent vertices of the
				# dequeued vertex s. If a adjacent
				# has not been visited, then mark it
				# visited and enqueue it
				for i in self.graph[s]:
					if visited[i] == False:
						queue.append(i)
						visited[i] = True

	# Driver code

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print ("Following is Breadth First Traversal"
					" (starting from vertex 2)")
	g.BFS(2)


### DFS

Depth First Traversal for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice.  

	from collections import defaultdict

	# This class represents a directed graph using
	# adjacency list representation


	class Graph:

		# Constructor
		def __init__(self):

			# default dictionary to store graph
			self.graph = defaultdict(list)

		# function to add an edge to graph
		def addEdge(self, u, v):
			self.graph[u].append(v)

		# A function used by DFS
		def DFSUtil(self, v, visited):

			# Mark the current node as visited
			# and print it
			visited.add(v)
			print(v, end=' ')

			# Recur for all the vertices
			# adjacent to this vertex
			for neighbour in self.graph[v]:
				if neighbour not in visited:
					self.DFSUtil(neighbour, visited)

		# The function to do DFS traversal. It uses
		# recursive DFSUtil()
		def DFS(self, v):

			# Create a set to store visited vertices
			visited = set()

			# Call the recursive helper function
			# to print DFS traversal
			self.DFSUtil(v, visited)

	# Driver code


	# Create a graph given
	# in the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is DFS from (starting from vertex 2)")
	g.DFS(2)

