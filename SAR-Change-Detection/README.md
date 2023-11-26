## 原理

基于CNN的SAR图像变化检测方法，大概包括下面步骤，通过空间模糊聚类生成虚假标签（pseudo labels），生成训练样本并选择合适的训练样本，训练CNN得到分类器，使用训练好的CNN对变化像素和无变化像素进行分类。

空间模糊聚类算法，SFCM

![](https://imageurlbed.oss-cn-shenzhen.aliyuncs.com/img/SFCM.png)

CNN，分为特征提取和特征映射层，采用sigmoid函数激活

![](https://imageurlbed.oss-cn-shenzhen.aliyuncs.com/img/SARCNN.png)

## 项目模型使用

### step1 数据处理
1.pre_pseudo_label_SFCM.py：制作pre pseudo label

2.choose_correct_sample.py：选择合适样本

3.split train_val.py：将数据集分为训练集和测试集

### step2 模型训练
1.train.py：训练模型

### step3 生成结果及评估
1.make_test_sample.py：制作图像测试样例

2.inference.py：使用模型进行SAR图像变化检测
