import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from ClassNN import NeuralNetwork

# Import the MNIST training data
data_file = open("path to mnist_train_100.csv", 'r')
data_list = data_file.readlines()
data_file.close()

# Display the first image from the dataset
all_values = data_list[1].split(',')
image_array = np.asfarray(all_values[1:]).reshape((28, 28))
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.show()

# Prepare the input by converting pixel values from 0-255 to 0.01-1.0
scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
print(scaled_input)

# Define the input, hidden, and output nodes
input_nodes = 784
hidden_nodes = 100
output_nodes = 10

# Define the learning rate
learning_rate = 0.3

# Create an instance of the Neural Network
Neural_Network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# Load the training data
training_data_file = open("path to mnist_train_100.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# # Train the neural network
# for record in training_data_list:
#     # Split the record by commas
#     all_values = record.split(',')
#     # Scale and shift the inputs
#     inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
#     # Create target output values (all 0.01, except the correct label which is 0.99)
#     targets = np.zeros(output_nodes) + 0.01
#     targets[int(all_values[0])] = 0.99
#     # Train the neural network
#     Neural_Network.train(inputs, targets)

# Load the test data
test_data_file = open("path to mnist_test_10.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# Test the neural network
scorecard = []
for record in test_data_list:
    all_values = record.split(',')
    # Correct label is the first value
    correct_label = int(all_values[0])
    print(correct_label, "Correct Label")
    # Scale and shift the inputs
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # Query the network
    outputs = Neural_Network.query(inputs)
    label = np.argmax(outputs)
    print(label, "Network's Answer")
    # Append correct/incorrect to the scorecard
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)

# Perform multiple epochs of training
epochs = 2
for e in range(epochs):
    for record in training_data_list:
        all_values = record.split(',')
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        Neural_Network.train(inputs, targets)

# Process an external image for testing
img = Image.open("path to mnist_train_2.png","r").convert('L')
img = img.resize((28, 28))
img_array = np.array(img)
img_data = 255.0 - img_array.reshape(784)
img_data = (img_data / 255.0 * 0.99) + 0.01

plt.imshow(img_array, cmap='Greys', interpolation='None')
plt.show()

Neural_Network.query(img_data)
# print(Neural_Network.query(img_data))
print('%')
print('%')
print('%')
print(f'The Neural Network thinks your number is a:', np.argmax(Neural_Network.query(img_data)))