#coding:utf8
#1.导入python必须的模块，包括了input_data.py用于下载训练测试集等
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import os
import argparse
import sys
from tensorflow.examples.tutorials.mnist import input_data


FlAGS = None
def main():
    with tf.Graph().as_default():
        # Input 输入
        with tf.name_scope('input'):
            X = tf.placeholder(tf.float32, shape=[None, 784], name='X')
            Y_true = tf.placeholder(tf.float32, shape=[None, 10], name='Y_true')
        # inference前向预测训练模型
        with tf.name_scope('Inference'):
            W = tf.Variable(tf.zeros([784, 10]), name='Weight')
            b = tf.Variable(tf.zeros([10]), name='Biase')
            logits = tf.add(tf.matmul(X, W), b)
            # Softmax把Y_pred变成概率分布
            with tf.name_scope("softmax"):
                Y_pred = tf.nn.softmax(logits)

        # Loss：定义损失节点
        with tf.name_scope("TrainLoss"):
            TrainLoss = tf.reduce_mean(-tf.reduce_sum(Y_true * tf.log(Y_pred), axis=1))

        # 定义训练节点
        with tf.name_scope("Train"):
            Optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
            TrainStep = Optimizer.minimize(TrainLoss)

        # 初始化节点
        InitOp = tf.global_variables_initializer()
        print("计算图写入时间文件，在TensorBoard里面查看")
        # 保存计算图
        writer = tf.summary.FileWriter(logdir='logs/mnist_softmax', graph=tf.get_default_graph())
        writer.close()
        print ("开始运行计算图")

        #加载数据
        mnist = input_data.read_data_sets(FLAGS.data_dir,one_hot=True)

        #声明一个交互式会话
        sess = tf.InteractiveSession()
        #初始化所有变量：W b
        sess.run(InitOp)

        for step in range(1000):
            batch_xs,batch_ys = mnist.train.next_batch(100)
            #将当前批次的样本喂给计算图中的输入占位符，启动训练节点开启训练
            train_loss = sess.run([TrainStep,TrainLoss],
                                  feed_dict = {X:batch_xs,Y_true:batch_ys})
            print("train step:",step,"train loss:",train_loss)

if __name__ == '__main__':
    #首先申明一个参数解析器对象
    parser = argparse.ArgumentParser()
    #为参数解析器添加参数：data_dir(指定数据集存放路径)
    parser.add_argument('--data_dir',type=str,
                        default='mnist_data/',#参数默认值
                        help='数据集存放路径')
    FLAGS,unparsed = parser.parse_known_args() #解析参数
    #运行TensorFlow应用
    tf.app.run(main=main, argv=[sys.argv[:1]] + unparsed)