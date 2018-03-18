#basic tensorflow program that adds one to a variable and uses a loop to run the addition ten times.
#https://learningtensorflow.com/lesson2/

import tensorflow as tf

x = tf.constant([35, 40], name='x')
y = tf.Variable(x + 5, name='y')

z = tf.Variable(0, name='x')

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))

    for i in range(5):
        z = z + 1
        print(session.run(z))

