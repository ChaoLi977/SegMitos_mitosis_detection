#! usr/bin/env python
# -*- coding: utf-8 -*-

# author: Chao Li
# date:2017/6/16

import os
import cv2
import sys
import time
import numpy as np
import scipy.io as sio

def extract_fcn_amida13_test(model, gpu_id, dirname):
	caffe_root = '/data/lc/hed/'
	sys.path.insert(0, caffe_root + 'python')  #we use hed caffe to test
	import caffe
	caffe.set_mode_gpu()
	caffe.set_device(gpu_id)
	net_model = 'deploy.prototxt'
	net_weights = model
	phase = 'test'

	if  not os.path.isfile(net_weights):
		raise Exception('Please download CaffeNet from Model Zoo before you run this demo')

	# Initialize a network
	net = caffe.Net(net_model, net_weights, caffe.TEST)
	#specify folder
	root_folder = '/data/lc/data/AMIDA13/test_4imgs/4imgs/' # the image patches of AMIDA13
	folder = dirname

	#input_data is Height x Width x Channel x Num
	for t in range(len(folder)):
		start_time = time.time()
		imagedir = os.listdir(root_folder+folder[t])
		imgNum = len(imagedir)
		if not os.path.exists('/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/temp/feat/'+folder[t]):
			os.mkdir('/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/temp/feat/'+folder[t])

		for i in range(imgNum):
			name = imagedir[i]
			name1 = name[0:-4]
			im = cv2.imread(os.path.join(root_folder,folder[t],name))

			h = im.shape[0]
			w = im.shape[1]
			print 'h: %d  w: %d -----------------\n' % (h, w)
			input_data = prepare_image(im)
			net.blobs['data'].data[...] = input_data
			#do forward pass to get scores
			scores = net.forward()
			scores = scores['softmax-out'][0]
			feat = scores[1]   #here is different from matlab code 
			print 'feature shape: '+ str(feat.shape) + '\n'
			print 'extracting feature for %d image\n' % (i+1)
			save_folder = os.path.join('/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/temp/feat/',folder[t])
			sio.savemat(os.path.join(save_folder,name1+'.mat'), {'feat':feat})  
		end_time = time.time()
		print 'process time: %.7f' % (end_time-start_time)


def prepare_image(im):
	meanPixel = [104.00698793, 116.66876762, 122.67891434] #(BGR)
	final_data = np.zeros([1,3,500,500])

	im_data = np.float32(im)  # convert from uint8 to single
	im_data[:,:,0] = im_data[:,:,0] - meanPixel[0]  # subtract mean_data channel 0 (already in W x H x C, BGR)
	im_data[:,:,1] = im_data[:,:,1] - meanPixel[1]  # subtract mean_data channel 1 (already in W x H x C, BGR)
	im_data[:,:,2] = im_data[:,:,2] - meanPixel[2]  # subtract mean_data channel 2 (already in W x H x C, BGR)
	im_data = np.transpose(im_data, [2, 0, 1])  # flip channel to the first dimension
	final_data[0] = im_data
	return final_data

if __name__ == '__main__' :
	extract_fcn_amida13_test('/data/lc/SegMitos/AMIDA13-32s/snapshot/train_iter_90000.caffemodel', 1, '13')


	

