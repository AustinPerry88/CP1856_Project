# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:28 2024

@author: shang
"""

from ReadWrite import get_all_videos, save_all_videos
import display_videos

def edit_video():
    videos = get_all_videos()
    display_videos.display_videos()
    index = int(input("Enter the index of the video to edit: ")) - 1

    if 0 <= index < len(videos):
        new_title = input(f"Enter new title ({videos[index][0]}): ") or videos[index][0]
        new_director = input(f"Enter new director ({videos[index][1]}): ") or videos[index][1]
        new_release_year = input(f"Enter new release year ({videos[index][2]}): ") or videos[index][2]
        new_genre = input(f"Enter new genre ({videos[index][3]}): ") or videos[index][3]
        new_duration = input(f"Enter new duration ({videos[index][4]}): ") or videos[index][4]

        videos[index] = [new_title, new_director, new_release_year, new_genre, new_duration]
        save_all_videos(videos)
        print("Video edited successfully!")
    else:
        print("Invalid index!")
