import argparse
import glob
import os
from pathlib import Path
import sys
from PIL import Image
import nibabel as nib
import numpy as np

input_path = "D:/VIP Cup/Dataset/ICIP training data/0/RawDataQA (1)/"
output_path= "D:/VIP Cup/test12.nii.gz"
vip_dataset = "D:/VIP Cup/Dataset/ICIP training data/"

converted_nifti_count = 0

def is_tiff_dir(curr_path):
    '''function to check if the current directory having any tiff files'''
    num_dcm = len(glob.glob(os.path.join(curr_path, '*.tiff')))
    return num_dcm>0

def convert_tiff_dir_to_nifti(input_dir, output_path, stack_axis=2):

    try:
        img_dir = input_dir
        fns = sorted([str(fn) for fn in glob.glob(os.path.join(img_dir,'*.tiff*'))])
        if not fns:
            raise ValueError(f'img_dir ({input_dir}) does not contain any .tif or .tiff images.')
        imgs = []
        for fn in fns:
            img = np.asarray(Image.open(fn)).astype(np.float32).squeeze()
            if img.ndim != 2:
                raise Exception(f'Only 2D data supported. File {fn} has dimension {img.ndim}.')
            imgs.append(img)
        img = np.stack(imgs, stack_axis)
        nib.Nifti1Image(img,None).to_filename(output_path)
    except Exception as e:
        print(e)

convert_tiff_dir_to_nifti(input_path, output_path)

if __name__ == "__main__":

    dataset = glob.iglob(os.path.join(vip_dataset, '**'), recursive=True)

    for i,file in enumerate(dataset):
        if is_tiff_dir(file):
            print(file)