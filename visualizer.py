import os
import json

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DATA_2D_ROOT = './data/2D_data'
DATA_3D_ROOT = './data/3D_data'

VIDEO_2D_ROOT = './visualized_video/2D_data'
VIDEO_3D_ROOT = './visualized_video/3D_data'


def vis_2d(file_name: str) -> None:
    """
    Visualize 2D data
    """
    json_open = open(os.path.join(DATA_2D_ROOT, file_name), 'r')
    json_load = json.load(json_open)

    ims = []
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    for frame in json_load:
        for data in frame:
            t_data = np.array(data).T
            images1 = ax1.scatter(t_data[0], t_data[1], c='r', marker='o')
            images2 = ax1.plot([data[0][0], data[1][0]], [
                data[0][1], data[1][1]], c='g')
            images3 = ax1.plot([data[0][0], data[2][0]], [
                data[0][1], data[2][1]], c='g')
            images4 = ax1.plot([data[1][0], data[3][0]], [
                data[1][1], data[3][1]], c='g')
            images5 = ax1.plot([data[4][0], data[0][0]], [
                data[4][1], data[0][1]], c='g')
            images6 = ax1.plot([data[4][0], data[1][0]], [
                data[4][1], data[1][1]], c='g')
            images7 = ax1.plot([data[4][0], data[5][0]], [
                data[4][1], data[5][1]], c='b')
            images8 = ax1.plot([data[5][0], data[7][0]], [
                data[5][1], data[7][1]], c='b')
            images9 = ax1.plot([data[5][0], data[8][0]], [
                data[5][1], data[8][1]], c='b')
            images10 = ax1.plot([data[5][0], data[9][0]], [
                data[5][1], data[9][1]], c='b')
            images11 = ax1.plot([data[8][0], data[12][0]], [
                data[8][1], data[12][1]], c='c')
            images12 = ax1.plot([data[9][0], data[13][0]], [
                data[9][1], data[13][1]], c='c')
            images13 = ax1.plot([data[12][0], data[16][0]], [
                data[12][1], data[16][1]], c='c')
            images14 = ax1.plot([data[13][0], data[17][0]], [
                data[13][1], data[17][1]], c='c')
            images15 = ax1.plot([data[7][0], data[6][0]], [
                data[7][1], data[6][1]], c='b')
            images16 = ax1.plot([data[6][0], data[10][0]], [
                data[6][1], data[10][1]], c='b')
            images17 = ax1.plot([data[6][0], data[11][0]], [
                data[6][1], data[11][1]], c='b')
            images18 = ax1.plot([data[10][0], data[14][0]], [
                data[10][1], data[14][1]], c='c')
            images19 = ax1.plot([data[11][0], data[15][0]], [
                data[11][1], data[15][1]], c='c')
            images20 = ax1.plot([data[14][0], data[18][0]], [
                data[14][1], data[18][1]], c='c')
            images21 = ax1.plot([data[15][0], data[19][0]],
                                [data[15][1], data[19][1]], c='c')

            ims.append([images1] + images2 + images3 + images4 +
                       images5 + images6 + images7 + images8 + images9 + images10 + images11 + images12 + images13 + images14 + images15 + images16 + images17 + images18 + images19 + images20 + images21)

    ani = animation.ArtistAnimation(fig, ims, interval=250, blit=True)
    file_path = os.path.join(VIDEO_2D_ROOT, file_name.split('.')[0] + '.mp4')
    ani.save(file_path, writer='ffmpeg', fps=4)
    plt.show()


