import numpy as np


class FullBody():
    # lengthはモデルの長さの何倍かで表す

    # 頭のモデル
    body: np.ndarray

    # 全体のパラメータ
    theta_x: int
    theta_y: int
    theta_z: int
    scale: int
    slide_x: int
    slide_y: int

    # nose
    nose_roll: int
    nose_pitch: int
    nose_yaw: int

    # throat
    throat_roll: int
    throat_pitch: int
    throat_yaw: int
    throat_length: int

    # front leg
    l_f_elbow_roll: int
    l_f_elbow_yaw: int
    l_f_elbow_pitch: int
    l_f_elbow_length: int

    r_f_elbow_roll: int
    r_f_elbow_yaw: int
    r_f_elbow_pitch: int
    r_f_elbow_length: int

    l_f_knee_pitch: int

    r_f_knee_pitch: int

    l_f_paw_pitch: int

    r_f_paw_pitch: int

    # back leg
    l_b_elbow_roll: int
    l_b_elbow_yaw: int
    l_b_elbow_pitch: int
    l_b_elbow_length: int

    r_b_elbow_roll: int
    r_b_elbow_yaw: int
    r_b_elbow_pitch: int
    r_b_elbow_length: int

    l_b_knee_pitch: int

    r_b_knee_pitch: int

    l_b_paw_pitch: int

    r_b_paw_pitch: int

    # other
    withers_pitch: int
    withers_length: int

    tail_base_pitch: int
    tail_base_yaw: int

    def __init__(self) -> None:
        # 全体のパラメータ
        self.theta_x = 0
        self.theta_y = 0
        self.theta_z = 0
        self.scale = 0
        self.slide_x = 0
        self.slide_y = 0
        self.nose_roll = 0
        self.nose_pitch = 0
        self.nose_yaw = 0
        self.throat_roll = 0
        self.throat_pitch = 0
        self.throat_yaw = 0
        self.throat_length = 1
        self.l_f_elbow_roll = 0
        self.l_f_elbow_yaw = 0
        self.l_f_elbow_pitch = 0
        self.l_f_elbow_length = 1
        self.r_f_elbow_roll = 0
        self.r_f_elbow_yaw = 0
        self.r_f_elbow_pitch = 0
        self.r_f_elbow_length = 1
        self.l_f_knee_pitch = 0
        self.r_f_knee_pitch = 0
        self.l_f_paw_pitch = 0
        self.r_f_paw_pitch = 0
        self.l_b_elbow_roll = 0
        self.l_b_elbow_yaw = 0
        self.l_b_elbow_pitch = 0
        self.l_b_elbow_length = 1
        self.r_b_elbow_roll = 0
        self.r_b_elbow_yaw = 0
        self.r_b_elbow_pitch = 0
        self.r_b_elbow_length = 1
        self.l_b_knee_pitch = 0
        self.r_b_knee_pitch = 0
        self.l_b_paw_pitch = 0
        self.r_b_paw_pitch = 0
        self.withers_pitch = 0
        self.withers_length = 1
        self.tail_base_pitch = 0
        self.tail_base_yaw = 0

    def _getRotateXMatrix(self, theta_x: int):
        sinx = np.sin(theta_x)
        cosx = np.cos(theta_x)
        return np.array([
            [1, 0, 0],
            [0, cosx, -sinx],
            [0, sinx, cosx]
        ])

    def _getRotateYMatrix(self, theta_y: int):
        siny = np.sin(theta_y)
        cosy = np.cos(theta_y)
        return np.array([
            [cosy, 0, siny],
            [0, 1, 0],
            [-siny, 0, cosy]
        ])

    def _getRotateZMatrix(self, theta_z: int):
        sinz = np.sin(theta_z)
        cosz = np.cos(theta_z)
        return np.array([
            [cosz, -sinz, 0],
            [sinz, cosz, 0],
            [0, 0, 1]
        ])

    def rotateXYZ(self, theta_x: int, theta_y: int, theta_z: int, target: np.ndarray, center) -> None:
        self.slide(-center[0], -center[1], -center[2], target)
        rx = self._getRotateXMatrix(theta_x)
        ry = self._getRotateYMatrix(theta_y)
        rz = self._getRotateZMatrix(theta_z)

        target = target @ rx @ ry @ rz

        self.slide(center[0], center[1], center[2], target)

    def scale(self, scale: float, target: np.ndarray, center) -> None:
        self.slide(-center[0], -center[1], -center[2], target)
        s = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, scale]
        ])
        target = target @ s
        self.slide(center[0], center[1], center[2], target)

    def slide(self, x: float, y: float, target: np.ndarray, z=0.0) -> None:
        s = np.array([[x, y, z] for _ in range(20)])
        target = target + s

    def rotateJoint(self, joint: np.ndarray, center: np.ndarray, joint_roll: float = 0, joint_pitch: float = 0, joint_yaw: float = 0, length: float = 1) -> None:
        self.rotateXYZ(joint_roll, joint_pitch, joint_yaw, joint, center)
        self.scale(length, joint, center)

    def update(self, theta_x: float, theta_y: float, theta_z: float, scale: float, x: float, y: float, ) -> None:
        self.theta_x = theta_x
        self.theta_y = theta_y
        self.theta_z = theta_z
        self.scale = scale
        self.slide_x = x
        self.slide_y = y
        self.nose_roll = 0
        self.nose_pitch = 0
        self.nose_yaw = 0
        self.throat_roll = 0
        self.throat_pitch = 0
        self.throat_yaw = 0
        self.throat_length = 1
        self.l_f_elbow_roll = 0
        self.l_f_elbow_yaw = 0
        self.l_f_elbow_pitch = 0
        self.l_f_elbow_length = 1
        self.r_f_elbow_roll = 0
        self.r_f_elbow_yaw = 0
        self.r_f_elbow_pitch = 0
        self.r_f_elbow_length = 1
        self.l_f_knee_pitch = 0
        self.r_f_knee_pitch = 0
        self.l_f_paw_pitch = 0
        self.r_f_paw_pitch = 0
        self.l_b_elbow_roll = 0
        self.l_b_elbow_yaw = 0
        self.l_b_elbow_pitch = 0
        self.l_b_elbow_length = 1
        self.r_b_elbow_roll = 0
        self.r_b_elbow_yaw = 0
        self.r_b_elbow_pitch = 0
        self.r_b_elbow_length = 1
        self.l_b_knee_pitch = 0
        self.r_b_knee_pitch = 0
        self.l_b_paw_pitch = 0
        self.r_b_paw_pitch = 0
        self.withers_pitch = 0
        self.withers_length = 1
        self.tail_base_pitch = 0
        self.tail_base_yaw = 0

        self.rotateXYZ(self.theta_x, self.theta_y, self.theta_z)
        self.scale(self.scale)
        self.slideXY(self.slide_x, self.slide_y)

    def getLoss(self, im_body) -> float:
        return np.sum(np.square(self.body - im_body))/len(self.body)


class HeadModelData():
    @staticmethod
    def getHeadData():
        return np.array([
            [
                1339.4813232421875,
                1004.5853271484375,
                0.996397852897644
            ],
            [
                1289.616943359375,
                997.4617919921875,
                0.8979284763336182
            ],
            [
                1360.851806640625,
                954.720947265625,
                0.84747314453125
            ],
            [
                1282.493408203125,
                944.0357666015625,
                0.8657176494598389
            ],
            [
                1303.8638916015625,
                1033.0792236328125,
                0.9093841910362244
            ],
        ])
