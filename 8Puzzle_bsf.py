goal = [1,2,3,4,5,6,7,8,0]

class Node :
    def __init__(self,start,parent,operator,depth,cost):
        self.start = start
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost


#start=[1,2,3,0,4,5,7,8,6]

def print_result(start):
    i=0
    print("\n")
    for i in range(0,3,1):
        print("%i | %i | %i | "%(start[i],start[i+3],start[i+6]))

#print_result(start)

def find_null(new_start):
    idx=new_start.index(0)
    return idx

#find_null(start)

def move_up(start):
    new_start=start[:]
    idxNull=find_null(new_start)
    if idxNull not in [0,3,6]:
        new_start[idxNull-1],new_start[idxNull]=new_start[idxNull],new_start[idxNull-1]
        #print_result(new_start)
        return new_start
    else:
        #print("\nYou can't move up")
        return None
    

def move_down(start):
    new_start=start[:]
    idxNull=find_null(new_start)
    if idxNull not in [2,5,8]:
        new_start[idxNull+1],new_start[idxNull]=new_start[idxNull],new_start[idxNull+1]
        #print_result(new_start)
        return new_start
    else:
        #print("\nYou can't move down")
        return None
    

def move_left(start):
    new_start=start[:]
    idxNull=find_null(new_start)
    if idxNull not in [0,1,2]:
        new_start[idxNull-3],new_start[idxNull]=new_start[idxNull],new_start[idxNull-3]
       # print_result(new_start)
        return new_start
    else:
        #print("\nYou can't move left")
        return None
    

def move_right(start):
    new_start=start[:]
    idxNull=find_null(new_start)
    if idxNull not in [6,7,8]:
        
        new_start[idxNull+3],new_start[idxNull]=new_start[idxNull],new_start[idxNull+3]
       # print_result(new_start)
        return new_start
         
    else:
        #print("\nYou can't move right")
        return None

#Create Node
def c_node(start,parant,operator,depth,cost):
    return Node(start,parant,operator,depth,cost)

def expand_node(node,nodes):
    expand_nodes=[]
    expand_nodes.append(c_node(move_up(node.start),node,"Up",node.depth+1,0))
    expand_nodes.append(c_node(move_down(node.start),node,"down",node.depth+1,0))
    expand_nodes.append(c_node(move_left(node.start),node,"left",node.depth+1,0))
    expand_nodes.append(c_node(move_right(node.start),node,"right",node.depth+1,0))
    expand_nodes=[node for node in expand_nodes if node.start!=None]
    return expand_nodes

def bfs(start,goal):
    nodes = []
    nodes.append(c_node(start,None,None,0,0))
    while True:
        if len(nodes)==0:
            return None
        node=nodes.pop(0)
        if node.start==goal:
            moves=[]
            temp=node
            
            while True :
                moves.insert(0,temp.operator)
                if temp.depth == 1:
                    break
                temp = temp.parent
            return moves
        nodes.extend(expand_node(node,nodes))

def dfs(start,goal,depth=10):
    depth_limit=depth
    nodes = []
    #expand_node = []
    nodes.append(c_node(start,None,None,0,0))
    while True:
        if len(nodes)==0:
            return None
        node=nodes.pop(0)
        if node.start==goal:
            moves=[]
            temp=node
            
            while True :
                moves.insert(0,temp.operator)
                if temp.depth == 1:
                    break
                temp = temp.parent
            return moves
        if node.depth<depth_limit:
            expand_nodes=expand_node(node,nodes)
            expand_nodes.extend(nodes)
            nodes=expand_nodes
        



def dfid(start,goal,depth=60):
    for i in range(depth):
        result=dfs(start,goal,i)
        if result!=None:
            return result

def main():
    result = []
    start = [1,2,3,0,4,5,7,8,6]
    
    print("Start  : ")
    print_result(start)
    print("\n")
    result=bfs(start,goal)
    res=dfs(start,goal)
    ans=dfid(start,goal)
    if result==None:
        print("no solution")
    elif result==[None]:
        print("start is goal")
    else:
        print(result)

    if res==None:
        print("no solution")
    elif res==[None]:
        print("start is goal")
    else:
        print(res)
       # print(res)
    if ans==None:
        print("no solution")
    elif ans==[None]:
        print("start is goal")
    else:
        print(ans)
       # print(res)
        
    
   # new_start = start[:]
    #index = new_start.index(0)
    #print(index)

if __name__=="__main__":
    main()
    
#ch=-1
#while ch!=7:
#    print("\n1.Print Status")
#    print("2.Move Up")
#    print("3.Move Down")
#    print("4.Move Left")
#    print("5.Move Right")
#    print("6.Main")
#    print("7.EXIT")
#    ch = int(input("Enter your choice :"))
#
#    if ch==1:
#        print_result(start)
#    elif ch==2:
#        move_up(start)
#    elif ch==3:
#        move_down(start)
#    elif ch==4:
#        move_left(start)
#    elif ch==5:
#        move_right(start)
#    elif ch==6:
         
       
