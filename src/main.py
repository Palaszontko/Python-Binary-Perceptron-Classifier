import random
import sys

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

    def start(self):
        trainData = self.loadCsv(self.trainDataPath)
        testData = self.loadCsv(self.testDataPath)
        self.setRandomWeightsAndthreshold(len(trainData[0].weights))

        # Map tags to values (0,1)
        outputMap_tagToValue = self.mapTagsToValues([sample.dataTag for sample in trainData])
        outputMap_valueToTag = {v: k for k, v in outputMap_tagToValue.items()}

        # Shuffle train data
        random.shuffle(trainData)

        for sample in trainData:
            y = self.compute(sample.weights)
            self.learn(sample.weights, outputMap_tagToValue[sample.dataTag], y)

        correct = {outputMap_valueToTag[0]: 0, outputMap_valueToTag[1]: 0}
        all = 0

        for sample in testData:
            y = self.compute(sample.weights)
            if y == outputMap_tagToValue[sample.dataTag]: 
                correct[outputMap_valueToTag[y]] += 1
            all += 1

        print(f"Accuracy: {sum(correct.values())/all * 100}%")

        class_counts = {tag: sum(1 for s in testData if s.dataTag == tag) for tag in outputMap_tagToValue.keys()}
                
        for key, value in correct.items():
            print(f"Accuracy for {key}: {value/(class_counts[key]) * 100}%")
            if value/(all/2) != 1:
                print("Perceptron isn't perfect")
                print("Do you want to continue learning? (y/n)")
                answer = input()
                if answer == 'y':
                    self.start()
                else:
                    break
        
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

def main():
    alpha = input("Enter alpha: ")
    trainDataPath = input("Enter train data path: ")
    testDataPath = input("Enter test data path: ")

    alpha = 0.1
    trainDataPath = "data/trainData.csv"
    testDataPath = "data/testData.csv"

    perceptron = Perceptron(float(alpha), 0, trainDataPath, testDataPath)
    perceptron.start()


    
if __name__ == "__main__":
    main()