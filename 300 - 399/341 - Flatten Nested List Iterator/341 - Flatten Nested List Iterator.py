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


class NestedIterator_best_speed:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = self.initializeList(nestedList)
        self.iter = 0
        self.size = len(self.nestedList)
        
    def initializeList(self, nestedList: [NestedInteger]):   
        initializedList = []
        
        if isinstance(nestedList, list):
            for elem in nestedList:
                if elem.isInteger():
                    initializedList.append(elem.getInteger())
                else:
                    initializedList.extend(self.initializeList(elem))
        else:
            for elem in nestedList.getList():
                if elem.isInteger():
                    initializedList.append(elem.getInteger())
                else:
                    initializedList.extend(self.initializeList(elem))
                
        return initializedList
    
    def next(self) -> int:
        if self.hasNext():
            self.iter += 1
            return self.nestedList[self.iter-1]
        raise Exception("NestedIterator arrived to the end of the Nested List.")
        
    def hasNext(self) -> bool:
        return (self.iter < self.size)


class NestedIterator_best_memory:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList
        self.stack.reverse()
    
    def next(self) -> int:
        current = self.stack.pop()
        ele = current.getInteger()  
        return ele 
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            res = self.stack.pop()
            l = res.getList()
            l.reverse()
            self.stack += l
        return len(self.stack) > 0
