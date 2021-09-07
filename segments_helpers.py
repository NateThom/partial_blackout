import statistics
import numpy as np

def landmark_points(image_name, landmarks):
    ########## Hardcoded / Predefined Landmarks #########
    # Eye Brow
    brow_points = np.array([
            [landmarks.loc[image_name, f'x_{17}'], landmarks.loc[image_name, f'y_{17}']],
            [landmarks.loc[image_name, f'x_{18}'], landmarks.loc[image_name, f'y_{18}']],
            [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}']],
            [landmarks.loc[image_name, f'x_{20}'], landmarks.loc[image_name, f'y_{20}']],
            [landmarks.loc[image_name, f'x_{21}'], landmarks.loc[image_name, f'y_{21}']],
            [landmarks.loc[image_name, f'x_{22}'], landmarks.loc[image_name, f'y_{22}']],
            [landmarks.loc[image_name, f'x_{23}'], landmarks.loc[image_name, f'y_{23}']],
            [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}']],
            [landmarks.loc[image_name, f'x_{25}'], landmarks.loc[image_name, f'y_{25}']],
            [landmarks.loc[image_name, f'x_{26}'], landmarks.loc[image_name, f'y_{26}']],
    ], dtype=np.int32)

    # Eye
    eye_points = np.array([
            [landmarks.loc[image_name, f'x_{36}'], landmarks.loc[image_name, f'y_{36}']],
            [landmarks.loc[image_name, f'x_{37}'], landmarks.loc[image_name, f'y_{37}']],
            [landmarks.loc[image_name, f'x_{38}'], landmarks.loc[image_name, f'y_{38}']],
            [landmarks.loc[image_name, f'x_{39}'], landmarks.loc[image_name, f'y_{39}']],
            [landmarks.loc[image_name, f'x_{40}'], landmarks.loc[image_name, f'y_{40}']],
            [landmarks.loc[image_name, f'x_{41}'], landmarks.loc[image_name, f'y_{41}']],
            [landmarks.loc[image_name, f'x_{36}'], landmarks.loc[image_name, f'y_{36}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
            [landmarks.loc[image_name, f'x_{43}'], landmarks.loc[image_name, f'y_{43}']],
            [landmarks.loc[image_name, f'x_{44}'], landmarks.loc[image_name, f'y_{44}']],
            [landmarks.loc[image_name, f'x_{45}'], landmarks.loc[image_name, f'y_{45}']],
            [landmarks.loc[image_name, f'x_{46}'], landmarks.loc[image_name, f'y_{46}']],
            [landmarks.loc[image_name, f'x_{47}'], landmarks.loc[image_name, f'y_{47}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
    ], dtype=np.int32)

    # Nose
    nose_points = np.array([
            [landmarks.loc[image_name, f'x_{31}'] - (
                    landmarks.loc[image_name, f'x_{32}'] - landmarks.loc[
                image_name, f'x_{31}']),
             landmarks.loc[image_name, f'y_{31}']],
            [landmarks.loc[image_name, f'x_{32}'], landmarks.loc[image_name, f'y_{32}']],
            [landmarks.loc[image_name, f'x_{33}'], landmarks.loc[image_name, f'y_{33}']],
            [landmarks.loc[image_name, f'x_{34}'], landmarks.loc[image_name, f'y_{34}']],
            [landmarks.loc[image_name, f'x_{35}'] + (
                    landmarks.loc[image_name, f'x_{35}'] - landmarks.loc[
                image_name, f'x_{34}']),
             landmarks.loc[image_name, f'y_{35}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
            [landmarks.loc[image_name, f'x_{27}'], landmarks.loc[image_name, f'y_{27}']],
            [landmarks.loc[image_name, f'x_{39}'], landmarks.loc[image_name, f'y_{39}']],
            [landmarks.loc[image_name, f'x_{31}'] - (
                    landmarks.loc[image_name, f'x_{32}'] - landmarks.loc[
                image_name, f'x_{31}']),
             landmarks.loc[image_name, f'y_{31}']],
    ], dtype=np.int32)

    # Mouth
    mouth_points = np.array([
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']],
            [landmarks.loc[image_name, f'x_{49}'], landmarks.loc[image_name, f'y_{49}']],
            [landmarks.loc[image_name, f'x_{50}'], landmarks.loc[image_name, f'y_{50}']],
            [landmarks.loc[image_name, f'x_{51}'], landmarks.loc[image_name, f'y_{51}']],
            [landmarks.loc[image_name, f'x_{52}'], landmarks.loc[image_name, f'y_{52}']],
            [landmarks.loc[image_name, f'x_{53}'], landmarks.loc[image_name, f'y_{53}']],
            [landmarks.loc[image_name, f'x_{54}'], landmarks.loc[image_name, f'y_{54}']],
            [landmarks.loc[image_name, f'x_{55}'], landmarks.loc[image_name, f'y_{55}']],
            [landmarks.loc[image_name, f'x_{56}'], landmarks.loc[image_name, f'y_{56}']],
            [landmarks.loc[image_name, f'x_{57}'], landmarks.loc[image_name, f'y_{57}']],
            [landmarks.loc[image_name, f'x_{58}'], landmarks.loc[image_name, f'y_{58}']],
            [landmarks.loc[image_name, f'x_{59}'], landmarks.loc[image_name, f'y_{59}']],
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']]
    ], dtype=np.int32)

    # Neck
    neck_points = np.array([
            [landmarks.loc[image_name, f'x_{5}'], landmarks.loc[image_name, f'y_{5}']],
            [landmarks.loc[image_name, f'x_{6}'], landmarks.loc[image_name, f'y_{6}']],
            [landmarks.loc[image_name, f'x_{7}'], landmarks.loc[image_name, f'y_{7}']],
            [landmarks.loc[image_name, f'x_{8}'], landmarks.loc[image_name, f'y_{8}']],
            [landmarks.loc[image_name, f'x_{9}'], landmarks.loc[image_name, f'y_{9}']],
            [landmarks.loc[image_name, f'x_{10}'], landmarks.loc[image_name, f'y_{10}']],
            [landmarks.loc[image_name, f'x_{11}'], landmarks.loc[image_name, f'y_{11}']],
            [landmarks.loc[image_name, f'x_{11}'], landmarks.loc[image_name, f'y_{11}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{10}'], landmarks.loc[image_name, f'y_{10}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{9}'], landmarks.loc[image_name, f'y_{9}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{8}'], landmarks.loc[image_name, f'y_{8}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{7}'], landmarks.loc[image_name, f'y_{7}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{6}'], landmarks.loc[image_name, f'y_{6}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
            [landmarks.loc[image_name, f'x_{5}'], landmarks.loc[image_name, f'y_{5}'] - (
                    landmarks.loc[image_name, f'y_{33}'] - landmarks.loc[
                image_name, f'y_{58}'])],
    ], dtype=np.int32)
    #####################################################
    return brow_points, eye_points, nose_points, mouth_points, neck_points

def top_to_bottom_segments(path_to_celeba_image, landmarks):
    eye_brow_points, eye_points, nose_points, mouth_points, chin_points = landmark_points(path_to_celeba_image[-10:], landmarks)

    # list of segments, only considering vertical (y) axis
    segments = [min(eye_brow_points[0:len(eye_brow_points), 1]),
                min(eye_points[0:len(eye_points), 1]),
                max(eye_points[0:len(eye_points),1]),
                max(nose_points[0:len(nose_points),1]),
                max(mouth_points[0:len(mouth_points),1]),
                statistics.mean(chin_points[0:len(chin_points),1])]

    return segments


def bottom_to_top_segments(path_to_celeba_image, path_to_landmarks):
    #landmarks = pd.read_csv(path_to_landmarks, sep=',')
    #landmarks.set_index('image_name', inplace=True)
    #image = cv2.imread(path_to_celeba_image)

    eye_brow_points, eye_points, nose_points, mouth_points, chin_points = landmark_points(path_to_celeba_image[-10:], landmarks)

    # list of segments, only considering vertical (y) axis
    segments = [max(chin_points[0:len(chin_points), 1]),
                max(mouth_points[0:len(mouth_points), 1]),
                min(mouth_points[0:len(mouth_points), 1]),
                max(nose_points[0:len(nose_points), 1]),
                max(eye_points[0:len(eye_points), 1]),
                max(eye_brow_points[0:len(eye_brow_points), 1])
                ]

    return segments