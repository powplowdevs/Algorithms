# Input:  mat[][] = {{1, 2, 9}
#                    {5, 3, 8}
#                    {4, 6, 7}}
# Output: 4
# The longest path is 6-7-8-9.  

#DEFINE MATRIX
mat = [[1, 2, 9], 
       [5, 3, 8],
       [4, 6, 7]]
#DEFINE MATRIX SIZE
SIZE = (3,3)

#VARS
full_list = []
new_full_list = []
connections = []
path = []

#FUNCTIONS
def find_neighbors(level,spot,ele):
    neighbors = []
    
    for i in range(4):
        #check for top neighboor
        if i == 0 and level-1 > -1:
            try:
                neighbors.append([mat[level-1][spot],level-1,spot])
            except:
                pass
        #check for bottom neighboor
        if i == 1 and level+1 < SIZE[1] :
            try:
                neighbors.append([mat[level+1][spot],level+1,spot])
            except:
                pass
        #check for left neighboor
        if i == 2 and spot-1 > -1:
            try:
                neighbors.append([mat[level][spot-1],level,spot-1])
            except:
                pass
        #check for right neighboor
        if i == 3 and spot+1 < SIZE[0]:
            try:
                neighbors.append([mat[level][spot+1], level, spot+1])
            except:
                pass

    return neighbors

#GET FULL LIST OF ALL NUMBER NEIGHBORS
for level, nele in enumerate(mat):
    for spot, ele in enumerate(nele):
        #find neighbor numbers
        full_list += [find_neighbors(level,spot,ele)]
#print(full_list)
# [
#  1   [[5, 1, 0], [2, 0, 1]], 
#  2   [[3, 1, 1], [1, 0, 0], [9, 0, 2]], 
#  9   [[8, 1, 2], [2, 0, 1]], 
#  5   [[1, 0, 0], [4, 2, 0], [3, 1, 1]], 
#  3   [[2, 0, 1], [6, 2, 1], [5, 1, 0], [8, 1, 2]], 
#  8   [[9, 0, 2], [7, 2, 2], [3, 1, 1]], 
#  4   [[5, 1, 0], [6, 2, 1]], 
#  6   [[3, 1, 1], [4, 2, 0], [7, 2, 2]], 
#  7   [[8, 1, 2], [6, 2, 1]]
# ]

#EDIT FULL LIST
i=0
for level, nele in enumerate(mat):
    for spot, ele in enumerate(nele):
        new_full_list.append([ele,full_list[i]])
        i+=1
        
# print(new_full_list)
# [
#   [1, [[5, 1, 0], [2, 0, 1]]], 
#   [2, [[3, 1, 1], [1, 0, 0], [9, 0, 2]]], 
#   [9, [[8, 1, 2], [2, 0, 1]]], 
#   [5, [[1, 0, 0], [4, 2, 0], [3, 1, 1]]], 
#   [3, [[2, 0, 1], [6, 2, 1], [5, 1, 0], [8, 1, 2]]], 
#   [8, [[9, 0, 2], [7, 2, 2], [3, 1, 1]]], 
#   [4, [[5, 1, 0], [6, 2, 1]]], 
#   [6, [[3, 1, 1], [4, 2, 0], [7, 2, 2]]], 
#   [7, [[8, 1, 2], [6, 2, 1]]]
# ]


#FIND PATH
for index, fnabs in enumerate(new_full_list):
    current_number = fnabs[0]
    for index, nabs in enumerate(fnabs[1]):
        if nabs[0] == current_number + 1:
            connections.append([current_number , nabs[0]])

#print(connections)
#[[1, 2], [2, 3], [8, 9], [4, 5], [6, 7], [7, 8]]

#FIND CONNECTION CHAIN
for index, spot in enumerate(connections):
    current = spot
    for index, spot in enumerate(connections):
        if current != spot and current[1] == spot[0]:
            #path.append(spot)
            path.append(spot)
            #print(path)
        else:
            #print("line break")
            pass

print(path)