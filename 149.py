import collections
class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        res = 1
        for i in range(len(points)):
            p1 = points[i]
            count = collections.defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float("inf")  
                else:
                    slope = (p2[1] - p1[1]) / float(p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)  
        return res