class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        l = len(self.data)
        if l%2 == 1:
            return self.data[l//2]
        return (self.data[l // 2] + self.data[l // 2 - 1]) / 2
        