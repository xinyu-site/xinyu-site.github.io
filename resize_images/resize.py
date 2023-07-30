from PIL import Image
import os
def resize_image(input_path, output_path, new_width, new_height):
    try:
        # 打开图片
        image = Image.open(input_path)
        
        # 改变尺寸
        resized_image = image.resize((new_width, new_height))
        
        # 保存改变后的图片
        resized_image.save(output_path)
        print(f"图片已成功改变尺寸并保存至 {output_path}")
    except Exception as e:
        print(f"出现错误：{e}")

# 示例用法：
input_image_path = "robot.jpg"  # 替换为你的输入图片路径
output_message = {'image-alignment':[[150, 300, 580, 1200], [150, 200, 300, 4002]], 
'mstile':[[70, 144, 150, 310, 310], [70, 144, 150, 150, 310]],
'apple-touch-icon':[[60, 76, 120, 152, 180],[60, 76, 120, 152, 180]],
'favicon':[[16, 16, 32], [16, 32, 32]],
'android-chrome':[[192, 512], [192, 512]]
}
for key, size_list in output_message.items():
    for i in range(len(size_list[0])):
        new_width, new_height = size_list[0][i], size_list[1][i]
        if 'image-alignment' in key:
            output_image_path = os.path.join('output', '{}-{}x{}.jpg'.format(key, str(new_width), str(new_height)))
        else:
            output_image_path = os.path.join('output', '{}-{}x{}.png'.format(key, str(new_width), str(new_height)))
        print(output_image_path)
        resize_image(input_image_path, output_image_path, new_width, new_height)
