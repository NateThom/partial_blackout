# Each segment has another segment of the image showing (not black)
# As if you are slowly lookinng at someone's face from above
# Segment numbers are as follows:
# 1. Forehead (dowm to eyebrows)
# 2. Eyebrows (down to eyes)
# 3. Eyes
# 4. Nose
# 5. Mouth
# 6. Chin
# 7. Full 

import logging
import numpy as np
import os
import pandas as pd
import cv2
from tqdm import tqdm
import segments_helpers as helpers
from datetime import date

today = date.today()

# yy-mm-dd
today = today.strftime("%y-%m-%d")

# global variables
BLACK = [0,0,0]
IMAGE_HEIGHT = 218
IMAGE_WIDTH = 178

landmarks_file_name = "/home/nthom/Documents/datasets/UNR_Facial_Attribute_Parsing_Dataset/landmarks.csv"
path_to_images = "/home/nthom/Documents/datasets/CelebA/Img/img_celeba/"
path_to_masks = "./data/segmented_images/"
path_to_corners = "/home/nthom/Documents/CelebA_Partial_Blackout/crop_points.csv"

# create the directory to store the images if it doesn't exist
if not os.access(path_to_masks, os.F_OK):
    os.mkdir(path_to_masks)

# get a sorted list of the images in the given directory
image_name_list = sorted(os.listdir(path_to_images))

# get the landmarks
landmarks_df = pd.read_csv(landmarks_file_name, index_col="image_name")
landmarks_df_head = landmarks_df.head
print(f"Landmarks Dataframe Head:\n {landmarks_df_head} \n")

# get the bounding boxes
corners_df = pd.read_csv(path_to_corners, index_col=0)
print(f"Bounding Boxes Dataframe Head: \n {corners_df.head}")
print(f"Bounding Boxes Dataframe headers: {corners_df.columns}")

# change this list if only certain segments are desired
segment_numbers = [1, 2, 3, 4, 5, 6, 7]


for image_name in tqdm(image_name_list):
    # Sanity checks
    landmark_exists = image_name in landmarks_df.index
    corners_exists = image_name in corners_df.index

    if not landmark_exists:
       print(f"Image {image_name} not found in landmarks file!\n")
    if not corners_exists:
       print(f"Image {image_name} not found in corners file!\n")
  
    if landmark_exists and corners_exists:
        # get the landmarks
        landmarks = helpers.top_to_bottom_segments(image_name, landmarks_df) 
        # get the info about the bounding box
        x_min, x_max, y_min, y_max = corners_df.loc[image_name]  
        landmarks = np.append(landmarks, [y_max])

        # create the segments 
        for segment_number in segment_numbers:
            # get the image
            img = cv2.imread(path_to_images + image_name)

            # create the segment directory to store the images if it doesn't exist
            directory = "segment" + str(segment_number)
            if not os.access(path_to_masks + directory, os.F_OK):
                os.mkdir(path_to_masks + directory)

            # The image will be black from the landmark point down to the bottom
            landmark = landmarks[segment_number - 1]
            logging.info(f"The landmark for segment {segment_number} is {landmark}.")
            img[landmark:, :] = BLACK 

                     
            # crop the image
            cropped_img = img[y_min:y_max, x_min:x_max]
            cropped_img = cv2.resize(cropped_img, (178, 218))
            # save the cropped image
            if cv2.imwrite(path_to_masks + directory + "/segment" + str(segment_number) + "_" + image_name, cropped_img) == False:
                print(f"Image {segment_number}_{image_name} not saved successfully!")
