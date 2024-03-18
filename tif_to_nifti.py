import argparse
from glob import glob
import os
from pathlib import Path
import sys
from PIL import Image
import nibabel as nib
import numpy as np

input_path = "D:/VIP Cup/Dataset/ICIP training data/0/RawDataQA (1)/"
output_path= "D:/VIP Cup/"


def split_filename(filepath):
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext

'''
def main():
    try:
        #args = arg_parser().parse_args()
        img_dir = input_path
        fns = sorted([str(fn) for fn in glob(os.path.join(img_dir,'*.tiff*'))])
        if not fns:
            raise ValueError(f'img_dir ({input_path}) does not contain any .tif or .tiff images.')
        imgs = []
        for fn in fns:
            _, base, ext = split_filename(fn)
            img = np.asarray(Image.open(fn)).astype(np.float32).squeeze()
            if img.ndim != 2:
                raise Exception(f'Only 2D data supported. File {base}{ext} has dimension {img.ndim}.')
            imgs.append(img)
        img = np.stack(imgs, axis=1)
        nib.Nifti1Image(img,None).to_filename(os.path.join(output_path, f'test.nii.gz'))
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
'''

try:
    img_dir = input_path
    fns = sorted([str(fn) for fn in glob(os.path.join(img_dir,'*.tiff*'))])
    if not fns:
        raise ValueError(f'img_dir ({input_path}) does not contain any .tif or .tiff images.')
    imgs = []
    for fn in fns:
        _, base, ext = split_filename(fn)
        img = np.asarray(Image.open(fn)).astype(np.float32).squeeze()
        if img.ndim != 2:
            raise Exception(f'Only 2D data supported. File {base}{ext} has dimension {img.ndim}.')
        imgs.append(img)
    img = np.stack(imgs, axis=2)
    nib.Nifti1Image(img,None).to_filename(os.path.join(output_path, f'test.nii.gz'))
except Exception as e:
    print(e)