import numpy as np
import os
import cv2

def put_mask(img_path,mask_path,mask_img_path):
    # 1.读取原图
    image = cv2.imread(img_path)
    image = cv2.resize(image, (256, 256))
    # 2.读取mask图
    mask = cv2.imread(mask_path)
    mask = cv2.resize(mask, (256, 256))
    print("开始合并！")
    # alpha 为image的透明度
    alpha = 1
    # beta 为mask的透明度
    beta = 0.5
    gamma = 0
    # cv2.addWeighted 将image与mask融合
    mask_img = cv2.addWeighted(image, alpha, mask, beta, gamma)
    # 读出融合后的图mask_img
    cv2.imwrite(mask_img_path, mask_img)

def get_path_list(root_path):
    return os.listdir(root_path)



def run(root_image_path, root_mask_path, result_path):
    image_path_list = get_path_list(root_image_path)
    mask_path_list = get_path_list(root_mask_path)
    for i in range(len(image_path_list)):
        put_mask(os.path.join(root_image_path, image_path_list[i]), os.path.join(root_mask_path,mask_path_list[i]), os.path.join(result_path, f'{i}.png'))


run('./images/image', './images/mask', './images/image_masked')