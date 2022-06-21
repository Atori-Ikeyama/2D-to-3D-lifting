import os
import json

import numpy as np

import head_model

PRE_2D_DATA_ROOT = './data/predata'
INPUT_DATA_ROOT = './data/2D_data'
OUTPUT_DATA_ROOT = './data/3D_data'


def get_index_by_name(name: str) -> int:
    """
    Get index by name
    """
    if name == 'l_eye':
        return 0
    elif name == 'r_eye':
        return 1
    elif name == 'l_ear_base':
        return 2
    elif name == 'r_ear_base':
        return 3
    elif name == 'nose':
        return 4
    elif name == 'throat':
        return 5
    elif name == 'tail_base':
        return 6
    elif name == 'withers':
        return 7
    elif name == 'l_f_elbow':
        return 8
    elif name == 'r_f_elbow':
        return 9
    elif name == 'l_b_elbow':
        return 10
    elif name == 'r_b_elbow':
        return 11
    elif name == 'l_f_knee':
        return 12
    elif name == 'r_f_knee':
        return 13
    elif name == 'l_b_knee':
        return 14
    elif name == 'r_b_knee':
        return 15
    elif name == 'l_f_paw':
        return 16
    elif name == 'r_f_paw':
        return 17
    elif name == 'l_b_paw':
        return 18
    elif name == 'r_b_paw':
        return 19

    return -1

# 鼻，両目，両耳の付け根の5点のx,y座標から，それらのz座標を推定する


def head_estimator(im_head: np.ndarray) -> list:
    min_deg_x = 0
    min_deg_y = 0
    min_deg_z = 0
    min_scale = 1
    model = head_model.Head(im_head[4][0], im_head[4][1])
    min_loss = float('inf')

    # 姿勢の調整
    for i in range(20):
        for deg_x in range(18):
            for deg_y in range(18):
                for deg_z in range(9):
                    # 0.1×i倍のスケール
                    if i < 10:
                        scale = 0.1 * (i + 1)
                    else:
                        scale = 0.2 * (i + 1)
                    # モデルの計算
                    model.update(deg_x*20, deg_y*20, deg_z*20, scale)
                    # モデルの誤差の計算
                    loss = model.get_loss(im_head)
                    if loss < min_loss:
                        min_loss = loss
                        min_deg_x = deg_x
                        min_deg_y = deg_y
                        min_deg_z = deg_z
                        min_scale = scale

    for i in range(20):
        # 0.1×i倍のスケール
        if i < 10:
            scale = 1 - 0.01 * (i + 1)
        else:
            scale = 1 + 0.01 * i
        # モデルの計算
        model.update(min_deg_x*20, min_deg_y*20, min_deg_z*20, min_scale*scale)
        # モデルの誤差の計算
        loss = model.get_loss(im_head)
        if loss < min_loss:
            min_loss = loss
            min_scale = scale

    return [model.current, min_scale]


def body_estimator(head: np.ndarray, scale: float, pose_2d: list, last_pose: list) -> list:
    """
    Estimate body coordinate
    """
    body = []
    start_joint = head[0].tolist()  # 鼻をはじめのスタート関節とする

    with open(os.path.join('.', 'joint_distance.json'), 'r') as f:
        joints_distance = json.load(f)

    for index, distance in enumerate(joints_distance.values()):
        scaled_distance = distance * scale
        start_joint = joint_estimator(
            start_joint, pose_2d[index], scaled_distance, scale)
        body.append(start_joint)

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
    body_estimator()

    # # 2次元の姿勢座標を取得
    # output_data = []
    # input_data_names = os.listdir(INPUT_DATA_ROOT)
    # output_data_names = os.listdir(OUTPUT_DATA_ROOT)
    # input_data_names = [
    #     name for name in input_data_names if name not in output_data_names]

    # for name in input_data_names:
    #     with open(os.path.join(INPUT_DATA_ROOT, name), 'r') as f:
    #         data = json.load(f)

    #     for frame in data:
    #         o_frame = []
    #         for pose in frame:
    #             head, scale = head_estimator(pose)
    #             body = body_estimator(head, scale)
    #             o_pose = normalize_coordinate(body)
    #             o_frame.append(o_pose)
    #         output_data.append(o_frame)

    #     with open(os.path.join(OUTPUT_DATA_ROOT, name), 'w') as f:
    #         json.dump(output_data, f)


if __name__ == '__main__':
    main()
