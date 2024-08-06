# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:12:01 2024

@author: shang
"""

from ReadWrite import get_all_videos

def display_videos():
    videos = get_all_videos()
    if len(videos) == 0:
        print("No videos in the library.")
    else:
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video[0]}")
