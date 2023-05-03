import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_find(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)

        assert(tree.find(3) is not None)

        assert(tree.find(10) is None)
 
if __name__ == '__main__':
    unittest.main()