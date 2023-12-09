from django.shortcuts import render
import cv2
import numpy as np
import os
from django.http import HttpResponse
from change_detector.SAR_model.detect import process_images

def detect_change(request):
    if request.method == 'POST' and request.FILES.get('image1') and request.FILES.get('image2'):
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']

        # 用户文件夹路径
        USR_DATA = os.path.join('dataset')

        file_path1 = os.path.join(USR_DATA, '1.bmp')
        file_path2 = os.path.join(USR_DATA, '2.bmp')
        # 保存图像为BMP格式
        with open(file_path1, 'wb+') as destination1:
            for chunk in image1.chunks():
                destination1.write(chunk)

        with open(file_path2, 'wb+') as destination2:
            for chunk in image2.chunks():
                destination2.write(chunk)

        # 将两张图片一起传递给图像处理函数
        process_images()
        results = 0
        # results = process_images([img1, img2])

        return render(request, 'detect.html')
    return render(request, 'detect.html')
