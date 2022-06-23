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

    print('start head position estimation')

    # 姿勢の調整
    for i in range(20):
        for deg_x in range(18):
            for deg_y in range(18):
                for deg_z in range(18):
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
            print(f'losss: {loss}')
            min_loss = loss
            min_scale = scale

    print(f'head: {model.current}')

    return [model.current, min_scale]


def body_estimator(head: np.ndarray, scale: float, pose_2d: list) -> list:
    """
    Estimate body coordinate
    """
    print('start body position estimation')

    body = head.tolist() + [[0, 0, 0] for _ in range(15)]
    print(len(body))

    with open(os.path.join('.', 'joint_distance.json'), 'r') as f:
        joints_distance: dict = json.load(f)

    for name, distance in joints_distance.items():
        start_n, target_n = name.split('2')
        start_i = get_index_by_name(start_n)
        target_i = get_index_by_name(target_n)
        # print(f'start index: {start_i}')
        # print(f'target index: {target_i}')
        start = body[start_i]
        target = pose_2d[target_i]
        # print(f'start name: {start_n}')
        # print(f'target name: {target_n}')

        scaled_distance = distance * scale
        estimated_joint = joint_estimator(
            start, target, scaled_distance)
        body[target_i] = estimated_joint

    # print(f'body: {body}')

    return body


# 始点のx,y,z座標と終点のx,y座標と猫の骨格情報から，　終点のz座標を推定する
def joint_estimator(start: list, end: list, dis: float) -> list:
    D = np.sqrt(
        np.abs(dis**2 - (start[0] - end[0])**2 - (start[1] - end[1])**2))
    z1 = start[2] + D
    # z2 = start[2] - D
    end.append(z1)
    return end


# ３D座標を正規化する
def normalize_coordinate(data: np.ndarray) -> list:
    """
    Normalize coordinate
    """
    # TODO
    return data


def main():

    # # 2次元の姿勢座標を取得
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
            for i_pose in frame:
                head, scale = head_estimator(i_pose[:5])
                print(f'scale: {scale}')
                body = body_estimator(head, scale, i_pose)
                o_pose = normalize_coordinate(body)
                o_frame.append(o_pose)

            output_data.append(o_frame)

        with open(os.path.join(OUTPUT_DATA_ROOT, name), 'w') as f:
            json.dump(output_data, f, indent=4)


if __name__ == '__main__':
    main()
