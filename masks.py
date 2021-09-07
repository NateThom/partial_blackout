import corners_helpers
import os
import pandas
import cv2
import numpy as np

def get_attribute_points(image_name, landmarks, attribute_label='mouth'):

    ''' Gets the points that define a given attribute'''

    attribute_functions = {
        'mouth': corners_helpers.mouth
    }

    attribute_points = attribute_functions[attribute_label](image_name, landmarks)
    return attribute_points

def create_attribute_mask(image, attribute_points):
    '''Creates an attribute mask for the given image for a given attribute  '''
    height, width, depth = image.shape
    black_image = np.zeros( (height, width, depth), np.uint8)
    cv2.fillPoly(img=black_image, pts=attribute_points, color=255) #  , lineType=cv2.LINE_AA)

    return black_image


def create_attribute_masks(input_directory='.', output_directory='./attribute_masks',\
                            landmarks_path='./test/data/reformatted_celebA_unaligned_images__facial_landmarks.csv',\
                            attribute_list=['mouth']):
    ''' Creates attribute masks for the images in the given directory and saves them to 
    the output directory. A subdirectory is created in the output directory for every attribute
    in the attribute list'''
    image_names = sorted(os.listdir(input_directory))

    landmarks_df = pandas.read_csv(landmarks_path, index_col='image_name')
    corners_df = pandas.read_csv(path_to_corners, index_col=0)

    if not os.access(output_directory, os.F_OK):
        os.mkdir(output_directory)

    for image_name in image_names:
        for attribute in attribute_list:
            landmarks_exist = image_name in landmarks_df.index
            if landmarks_exist:
                attribute_points = get_attribute_points(image_name, landmarks_df, attribute)
                image_path = input_directory + '/' + image_name
                image = cv2.imread(image_path)
                mask = create_attribute_mask(image, attribute_points)
                

                attribute_directory = output_directory + '/' + attribute + "_masks"
                if not os.access(attribute_directory, os.F_OK):
                    os.mkdir(attribute_directory)
                    
                # crop and resize the mask before saving
                x_min, x_max, y_min, y_max = corners_df.loc[image_name]
                cropped_mask = mask[y_min:y_max, x_min:x_max]
                resized_and_cropped_mask = cv2.resize(cropped_mask, (178, 218))

                # save it
                mask_name = attribute + '_mask_' + image_name
                mask_path = attribute_directory + '/' + mask_name 
                if cv2.imwrite(mask_path, resized_and_cropped_mask) == False:
                    print(f'Mask {mask_name} not saved successfully!')

                
path_to_celeba_images = '/home/nthom/Documents/datasets/CelebA/Img/img_celeba/'
path_to_corners = '/home/nthom/Documents/CelebA_Partial_Blackout/crop_points.csv'
path_to_masks = './test/output/attribute_masks_chunk'
path_to_landmarks = '/home/nthom/Documents/datasets/UNR_Facial_Attribute_Parsing_Dataset/landmarks.csv'
list_of_attributes = ['mouth']

create_attribute_masks(path_to_celeba_images, path_to_masks, path_to_landmarks, list_of_attributes)
