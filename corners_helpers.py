import numpy as np

def chin(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the chin

    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of chin points"""
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{5}'], landmarks.loc[image_name, f'y_{5}']],
            [landmarks.loc[image_name, f'x_{6}'], landmarks.loc[image_name, f'y_{6}']],
            [landmarks.loc[image_name, f'x_{7}'], landmarks.loc[image_name, f'y_{7}']],
            [landmarks.loc[image_name, f'x_{8}'], landmarks.loc[image_name, f'y_{8}']],
            [landmarks.loc[image_name, f'x_{9}'], landmarks.loc[image_name, f'y_{9}']],
            [landmarks.loc[image_name, f'x_{10}'], landmarks.loc[image_name, f'y_{10}']],
            [landmarks.loc[image_name, f'x_{11}'], landmarks.loc[image_name, f'y_{11}']],
            [landmarks.loc[image_name, f'x_{54}'], landmarks.loc[image_name, f'y_{54}']],
            [landmarks.loc[image_name, f'x_{55}'], landmarks.loc[image_name, f'y_{55}']],
            [landmarks.loc[image_name, f'x_{56}'], landmarks.loc[image_name, f'y_{56}']],
            [landmarks.loc[image_name, f'x_{57}'], landmarks.loc[image_name, f'y_{57}']],
            [landmarks.loc[image_name, f'x_{58}'], landmarks.loc[image_name, f'y_{58}']],
            [landmarks.loc[image_name, f'x_{59}'], landmarks.loc[image_name, f'y_{59}']],
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']]
        ]
    ], dtype=np.int32)
    return points


def left_cheek(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the left cheek 

    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of left cheek points"""
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{0}'], landmarks.loc[image_name, f'y_{0}']],
            [landmarks.loc[image_name, f'x_{1}'], landmarks.loc[image_name, f'y_{1}']],
            [landmarks.loc[image_name, f'x_{2}'], landmarks.loc[image_name, f'y_{2}']],
            [landmarks.loc[image_name, f'x_{3}'], landmarks.loc[image_name, f'y_{3}']],
            [landmarks.loc[image_name, f'x_{4}'], landmarks.loc[image_name, f'y_{4}']],
            [landmarks.loc[image_name, f'x_{5}'], landmarks.loc[image_name, f'y_{5}']],
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']],
            [landmarks.loc[image_name, f'x_{31}'], landmarks.loc[image_name, f'y_{31}']],
            [landmarks.loc[image_name, f'x_{39}'], landmarks.loc[image_name, f'y_{39}']],
            [landmarks.loc[image_name, f'x_{40}'], landmarks.loc[image_name, f'y_{40}']],
            [landmarks.loc[image_name, f'x_{41}'], landmarks.loc[image_name, f'y_{41}']],
            [landmarks.loc[image_name, f'x_{36}'], landmarks.loc[image_name, f'y_{36}']],
            [landmarks.loc[image_name, f'x_{0}'], landmarks.loc[image_name, f'y_{0}']],
        ]
    ], dtype=np.int32)
    return points


