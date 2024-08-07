# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:57:27 2024

@author: Austin
"""
import ReadWrite
import DisplayVideos

def delete_video():
    """
    Deletes a video from the video list based on the inputted index.

    """

    video_list = ReadWrite.read_file()
    DisplayVideos.display_videos()
    print()
    
    while True:   
    
        try:
            choice = (int(input("Enter the movie index: ")) -1)
            
            if 0 <= choice < len(video_list):
            
                video_list.pop(choice)
                
                ReadWrite.write_file(video_list)
                
                print("Video has been deleted.")
                
                break
                
            else:
                ("Index out of range. Please enter a valid index.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")