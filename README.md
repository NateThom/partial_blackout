# Understanding Machine Perception of Faces 

## University of Nevada, Reno Machine Perception Laboratory
___
## Helper Programs
### corners.py: Finds crop points for each landmarked image provided and outputs them to a csv.
### corners_helpers.py: Contains functions which define regions of the face (i.e. chin, eyes, cheeks...) based on landmarks.
### segments.py: Generates segment/partial blackout images based on landmarks and crop points.
### segments_helpers.py: Contains functions to generate segments of the face based on landmarks as well as defining regions of the face.
### masks.py: Creates a copy of each image in CelebA such that a segment of interest (defined by landmarks) is show in pixel values of white (255) and the rest of the image is black (0).
___
## Data
The pre-generated data and CelebA can be found here: https://nevada.box.com/s/efvh8evc8ix1gmkpm9bgio2voxr3unhr
