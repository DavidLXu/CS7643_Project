#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from importlib.resources import path
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import os
from skimage import io
import random
import cv2


path1, path2 = '/root/DepthEstimation/nyu_depths/', '/root/DepthEstimation/result/' 
#path2 = '/dev/shm/result/'
outset = os.listdir(path1)
gtset = os.listdir(path2)
assert len(outset) == len(gtset)
di, gi = cv2.imread(path1), cv2.imread(path2)
rmse, absrel, acc = [], [], []
for i in range(len(outset)):
    di, gi = cv2.imread(os.path.join(path1, outset[i])), cv2.imread(os.path.join(path2, gtset[i])) 
    di, gi, ac = np.array(di)/255., np.array(gi)/255., np.maximum(di/gi, gi/di)
    r, a = np.sqrt(np.sum(np.square(di-gi))/np.size(di)), np.sum(np.abs(di-gi)/di)/np.size(di)
    ac = np.sum((ac>1.25).astype(np.int32))/np.size(ac)
    rmse.append(r)
    absrel.append(a)
    acc.append(ac)
print('finish evaluating, rmse is {:.4f}, absrel is {:.4f}, acc is {:.4f}'.format(np.mean(rmse), np.mean(absrel), np.mean(acc)))