def vis_3d(file_name: str) -> None:
    """
    Visualize 3D data
    """
    json_open = open(os.path.join(DATA_3D_ROOT, file_name), 'r')
    json_load = json.load(json_open)

    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')

    ims = []

    for frame in json_load:
        for data in frame:
            t_data = np.array(data).T
            images1_1 = ax1.scatter3D(
                t_data[0], t_data[1], t_data[2], c='r', marker='o')
            images1_2 = ax1.plot([data[0][0], data[1][0]], [
                data[0][1], data[1][1]], [data[0][2], data[1][2]], c='g')
            images1_3 = ax1.plot([data[0][0], data[2][0]], [
                data[0][1], data[2][1]], [data[0][2], data[2][2]], c='g')
            images1_4 = ax1.plot([data[1][0], data[3][0]], [
                data[1][1], data[3][1]], [data[1][2], data[3][2]], c='g')
            images1_5 = ax1.plot([data[4][0], data[0][0]], [
                data[4][1], data[0][1]], [data[4][2], data[0][2]], c='g')
            images1_6 = ax1.plot([data[4][0], data[1][0]], [
                data[4][1], data[1][1]], [data[4][2], data[1][2]], c='g')
            images1_7 = ax1.plot([data[4][0], data[5][0]], [
                data[4][1], data[5][1]], [data[4][2], data[5][2]], c='b')
            images1_8 = ax1.plot([data[5][0], data[7][0]], [
                data[5][1], data[7][1]], [data[5][2], data[7][2]], c='b')
            images1_9 = ax1.plot([data[5][0], data[8][0]], [
                data[5][1], data[8][1]], [data[5][2], data[8][2]], c='b')
            images1_10 = ax1.plot([data[5][0], data[9][0]], [
                data[5][1], data[9][1]], [data[5][2], data[9][2]], c='b')
            images1_11 = ax1.plot([data[8][0], data[12][0]], [
                data[8][1], data[12][1]], [data[8][2], data[12][2]], c='c')
            images1_12 = ax1.plot([data[9][0], data[13][0]], [
                data[9][1], data[13][1]], [data[9][2], data[13][2]], c='c')
            images1_13 = ax1.plot([data[12][0], data[16][0]], [
                data[12][1], data[16][1]], [data[12][2], data[16][2]], c='c')
            images1_14 = ax1.plot([data[13][0], data[17][0]], [
                data[13][1], data[17][1]], [data[13][2], data[17][2]], c='c')
            images1_15 = ax1.plot([data[7][0], data[6][0]], [
                data[7][1], data[6][1]], [data[7][2], data[6][2]], c='b')
            images1_16 = ax1.plot([data[6][0], data[10][0]], [
                data[6][1], data[10][1]], [data[6][2], data[10][2]], c='b')
            images1_17 = ax1.plot([data[6][0], data[11][0]], [
                data[6][1], data[11][1]], [data[6][2], data[11][2]], c='b')
            images1_18 = ax1.plot([data[10][0], data[14][0]], [
                data[10][1], data[14][1]], [data[10][2], data[14][2]], c='c')
            images1_19 = ax1.plot([data[11][0], data[15][0]], [
                data[11][1], data[15][1]], [data[11][2], data[15][2]], c='c')
            images1_20 = ax1.plot([data[14][0], data[18][0]], [
                data[14][1], data[18][1]], [data[14][2], data[18][2]], c='c')
            images1_21 = ax1.plot([data[15][0], data[19][0]],
                                  [data[15][1], data[19][1]], [data[15][2], data[19][2]], c='c')
            # ax1.plot([-50, 50, 50, 50], [-50, -50, 50, 50],
            #          [-50, -50, -50, 50])
            ax1.set_xlabel('X')
            ax1.set_ylabel('Y')
            ax1.set_zlabel('Z')

            images2_1 = ax2.scatter3D(
                t_data[0], t_data[1], t_data[2], c='r', marker='o')
            images2_2 = ax2.plot([data[0][0], data[1][0]], [
                data[0][1], data[1][1]], [data[0][2], data[1][2]], c='g')
            images2_3 = ax2.plot([data[0][0], data[2][0]], [
                data[0][1], data[2][1]], [data[0][2], data[2][2]], c='g')
            images2_4 = ax2.plot([data[1][0], data[3][0]], [
                data[1][1], data[3][1]], [data[1][2], data[3][2]], c='g')
            images2_5 = ax2.plot([data[4][0], data[0][0]], [
                data[4][1], data[0][1]], [data[4][2], data[0][2]], c='g')
            images2_6 = ax2.plot([data[4][0], data[1][0]], [
                data[4][1], data[1][1]], [data[4][2], data[1][2]], c='g')
            images2_7 = ax2.plot([data[4][0], data[5][0]], [
                data[4][1], data[5][1]], [data[4][2], data[5][2]], c='b')
            images2_8 = ax2.plot([data[5][0], data[7][0]], [
                data[5][1], data[7][1]], [data[5][2], data[7][2]], c='b')
            images2_9 = ax2.plot([data[5][0], data[8][0]], [
                data[5][1], data[8][1]], [data[5][2], data[8][2]], c='b')
            images2_10 = ax2.plot([data[5][0], data[9][0]], [
                data[5][1], data[9][1]], [data[5][2], data[9][2]], c='b')
            images2_11 = ax2.plot([data[8][0], data[12][0]], [
                data[8][1], data[12][1]], [data[8][2], data[12][2]], c='c')
            images2_12 = ax2.plot([data[9][0], data[13][0]], [
                data[9][1], data[13][1]], [data[9][2], data[13][2]], c='c')
            images2_13 = ax2.plot([data[12][0], data[16][0]], [
                data[12][1], data[16][1]], [data[12][2], data[16][2]], c='c')
            images2_14 = ax2.plot([data[13][0], data[17][0]], [
                data[13][1], data[17][1]], [data[13][2], data[17][2]], c='c')
            images2_15 = ax2.plot([data[7][0], data[6][0]], [
                data[7][1], data[6][1]], [data[7][2], data[6][2]], c='b')
            images2_16 = ax2.plot([data[6][0], data[10][0]], [
                data[6][1], data[10][1]], [data[6][2], data[10][2]], c='b')
            images2_17 = ax2.plot([data[6][0], data[11][0]], [
                data[6][1], data[11][1]], [data[6][2], data[11][2]], c='b')
            images2_18 = ax2.plot([data[10][0], data[14][0]], [
                data[10][1], data[14][1]], [data[10][2], data[14][2]], c='c')
            images2_19 = ax2.plot([data[11][0], data[15][0]], [
                data[11][1], data[15][1]], [data[11][2], data[15][2]], c='c')
            images2_20 = ax2.plot([data[14][0], data[18][0]], [
                data[14][1], data[18][1]], [data[14][2], data[18][2]], c='c')
            images2_21 = ax2.plot([data[15][0], data[19][0]],
                                  [data[15][1], data[19][1]], [data[15][2], data[19][2]], c='c')

            ax2.view_init(azim=180)
            ax2.set_xlabel('X')
            ax2.set_ylabel('Y')
            ax2.set_zlabel('Z')

            ims.append([images1_1] + images1_2 + images1_3 + images1_4 +
                       images1_5 + images1_6 + images1_7 + images1_8 + images1_9 +
                       images1_10 + images1_11 + images1_12 + images1_13 +
                       images1_14 + images1_15 + images1_16 + images1_17 +
                       images1_18 + images1_19 + images1_20 + images1_21 +
                       [images2_1] + images2_2 + images2_3 + images2_4 +
                       images2_5 + images2_6 + images2_7 + images2_8 + images2_9 +
                       images2_10 + images2_11 + images2_12 + images2_13 +
                       images2_14 + images2_15 + images2_16 + images2_17 +
                       images2_18 + images2_19 + images2_20 + images2_21
                       )

    ani = animation.ArtistAnimation(fig, ims, interval=250, blit=True)
    file_path = os.path.join(VIDEO_3D_ROOT, file_name.split('.')[0] + '.mp4')
    ani.save(file_path, writer='ffmpeg', fps=4)
    plt.show()


def main():
    # vis_d('「おやつくれニャ〜」と飛び出して来ておかわりまで要求する猫 [bTXOn-6K1M4].json')
    vis_3d('「おやつくれニャ〜」と飛び出して来ておかわりまで要求する猫 [bTXOn-6K1M4].json')


if __name__ == '__main__':
    main()
