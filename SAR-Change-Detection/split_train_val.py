import os
import shutil
import numpy as np
import random

org_img_path = './step2_dataset_dst/FarmlandD_final/image/'
org_lab_path = './step2_dataset_dst/FarmlandD_final/label/'

dst_train_img_path = './step2_dataset_dst/FarmlandD_final//train/image/'
dst_train_lab_path = './step2_dataset_dst/FarmlandD_final//train/label/'
dst_val_img_path = './step2_dataset_dst/FarmlandD_final//val/image/'
dst_val_lab_path = './step2_dataset_dst/FarmlandD_final//val/label/'

if not os.path.exists(dst_train_img_path):
    os.makedirs(dst_train_img_path)
if not os.path.exists(dst_train_lab_path):
    os.makedirs(dst_train_lab_path)
if not os.path.exists(dst_val_img_path):
    os.makedirs(dst_val_img_path)
if not os.path.exists(dst_val_lab_path):
    os.makedirs(dst_val_lab_path)

file_list = os.listdir(org_img_path)
file_list_id = [i for i in range(0,len(file_list))]

random.shuffle(file_list_id)
train_id = file_list_id[0:int(0.8*len(file_list))]

val_id = file_list_id[int(0.8*len(file_list)):]

for id in train_id:
    shutil.copyfile(org_img_path + file_list[id], dst_train_img_path + file_list[id])
    shutil.copyfile(org_lab_path + file_list[id], dst_train_lab_path + file_list[id])

for id in val_id:
    shutil.copyfile(org_img_path + file_list[id], dst_val_img_path + file_list[id])
    shutil.copyfile(org_lab_path + file_list[id], dst_val_lab_path + file_list[id])
