# Perceptron Classifier

Python implementation of a binary classifier using single-layer perceptron with delta rule learning.

**Features**

- Δelta rule weight updates
- Automatic threshold adjustment
- Interactive prediction mode
- Class-specific accuracy reports
- Continuous learning option

**Usage**

1. CSV format: feature1;feature2;...;class
2. Exactly 2 unique class tags required
3. Run: python perceptron.py

**Data Requirements**

- Training/test files: data/trainData.csv, data/testData.csv
- Example row: 6.8;3.2;5.9;2.3;ClassA

**Key Parameters**

- Learning rate (alpha): 0.1 (hardcoded)
- Random weights/threshold: [-5,5] range

**Output**
Accuracy: 92.5%
Accuracy for ClassA: 95.2%
Accuracy for ClassB: 89.3%

**Interactive Commands**

- Test samples: 0.8;1.5 format
- Exit: exit
- Retrain: y after imperfect results
