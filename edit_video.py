# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:28 2024

@author: shang
"""

import ReadWrite
import DisplayVideos

def edit_video():
    """
   Edits a video from the video list based on the inputted index.

   """
    video_list = ReadWrite.read_file()
    DisplayVideos.display_videos()
    print()
    index = int(input("Enter the index of the video to edit: ")) - 1

    if 0 <= index < len(video_list):
        new_title = input(f"Enter new title ({video_list[index][0]}): ") or video_list[index][0]
        new_director = input(f"Enter new director ({video_list[index][1]}): ") or video_list[index][1]
        new_release_year = input(f"Enter new release year ({video_list[index][2]}): ") or video_list[index][2]
        new_genre = input(f"Enter new genre ({video_list[index][3]}): ") or video_list[index][3]
        new_duration = input(f"Enter new duration ({video_list[index][4]}): ") or video_list[index][4]

        video_list[index] = [new_title, new_director, new_release_year, new_genre, new_duration]
        ReadWrite.write_file(video_list)
        print("Video edited successfully!")
    else:
        print("Invalid index!")
