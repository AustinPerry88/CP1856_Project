# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:58:09 2024

@author: Austin
"""

import ReadWrite

def video_info():
    """
    Displays the full information of all videos in the video list.

    """   
    
    video_list = ReadWrite.read_file()
    
    while True:   
    
        try:
            choice = (int(input("Enter the movie index: ")) -1)
            
            if 0 <= choice < len(video_list):
            
                print(f"Title: {video_list[choice][0]}")
                print(f"Director: {video_list[choice][1]}")
                print(f"Release Year: {video_list[choice][2]}")
                print(f"Genre: {video_list[choice][3]}")
                
                hours = int(video_list[choice][4]) // 60
                minutes = int(video_list[choice][4]) % 60
                
                print(f"Duration: {hours} Hours {minutes} minutes")
                
                break
                
            else:
                print("Index out of range. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")