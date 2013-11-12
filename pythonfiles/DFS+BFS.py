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
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':[]}
nodes_counter =0
component =0
print (recursive_dfs(graph, 'A'))
print (component, nodes_counter)
