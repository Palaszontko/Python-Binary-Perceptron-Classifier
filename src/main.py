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

