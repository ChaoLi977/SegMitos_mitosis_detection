## Deploy the trained model to testing images of mitosis dataset

```bash
python Demo.py
```

The image paths need to be changed to your directories. 
We use AMIDA13 dataset to show the processing of mitosis detection by our method. But you can change the related data paths to other datasets, e.g. 2012 MITOSIS dataset, 2014 MITOSIS dataset.

Considering the GPU memory, we run the SegMitos model on image patches sized 500*500 pixels and then piece together the patch results.
For a faster detection speed, the SegMiots model can be applied directly to the full image at the cost of more memory.
