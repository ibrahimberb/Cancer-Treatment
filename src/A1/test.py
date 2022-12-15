# check if tensorflow uses GPU
from tensorflow.python.client import device_lib
import tensorflow as tf


print(tf.__version__)

print(device_lib.list_local_devices())
