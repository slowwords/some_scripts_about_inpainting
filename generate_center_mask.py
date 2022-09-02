import os.path
import random
import cv2
import numpy as np
import time

t = time.time()  # 用时间戳来唯一命名

def create_mask(width, height, mask_width, mask_height, x=None, y=None):
    # 黑色是0  白色缺失部分是255   实际使用时，需要将255变为1。 因为需要和原图做加减运算
    mask = np.zeros((height, width))  # 生成一个覆盖全部大小的全黑mask
    mask_x = x if x is not None else random.randint(0, width - mask_width)  # 缺失部分左下角的x坐标
    mask_y = y if y is not None else random.randint(0, height - mask_height)  # 缺失部分左上角的y坐标
    mask[mask_y:mask_y + mask_height, mask_x:mask_x + mask_width] = 255  # 将中间缺失白色部分标为1
    return mask


def run(root_path, num):
    for i in range(num):
        img = np.zeros((256, 256))
        imgh, imgw = img.shape[0:2]  # imgw = 256 imgh = 256
        mask = create_mask(imgw, imgh, 64, 64, x=96, y=96)
        save_path = os.path.join(root_path, str(int(i)) + ".png")
        cv2.imwrite(save_path, mask)
        print(f'save {i} mask OK!')

run('./images/mask/',10)