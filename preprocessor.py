import os
import json
from turtle import color, width
from cv2 import ROTATE_90_COUNTERCLOCKWISE

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyrsistent import v

from visualizer import vis2D

# 2D　のjsonファイルを読み込み、前処理をして、2D_dataにjsonファイルを生成する。

PRE_2D_DATA_ROOT = './data/predata'
OTUPUT_DATA_ROOT = './data/2D_data'

# 信頼度の低いデータを削除する。


def is_low_confidence(data: list) -> bool:
    """
    Remove low confidence data
    """
    for pose in data:
        if pose['bbox']['score'] < 0.8:
            return True

        if pose['keypoints']['Nose']['score'] < 0.8:
            return True

    return False


# bboxで切り抜いて，左下を原点にし，幅×高さ=10000に変換する。
def _convert_bbox_to_relative_coordinate(left: float, top: float, right: float, bottom: float) -> list:
    """
    Convert bbox to relative coordinate
    """
    pre_w = right - left  # 幅
    pre_h = bottom - top  # 高さ
    ratio = pre_h / pre_w  # 高さと幅の比
    r_ratio = np.sqrt(ratio)  # 高さと幅の比のルート
    width = 100 / r_ratio  # 調整後の幅
    height = width * r_ratio  # 調整後の高さ
    scale = width / pre_w  # 調整後と調整前の比
    slide_x = left
    slide_y = top
    res = [width, height, scale, slide_x, slide_y]
    return res


def json_to_list(data: list) -> list:
    """
    Json to list
    """
    res = []
    for pose in data:
        temp = []
        w, h, s, x, y = _convert_bbox_to_relative_coordinate(
            pose['bbox']['left'], pose['bbox']['top'], pose['bbox']['right'], pose['bbox']['bottom'])
        for joint in pose['keypoints']:
            j = []
            k_x = (pose['keypoints'][joint]['x'] - x) * s  # x座標を変換
            j.append(k_x)
            k_y = h - (pose['keypoints'][joint]['y'] - y) * s  # y座標を変換
            j.append(k_y)
            temp.append(j)

        res.append(temp)
    return res


def main():
    data_2d_names = os.listdir(PRE_2D_DATA_ROOT)
    processed_data_names = os.listdir(OTUPUT_DATA_ROOT)
    data_2d_names = [
        name for name in data_2d_names if name not in processed_data_names]
    if len(data_2d_names) == 0:
        print('No data to process')
        return

    json_open_2d = open(os.path.join(PRE_2D_DATA_ROOT, data_2d_names[0]), 'r')
    json_load_2d = json.load(json_open_2d)
    output_json = []

    for data_2d in json_load_2d:
        # 空のデータを削除スキップ
        if data_2d == []:
            continue

        # 信頼度の低いデータをスキップ
        if is_low_confidence(data_2d):
            continue

        data = json_to_list(data_2d)
        output_json.append(data)

    f = open(os.path.join(OTUPUT_DATA_ROOT, data_2d_names[0]), 'w')
    json.dump(output_json, f, indent=4)


if __name__ == '__main__':
    main()
