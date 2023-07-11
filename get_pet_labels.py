#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
##
# Imports python modules
# To make a output directory 
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    # reading file names with os.listdir
    filename_list = listdir(image_dir)
    # making empty dict
    results_dic = dict() 
    
    for idx in range(0, len(filename_list), 1): 
        if filename_list[idx] not in results_dic: 
            if filename_list[idx][0] != ".":
                pet_image = filename_list[idx]
                low_pet_image = pet_image.lower()
                word_list_pet_image = low_pet_image.split("_")
                pet_name = " "
                for word in word_list_pet_image: 
                    if word.isalpha(): 
                        pet_name += word + " "
                # deleting space of first and end 
                pet_name = pet_name.strip()
            # name should be stored as a list since we are going to add more information as a list object to the dic in following keys. 
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_name]
              
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])
                
    return results_dic


