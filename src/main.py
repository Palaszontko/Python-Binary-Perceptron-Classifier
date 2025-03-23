class Sample:
    def __init__(self, weights : list, dataTag : str):
        self.weights = weights
        self.dataTag = dataTag

    def __str__(self):
        return f"Data Tag: {self.dataTag}, Weights: {self.weights}"
    
