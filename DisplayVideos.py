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
    video_list = ReadWrite.read_file('TestList.csv')
    
    
   
    if not video_list:
        print("Video list is empty.")
        return
        
            
    for i, video in enumerate(video_list, start=1):
            print(f"{i}. {video[0]}")
            