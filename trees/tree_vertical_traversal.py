class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def vertical_traversal(root):
    if root is None:
        return
    queue = [root]
    map_hd = {}
    hd = {}
    map_hd[0] = [root.data]
    hd[root.data] = 0

    while len(queue):
        temp = queue.pop(0)
        if temp.left:
            queue.append(temp.left)
            hd[temp.left.data] = hd[temp.data] - 1
            if map_hd.get(hd[temp.left.data]) is None:
                map_hd[hd[temp.left.data]] = []
            map_hd[hd[temp.left.data]].append(temp.left.data)
        if temp.right:
            queue.append(temp.right)
            hd[temp.right.data] = hd[temp.data] + 1
            if map_hd.get(hd[temp.right.data]) is None:
                map_hd[hd[temp.right.data]] = []
            map_hd[hd[temp.right.data]].append(temp.right.data)
    
    hds = sorted(map_hd.keys())
    # print(map_hd)
    # print(hds)
    traversal = []
    for hd in hds:
        traversal.extend(map_hd[hd])
    return traversal

tree = Node(1) 
tree.left = Node(2) 
tree.right = Node(3) 
tree.left.left = Node(4) 
tree.left.right = Node(5) 
tree.right.left = Node(6) 
tree.right.right = Node(7) 
tree.right.left.right =Node(8) 
tree.right.right.left = Node(10) 
tree.right.right.right = Node(9) 
tree.right.right.left.right = Node(11) 
tree.right.right.left.right.right = Node(12) 
print(vertical_traversal(tree))