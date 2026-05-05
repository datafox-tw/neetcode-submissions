class CountSquares:
    from collections import defaultdict
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []


    def add(self, point: List[int]) -> None:
        # count how many points in a specific location(which is duplicated but not the same)
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)    

    def count(self, point: List[int]) -> int:
        px, py = point
        result = 0
        # check every point and its availability, O(N)
        for x,y in self.pts:
            # as hint disclosed (and our thought), we should find the diag' point and see if the rest two points exist
            if x==px or y==py or (abs(x-px) != abs(y-py)): # we want square not rectangle
                continue
            # count the rest two points exist or not
            diag1 = self.ptsCount[(x, py)] 
            diag2 = self.ptsCount[(px, y)]
            result += diag1*diag2 # if one of them is zero then no square 
        return  result

