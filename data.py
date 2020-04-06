import numpy as np
import random as rand

# class to represetn data
class Data:

    #__init__ is the constructor of this class
    # 'self' is 'this'
    def __init__(self, n, d):
        # n: number of data points
        # d: dimension of x
        # this function should create a list of n data points (x, y) 
        #           where x has d attributes 
        

        # to create a single data point you could do soemthing like x = [rand.randint(0, 1) for _ in range(d)]
        # then add all those data points with their labels to self.data
        self.data = []

class Learner:

    def __init__(self, data):
        # splits data into two halves by yhe middle index
        # // is division that rounds down to an int
        # list[a:b] is all list elements from index a to b, if a or b is left empty they are treated as either 0 or len(list)
        self.train_data = data[:len(data)//2]
        self.test_data = data[len(data)//2 + 1:]

    def algorithm1(self):
        # This should be your attempt at learning learning the data.
        data = self.train_data
        n = len(data)
        x0, y0 = data[0]
        d = len(x0)

    def test(self, w):
        # w is the weight vector learned from training
        # dont change this code
        training_error = 0.0
        for x, y in self.train_data:
            training_error += sum([(y - w[k]*x[k])**2 for k in range(len(x))])
        training_error /= float(len(self.train_data))
        print('training error:', training_error)

        testing_error = 0.0
        for x, y in self.test_data:
            testing_error += sum([(y - w[k]*x[k])**2 for k in range(len(x))])
        testing_error /= float(len(self.test_data))
        print('testing error:', testing_error)



        
