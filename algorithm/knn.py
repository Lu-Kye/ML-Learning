import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

arr = np.ndarray(shape=[2, 2], dtype=int, buffer=np.array([0,3,1,2]))
print("2d_arr:" + str(arr))
arr_min = np.amin(arr, axis=0)
print("first_axis:" + str(arr_min))
arr_min = np.amin(arr, axis=1)
print("second_axis:" + str(arr_min))