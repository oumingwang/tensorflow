#coding:utf8
#导入mnist数据集
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("mnist_data/",one_hot=True)


#控制训练集数量

Xtrain,Ytrain = mnist.train.next_batch(5000)
Xtest,Ytest = mnist.test.next_batch(200)

print ("Xtrian.shape",Xtrain.shape,'Xtest.shape',Xtest.shape)
print ("Ytrian.shape",Ytrain.shape,'Ytest.shape',Ytest.shape)

#计算图输入占位符
xtrain = tf.placeholder('float',[None,784])
xtest = tf.placeholder('float',[784])


#计算L1距离
distance = tf.reduce_sum(tf.abs(tf.add(xtrain,tf.negative(xtest))),axis=1)

pred = tf.arg_min(distance,0)

#accuracy计算准确度
accuracy = 0


#初始化节点，会话

init = tf.global_variables_initializer()
with tf.Session() as sess :
    sess.run(init)
    Ntest = len(Xtest)
    #遍历测试集，求出对测试集的预测结果
    for i in range(Ntest):
        nn_index = sess.run(pred,feed_dict = {xtrain : Xtrain ,xtest : Xtest[i,:]})
        pred_class_label = np.argmax(Ytrain[nn_index])
        true_class_label = np.argmax(Ytest[i])
        print ("Test",i,'Predicted',pred_class_label,
               'True class label',true_class_label)

        if pred_class_label == true_class_label:
            accuracy += 1
    print ('Done!')
    accuracy /= Ntest
    print ("Accuracy",accuracy)