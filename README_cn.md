# SuperYOLO: Super Resolution Assisted Object Detection in Multimodal Remote Sensing Imagery

⭐ This code has been completely released ⭐

⭐ our [article](https://ieeexplore.ieee.org/abstract/document/10075555) ⭐

⭐ We also finish the work about the **quantization** based on SuperYOLO：
 [Guided Hybrid Quantization for Object Detection in Multimodal Remote Sensing Imagery via One-to-one Self-teaching](https://github.com/icey-zhang/GHOST)!!!⭐

<p align="center"> <img src="Fig/framework.png" width="60%"> </p>

## Requirements

```python
pip install -r requirements.txt
```

## 训练

### 1. 准备训练数据

- **1.1** 为了实现超分辨率辅助分支，在训练过程中，网络的输入图像从1024 x 1024大小降采样到512 x 512。在测试过程中，图像大小为512 x 512，与其他对比算法的输入保持一致。
- **1.2** 从VEDAI数据集(#)下载数据用于我们的实验。请确保下载的数据集版本适用于您的研究需求。[baiduyun](https://pan.baidu.com/s/1L0SWi5AQA6ZK9jDIWRY7Fg) (code: hvi4) or [google drive](https://drive.google.com/file/d/1Fz0VVlBS924pM3RQvcTsD_qaGjxzIv3y/view?usp=sharing). And the path of dataset is like that

```python
SuperYOLO
├── dataset
│   ├── VEDAI
│   │   ├── images
│   │   ├── labels
│   │   ├── fold01.txt
│   │   ├── fold01test.txt
│   │   ├── fold02.txt
│   │   ├── .....
│   ├── VEDAI_1024
│   │   ├── images
│   │   ├── labels
```

- 1.3 Note that we transform the labels of the dataset to be horizontal boxes by [transform code](data/transform.py). You shoud run transform.py before training the model. Change the **PATH = './dataset/'** and then run the code.

### 2. Begin to train multi images

<!--
```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --super --train_img_size 1024 --hr_input --data data/SRvedai.yaml --ch 4 --input_mode RGB+IR
```

new fusion method MF
-->

```python
python train.py --cfg models/SRyolo_MF.yaml --super --train_img_size 1024 --hr_input --data data/SRvedai.yaml --ch 64 --input_mode RGB+IR+MF
```

### 3. Begin to train RGB or IR images

```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --super --train_img_size 1024 --hr_input --data data/SRvedai.yaml --ch 3 --input_mode RGB
```

```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --super --train_img_size 1024 --hr_input --data data/SRvedai.yaml --ch 3 --input_mode IR
```

### 4. Begin to train multi images without SR branch

<!--
```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 4 --input_mode RGB+IR
```

new fusion method MF
-->

```python
python train.py --cfg models/SRyolo_MF.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 64 --input_mode RGB+IR+MF
```

### 5. Begin to train RGB or IR images without SR branch

```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 3 --input_mode RGB
```

```python
python train.py --cfg models/SRyolo_noFocus_small.yaml --train_img_size 512 --data data/SRvedai.yaml --ch 3 --input_mode IR
```

## Test

### 1. Pretrained Checkpoints

You can use our pretrained checkpoints for test process.
Download pre-trained model and put it in [here](https://github.com/icey-zhang/SuperYOLO/tree/main/weights).

### 2. Begin to test

<!--
```python
python test.py --weights runs/train/exp/best.pt --input_mode RGB+IR 
```

new fusion method MF
-->

```python
python test.py --weights runs/train/exp/best.pt --input_mode RGB+IR+MF
```

## Results

| Model Summary    | superyolov8_dsconv            | superyolov8            | superyolov5(原文章模型) |
| ---------------- | ----------------------------- | ---------------------- | ----------------------- |
| Layers           | 150                           | 146                    | 277                     |
| Parameters       | 3,235,384                     | 4,810,936              | 7,723,132               |
| Gradients        | 0                             | 0                      | 0                       |
| GFLOPS           | 37.4                          | 56.0                   | 56.0                    |
| Model File       | SRyolo_MF_Fire_v8_dwconv.yaml | SRyolo_MF_Fire_v8.yaml | SRyolo_MF_Fire.yaml     |
| Images Found     | 105                           | 105                    | 105                     |
| Missing Labels   | 0                             | 0                      | 0                       |
| Empty Labels     | 0                             | 0                      | 0                       |
| Corrupted Labels | 0                             | 0                      | 0                       |
| Class            | all                           | all                    | all                     |
| Images           | 105                           | 105                    | 105                     |
| Labels           | 137                           | 137                    | 137                     |
| Precision (P)    | 0.9461                        | 0.9166                 | 0.8955                  |
| Recall (R)       | 0.8966                        | 0.9629                 | 0.8753                  |
| mAP@.5           | 0.964                         | 0.9522                 | 0.8724                  |
| mAP@.5:.95       | 0.5866                        | 0.609                  | 0.5575                  |
| Speed (ms)       | 39.953/4.336/44.288           | 44.743/3.597/48.340    | 48.565/3.847/52.412     |
| Results Saved To | runs/test/exp9                | runs/test/exp11        | runs/test/exp12         |



## Time

2024.4
SuperYOLO won the **Highly Cited Paper** and **Hot paper** ！！！！！

<p align="center"> <img src="https://github.com/icey-zhang/SuperYOLO/assets/54712081/97d18c2c-4388-4662-801b-ab296dbfb912" alt="SuperYOLO" width="40%"/> </p>

2023.2.14 open the train.py

2023.2.14 update the new fusion method (MF)

<p align="center"> <img src="Fig/Fusion_se.png" width="60%"></p>

2023.2.16 update the test.py for visualization of detection results

## Visualization of results

<p align="center"> <img src="Fig/results.png" width="60%"> </p>

## Acknowledgements

This code is built on [YOLOv5 (PyTorch)](https://github.com/ultralytics/yolov5). We thank the authors for sharing the codes.

## Licencing

Copyright (C) 2020 Jiaqing Zhang

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.

## Contact

If you have any questions, please contact me by email (jqzhang_2@stu.xidian.edu.cn).

## Citation

If our code is helpful to you, please cite:

```
@ARTICLE{10075555,
  author={Zhang, Jiaqing and Lei, Jie and Xie, Weiying and Fang, Zhenman and Li, Yunsong and Du, Qian},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={SuperYOLO: Super Resolution Assisted Object Detection in Multimodal Remote Sensing Imagery}, 
  year={2023},
  volume={61},
  number={},
  pages={1-15},
  doi={10.1109/TGRS.2023.3258666}}

@article{zhang2023guided,
  title={Guided Hybrid Quantization for Object Detection in Remote Sensing Imagery via One-to-one Self-teaching},
  author={Zhang, Jiaqing and Lei, Jie and Xie, Weiying and Li, Yunsong and Yang, Geng and Jia, Xiuping},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  year={2023},
  publisher={IEEE}
}

```

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://api.star-history.com/svg?repos=icey-zhang/SuperYOLO&type=Date&theme=dark
    "
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://api.star-history.com/svg?repos=icey-zhang/SuperYOLO&type=Date
    "
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=icey-zhang/SuperYOLO&type=Date"
  />
</picture>
