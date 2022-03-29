# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:  # 51.34% 6.59%
    def __init__(self, nestedList: [NestedInteger]):
        def helper(arr):
            if type(arr) == list:
                for el in arr:
                    helper(el)
            elif arr.isInteger():
                self.flat.append(arr.getInteger())
            else:
                helper(arr.getList())
            return
        
        self.index = 0
        self.flat = []
        helper(nestedList)
    
    def next(self) -> int:
        res = self.flat[self.index]
        self.index += 1
        return res
        
    
    def hasNext(self) -> bool:
        return self.index < len(self.flat)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())