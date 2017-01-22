    def __init__(self, array):
        self.array = array
        self.maximumDifference = 0
        self.dif = 0
        
    def computeDifference(self):
        menor = min(self.array)
        maior = max(self.array)
        self.maximumDifference = maior - menor 