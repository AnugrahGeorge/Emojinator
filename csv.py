Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from scipy.misc import imread
import numpy as np
import pandas as pd
import os
root = './gestures' # or ‘./test’ depending on for which the CSV is being created

# go through each directory in the root folder given above
for directory, subdirectories, files in os.walk(root):
# go through each file in that directory
    for file in files:
    # read the image file and extract its pixels
        print(file)
        im = imread(os.path.join(directory,file))
        value = im.flatten()
# I renamed the folders containing digits to the contained digit itself. For example, digit_0 folder was renamed to 0.
# so taking the 9th value of the folder gave the digit (i.e. "./train/8" ==> 9th value is 8), which was inserted into the first column of the dataset.
        value = np.hstack((directory[11:],value))
        df = pd.DataFrame(value).T
        df = df.sample(frac=1) # shuffle the dataset
        with open('train_foo.csv', 'a') as dataset:
            df.to_csv(dataset, header=False, index=False)
© 2021 GitHub, Inc.