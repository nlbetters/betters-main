# Artificial Neural Network (ANN)

## How it started 
This project started as an assignment for a class (ENEE301), but after I made it, I was intrigued by the possibilities. We built the original network and trained it using the MNIST dataset, which has 60,000 handwritten numbers for training. After that, I started experimenting with different parameters, network sizes, and weight initializations to see how they affected overall accuracy.

## Future Plans
Even though the original MNIST network works, I want to take this project way further. The main idea is to train a second neural network using images of human faces showing different emotions. Paired with a camera, the ANN would ideally be able to recognize certain visual patterns and predict the user’s emotion in real time.

Once I get that part working, the next goal is to run everything on a Raspberry Pi with a camera module so it becomes a standalone system. After that, I want to add some “flare,” like a small UI or LED indicators that react to the detected emotion, and possibly optimize the model so it can run smoothly on lightweight hardware.

**Note:** The MNIST dataset isn’t included in this repository because the files are too large for GitHub’s upload limit, but the full dataset is online, and fairly easy to download and use.