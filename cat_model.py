import dataclasses
# TODO
# 猫の骨格モデルを定義するクラス


@dataclasses.dataclass
class Cat():
    nose2l_eye_distance: float
    nose2r_eye_distance: float
    l_eye2r_eye_distance: float
    l_eye2l_ear_base_distance: float
    r_eye2r_ear_base_distance: float
    nose2throat_distance: float
    throat2withers_distance: float
    throat2l_f_elbow_distance: float
    throat2r_f_elbow_distance: float
    l_f_elbow2l_f_knee_distance: float
    r_f_elbow2r_f_knee_distance: float
    l_f_knee2l_f_paw_distance: float
    r_f_knee2r_f_paw_distance: float
    withers2tail_base_distance: float
    tail_base2l_b_elbow_distance: float
    tail_base2r_b_elbow_distance: float
    l_b_elbow2l_b_knee_distance: float
    r_b_elbow2r_b_knee_distance: float
    l_b_knee2l_b_paw_distance: float
    r_b_knee2r_b_paw_distance: float
