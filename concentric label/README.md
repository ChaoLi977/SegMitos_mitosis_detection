# Concentric Label

This folder is for preparing mitosis data and generating the random concentric labels.
We use AMIDA13 MITOSIS dataset for example, other datasets can be processed in a similar way.

## Download the AMIDA13 dataset. 

Now the web of AMIDA13 cannot be accessed, but you can still download the data from TUPAC16 dataset  https://mitos-atypia-14.grand-challenge.org/Donwload/)

The first 12 (01-12) folders are for training, and the next 11 (13-23) folders are for testing.

## Steps to produce the concentric label and perform data augmentation.

a. Run GetRandomRingLabel.m

For generating the random concentric label for full images(sized 2000*2000). The r is randomly chosen from a uniform distribution between 10 and 17 pixels, and the R is randomly 1.5 times to 2.5 times the length of the r.

b. Run crop4imgs.m

For cropping patches from full histopathology images. The size of a patch is 500*500 pixels. Hence we crop 4x4 patches for each full image. 

c. Run crop4imgs_gt.m

For cropping patches from full label images. The size of a patch is 500*500 pixels. Hence we crop 4x4 patches for each full image.  

d. Run PosOrNeg.m

For generating the list of all positive patches. Since we will make more augmentation for positive patch to balance the data.

e. Run augmentData.m

For performing data augmentation on histopathology patches.

f. Run augmentData_gt.m

For performing data augmentation on label image patches. 



