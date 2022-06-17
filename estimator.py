import os
import json

import numpy as np
import matplotlib.pyplot as plt

import head_model
# 猫の骨格情報と2次元の姿勢座標から，　猫の3次元の姿勢を推定する

PRE_2D_DATA_ROOT = './data/predata'
INPUT_DATA_ROOT = './data/2D_data'
OUTPUT_DATA_ROOT = './data/3D_data'


# 鼻，両目，両耳の付け根の5点のx,y座標から，それらのz座標を推定する
def head_estimator(head: np.ndarray) -> list:
    deg_x = 0.
    deg_y = 0.
    deg_z = 0.
    scale = 1.
    model = head_model.Head(head[4][0], head[4][1])

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

    return (model.current, scale)


# 始点のx,y,z座標と終点のx,y座標と猫の骨格情報から，　終点のz座標を推定する
def joint_estimator(start: list, end: list, dis: list, scale: float) -> list:
    D = np.sqrt((dis*scale)**2 -
                (start[0] - end[0])**2 - (start[1] - end[1])**2)
    z1 = start[2] + D
    z2 = start[2] - D
    return z1

# ３D座標を正規化する


def normalize_coordinate(data: np.ndarray) -> list:
    """
    Normalize coordinate
    """
    # TODO
    return data





def main():
    # 2次元の姿勢座標を取得
    joint_distance = []
    data_3d = []

    # print(data_2d)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(, c='r', marker='o')
    # ax.set_title("Scatter Plot")
    # plt.show()
    # break

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.scatter3D(np.ravel(X1), np.ravel(X2), y)
    # ax.set_title("Scatter Plot")
    # plt.show()


if __name__ == '__main__':
    main()
