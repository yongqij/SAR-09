Author：Jerry Jiang
Create Time: 2023-11-19

# SAR图像变化检测 SAR IMAGE CHANGE DETECTION
## 项目框架
项目根文件夹下有两个文件夹，分别是**change_detector（应用程序文件夹）**和**image_change_detector（主文件夹）**，我们的程序主要放在change_detector文件夹中。除此之外有一个**dataset（用户缓存临时文件夹）**，用来临时存放图片识别途中产生的文件。
### manage.py文件
我们部署这个程序到网页上使用代码
```python
python manage.py runserver
```
进行部署

## dataset

### image_process

存放处理图片过程中产生的子文件

### image1.bmp, image2.bmp, result.bmp

分别为两个要检测的图片和最后生成的图像处理图片，前面两个由用户在网页上传，最后一个为模型处理结果，但不是最后返回给用户的图片。

## change_detector文件夹（主要）
介绍里面几个主要的文件（夹）

### SAR_model文件夹

这个文件夹里存放我们的SAR图像检测模型及代码，因为我们的model已经在本地跑完了，所以这里面并没有关于model训练的代码，我们使用pth文件保存了最优模型直接使用。

里面的detect.py是编写用来调用函数的文件，我们的前端点击后直接调用detect.py中的process_image函数即可进行处理。

### template文件夹中的detect.html
这个html文件进行网页的显示，我们需要用这个文件来实现SAR图片的网页传输和结果反馈，单独放在template文件夹中。
```python
#下面这一段代码是 Django 模板标签中的一部分，用于处理 CSRF（Cross Site Request Forgery，跨站请求伪造）保护。
{% csrf_token %} 
```
### views.py
这个文件包含Django中视图函数的定义，负责处理**从浏览器发来的请求，并返回相应的HTTP响应**。
每一个视图函数都对应一个特定的URL地址，视图接受一个HttpRequest对象作为参数，并返回一个HttpResponse对象或者其他Http相关相应。

比如我们这个里面的一个例子，这个函数用来响应http中的“检测”按钮，保存用户从网站上传的图片，并且调用我们的process_images()图像处理函数。

```python
# 简单样例
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

```
### urls.py
这个文件用来**将URL映射到相应的视图函数**。
```python
urlpatterns = [
    path('', views.detect_change, name='detect_change'),
]
```
比如上面这一段代表当用户访问网站根目录时，我们将调用名为detect_change的视图函数来处理请求。
### SAR.py
这个文件用来存放我们的图像处理代码。
当然这个文件不能直接使用，我们需要**在视图文件中引用这个模块并且调用相应函数**。
```python
# 比如在我们这个视图文件里引用SAR.py中的函数
from . import SAR
processed_image = SAR.process_image(image_file)
```

## image_change_detector 文件夹（不重要，只需要设置一些东西）
### urls.py
同我们的change_detector文件，只不过这里是在主文件夹中，一样是应用程序URL映射。
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('change_detector.urls')),  # 包含应用程序的URL
]
```
### setting.py
这里我暂时只用到了设置模板文件路径
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 只用到了下面这一行DIRS
        'DIRS': [os.path.join(BASE_DIR, 'change_detector', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```