from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        visited = [False] * (len(self.graph)) 
        queue = [] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            s = queue.pop(0) 
            print ("\t", s, end = " ") 
  
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                    '''
class Graph2: 
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self, u, v): 
        self.graph[u].append(v)
    def DFSUtil(self, v, visited): 
        visited[v] = True
        print("\t",v, end = ' ') 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
    def DFS(self, v): 
        visited = [False] * (len(self.graph)) 
        self.DFSUtil(v, visited)

        
class Node(): 
 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
def getPreIndex(): 
    return constructTreeUtil.preIndex

def incrementPreIndex(): 
    constructTreeUtil.preIndex += 1
 
def constructTreeUtil(pre, low, high, size): 
 
    if( getPreIndex() >= size or low > high): 
        return None
    root = Node(pre[getPreIndex()]) 
    incrementPreIndex() 
  

    if low == high : 
        return root  
  
    for i in range(low, high+1): 
        if (pre[i] > root.data): 
            break  
    root.left = constructTreeUtil(pre, getPreIndex(),  i-1 , size)  
  
    root.right = constructTreeUtil(pre, i, high, size)  
      
    return root 
def constructTree(pre): 
    size = len(pre)  
    constructTreeUtil.preIndex = 0 
    return constructTreeUtil(pre, 0, size-1, size)

def deleteNode(root, data): 
  
    if root is None: 
        return root  
    if data < root.data: 
        root.left = deleteNode(root.left, data) 
    elif(data > root.data): 
        root.right = deleteNode(root.right, data) 
    else: 
  
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp     
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = minValueNode(root.right) 
        root.data = temp.data 
        root.right = deleteNode(root.right , temp.data) 
    return root  
  
  '''
def printInorder(root): 
    if root is None: 
        return 
    printInorder(root.left) 
    print (root.data) 
    printInorder(root.right)
def printPostorder(root): 
    if root: 
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.data) 
'''
def hashing_func(key,hash_table):
    return key % len(hash_table)
def insertHASH(hash_table, key, value):
    hash_key = hashing_func(key, hash_table)
    hash_table[hash_key] = value
def insertCHAINING(hash_table, key, value):
    hash_key = hashing_func(key,hash_table)
    hash_table[hash_key].append(value)
def insertPROBING(hash_table, key, value):
    hash_key = hashing_func(key,hash_table)
    if not hash_table[hash_key]:
        hash_table[hash_key].append(value)
    else:
        while hash_table[hash_key]:
            hash_key +=1
        hash_table[hash_key].append(value)
'''




    
def main():
    print('\t\t------------Welcome to Lyncia\'s Data Structures Program------------')
    print('\t\tPlease review the options and choose accordingly!')
    print('\n\t\t\t\t 1- Binary Search Tree\n\t\t\t\t   2- Hash Tables\n\t\t\t\t     3- Graphs\n\t\t\t\t      4- Quit')
    choice = int(input('Enter Choice Here:'))
    while choice != 4:
        if choice == 1:
            bts()
        elif choice ==2:
            hashTables()
        elif choice ==3:
            graph()
        
        print('\n\t\t\t\t 1- Binary Search Tree\n\t\t\t\t   2- Hash Tables\n\t\t\t\t     3- Graphs\n\t\t\t\t      4- Quit')
        choice = int(input('Enter Choice Here:'))


def graph():
    print("\t\t     The Key for this Graph is:\n\n\t\t0:Susan, 1:Darlene, 2:Fred, 3:Brent\n\t\t 4:Sander, 5:Lance, 6:Fran, 7: John, 8:Jean, 9: Mike")
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(2,3)
    g.addEdge(4,0)
    g.addEdge(5,6)
    g.addEdge(4,6)
    g.addEdge(6,7)
    g.addEdge(5,8)
    g.addEdge(8,0)
    g.addEdge(9,1)
    g.addEdge(3,5)
    g.addEdge(0,7)
    print("\n\nBreadth First Traversal From Austin\n")
    
    g.BFS(0)
    '''
    g2 = Graph2()
    g2.addEdge(0,1)
    g2.addEdge(2,3)
    g2.addEdge(4,0)
    g2.addEdge(5,6)
    g2.addEdge(4,6)
    g2.addEdge(6,7)
    g2.addEdge(5,8)
    g2.addEdge(8,0)
    g2.addEdge(9,1)
    g2.addEdge(3,5)
    g2.addEdge(0,7)
    print("\nDepth First Traversal From Austin:\n")
    g2.DFS(0)

def bts():
    infile = open('bstnumbers.txt','r')
    numbers = infile. readlines()
    for x in range (len(numbers)):
        numbers[x] = numbers[x].rstrip('\n')
        numbers[x] = int (numbers[x])
    root = constructTree(numbers) 
    print ("\n\t\tInorder traversal of the constructed tree:")
    printInorder(root )
    print ('\n')
    print ("\t\tPostorder traversal of the constructed tree:")
    printPostorder(root)
    num = int(input('Number to Delete:'))
    root = deleteNode(root, num)
    print ("\n\t\tInorder traversal of the constructed tree:")
    printInorder(root )
    infile.close()
def hashTables():
    infile = open('hashnumbers.txt','r')
    numbers = infile. readlines()
    hash_table = [None] * len(numbers)
    for x in range (len(numbers)):
        numbers[x] = numbers[x].rstrip('\n')
        numbers[x] = int (numbers[x])
        insertHASH(hash_table, numbers[x],str(numbers[x]))
    print('Hash table Ignoring any Collisions:', hash_table)

    Chash_table = [[] for _ in range(len(numbers))]
    for x in range (len(numbers)):
        insertCHAINING(Chash_table, numbers[x],numbers[x])   
    print('Hash Table using Link Chaining:', Chash_table)
    Phash_table = [[] for _ in range(len(numbers))]
    for x in range (len(numbers)):
         insertPROBING(Phash_table, numbers[x],numbers[x])  
    print('Hash Table using Linear Probing:', Phash_table)'''
main()



 
  
  

