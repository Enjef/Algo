class Solution:
    def minOperations(self, boxes):  # 9.72% 76.39%
        boxes = [int(x) for x in boxes]
        out = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                out[i] += abs(i - j) * boxes[j]
        return out

    def minOperations_mock(self, boxes: str) -> List[int]:  # 77.87% 50.48%
        boxes = [int(x) for x in boxes]
        out = [0] * len(boxes)
        n = len(boxes)
        acc = 0
        balls = 0
        for i in range(n):
            out[i] += acc + balls
            acc = acc + balls
            balls += boxes[i]
        acc = 0
        balls = 0
        for i in range(n-1,-1,-1):
            out[i] += acc + balls
            acc = acc + balls
            balls += boxes[i]
        return out

    def minOperations_best_speed(self, boxes):
        left = 0
        right = 0
        dist = 0
        for i in range(len(boxes)):
            if boxes[i] == "1":
                dist += i
                if i == 0:
                    left += 1
                else:
                    right += 1       
        arr = [dist]
        for i in range(1, len(boxes)):
            arr.append(arr[i-1] + left - right)
            if boxes[i] == '1':
                left += 1
                right -= 1
        return arr

    def minOperations(self, boxes):
        if not boxes:
            return None
        len_boxes = len(boxes)
        ans = [0] * len_boxes
        index = []
        for i, n in enumerate(boxes):
            if n == '1':
                index.append(i)
        for i in range(len_boxes):
            for ball_idx in index:
                ans[i] += abs(ball_idx-i)
        return ans
