# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:57:51 2024

@author: Austin
"""

import ReadWrite

def display_videos():
    """
    Displays the title of all videos in the list.

    """
    video_list = ReadWrite.read_file()
    counter = 1 
    
   
    if not video_list:
        print("Video list is empty.")
        return
        
            
    for video in video_list:
                
        print(f"{counter}. {video[0]}")
        counter += 1
            