import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('/tmp/data/', one_hot = True)

nodesHL1 = 500; nodesHL2 = 500; nodesHL3 = 500;
classes = 10
batchSize = 100

x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')

def neuralNetworkMode(data):
	hiddenLayer1 = {'weights': tf.Variable(tf.random_normal([]))}
