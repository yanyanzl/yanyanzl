
# Basic Terms for Tensorflow, AI, Machine Learning


### Vector:
    
- A vector is a quantity or phenomenon that has two independent properties: magnitude and direction. The term also denotes the mathematical or geometrical representation of such a quantity. Examples of vectors in nature are velocity, momentum, force, electromagnetic fields and weight.

### The tf.keras.datasets
    - tf.keras.datasets module provide a few toy datasets (already-vectorized, in Numpy format) that can be used for debugging a model or creating simple code examples.
    - If you are looking for larger & more useful ready-to-use datasets, take a look at TensorFlow Datasets.
    - https://github.com/tensorflow/datasets
    
### DAG (directed acyclic graph) : 
    - A directed acyclic graph is a directed graph that has no cycles. 
    - A vertex v of a directed graph is said to be reachable from another vertex u when there exists a path that starts at u and ends at v. 
    - As a special case, every vertex is considered to be reachable from itself (by a path with zero edges).

### Dense Layer:
- Dense Layeris simple layer of neurons in which each neuron receives input from all the neurons of previous layer, thus called as dense. Dense Layer is used to classify image based on output from convolutional layers. Working of single neuron.

### CNN (Convolutional Neural Network)

![CNN](images/cnn.jpg "cnn")
- image is 2-dimensional array of pixels. Any image can be classified based on it’s features. Scikit-learn algorithms like SVM, decision-tree, Random-Forest, etc which are good at solving classification problem, fail to extract appropriate features from the image.

- That’s where Convolutional Neural Network comes into the picture. CNN is combination of Convolutional Layers and Neural Network.

- Basically any Neural Network which is used for image processing, consist of following layers -
    - Input layer, Convolutional Layer, Pooling Layer, Dense Layer.

- Convolution is nothing but a filter which is applied on image to extract feature from it. 
- We will use such different convolutions to extract different features like edges, high-lighted patterns from the image.

- They have applications in:
    - image and video recognition,
    - recommender systems,
    - image classification,
    - image segmentation,
    - medical image analysis,
    - natural language processing,
    - brain–computer interfaces,
    - financial time series.



### Computer Vision 
- Computer Vision is a field of computer science that focuses on enabling computers to identify and understand objects and people in images and videos.
- Computer vision is an interdisciplinary field that deals with how computers can be made to gain high-level understanding from digital images or videos. From the perspective of engineering, it seeks to automate tasks that the human visual system can do.[5][6][7] "Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images. It involves the development of a theoretical and algorithmic basis to achieve automatic visual understanding."[8] As a scientific discipline, computer vision is concerned with the theory behind artificial systems that extract information from images. The image data can take many forms, such as video sequences, views from multiple cameras, or multi-dimensional data from a medical scanner.[9] As a technological discipline, computer vision seeks to apply its theories and models for the construction of computer vision systems. Machine vision refers to a systems engineering discipline, especially in the context of factory automation, In more recent times the terms computer vision and machine vision have converged to a greater degree

### What are graphs?
    - In the previous three guides, you ran TensorFlow eagerly. This means TensorFlow operations are executed by Python, operation by operation, and return results back to Python.
    
    - While eager execution has several unique advantages, graph execution enables portability outside Python and tends to offer better performance. Graph execution means that tensor computations are executed as a TensorFlow graph, sometimes referred to as a tf.Graph or simply a "graph."
    
    - Graphs are data structures that contain a set of tf.Operation objects, which represent units of computation; and tf.Tensor objects, which represent the units of data that flow between operations. They are defined in a tf.Graph context. Since these graphs are data structures, they can be saved, run, and restored all without the original Python code.
    
    - This is what a TensorFlow graph representing a two-layer neural network looks like when visualized in TensorBoard:
    
    
    
    
    
    
    