def right_cheek(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the right cheek 

    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of right cheek points"""

    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{16}'], landmarks.loc[image_name, f'y_{16}']],
            [landmarks.loc[image_name, f'x_{15}'], landmarks.loc[image_name, f'y_{15}']],
            [landmarks.loc[image_name, f'x_{14}'], landmarks.loc[image_name, f'y_{14}']],
            [landmarks.loc[image_name, f'x_{13}'], landmarks.loc[image_name, f'y_{13}']],
            [landmarks.loc[image_name, f'x_{12}'], landmarks.loc[image_name, f'y_{12}']],
            [landmarks.loc[image_name, f'x_{11}'], landmarks.loc[image_name, f'y_{11}']],
            [landmarks.loc[image_name, f'x_{54}'], landmarks.loc[image_name, f'y_{54}']],
            [landmarks.loc[image_name, f'x_{35}'], landmarks.loc[image_name, f'y_{35}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
            [landmarks.loc[image_name, f'x_{47}'], landmarks.loc[image_name, f'y_{47}']],
            [landmarks.loc[image_name, f'x_{46}'], landmarks.loc[image_name, f'y_{46}']],
            [landmarks.loc[image_name, f'x_{45}'], landmarks.loc[image_name, f'y_{45}']],
            [landmarks.loc[image_name, f'x_{16}'], landmarks.loc[image_name, f'y_{16}']],
        ]
    ], dtype=np.int32)
    return points


def upper_lip(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the upper lip
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of upper lip points"""

    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']],
            [landmarks.loc[image_name, f'x_{31}'], landmarks.loc[image_name, f'y_{31}']],
            [landmarks.loc[image_name, f'x_{32}'], landmarks.loc[image_name, f'y_{32}']],
            [landmarks.loc[image_name, f'x_{33}'], landmarks.loc[image_name, f'y_{33}']],
            [landmarks.loc[image_name, f'x_{34}'], landmarks.loc[image_name, f'y_{34}']],
            [landmarks.loc[image_name, f'x_{35}'], landmarks.loc[image_name, f'y_{35}']],
            [landmarks.loc[image_name, f'x_{54}'], landmarks.loc[image_name, f'y_{54}']],
            [landmarks.loc[image_name, f'x_{53}'], landmarks.loc[image_name, f'y_{53}']],
            [landmarks.loc[image_name, f'x_{52}'], landmarks.loc[image_name, f'y_{52}']],
            [landmarks.loc[image_name, f'x_{51}'], landmarks.loc[image_name, f'y_{51}']],
            [landmarks.loc[image_name, f'x_{50}'], landmarks.loc[image_name, f'y_{50}']],
            [landmarks.loc[image_name, f'x_{49}'], landmarks.loc[image_name, f'y_{49}']],
            [landmarks.loc[image_name, f'x_{48}'], landmarks.loc[image_name, f'y_{48}']]
        ]
    ], dtype=np.int32)
    return points


def mouth(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the mouth    
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of mouth points"""

    
    points = np.array([
        [
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
        ]
    ], dtype=np.int32)
    return points


def left_eye(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the left eye    
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of left eye points"""

    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{36}'], landmarks.loc[image_name, f'y_{36}']],
            [landmarks.loc[image_name, f'x_{37}'], landmarks.loc[image_name, f'y_{37}']],
            [landmarks.loc[image_name, f'x_{38}'], landmarks.loc[image_name, f'y_{38}']],
            [landmarks.loc[image_name, f'x_{39}'], landmarks.loc[image_name, f'y_{39}']],
            [landmarks.loc[image_name, f'x_{40}'], landmarks.loc[image_name, f'y_{40}']],
            [landmarks.loc[image_name, f'x_{41}'], landmarks.loc[image_name, f'y_{41}']],
            [landmarks.loc[image_name, f'x_{36}'], landmarks.loc[image_name, f'y_{36}']]
        ]
    ], dtype=np.int32)
    return points


