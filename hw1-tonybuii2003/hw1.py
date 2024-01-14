# Problem 1
def isValid(s: str):
    my_dict = {}
    ans = {}
    allow_dup = 1
    for i in s:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1
    for i in my_dict.values():
        if i not in ans:
            ans[i] = 1
        if len(ans) > 1:
            if allow_dup == 0:
                return "NO"
            else:
                ans.popitem()
                allow_dup-=1
    return "YES"
a = isValid('aabbccddeeffgghhhh')
print(a)
# Problem 2
def isBalanced(s: str):
    if len(s) % 2 != 0:
        return "NO"
    open_stack = []
    openning = ('{','(','[')
    closing = ('}',')',']')
    my_map = {'}':'{',']':'[',')':'('}
    for i in s:
        if i in openning:
            open_stack.append(i)
        if i in closing:
            if not open_stack:
                return 'NO'
            if open_stack.pop() != my_map.get(i):
                return "NO"          
    if open_stack:
        return "NO"
    return "YES"
# Bonus Problem
def countValidStrings(s: str):
    if isBalanced(s):
        return 0
    def dfs(string, current_index, l, r, result):
        nonlocal longest, res
        if current_index >= len(string):
            if l == r:
                if len(result) > longest:
                    longest = len(result)
                    res = set()
                    res.add("".join(result))
                elif len(result) == longest:
                    res.add("".join(result))
        else:
            current_char = string[current_index]
            if current_char == '(':
                result.append(current_char)
                dfs(string, current_index + 1, l + 1, r, result)
                result.pop()
                dfs(string, current_index + 1, l, r, result)
            elif current_char == ')':
                dfs(string, current_index + 1, l, r, result)
                if l > r:
                    result.append(current_char)
                    dfs(string, current_index + 1, l, r + 1, result)
                    result.pop()
            else:
                result.append(current_char)
                dfs(string, current_index + 1, l, r, result)
                result.pop()
    longest = -1
    res = set()
    dfs(s, 0, 0, 0, [])
    return len(res)
# Problem 3
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left
    def __str__(self):
        return f'{self.data},({self.left}{self.right})'
    def preOrder(self):
        mystack = []
        if self != None:
            mystack.append(self.data)
            if self.left != None:
                mystack.extend(self.left.preOrder())
            if self.right != None:
                mystack.extend(self.right.preOrder())
        return mystack
    def inOrder(self):
        mystack = []
        if self != None:
            if self.left != None:
                mystack.extend(self.left.inOrder())
            mystack.append(self.data)
            if self.right != None:
                mystack.extend(self.right.inOrder())
        return mystack
    def postOrder(self):
        mystack = []
        if self != None:
            
            if self.left != None:
                mystack.extend(self.left.postOrder())
            if self.right != None:
                mystack.extend(self.right.postOrder())
            mystack.append(self.data)
        return mystack
    def getHeight(self, value):
        return self.getHeightHelper(self, value, 0)
        
    def getHeightHelper(self, node, value, currentheight):
        if node == None:
            return -1
        if node.data == value:
            return currentheight
        left_height = self.getHeightHelper(node.left, value, currentheight+1)
        if left_height!=-1:
            return left_height
        right_height = self.getHeightHelper(node.right, value, currentheight+1)
        return right_height
    def sumTree(self):
        return self.sumTreeHelper(self)
    def sumTreeHelper(self, node):
        if node == None:
            return 0
        left = node.sumTreeHelper(node.left)
        right =node.sumTreeHelper(node.right)
        return node.data + left + right


