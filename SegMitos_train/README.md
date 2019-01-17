This folder contains the code to train the SegMitos model with the concentric labels.

We use the [FCN](https://github.com/shelhamer/fcn.berkeleyvision.org) framework to train the SegMitos model.

Note that our model uses the old version of Caffe crop layer, which doesn't accept "crop_param" parameter.
Specifically, we use the Caffe of HED. Latest version of Caffe can also be used to train the model as long as adding the "crop param" of crop layers.

Here we use AMIDA13 dataset as an example to show how to train the model. Though in our paper we use the SegMitos-32s
model that has been trained on 2012 MITOSIS dataset to initialize the model, we have also tried the [PASCAL-trained
FCN-32s model](http://dl.caffe.berkeleyvision.org/fcn32s-heavy-pascal.caffemodel) as base model and got a similar result.
