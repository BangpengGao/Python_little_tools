# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:01:38 2018

@author: Lidh
"""
import math
import numpy as np
import tensorflow as tf

class GX_network:
    def __init__(self):
        self.graph=tf.Graph()
    def getActivationFunction(self,act):
        if act==0:
            return None
        if act==1:
            return tf.nn.softplus
        if act==2:
            return tf.nn.softmax
        if act==3:
            return tf.nn.softsign
        if act==4:
            return tf.nn.tanh
        if act==5:
            return tf.nn.sigmoid
        if act==6:
            return tf.nn.relu
        if act==7:
            return tf.nn.relu6
        return None

    def getWayOfTrain(self,way=0):
        if way == 0:
            return tf.train.AdamOptimizer
        else:
            return tf.train.GradientDescentOptimizer

    def getLossFunction(self,lossF=-1):
        if lossF == 0:
            return tf.sqrt(tf.reduce_mean(tf.reduce_sum(tf.square(self.ys-self.predition),reduction_indices=[1])))
        if lossF == 1:
            return -tf.reduce_mean(self.ys * tf.log(tf.clip_by_value(self.predition,1e-8,1.0)))
        return tf.reduce_mean(tf.reduce_sum(tf.square(self.ys-self.predition), reduction_indices=[1]))

    def add_layer(self,inputs,in_size,out_size,activation_function=None):
        w=tf.Variable(tf.random_normal([in_size,out_size]))
        #w=tf.Variable(tf.zeros([in_size,out_size]))
        b=tf.Variable(tf.zeros([1,out_size])+0.1)
        Wx_plus_b=tf.matmul(inputs,w)+b
        if activation_function is None:
            outputs=Wx_plus_b
        else:
            outputs=activation_function(Wx_plus_b)
        return outputs

    def addLayer(self,inputs,in_size,activationFunction):
        """
        create a layyer

        params
        @inputs: the inputs of graph
        @in_size: the dimension of input
        @activationFunction: activate function
        """
        w=tf.Variable(tf.random_normal([in_size,1]))
        b=tf.Variable(tf.zeros([1,1])+0.1)
        Wx_plus_b=tf.matmul(inputs,w)+b
        if activationFunction is None:
            outputs=Wx_plus_b
        else:
            outputs=activationFunction(Wx_plus_b)
        return outputs

    def buildGraphByParamters(self,inputs,in_size,structs):
        """
        create tensorflow graph structure

        params
        @inputs: the inputs of graph
        @in_size: the dimension of input
        @structs: the structure params of graph 
        """
        lastOutput=inputs
        last_ps=in_size
        for i in range(len(structs["layers"])):
            layyer=[]
            for j in range(structs["layers"][i]):
                key = "H"+str(i)+"-"+str(j)
                if key in structs["fun"].keys():
                    if type(layyer).__name__=="list":
                        layyer=self.addLayer(lastOutput,last_ps,self.getActivationFunction(structs["fun"][key]))
                    else:
                        layyer=tf.concat([layyer,self.addLayer(lastOutput,last_ps,self.getActivationFunction(structs["fun"][key]))],1)
            lastOutput=layyer
            last_ps=structs["layers"][i]
        return lastOutput,last_ps

    def predict(self,xData):
        res=self.sess.run(self.predition,feed_dict={self.xs:xData})
        return res

    def createNetwork(self,structs,type=None,lossF=-1,trainWay=0):
        """
        create nerual network

        params
        @ structs: structures of nerual network, include learning rate,layyers,numbers of hidden units in each layyer,dimension of input
        @ type: way of create nerual network
        @ lossF: loss function 
        @ trainWay: way of train 
        """
        tf.reset_default_graph()
        lay_nums=len(structs['layers'])
        if lay_nums<2:
            raise RuntimeError('lar_num Error')
        last_ps=structs['input_ps']
        self.xs=tf.placeholder(tf.float32,[None,last_ps],name='xs')
        last_output=self.xs
        if type==None:
            for struct_layer in structs['layers']:
                layer=self.add_layer(last_output,last_ps,struct_layer['ps'],self.getActivationFunction(struct_layer['act']))
                last_output=layer
                last_ps=struct_layer['ps']
        else:
            last_output,last_ps=self.buildGraphByParamters(last_output,last_ps,structs)
        self.predition=last_output
        self.ys=tf.placeholder(tf.float32,[None,last_ps],name='ys')
        self.loss=self.getLossFunction(lossF)
        self.train_gx=self.getWayOfTrain(trainWay)(structs["learn_rate"]).minimize(self.loss)       
        init=tf.global_variables_initializer()
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)
        self.sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
        self.sess.run(init)

    def save_network(self,base_dir):
        tf.add_to_collection('loss', self.loss)  
        tf.add_to_collection('predition', self.predition)
        tf.add_to_collection('train_gx', self.train_gx)
        saver = tf.train.Saver()
        saver.save(self.sess,save_path=base_dir)

    def load_network(self,base_dir):
        with self.graph.as_default():
            self.saver = tf.train.import_meta_graph(base_dir+'.meta')
        self.sess=tf.Session(graph=self.graph)
        with self.sess.as_default():
            with self.graph.as_default():
                self.saver.restore(self.sess,base_dir)
                self.predition=tf.get_collection('predition')[0]    
                self.loss=tf.get_collection('loss')[0] 
                self.train_gx=tf.get_collection('train_gx')[0] 
                graph = tf.get_default_graph()
                self.xs = graph.get_operation_by_name('xs').outputs[0]
                self.ys = graph.get_operation_by_name('ys').outputs[0]

    def train(self,xData,yData,trainTimes=-1,isPrint=False,minIncrementNums=100,maxTrainTime=10000,minIncrement=0.0000001):
        if trainTimes==-1:
            loss_flag = 0;condition = 0;i = 0
            while condition<minIncrementNums and i<maxTrainTime:
                self.sess.run(self.train_gx,feed_dict={self.xs:xData,self.ys:yData})
                thisLoss = self.sess.run(self.loss,feed_dict={self.xs:xData,self.ys:yData})/100
                if abs(loss_flag - thisLoss) <= minIncrement:
                    condition += 1
                else:
                    condition = 0
                loss_flag = thisLoss
                if isPrint and (i+1)%50 == 0:
                    print('epoch:'+str(i+1)+',error:'+str(thisLoss))
                i+=1
            return self.sess.run(self.loss,feed_dict={self.xs:xData,self.ys:yData})/100
        else:
            for i in range(trainTimes):
                self.sess.run(self.train_gx,feed_dict={self.xs:xData,self.ys:yData})
                if isPrint and (i+1)%50 == 0:
                    print('epoch:'+str(i+1)+',error:'+str(self.sess.run(self.loss,feed_dict={self.xs:xData,self.ys:yData})/100))
            return self.sess.run(self.loss,feed_dict={self.xs:xData,self.ys:yData})/100

    def calClassifiedAccuracy(self,xData,yData):
        y_predict = self.predict(xData)
        if y_predict.shape[1] > 1:
            y_predict = tf.argmax(y_predict, 1)
            if yData.shape[1] > 1:
                yData = tf.argmax(yData, 1)
            else:
                yData = tf.squeeze(yData)
            return np.mean(y_predict==yData)
        else:
            yData = np.squeeze(yData)
            y_predict = np.squeeze(y_predict)
            return np.mean(np.round(y_predict)==yData)

    def calPCC(self,xData,yData):
        y_predict = self.predict(xData)
        y_predict = np.squeeze(y_predict)
        yData = np.squeeze(yData)
        mean_a = np.mean(yData)
        mean_b = np.mean(y_predict)
        pearsNumerator = sum((yData-mean_a)*(y_predict-mean_b))
        pearsDenominator = math.sqrt((sum((yData-mean_a)**2))*(sum((y_predict-mean_b)**2)))
        if pearsDenominator==0.0:
            return 0.0
        return pearsNumerator/pearsDenominator
