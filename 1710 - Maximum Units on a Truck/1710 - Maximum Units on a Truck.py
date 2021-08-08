class Solution:
    def maximumUnits(
            self,
            boxTypes: List[List[int]], truckSize: int) -> int:  # 5.06% 41.97%
        boxTypes.sort(key=lambda x: x[1])
        out = 0
        while truckSize:
            if boxTypes[-1][0] == 0:
                boxTypes.pop()
            if not boxTypes:
                break
            out += boxTypes[-1][1]
            boxTypes[-1][0] -= 1
            truckSize -= 1
        return out

    def maximumUnits_plus_blocks(
            self,
            boxTypes: List[List[int]],
            truckSize: int) -> int:  # 71.22% 70.94%
        boxTypes.sort(key=lambda x: x[1])
        out = 0
        while truckSize and boxTypes:
            largest_qty, largest_items = boxTypes.pop()
            if largest_qty <= truckSize:
                out += largest_qty * largest_items
                truckSize -= largest_qty
            else:
                out += truckSize * largest_items
                truckSize = 0
        return out

    def maximumUnits_best(
            self,
            boxTypes: List[List[int]],
            truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        remainingCapacity = truckSize
        totalUnits = 0
        for x in boxTypes:
            numBoxes = x[0]
            unitsPerBox = x[1]
            if numBoxes <= remainingCapacity:
                remainingCapacity -= numBoxes
                totalUnits += numBoxes*unitsPerBox
            else:
                totalUnits += remainingCapacity*unitsPerBox
                remainingCapacity = 0
            if remainingCapacity == 0:
                break
        return totalUnits
