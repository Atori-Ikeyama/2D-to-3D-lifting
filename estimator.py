import os
import json

import numpy as np

import head_model

PRE_2D_DATA_ROOT = './data/predata'
INPUT_DATA_ROOT = './data/2D_data'
OUTPUT_DATA_ROOT = './data/3D_data'


# 鼻，両目，両耳の付け根の5点のx,y座標から，それらのz座標を推定する
def head_estimator(im_head: np.ndarray) -> list:
    deg_x = 0.
    deg_y = 0.
    deg_z = 0.
    scale = 1.
    model = head_model.Head(im_head[4][0], im_head[4][1])
    min_loss = float('inf')

    # scaleのログスケールの調整
    for i in range(10):
        scale = 10**(5 - i)
        model.update(deg_x, deg_y, deg_z, scale)

    # 姿勢の調整
    for i in range(20):
        for deg_x in range(18):
            for deg_y in range(18):
                for deg_z in range(9):
                    # iが10までは,0.1×i倍のスケール, iが11からは,1×i倍のスケール
                    model.update(deg_x*20, deg_y*20, deg_z*20,
                                 scale*10**(1 - int(i/10))*i)
                    loss = model.get_loss(im_head)
                    min_loss = min(min_loss, loss)

    return [model.current, scale]


def body_estimator(head: np.ndarray, scale: float) -> list:
    """
    Estimate body coordinate
    """
    with open(os.path.join('.', 'joint_distance.json'), 'r') as f:
        joint_distance = json.load(f)

    # TODO
    return body


# 始点のx,y,z座標と終点のx,y座標と猫の骨格情報から，　終点のz座標を推定する
def joint_estimator(start: list, end: list, dis: float, scale: float) -> list:
    D = np.sqrt((dis*scale)**2 -
                (start[0] - end[0])**2 - (start[1] - end[1])**2)
    z1 = start[2] + D
    z2 = start[2] - D
    return [z1, z2]


# ３D座標を正規化する
def normalize_coordinate(data: np.ndarray) -> list:
    """
    Normalize coordinate
    """
    # TODO
    return data


def main():
    # 2次元の姿勢座標を取得
    output_data = []
    input_data_names = os.listdir(INPUT_DATA_ROOT)
    output_data_names = os.listdir(OUTPUT_DATA_ROOT)
    input_data_names = [
        name for name in input_data_names if name not in output_data_names]

    for name in input_data_names:
        with open(os.path.join(INPUT_DATA_ROOT, name), 'r') as f:
            data = json.load(f)

        for frame in data:
            o_frame = []
            for pose in frame:
                head, scale = head_estimator(pose)
                body = body_estimator(head, scale)
                o_pose = normalize_coordinate(body)
                o_frame.append(o_pose)
            output_data.append(o_frame)

        with open(os.path.join(OUTPUT_DATA_ROOT, name), 'w') as f:
            json.dump(output_data, f)


if __name__ == '__main__':
    main()
