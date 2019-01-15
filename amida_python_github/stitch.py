#! /usr/bin/env python 
# -*- coding: utf-8 -*-

import os 
import cv2
import glob
import numpy as np
import scipy.io as sio
from show_fcnout import show_fcnout

def stitch(featfolder, savefolder, dirname):
	root_folder = '/data/lc/data/AMIDA13/mitoses_ground_truth/'
	show_fcnout(featfolder, dirname)
	for i in range(len(dirname)):
		filepath = root_folder + dirname[i] + '/*.csv'
		img = glob.glob(filepath)
		n = len(img)
		for j in range(n):
			imgname = img[j].split('/')[-1]
			stitchPatch(root_folder, dirname[i], imgname, featfolder, savefolder)
			stitchPatchImg(root_folder, dirname[i], imgname,savefolder)

def stitchPatch(root_folder, dir1, imgname, featfolder, savefolder):  
    # stitch the features of patches to feature of full image
	name = os.path.join(dir1, imgname)
	print 'name:%s\n' %(name)
	Im = os.path.join(featfolder, name[0:-4])
	I = [None]*16
	for i in range(9):
		dict1 = sio.loadmat(Im+'_0'+str(i+1)+'.mat')
		I[i] = dict1['feat']
	for i in range(9,16):
		dict2 = sio.loadmat(Im+'_'+str(i+1)+'.mat')
		I[i] = dict2['feat']
	A = np.zeros((4*500,4*500))
	for row in range(4):
		for col in range(4):
			A[row*500:(row+1)*500,col*500:(col+1)*500] = I[row*4+col]
	sio.savemat(savefolder+name[0:-4], {'A':np.mat(A)})

def stitchPatchImg(root_folder, dir1, imgname, savefolder):
    # stitch the visual feature map of patches to feature map of full image
	name = os.path.join(dir1, imgname[0:-4])
	imgfolder = '/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/visualFCNTemp/'
	Im = imgfolder + name
	I = [None]*16
	for i in range(9):
		patch = cv2.imread(Im+'_0'+str(i+1)+'.bmp')
		I[i] = patch
	for i in range(9,16):
		patch = cv2.imread(Im+'_'+str(i+1)+'.bmp')
		I[i] = patch
	A = np.zeros((4*500,4*500,3))
	for row in range(4):
		for col in range(4):
			A[row*500:(row+1)*500,col*500:(col+1)*500] = I[row*4+col]

	savefolder = savefolder[0:-9]+'fullImg/'
	cv2.imwrite(savefolder+name+'.jpg', A)
	print savefolder + name + '.jpg'