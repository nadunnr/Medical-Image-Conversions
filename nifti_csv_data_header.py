import numpy as np
import nibabel as nib
import glob
import os
import shutil
import csv


csv_path = 'D:/ScholarX/dataset_info.csv'

columns = ['patient_id', 'main size (MB)', 'seg. size(MB)', 'dimensions - x', 'dimensions - y', 'dimensions - z', 'vox. spacing - x', 'vox. spacing - y', 'vox. spacing - z']

out = 'D:/ScholarX/Output/'
patient_ids = os.listdir(out)

with open(csv_path, mode='w', newline='') as file:

    csv_writer = csv.writer(file)
    csv_writer.writerow(columns)

    for i,id in enumerate(patient_ids):

        temp = []

        path = os.path.join(out, id)
        files = os.listdir(path)

        main = os.path.join(path, files[0])
        segmentation = os.path.join(path, files[1])

        temp.append(id)

        #file_sizes
        main_size = format((os.stat(main).st_size /(1024*1024)),'.2f')
        temp.append(main_size)
        seg_size= format((os.stat(segmentation).st_size/(1024*1024)), '.2f')
        temp.append(seg_size)

        #image header info
        img = nib.load(main)
        header = img.header
        dimensions = list(header['dim'][1:4])
        spacing = list(header['pixdim'][1:4])

        for axis in dimensions:
            temp.append(axis)
        for axis in spacing:
            temp.append(axis)

        csv_writer.writerow(temp)