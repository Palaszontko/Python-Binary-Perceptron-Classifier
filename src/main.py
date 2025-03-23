class Sample:
    def __init__(self, weights : list, dataTag : str):
        self.weights = weights
        self.dataTag = dataTag

    def __str__(self):
        return f"Data Tag: {self.dataTag}, Weights: {self.weights}"
    
class Perceptron:
    def __init__(self, alpha : float, beta : float, trainDataPath : str, testDataPath : str):
        self.alpha = alpha
        self.beta = beta
        self.threshold = random.randrange(-5,5)
        self.trainDataPath = trainDataPath
        self.testDataPath = testDataPath

    def calculateNet(self, input):
        net = 0
        for i in range(len(input)):
            net += input[i] * self.weights[i]
        return net - self.threshold
    
    def compute(self, input):
        net = self.calculateNet(input)
        if net >= 0:
            return 1
        else:
            return 0
