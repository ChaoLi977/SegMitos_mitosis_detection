#! usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
import sys
import glob
import time
import scipy
import cPickle
import numpy as np
import scipy.io as sio
from skimage.filters import threshold_otsu
from skimage.measure import label


def matlab_style_gauss2D(shape=(3,3),sigma=0.5):
	"""
	2D gaussian mask - should give the same result as MATLAB's
	fspecial('gaussian',[shape],[sigma])
	"""
	m,n = [(ss-1.)/2. for ss in shape]
	y,x = np.ogrid[-m:m+1,-n:n+1]
	h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
	h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
	sumh = h.sum()
	if sumh != 0:
		h /= sumh
	return h

def getDETCentroid(featfolder, savefolder,dirname):
	path = featfolder
	for i in range(len(dirname)):
		filepath = path + dirname[i] + '/*.mat'
		fcn = glob.glob(filepath)
		n = len(fcn)
		for j in range(n):
			compCentroid_detect1(fcn[j],savefolder)
		#os.remove(glob.glob(path+dirname[i]+'/*'))


def compCentroid_detect1(fcn, savefolder):
	data_dict = sio.loadmat(fcn)
	f = matlab_style_gauss2D((10,10),0.25)
	A = cv2.filter2D(data_dict['A'], -1, f)

	level = threshold_otsu(A) #otsu threshold of image
	bw = A > level #binary image
	L,num = label(bw,8,return_num=True) #label  the segmented blobs
	#import pdb;pdb.set_trace()
	plot_x = np.zeros((num, 1)) # location of centroid
	plot_y = np.zeros((num, 1))

	sum_x = np.zeros((num, 1))
	sum_y = np.zeros((num, 1))
	area = np.zeros((num, 1))
	score = np.zeros((num, 1))

	height,width = bw.shape[0], bw.shape[1]
	for i in range(height):
		for j in range(width):
			if L[i,j] != 0:
				N = L[i,j]
				sum_x[N-1] = sum_x[N-1]+i*A[i,j]
				sum_y[N-1] = sum_y[N-1]+j*A[i,j]
				area[N-1] = area[N-1] + 1
				score[N-1] = score[N-1] + A[i,j]

	plot_x = np.around(sum_x*1.0/score)
	plot_y = np.around(sum_y*1.0/score)
	score = score*1.0/area
	centroid = np.zeros((num,2))
	for row in range(num):
		centroid[row,0] = plot_x[row,0]
		centroid[row,1] = plot_y[row,0]
	#centroid = np.mat(centroid)
	savefile = savefolder + fcn[-9:]
	sio.savemat(savefile,{'centroid':centroid, 'area':area, 'score':score})