def right_eye(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the right eye    
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of right eye points"""
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
            [landmarks.loc[image_name, f'x_{43}'], landmarks.loc[image_name, f'y_{43}']],
            [landmarks.loc[image_name, f'x_{44}'], landmarks.loc[image_name, f'y_{44}']],
            [landmarks.loc[image_name, f'x_{45}'], landmarks.loc[image_name, f'y_{45}']],
            [landmarks.loc[image_name, f'x_{46}'], landmarks.loc[image_name, f'y_{46}']],
            [landmarks.loc[image_name, f'x_{47}'], landmarks.loc[image_name, f'y_{47}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']]
        ]
    ], dtype=np.int32)
    return points


def nose(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the nose    
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of nose points"""
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{31}'] - (
                    landmarks.loc[image_name, f'x_{32}'] - landmarks.loc[image_name, f'x_{31}']),
             landmarks.loc[image_name, f'y_{31}']],
            [landmarks.loc[image_name, f'x_{32}'], landmarks.loc[image_name, f'y_{32}']],
            [landmarks.loc[image_name, f'x_{33}'], landmarks.loc[image_name, f'y_{33}']],
            [landmarks.loc[image_name, f'x_{34}'], landmarks.loc[image_name, f'y_{34}']],
            [landmarks.loc[image_name, f'x_{35}'] + (
                    landmarks.loc[image_name, f'x_{35}'] - landmarks.loc[image_name, f'x_{34}']),
             landmarks.loc[image_name, f'y_{35}']],
            [landmarks.loc[image_name, f'x_{42}'], landmarks.loc[image_name, f'y_{42}']],
            [landmarks.loc[image_name, f'x_{27}'], landmarks.loc[image_name, f'y_{27}']],
            [landmarks.loc[image_name, f'x_{39}'], landmarks.loc[image_name, f'y_{39}']],
            [landmarks.loc[image_name, f'x_{31}'] - (
                    landmarks.loc[image_name, f'x_{32}'] - landmarks.loc[image_name, f'x_{31}']),
             landmarks.loc[image_name, f'y_{31}']],
        ]
    ], dtype=np.int32)
    return points


def left_eye_brow(image_name, landmarks):
    """  Returns a numpy array of landmarks defining the left eye brow    
    Args:
        image_name (str): name of image
        landmarks (df): dataframe containing the landmarks

    Returns:
        points: numpy array of left eye brow points"""
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{17}'], landmarks.loc[image_name, f'y_{17}']],
            [landmarks.loc[image_name, f'x_{18}'], landmarks.loc[image_name, f'y_{18}']],
            [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}']],
            [landmarks.loc[image_name, f'x_{20}'], landmarks.loc[image_name, f'y_{20}']],
            [landmarks.loc[image_name, f'x_{21}'], landmarks.loc[image_name, f'y_{21}']],
        ]
    ], dtype=np.int32)
    return points


def right_eye_brow(image_name, landmarks):
    
    points = np.array([
        [
            [landmarks.loc[image_name, f'x_{22}'], landmarks.loc[image_name, f'y_{22}']],
            [landmarks.loc[image_name, f'x_{23}'], landmarks.loc[image_name, f'y_{23}']],
            [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}']],
            [landmarks.loc[image_name, f'x_{25}'], landmarks.loc[image_name, f'y_{25}']],
            [landmarks.loc[image_name, f'x_{26}'], landmarks.loc[image_name, f'y_{26}']],
        ]
    ], dtype=np.int32)
    return points


def top_of_head(image_name, landmarks):
    
    if (landmarks.loc[image_name, f'y_{24}'] - (
            int(landmarks.loc[image_name, f'y_{8}'] * 1.1) - landmarks.loc[image_name, f'y_{33}']) > 0) and (
            landmarks.loc[image_name, f'y_{19}'] - (
            int(landmarks.loc[image_name, f'y_{8}'] * 1.1) - landmarks.loc[image_name, f'y_{33}']) > 0):
        points = np.array([
            [
                [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}']],
                [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}'] - (
                        int(landmarks.loc[image_name, f'y_{8}'] * 1.1) - landmarks.loc[image_name, f'y_{33}'])],
                [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}'] - (
                        int(landmarks.loc[image_name, f'y_{8}'] * 1.1) - landmarks.loc[image_name, f'y_{33}'])],
                [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}']],
            ]
        ], dtype=np.int32)
        for index1 in points:
            for index2 in index1:
                if index2[0] < 0 or index2[1] < 0:
                    return None
        return points
    else:
        points = np.array([
            [
                [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}']],
                [landmarks.loc[image_name, f'x_{24}'], landmarks.loc[image_name, f'y_{24}'] - (
                        landmarks.loc[image_name, f'y_{8}'] - int(landmarks.loc[image_name, f'y_{33}'] * 1.3))],
                [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}'] - (
                        landmarks.loc[image_name, f'y_{8}'] - int(landmarks.loc[image_name, f'y_{33}'] * 1.3))],
                [landmarks.loc[image_name, f'x_{19}'], landmarks.loc[image_name, f'y_{19}']],
            ]
        ], dtype=np.int32)
        for index1 in points:
            for index2 in index1:
                if index2[0] < 0 or index2[1] < 0:
                    return None
        return points


