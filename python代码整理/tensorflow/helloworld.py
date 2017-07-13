#coding:utf8
import os
import tensorflow as tf
#tf基本输出
hello = tf.constant('Hello ,TensorFlow!')
sess = tf.Session()
print (sess.run(hello))

#传量操作
a = tf.constant(2)
b = tf.constant(3)
#常量操作
with tf.Session() as sess:
    print ("a=2,b=3")
    print ("常量相加: %i" % sess.run(a+b))
    print ("常量相乘：%i" % sess.run(a*b))

#变量操作

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a,b)
mul = tf.multiply(a,b)

with tf.Session() as sess:
    print("变量相加： %i" % sess.run(add,feed_dict={a:2,b:3}))
    print("变量相乘： %i" % sess.run(mul,feed_dict={a:2,b:3}))


#矩阵相乘
matrix1 = tf.constant([[3.,3.]])
matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1,matrix2)

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
