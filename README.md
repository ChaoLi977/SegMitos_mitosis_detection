# SegMitos_mitosis_detection
Weakly Supervised Mitosis Detection in Breast Histopathology Images using Concentric Loss
By [Chao Li](https://chaoli977.weebly.com/), [Xinggang Wang](http://www.xinggangw.info/), [Wenyu Liu](http://mclab.eic.hust.edu.cn/MCWebDisplay/PersonDetails.aspx?Name=Wenyu%20Liu), [Longin Jan Latecki](https://cis.temple.edu/~latecki/), [Bo Wang](https://bowang87.weebly.com/) and [Junzhou Huang](http://ranger.uta.edu/~huang/)

Codes for our paper "Weakly Supervised Mitosis Detection in Breast Histopathology Images using Concentric Loss". 

    
### Contents
1. [Requirements: software](#requirements-software)
2. [Requirements: hardware](#requirements-hardware)
3. [Basic steps](#basic-steps)


### Requirements: software

We use the deep learning framework Caffe to train the segmentation network. 
The code for data preparation is written by Matlab, while the codes for training the SegMitos network and detecting the mitosis is written by Python.


### Requirements: hardware

We use a TITAN X GPU with ~12GB memory in our experiments. However, a good GPU with at least 8G of memory suffices.

### Basic steps

1. Install the [Caffe framework](http://caffe.berkeleyvision.org/). Note that our model uses the old version of Caffe crop layer, which doesn't have "crop_param" parameter. Specifically, we use the Caffe of [HED](https://github.com/s9xie/hed). Latest version of Caffe should also work, but the parameters of crop layer need to be added.

2. Prepare data and produce the concentric labels. Please see data/README.md for more details.

2. Train the SegMitos model: 
   ```bash
   cd SegMitos_train/AMIDA13-fcn32s
   python solve.py
   ```
3. Deploy the trained model on the testing images of mitosis dataset.
   
   ```bash
   cd SegMitos_detection/
   python Demo.py
   ```


