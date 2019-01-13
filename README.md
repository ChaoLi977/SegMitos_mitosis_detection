# SegMitos_mitosis_detection
Weakly Supervised Mitosis Detection in Breast Histopathology Images using Concentric Loss
By [Chao Li](https://chaoli977.weebly.com/), [Xinggang Wang](http://www.xinggangw.info/), [Wenyu Liu](http://mclab.eic.hust.edu.cn/MCWebDisplay/PersonDetails.aspx?Name=Wenyu%20Liu), [Longin Jan Latecki](https://cis.temple.edu/~latecki/), [Bo Wang](https://bowang87.weebly.com/) and [Junzhou Huang](http://ranger.uta.edu/~huang/)

Codes for our paper "Weakly Supervised Mitosis Detection in Breast Histopathology Images using Concentric Loss". 

    
### Contents
1. [Requirements: software](#requirements-software)
2. [Requirements: hardware](#requirements-hardware)
3. [Basic steps](#steps)
4. [Data preparation](#data-preparation)

### Requirements: software

We use the deep learning framework Caffe to train the segmentation network. 
The code for data preparation is written by Matlab. While the codes for training the SegMitos network and detecting the mitosis are written by Python.

Our segmentation model is based on FCN work.

### Requirements: hardware

We use a TITAN X GPU with ~12GB memory in our experiments. However, a good GPU with at least 8G of memory suffices.

### Basic steps

1. Install the [Caffe framework](http://caffe.berkeleyvision.org/)
2. Train the SegMitos model based on FCN architecture. 
   python solve.py
3. Deploy the trained model on mitosis images and produce the final detection results.
   


