import unittest
from LCA import *

class TestLCA(unittest.TestCase):


 def test_findLCA(self):

        # Empty Tree
        root = None

        expectedOutput = -1
        actualOutput = findLCA(root, 0, 0)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = -1
        actualOutput = findLCA(root, -4, 5)
        self.assertEqual(actualOutput, expectedOutput)


        # One Node Tree
        root = Node(1)

        expectedOutput = 1
        actualOutput = findLCA(root, 1, 1)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = -1
        actualOutput = findLCA(root, 0, 0)
        self.assertEqual(actualOutput, expectedOutput)        

        expectedOutput = -1
        actualOutput = findLCA(root, 1, 3)
        self.assertEqual(actualOutput, expectedOutput) 

        expectedOutput = -1
        actualOutput = findLCA(root, 4, 5)
        self.assertEqual(actualOutput, expectedOutput)               


        # One sided tree
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)

        expectedOutput = 3
        actualOutput = findLCA(root, 3, 3)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = 2
        actualOutput = findLCA(root, 3, 2)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = 1
        actualOutput = findLCA(root, 4, 1)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = -1
        actualOutput = findLCA(root, 1, 0)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = -1
        actualOutput = findLCA(root, 7, -5)
        self.assertEqual(actualOutput, expectedOutput)

        # clear tree for next tests
        root = None


        # Typical tree
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.left.right = Node(5) 
        root.right.left = Node(6) 
        root.right.right = Node(7) 

        # basic cases 
        expectedOutput = 2
        actualOutput = findLCA(root, 4, 5)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = 1
        actualOutput = findLCA(root, 4, 6)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = 1
        actualOutput = findLCA(root, 3, 4)
        self.assertEqual(actualOutput, expectedOutput)

        expectedOutput = 2
        actualOutput = findLCA(root, 2, 4)
        self.assertEqual(actualOutput, expectedOutput)

        # example where both nodes are equal
        expectedOutput = 7
        actualOutput = findLCA(root, 7, 7)
        self.assertEqual(actualOutput, expectedOutput)          


        # error cases
        # example where a node is 0
        expectedOutput = -1
        actualOutput = findLCA(root, 0, 5)
        self.assertEqual(actualOutput, expectedOutput) 

        # example where both nodes are 0
        expectedOutput = -1
        actualOutput = findLCA(root, 0, 0)
        self.assertEqual(actualOutput, expectedOutput)

        # example where one node is not in tree
        expectedOutput = -1
        actualOutput = findLCA(root, 8, 5)
        self.assertEqual(actualOutput, expectedOutput)

        # example where two nodes aren't in tree
        expectedOutput = -1
        actualOutput = findLCA(root, 9, 12)
        self.assertEqual(actualOutput, expectedOutput)

        # example where a node given is negative
        expectedOutput = -1
        actualOutput = findLCA(root, -1, 4)
        self.assertEqual(actualOutput, expectedOutput)

               


if __name__ == '__main__':
    unittest.main()