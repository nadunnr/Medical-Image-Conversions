import argparse
from glob import glob
import os
from pathlib import Path
import sys
from PIL import Image
import nibabel as nib
import numpy as np

input_path = "D:/VIP Cup/Dataset/ICIP training data/0/RawDataQA (1)/"
output_path= "D:/VIP Cup/test.nii.gz"


try:
    img_dir = input_path
    fns = sorted([str(fn) for fn in glob(os.path.join(img_dir,'*.tiff*'))])
    if not fns:
        raise ValueError(f'img_dir ({input_path}) does not contain any .tif or .tiff images.')
    imgs = []
    for fn in fns:
        img = np.asarray(Image.open(fn)).astype(np.float32).squeeze()
        if img.ndim != 2:
            raise Exception(f'Only 2D data supported. File {fn} has dimension {img.ndim}.')
        imgs.append(img)
    img = np.stack(imgs, axis=2)
    nib.Nifti1Image(img,None).to_filename(output_path)
except Exception as e:
    print(e)