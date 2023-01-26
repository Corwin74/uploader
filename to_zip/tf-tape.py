import tensorflow as tf
import random
import numpy as np

# Loss function
def loss(real_y, pred_y):
    return tf.abs(real_y - pred_y)

# Training data
x_train = np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.asarray([i*10+5 for i in x_train]) # y = 10x+5

# Trainable variables
a = tf.Variable(random.random(), trainable=True)
b = tf.Variable(random.random(), trainable=True)

# Step function
def step(real_x, real_y):
    with tf.GradientTape(persistent=True) as tape:
        # Make prediction
        pred_y = a * real_x + b
        # Calculate loss
        reg_loss = loss(real_y, pred_y)
    
    # Calculate gradients
    a_gradients, b_gradients = tape.gradient(reg_loss, (a, b))

    # Update variables
    a.assign_sub(a_gradients * 0.001)
    b.assign_sub(b_gradients * 0.001)

# Training loop
for _ in range(10000):
    step(x_train, y_train)

print(f'y ≈ {a.numpy()}x + {b.numpy()}')