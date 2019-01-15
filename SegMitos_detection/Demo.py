#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Chao Li
# date:2017/6/16

# The Demo for mitosis detection

import os 
import re
import glob
import numpy as np

import cal_F
import stitch
import getDETCentroid
import extract_fcn_amida13_test

def demo():
	model_folder = '/data/lc/SegMitos/AMIDA13-32s/snapshot'  # the model files path
	model_file = os.path.join(model_folder, 'xx.caffemodel')
	output_folder = '/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/'	
	dirname = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'] #test set
	if not os.path.exists(output_folder):
		os.mkdir(output_folder)
	f,p,r,area,score = test_model(model_file, output_folder, dirname)
	print('%s:F:%f p:%f r:%f area:%f score:%f\n' % (model_file,f,p,r,area,score))

def test_model(model, output_root,dirname):
	gpu_id = 1
	extract_fcn_amida13_test.extract_fcn_amida13_test(model, gpu_id, dirname)
	model_name = re.split('/', model) 
	ind = re.findall('(?<=\w{11})\d+', model_name[6])
	folder = os.path.join(output_root,ind[0])
	if not os.path.exists(folder):
		os.mkdir(folder)
	feat_temp='/data/lc/data/AMIDA13/SegMitos-out/AMIDA13/temp/feat/'

	fullFeat_f = os.path.join(folder, 'fullFeat/')  # segmentation map of full images
	fullImg_f = os.path.join(folder, 'fullImg/') # visual segmentation map
	cen_f = os.path.join(folder, 'centroid_tune/') # folder of predicted mitosis centroids

	if not os.path.exists(fullFeat_f):
		os.mkdir(fullFeat_f)
	if not os.path.exists(fullImg_f):
		os.mkdir(fullImg_f)
	if not os.path.exists(cen_f):
		os.mkdir(cen_f)
	for i in range(len(dirname)):
		if not os.path.exists(os.path.join(fullFeat_f,dirname[i])):
			os.mkdir(os.path.join(fullFeat_f,dirname[i]))
		if not os.path.exists(os.path.join(fullImg_f,dirname[i])):
			os.mkdir(os.path.join(fullImg_f,dirname[i]))
		if not os.path.exists(os.path.join(cen_f,dirname[i])):
			os.mkdir(os.path.join(cen_f,dirname[i]))

	stitch.stitch(feat_temp,fullFeat_f, dirname)
	getDETCentroid.getDETCentroid(fullFeat_f,cen_f, dirname)
	fmax, precision, recall, area, score=cal_F.cal_F(cen_f, dirname) #

	return fmax, precision, recall, area, score

if __name__ == '__main__':
	demo()
