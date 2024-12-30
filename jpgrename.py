import os
from PIL import Image
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
    
    for file_name in file_list:
        try:
            if file_name.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                # 打开RGB图像
                img_path = os.path.join(input_folder, file_name)
                img = Image.open(img_path)
                

                base_name, ext = os.path.splitext(file_name)
                # 重命名保存图像到输出文件夹
                output_path = os.path.join(output_folder, base_name+'_co.jpg')
                img.save(output_path)
                
                print(f"转换完成: {file_name}")
            else:
                print(f"跳过不支持的文件格式: {file_name}")
        except Exception as e:
                print(f"处理文件 {file_name} 时出错: {e}")
    
    print("批量转换完成")

# 调用函数并传入RGB图像文件夹路径和输出路径
rgb_to_infrared_batch("/home/crh/Desktop/SuperYOLO/dataset/fire_smoke/images", "/home/crh/Desktop/SuperYOLO/dataset/fire_smoke_co/images")