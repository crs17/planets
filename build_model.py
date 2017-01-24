import tensorflow as tf

import dataset


data = dataset.PlanetData()

batch_size = 10
planet_count = 1


def fill_feed_dict():


    return

with tf.Graph().as_default():

    time_ph = tf.placeholder(tf.float32, shape=(batch_size, 1))
    ra_ph = tf.placeholder(tf.float32, shape=(batch_size, planet_count))
    dec_ph = tf.placeholder(tf.float32, shape=(batch_size, planet_count))
