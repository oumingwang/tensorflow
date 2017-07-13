#coding:utf8
#线性模型计算图

import os
import tensorflow as tf


#建立绘画
with tf.Graph().as_default():
    #输入占位符
    with tf.name_scope('Input'):
        X = tf.placeholder(tf.float32,name='X')
        Y_true = tf.placeholder(tf.float32,name='Y_true')
    #模型参数变量
    with tf.name_scope('Inference'):
        W = tf.Variable(tf.zeros([1]),name='Weight')
        b = tf.Variable(tf.zeros([1]),name='Biase')

        #inference y = wx + b
        Y_pred = tf.add(tf.multiply(X,W),b)
    with tf.name_scope('Loss'):
        #添加损失节点
        TrainLoss = tf.reduce_mean(tf.pow((Y_true - Y_pred),2))/2
    with tf.name_scope('Train'):
        #训练节点
        Optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
        TrainOp = Optimizer.minimize(TrainLoss)
    with tf.name_scope('Eval'):
        #评估节点
        EvalLoss = tf.reduce_mean(tf.pow((Y_true - Y_pred),2))/2

    #初始化节点
    InitOp = tf.global_variables_initializer()


    print ("计算图写入时间文件，在TensorBoard里面查看")
    #保存计算图
    writer = tf.summary.FileWriter(logdir='logs',graph=tf.get_default_graph())
    writer.close()

    print ("开启回话，运行计算图，训练模型")
    sess = tf.Session()
    sess.run(InitOp)

