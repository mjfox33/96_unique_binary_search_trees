from curses.ascii import SO
from code_96_unique_binary_search_trees import Solution

def test_example_1():
    s = Solution()
    assert s.numTrees(6) == 132

def test_example_2():
    s = Solution()
    assert s.numTrees(19) == 1767263190