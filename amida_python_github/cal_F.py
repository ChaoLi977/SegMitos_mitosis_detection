#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import math
import numpy as np
import scipy.io as sio


def cal_F(folder_cen, dirname):
	'''adjust parameter, e.g. areath'''
	precision = np.zeros((1000,1))
	recall = np.zeros((1000,1))
	F = np.zeros((1000,1))
	scoreTh = np.zeros((1000,1))
	output = os.path.join(folder_cen, 'F-score.txt')
	fid = open(output, 'w')
	for i in range(300,1000,5):
		areaTh=i+1
		precision[i], recall[i], F[i], scoreTh[i] = cal_F1(areaTh,folder_cen, dirname)
		print 'areaTh=%d, scoreTh=%f\t precision:%f\t recall:%f\t F=%f\n' % (areaTh,scoreTh[i],precision[i],recall[i],F[i])
		fid.write('areaTh=%d, scoreTh=%f\t precision:%f\t recall:%f\t F=%f\n' % (areaTh,scoreTh[i],precision[i],recall[i],F[i]))
	f_max = max(F)
	ind = F.argmax()
	p_max = precision[ind]
	r_max = recall[ind]
	s_max = scoreTh[ind]
	a_max = ind
	fid.write('max-F:%f\t  areaTh=%f,\t scoreTh=%f,\t p=%f,\t r=%f\n' % (f_max,a_max,s_max,p_max, r_max))
	fid.close()
	return f_max,p_max,r_max,a_max,s_max


def cal_F1(areaTh, folder_cen, dirname):
	'''compute the P,R,F'''
	detfolder = folder_cen
    sum_gt = 0
	Label, Score = np.zeros((0,1)), np.zeros((0,1))
	for i in range(len(dirname)):
		filepath = detfolder + dirname[i] + '/*.mat'  
		img = glob.glob(filepath)
		n = len(img)
		for j in range(n):
			label, score, N_gt = calPr(img[j], areaTh)
			Label = np.vstack((Label, label))
			Score = np.vstack((Score,score))
            sum_gt = sum_gt+N_gt
	s = np.squeeze(np.argsort(Score,axis=0))
	Score_s = Score[s]
	Label_s = Label[s] #Label and Label_s shape = [n,1]
	Label_s[Label_s==0] = -1
	tp = sum(Label_s==1)
	n_det = Label_s.shape[0]
	fn = sum_gt-tp #   test set:533, the number of true mitosis in test set
	Label_s = np.concatenate((np.ones((fn[0],1)),Label_s),axis=0)
	Score_s = np.concatenate((-np.ones((fn[0],1)),Score_s),axis=0)
	f=np.zeros((100,1),dtype=np.float32)
	r_=np.zeros((100,1),dtype=np.float32)
	p_=np.zeros((100,1),dtype=np.float32)
	for i in range(30,90):  # filter detections by using score
		scoreTh = i/100.0
		pos = Score_s>scoreTh
		tp = sum(Label_s*pos==1)
		tp = float(sum(tp))
		r_[i] = tp/sum(Label_s==1)
		p_[i] = tp/sum(pos)
		f[i] = 2.0*r_[i]*p_[i]/(r_[i]+p_[i])
		if tp==0:
			f[i]=0
	F = np.max(f)
	num = f.argmax()
	R = r_[num]
	P = p_[num]
	scoreTh = num/100.0
	return P,R,F,scoreTh


def calPr(det, areaTh):   
    '''filter the detections by using area threshold'''
	data= sio.loadmat(det)
	area, score, centroid = data['area'], data['score'], data['centroid']
	if areaTh>0:  # filter by area
		ind = np.squeeze(area>areaTh)
		score = score[ind] #rank = 2
		area = area[ind]    
		centroid = centroid[ind] 
	score = score.reshape((-1,1))
	res = centroid.reshape((-1,2))  #res.shape = (n,2)
	res = res.astype(np.int64)
	gtfolder = '/data/lc/data/AMIDA13/GroundTruthMat/'  # the ground truth in .mat format
	gt = gtfolder + det[-9:-4] + '.mat'
	gt_datadict = sio.loadmat(gt)
	gt_centroid = gt_datadict['centroid'] #gt_centroid.shape = (n,2)
	gt_centroid = gt_centroid.astype(np.int64)
    N_gt = gt_centroid.shape[0]
	label = np.zeros((res.shape[0],1))   
	for i in range(res.shape[0]):
		for j in range(gt_centroid.shape[0]):
			if math.sqrt((res[i,0]-gt_centroid[j,0])**2 + (res[i,1]-gt_centroid[j,1])**2) < 32.5:
				label[i] = 1
				gt_centroid = np.delete(gt_centroid,j,0)#delete the detected mitosis
				break
	return label, score, N_gt