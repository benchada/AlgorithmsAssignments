from collections import defaultdict
from collections import priorityDictionary
class Vertex:
	def __init__(self,key):
		self.id=key
		self.connectedTo={}
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr] = weight
	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
	def getConnections(self):
		return self.connectedTo.keys()
	def getId(self):
		return self.id
	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	    
class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	def addVertex(self,key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	def getVertex(self,n):
		if n in self.vertList:
		    return self.vertList[n]
		else:
		    return None
	def __contains__(self,n):
		return n in self.vertList
	def addEdge(self,f,t,cost=0):
		 if f not in self.vertList:
			 nv = self.addVertex(f)
		 if t not in self.vertList:
			 nv = self.addVertex(t)
		 self.vertList[f].addNeighbor(self.vertList[t], cost)
	def getVertices(self):
		return self.vertList.keys()
	def __iter__(self):
		return iter(self.vertList.values())
	    

text_file = open('soc-Slashdot0811.txt', 'r')
lines = text_file.readlines()
print (len(lines))


#Building the graph as a dictionary from the list of lines

g = defaultdict(list)  
for i in len(lines):
	fromN, toN = lines[i].split(' ')  #From Node  to another node = getting the values
	g[fromN].append[toN]
	

######################



def Dijkstra(G,start,end=None):

	D = {}	# dictionary of final distances
	P = {}	# dictionary of predecessors
	Q = priorityDictionary()   # est.dist. of non-final vert.
	Q[start] = 0
	
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError("Dijkstra: found better path to already-final vertex")
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	
	return (D,P)

G1 = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}

print Dijkstra(G1, 'u')

###########################################

#All pairs shortest path algorithm

final = [] #List of tuples (D,P) Distances and predecessures
for node in g:
	final.append(Dijkstra (g, node))

#Checking for the largest path of distances
answer =0
for elem in final:
	if (elem[0] > count):
		count = elem[0]  #Updating the counter
		answer = elem  # returning the tuple as answer (D,P)

print ("The largest shortest path is" + P + "And it has the distance of" + D)
	
