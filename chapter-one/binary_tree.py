"""
A binary tree has a maximum of two children
"""

class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

t = Tree(Tree("a", "b"), Tree("c", "d"))

print('*' * 20)
print(t.right.left)


print('*' * 20)
print(t.left.right)


class Tree_2:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next

t_2 = Tree_2(Tree_2("a", Tree_2("b", Tree_2("c", Tree_2("d")))))
print(t_2.kids.next.next.val)
