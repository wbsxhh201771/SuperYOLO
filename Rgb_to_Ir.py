import os
import cv2
import numpy as np
from tqdm import tqdm

# def rgb_to_infrared(img):
#     """
#     将RGB图像转换为红外效果图像
#     :param img: OpenCV 图像 (numpy数组)
#     :return: 转换后的OpenCV图像 (numpy数组)
#     """
#     # 计算红外效果的值
#     infrared_array = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    
#     # 将红外效果的值复制到灰度通道
#     infrared_array = np.stack([infrared_array], axis=-1)
    
#     return infrared_array.astype(np.uint8)



def rgb_to_infrared(img):
    """
    将RGB图像转换为红外效果图像，并增强灰度图的对比度及边缘锐化
    :param img: OpenCV 图像 (numpy数组)
    :return: 转换后的OpenCV图像 (numpy数组)
    """
    # 计算红外效果的值
    infrared_array = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    # 将红外效果的值复制到灰度通道
    infrared_array = np.stack([infrared_array], axis=-1)

    # 将灰度图像转换为8位无符号整数类型
    infrared_array = infrared_array.astype(np.uint8)
    # 双边滤波
    infrared_array=cv2.bilateralFilter(infrared_array,9,75,75)

    # 创建 CLAHE 对象
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    # 应用 CLAHE 进行局部直方图均衡化
    infrared_array = clahe.apply(infrared_array)

    # # Gamma 校正
    # gamma = 1.5  # 你可以根据需要调整这个值
    # gamma_corrected = np.power(infrared_array / 255.0, gamma) * 255.0
    # gamma_corrected = gamma_corrected.astype(np.uint8)

    # # 使用Sobel算子进行边缘检测
    # sobelx = cv2.Sobel(gamma_corrected, cv2.CV_64F, 1, 0, ksize=3)
    # sobely = cv2.Sobel(gamma_corrected, cv2.CV_64F, 0, 1, ksize=3)
    # sobel = np.uint8(np.sqrt(sobelx**2 + sobely**2))
    # # 将边缘信息叠加到原始图像上
    # sharpened = cv2.addWeighted(infrared_array, 1.5, sobel, -0.8, 0)
    # sharpened=cv2.convertScaleAbs(infrared_array + sobel)

    return infrared_array 



def rgb_to_infrared_batch(input_folder, output_folder):
    """
    批量将RGB图像转换为红外效果图像
    :param input_folder: 输入文件夹路径
    :param output_folder: 输出文件夹路径
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取输入文件夹中所有的文件名
    file_list = os.listdir(input_folder)
    error_file_list = []
    
    # 使用 tqdm 包装文件列表以显示进度条
    for file_name in tqdm(file_list, desc="处理图像"):
        try:
            if file_name.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                # 读取RGB图像
                img_path = os.path.join(input_folder, file_name)
                img = cv2.imread(img_path)
                
                if img is None:
                    print(f"无法读取图像: {file_name}")
                    error_file_list.append(file_name)
                    continue
                
                # 将RGB图像转换为红外效果图像
                infrared_img = rgb_to_infrared(img)
                
                # 检查图像尺寸
                if min(infrared_img.shape[:2]) < 10:
                    print(f"跳过尺寸过小的图像: {file_name}")
                    error_file_list.append(file_name)
                    continue

                base_name, ext = os.path.splitext(file_name)
                # 保存红外图像到输出文件夹
                output_path = os.path.join(output_folder, base_name + '.jpg')
                cv2.imwrite(output_path, infrared_img)
                
                # print(f"转换完成: {file_name}")
            else:
                print(f"跳过不支持的文件格式: {file_name}")
        except Exception as e:
            print(f"处理文件 {file_name} 时出错: {e}")
    
    print("批量转换完成")
    print("以下文件转换失败:", error_file_list)

# 调用函数并传入RGB图像文件夹路径和输出路径
rgb_to_infrared_batch("/home/crh/Desktop/SuperYOLO/dataset/Fire_Car_test/test/images", "/home/crh/Desktop/SuperYOLO/dataset/Fire_Car_test/test/images_ir")

# from PIL import Image
# import os
# import numpy as np
# from tqdm import tqdm
# from PIL import ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True


# def rgb_to_infrared(img):
#     """
#     将RGB图像转换为红外效果图像
#     :param img: PIL.Image对象
#     :return: 转换后的PIL.Image对象
#     """
#     # 将图像转换为numpy数组
#     img_array = np.array(img)
    
#     # 计算红外效果的值
#     infrared_array = np.dot(img_array[..., :3], [0.299, 0.587, 0.114])
    
#     # 将红外效果的值复制到RGB三个通道
#     infrared_array = np.stack([infrared_array, infrared_array, infrared_array], axis=-1)
    
#     # 将numpy数组转换回PIL图像
#     infrared_img = Image.fromarray(infrared_array.astype(np.uint8))
    
#     return infrared_img

# def rgb_to_infrared_batch(input_folder, output_folder):
#     """
#     批量将RGB图像转换为红外效果图像
#     :param input_folder: 输入文件夹路径
#     :param output_folder: 输出文件夹路径
#     """
#     # 确保输出文件夹存在
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     # 获取输入文件夹中所有的文件名
#     file_list = os.listdir(input_folder)
#     error_file_list = []
#     for file_name in tqdm(file_list, desc="处理图像"):
#         try:
#             if file_name.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
#                 # 打开RGB图像
#                 img_path = os.path.join(input_folder, file_name)
#                 img = Image.open(img_path)
                
                
#                 # 将RGB图像转换为红外效果图像
#                 infrared_img = rgb_to_infrared(img)
#                 #  确保转换后的图像尺寸与原始图像一致
#                 # infrared_img = infrared_img.resize(img.size)
#                 # 检查图像尺寸
#                 if min(infrared_img .size) < 10:
#                     print(f"跳过尺寸过小的图像: {file_name}")
#                     error_file_list.append(file_name)
#                     continue

#                 base_name, ext = os.path.splitext(file_name)
#                 # 保存红外图像到输出文件夹
#                 output_path = os.path.join(output_folder, base_name+'_ir.jpg')
#                 infrared_img.save(output_path)
                
#                 # print(f"转换完成: {file_name}")
#             else:
#                 print(f"跳过不支持的文件格式: {file_name}")
#         except Exception as e:
#                 print(f"处理文件 {file_name} 时出错: {e}")
    
#     print("批量转换完成")
#     print("以下文件转换失败:",error_file_list)

# # 调用函数并传入RGB图像文件夹路径和输出路径
# rgb_to_infrared_batch("/home/crh/Desktop/SuperYOLO/dataset/Fire_Car_test/test/images", "/home/crh/Desktop/SuperYOLO/dataset/Fire_Car_test/test/images_ir")
# ['Car_test_00294.jpg', 'Car_test_00720.jpg', 'Car_test_00030.jpg', 'Car_test_00589.jpg', 'Car_test_00039.jpg', 'Car_test_00376.jpg', 'Car_test_00093.jpg', 'Car_test_01199.jpg', 'Car_test_fire_382.jpg', 'Car_test_00526.jpg', 'Car_test_00293.jpg', 'Car_test_00356.jpg', 'Car_test_00714.jpg', 'Car_test_00640.jpg', 'Car_test_01103.jpg']
