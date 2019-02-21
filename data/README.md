# Concentric Label

This folder is for preparing mitosis data and generating the random concentric labels.
We use AMIDA13 MITOSIS dataset for example, and other datasets can be processed in a similar way.

## Download the AMIDA13 dataset. 

Now the web of AMIDA13 cannot be accessed, but you can still download the data from TUPAC16 dataset (http://tupac.tue-image.nl/node/3) because the AMIDA13 is a part of TUPAC16 dataset.

The first 12 (01-12) folders are for training, and the next 11 (13-23) folders are for testing.

## Steps to produce the concentric label and perform data augmentation.

a. Run GetRandomRingLabel.m

For generating the random concentric label for full images(sized 2000*2000). The r is randomly chosen from a uniform distribution between 10 and 17 pixels, and the R is randomly 1.5 times to 2.5 times the length of the r.

b. Run crop4imgs.m

For cropping patches from full histopathology images. The size of a patch is 500*500 pixels, and the size of the full image is 2000*2000 pixels. Hence we can crop 16 patches for each full image. 

c. Run crop4imgs_gt.m

For cropping patches from full label images. The size of a patch is 500*500 pixels. Hence we crop 4x4 patches for each full image.  

d. Run PosOrNeg.m

For generating the list of all positive patches. Since we will make more augmentation for positive patches to balance the data.

e. Run augmentData.m

For performing data augmentation on histopathology patches. These augmented patches are used for training the SegMitos model.

f. Run augmentData_gt.m

For performing data augmentation on label image patches. These augmented label patches are used for training the SegMitos model.

g. Run csv2mat.m

For converting the .csv format ground truth to .mat format ground truth. Since we use the .mat format ground truth when calculating the F-value of detection results. 

## Download link of concentric labels
You can download the concentric annotations of three mitosis datasets (2012 MITOSIS dataset, 2014 MITOSIS dataset and AMIDA13 dataset) in Google Drive(https://drive.google.com/file/d/1X2Cbtyi4MSDtDw7kZzwlMMhs5YTMY2Oa/view?usp=sharing) or Baidu Pan(https://pan.baidu.com/s/12uneY7JRfZRac5HwCmNfLw}.



