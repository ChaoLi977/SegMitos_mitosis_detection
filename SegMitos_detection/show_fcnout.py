#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Chao Li
# date:2017/6/16

# show fcn output of mitos evaluation images

import os
import cv2 
import glob
import h5py
import numpy as np
import scipy.io as sio

def show_fcnout(featfolder, dirname):
    # convert the feature of patches to visualized feature map
	fcnfolder = featfolder
	for i in range(len(dirname)):
		filepath = fcnfolder + dirname[i] + '/*.mat' 
		print '%s\n'%(filepath)
		img = glob.glob(filepath)
		n = len(img)
		print 'the number of mat is %d\n'%(n)
		for j in range(n):
			showFCN(fcnfolder, dirname[i], img[j].split('/')[-1])

def showFCN(fcnfolder, dir1, imgname):
	fcn = os.path.join(fcnfolder, dir1, imgname)
	savefolder = '/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/visualFCNTemp/'
	data_dict = sio.loadmat(fcn)
	feat = 255*data_dict['feat'][:]
	f2 = feat
	name = os.path.join(dir1, imgname[0:-4])
	cv2.imwrite(savefolder+name+'.bmp', f2)
	print savefolder+name+'.bmp'
    
if __name__ == '__main__' :
	show_fcnout('/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/temp/feat/')