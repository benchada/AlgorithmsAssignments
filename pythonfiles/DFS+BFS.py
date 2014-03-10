global counter
counter =0

def explore_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  global nodes_counter
  nodes_counter = nodes_counter+1
  path=path+[start]
  for node in graph[start]: #if the start is connected to other nodes
    if node not in path:
      path=explore_dfs(graph, node, path)
  return path



def recursive_dfs(graph, start, path=[]):
    global component
    
    #path = path+[start]
    for node in graph:
        if node not in path:
            path = path + explore_dfs(graph,node)
            component = component +1

    return path
    


'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''

#Testing
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':[]}
nodes_counter =0
component =0
print (recursive_dfs(graph, graph[0]))
print (component, nodes_counter)

#We construct the reverse tree:

g = defaultdict(list)  
gr =defaultdict(list) 
for i in len(lines):
	fromN, toN = lines[i].split(' ')  #From Node  to another node = getting the values
	gr[toN].append[fromN]

#Running DFS on Gr
recursive_dfs(gr, start)




nodes_counter =0
component =0
print (component, nodes_counter)

