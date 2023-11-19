Author：Jerry Jiang
Create Time: 2023-11-19

# SAR图像变化检测 SAR IMAGE CHANGE DETECTION
## 项目框架
项目根文件夹下有两个文件夹，分别是**change_detector（应用程序文件夹）**和**image_change_detector（主文件夹）**，我们的程序主要放在change_detector文件夹中。
### manage.py文件
我们部署这个程序到网页上使用代码
```python
python manage.py runserver
```
进行部署
## change_detector文件夹
介绍里面几个主要的文件（夹）
### template文件夹中的detect.html
这个html文件进行网页的显示，我们需要用这个文件来实现SAR图片的网页传输和结果反馈，单独放在template文件夹中。
```python
#下面这一段代码是 Django 模板标签中的一部分，用于处理 CSRF（Cross Site Request Forgery，跨站请求伪造）保护。
{% csrf_token %} 
```
### views.py
这个文件包含Django中视图函数的定义，负责处理**从浏览器发来的请求，并返回相应的HTTP响应**。
每一个视图函数都对应一个特定的URL地址，视图接受一个HttpRequest对象作为参数，并返回一个HttpResponse对象或者其他Http相关相应。
```python
# 简单样例
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

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

## image_change_detector 文件夹
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