def left_ear(image_name, landmarks):
    
    if (landmarks.loc[image_name, f'x_{0}'] - landmarks.loc[image_name, f'x_{17}']) < -5:
        points = np.array([
            [
                [landmarks.loc[image_name, f'x_{0}'] - (
                        landmarks.loc[image_name, f'x_{17}'] - landmarks.loc[image_name, f'x_{0}']),
                 landmarks.loc[image_name, f'y_{0}']],
                [landmarks.loc[image_name, f'x_{1}'] - (
                        landmarks.loc[image_name, f'x_{17}'] - landmarks.loc[image_name, f'x_{1}']),
                 landmarks.loc[image_name, f'y_{1}']],
                [landmarks.loc[image_name, f'x_{2}'] - (
                        landmarks.loc[image_name, f'x_{17}'] - landmarks.loc[image_name, f'x_{2}']),
                 landmarks.loc[image_name, f'y_{2}']],
                [landmarks.loc[image_name, f'x_{3}'] - (
                        landmarks.loc[image_name, f'x_{17}'] - landmarks.loc[image_name, f'x_{3}']),
                 landmarks.loc[image_name, f'y_{3}']],
                [landmarks.loc[image_name, f'x_{3}'], landmarks.loc[image_name, f'y_{3}']],
                [landmarks.loc[image_name, f'x_{2}'], landmarks.loc[image_name, f'y_{2}']],
                [landmarks.loc[image_name, f'x_{1}'], landmarks.loc[image_name, f'y_{1}']],
                [landmarks.loc[image_name, f'x_{0}'], landmarks.loc[image_name, f'y_{0}']]
            ]
        ], dtype=np.int32)
        for index1 in points:
            for index2 in index1:
                if index2[0] < 0 or index2[1] < 0:
                    return None
        return points
    else:
        return None


def right_ear(image_name, landmarks):
    
    if (landmarks.loc[image_name, f'x_{16}'] - landmarks.loc[image_name, f'x_{26}']) > 5:
        points = np.array([
            [
                [landmarks.loc[image_name, f'x_{16}'] + (
                        landmarks.loc[image_name, f'x_{16}'] - landmarks.loc[image_name, f'x_{26}']),
                 landmarks.loc[image_name, f'y_{16}']],
                [landmarks.loc[image_name, f'x_{15}'] + (
                        landmarks.loc[image_name, f'x_{15}'] - landmarks.loc[image_name, f'x_{26}']),
                 landmarks.loc[image_name, f'y_{15}']],
                [landmarks.loc[image_name, f'x_{14}'] + (
                        landmarks.loc[image_name, f'x_{14}'] - landmarks.loc[image_name, f'x_{26}']),
                 landmarks.loc[image_name, f'y_{14}']],
                [landmarks.loc[image_name, f'x_{13}'] + (
                        landmarks.loc[image_name, f'x_{13}'] - landmarks.loc[image_name, f'x_{26}']),
                 landmarks.loc[image_name, f'y_{13}']],
                [landmarks.loc[image_name, f'x_{13}'], landmarks.loc[image_name, f'y_{13}']],
                [landmarks.loc[image_name, f'x_{14}'], landmarks.loc[image_name, f'y_{14}']],
                [landmarks.loc[image_name, f'x_{15}'], landmarks.loc[image_name, f'y_{15}']],
                [landmarks.loc[image_name, f'x_{16}'], landmarks.loc[image_name, f'y_{16}']]
            ]
        ], dtype=np.int32)
        for index1 in points:
            for index2 in index1:
                if index2[0] < 0 or index2[1] < 0:
                    return None
        return points
    else:
        return None

