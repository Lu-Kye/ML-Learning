import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

import utility.path as upath

def GetDataFrame():
    path = upath.GetCurrentAbsPath()
    mnist = input_data.read_data_sets(path + "/../MNIST_Data/data/", one_hot=False)
    
    images, labels = mnist.train.next_batch(500)
    images = np.array(images)
    labels = np.array(labels)
    
    return pd.DataFrame(images)
