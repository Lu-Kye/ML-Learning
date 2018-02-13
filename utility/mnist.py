import utility.path as upath
from tensorflow.examples.tutorials.mnist import input_data

def GetDatasets():
    path = upath.GetCurrentAbsPath()
    return input_data.read_data_sets(path + "/../MNIST_Data/data/", one_hot=False)
