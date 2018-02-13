import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np
import pandas as pd
import tensorflow as tf
import utility.path as upath
import utility.mnist as umnist

def GetDataFrame():
    mnist = umnist.GetDatasets()
    images, labels = mnist.train.next_batch(500)
    images = np.array(images)
    labels = np.array(labels)
    
    return pd.DataFrame(images)
