# Implement BFS
from collections import deque

class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        # self.parent = None
        self.children = []

    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        # for child in children:
        #     child.parent = self
        self.children.extend(children)
        return children

    def bfs_badqueue(self):
        da_qhugh = Queue()
        da_qhugh.add(self)
        da_contents = []

        while da_qhugh.isNotEmpty():
            da_node = da_qhugh.remove()
            da_contents.append(da_node.contents)
            for child in da_node.children:
                da_qhugh.add(child)

        #return "part 1 not implemented"  # obviously you delete this line when you do part 1
        return da_contents

    def bfs_deque(self):
        da_qhugh = deque()
        da_qhugh.append(self)
        da_contents = []

        while len(da_qhugh) > 0:
            da_node = da_qhugh.popleft()
            da_contents.append(da_node.contents)
            for child in da_node.children:
                da_qhugh.append(child)

        return da_contents
        #return "part 2 not implemented"  # obviously you delete this line when you do part 2

    def dfs_deque(self):
        da_qhugh = deque()
        da_qhugh.append(self)
        da_contents = []

        while len(da_qhugh) > 0:
            da_node = da_qhugh.pop()
            da_contents.append(da_node.contents)
            for i in range(len(da_node.children) - 1, -1, -1):
                da_qhugh.append(da_node.children[i])
        
        return da_contents

        #return "part 3 not implemented"  # obviously you delete this line when you do part 3


"""
A tree could look like this:


               Z
           /   |   \ 
        Q      R      S
      / | \   / \   / | \ 
    A   B  C  D E  F  G  H
   / \        |      / \ 
  T   U       W     X   Y
              |
              J


"""

root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren("Q", "R", "S")
[A, B, C] = Q.addChildren("A", "B", "C")
[D, E] = R.addChildren("D", "E")
[F, G, H] = S.addChildren("F", "G", "H")
[T, U] = A.addChildren("T", "U")
[W] = D.addChildren("W")
[X, Y] = G.addChildren("X", "Y")
[J] = W.addChildren("J")

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(" ")
# print("\nDFS should be: [", ', '.join(correct_dfs), "]")
correct_bfs = "Z Q R S A B C D E F G H T U W X Y J".split(" ")
# print("\nweird-order DFS should be: [", ', '.join(weird_correct_dfs), "]")

part1_ans = root1.bfs_badqueue()
print("\npart 1 goal:   ", correct_bfs)
if part1_ans == correct_bfs:
    print("part 1 successful match")
else:
    print("part 1 actual: ", part1_ans)

part2_ans = root1.bfs_deque()
print("\npart 2 goal:   ", correct_bfs)
if part2_ans == correct_bfs:
    print("part 2 successful match")
else:
    print("part 2 actual: ", part2_ans)


part3_ans = root1.dfs_deque()
print("\npart 3 goal:   ", correct_dfs)
if part3_ans == correct_dfs:
    print("part 3 successful match")
else:
    print("part 3 actual: ", part3_ans)