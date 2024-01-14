import unittest
import hw1
Node = hw1.Node

def test_p1():
    assert hw1.isValid('aabbcd') == 'NO'
def test2_p1():
    assert hw1.isValid('aabbcdddeefghi') == 'NO'
def test3_p1():
    assert hw1.isValid("abcdefghhgfedecba") == 'YES'


def test_p2():
    assert hw1.isBalanced('{[()]}') == 'YES'
def test2_p2():
    assert hw1.isBalanced('{[(])}') == 'NO'
def test3_p2():
    assert hw1.isBalanced('{{[[(())]]}}') == 'YES'
def test4_p2():
    assert hw1.isBalanced('[]()()(((([])))') == 'NO'
def test5_p2():
    assert hw1.isBalanced('[](){{{[]}}}') == 'YES'

def test1_p3():
    root = Node(2, Node(1, Node(6), Node(3)), Node(3, None, Node(9)))
    assert root.preOrder() == [2,1,6,3,3,9]
    assert root.inOrder() ==  [6,1,3,2,3,9]
    assert root.postOrder() ==  [6,3,1,9,3,2]
def test2_p3():
    root = Node(1, Node(2, Node(3)), Node(4,None,(Node(5, None, Node(6, None,
Node(7))))))
    assert root.preOrder() == [1,2,3,4,5,6,7] 
    assert root.inOrder() ==  [3,2,1,4,5,6,7]
    assert root.postOrder() ==  [3,2,7,6,5,4,1]