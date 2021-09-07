import corners_helpers # contains the functions that returns landmarks for ears, eyes, etc.
import pandas
import os
from tqdm import tqdm

# open the log file and write over if it already exists
path_to_landmarked_images = "/home/nthom/Documents/datasets/CelebA/Img/img_celeba/"
path_to_crop_points_csv = "./crop_points.csv"
path_to_landmarks = "/home/nthom/Documents/datasets/UNR_Facial_Attribute_Parsing_Dataset/landmarks.csv"
image_names = sorted(os.listdir(path_to_landmarked_images))

# create new dataframe to store the crop points
column_names = ['x_min', 'x_max', 'y_min', 'y_max']
crop_points_df = pandas.DataFrame(index=image_names, columns=column_names)

landmarks_df = pandas.read_csv(path_to_landmarks, index_col='image_name')

for i, image_name in enumerate(tqdm(image_names, position=0, desc="Images processed", leave=False, colour="green")):
    # sanity check
    landmark_exists = image_name in landmarks_df.index

    if not landmark_exists:
        print(f"Image {image_name} not found in landmarks csv!")
    else:
        x_min = float("inf")
        x_max = -float("inf")
        y_min = float("inf")
        y_max = -float("inf")

        # get the landmark points that define the boundaries of the face

        points = []
        points.append(corners_helpers.chin(image_name, landmarks_df))
        points.append(corners_helpers.left_cheek(image_name, landmarks_df))
        points.append(corners_helpers.right_cheek(image_name, landmarks_df))
        points.append(corners_helpers.upper_lip(image_name, landmarks_df))
        # points.append(corners_helpers.neck(image_name, landmarks_df))
        points.append(corners_helpers.mouth(image_name, landmarks_df))
        points.append(corners_helpers.left_eye(image_name, landmarks_df))
        points.append(corners_helpers.right_eye(image_name, landmarks_df))
        points.append(corners_helpers.nose(image_name, landmarks_df))
        points.append(corners_helpers.left_eye_brow(image_name, landmarks_df))
        points.append(corners_helpers.right_eye_brow(image_name, landmarks_df))
        points.append(corners_helpers.top_of_head(image_name, landmarks_df))
        points.append(corners_helpers.left_ear(image_name, landmarks_df))
        points.append(corners_helpers.right_ear(image_name, landmarks_df))

        # find the points farthest from the center of the image
        # so the cropped image is as small as possible
        # while showing  all the landmark points

        for region in points:
            if region is not None:
                for coordinates in region:
                    for value in coordinates:
                        if (not value[0] < 0) or (not value[1] < 0):
                            if value[0] < x_min:
                                x_min = value[0]
                            elif value[0] > x_max:
                                x_max = value[0]
                            if value[1] < y_min:
                                y_min = value[1]
                            elif value[1] > y_max:
                                y_max = value[1] 
        # put it in the dataframe 
        crop_points_df.loc[image_name] = [x_min, x_max, y_min, y_max]

# just in case
crop_points_df.dropna(axis='index', how='any', inplace=True)

# save the dataframe to a file
crop_points_df.to_csv(path_to_crop_points_csv, index_label="image_name")

print(f"\n\nSaved cropped points to {path_to_crop_points_csv}")
