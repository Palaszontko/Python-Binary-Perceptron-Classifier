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

    def setRandomWeightsAndthreshold(self, weightsSize : int):
        'Set random weights and threshold'
        self.weights = [round(random.uniform(-5,5), 5) for _ in range(weightsSize)]
        self.threshold = round(random.uniform(-5,5), 5)
        
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
    
    def learn(self, input, decision, y):
        'Delta rule'
        for i in range(len(self.weights)):
            self.weights[i] = round(self.weights[i] + (decision - y) * self.alpha * input[i], 7)

        self.threshold = round(self.threshold - (decision - y) * self.alpha, 7)

    def loadCsv(self, path : str) -> list:
        samples = []
        try:
            with open(path, 'r') as f:   
                data = f.readlines()

                for line in data:
                    if line == '' or line == '\n':
                        continue
                    line = line.strip().split(';')
                    samples.append(Sample([float(x) for x in line[:-1]], line[-1]))

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        return samples

