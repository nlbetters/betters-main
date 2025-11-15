import numpy as np
from scipy.special import expit

class NeuralNetwork:

    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        #define the input, hidden, and output layer sizes
        self.inodes = input_size
        self.hnodes = hidden_size
        self.onodes = output_size

        #define the learning rate
        self.lr = learning_rate

        #define the weight matrices
        self.wih = np.random.normal(0.0, pow(self.inodes, -0.5),
            (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.hnodes, -0.5),
            (self.onodes, self.hnodes))

        #define the activation function
        self.activation_function = lambda x: expit(x)

        pass

        #Train the Neural Network
    def train(self, input_list, targets_list):
            #convert the input list to a 2d array
            inputs = np.array(input_list, ndmin=2).T
            targets = np.array(targets_list, ndmin=2).T

            #calculate the signals into a hidden layer
            hidden_inputs = np.dot(self.wih, inputs)
            #Calculate the signals emerging from the hidden layer
            hidden_outputs = self.activation_function(hidden_inputs)
            #Calculate signals into final output layer
            final_inputs = np.dot(self.who, hidden_outputs)
            #Calculate the signals emerging from the final output layer
            final_outputs = self.activation_function(final_inputs)

            #Output layer is (target - actual)
            output_errors = targets - final_outputs
            #Hidden layer error is the output_errors, split by weights, Recombined at hidden nodes
            hidden_errors = np.dot(self.who.T, output_errors)

            #Update the weights for the links between the hidden and output layers
            self.who += self.lr * np.dot(output_errors * final_outputs * (1.0 - final_outputs), hidden_outputs.T)

            #update the weights for the links between the inputs and hidden layers
            self.wih += self.lr * np.dot(hidden_errors * hidden_outputs * (1.0 - hidden_outputs), inputs.T)

            pass

        #query the neural network
    def query(self, inputs_list):
            #conver the inputs into a 2d array
            inputs = np.array(inputs_list, ndmin=2).T
            #calculate signals into hidden layers
            hidden_inputs = np.dot(self.wih, inputs)
            #calculate the signals emerging from hidden layers
            hidden_outputs = self.activation_function(hidden_inputs)
            #calculate signals into final output layer
            final_inputs = np.dot(self.who, hidden_outputs)
            #calculate the signals emerging from the final output layer
            final_outputs = self.activation_function(final_inputs)

            return final_outputs
