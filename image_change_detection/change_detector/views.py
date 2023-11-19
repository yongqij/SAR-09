from django.shortcuts import render
from django.http import HttpResponse
from . import SAR
def detect_change(request):
    if request.method == 'POST' and request.FILES['image']:
        images = request.FILES.getlist('images')
        results = []
        processed_image = SAR.process_image(image_file)
        for image_file in images:
            # 处理每张图片的变化检测代码
            # 这里仅是一个示例，你需要添加实际的图像处理代码
            result = f"Change detected in {image_file.name}!"  
            results.append(result)
        return HttpResponse("<br>".join(results))  # 返回处理后的结果列表
    return render(request, 'detect.html')

