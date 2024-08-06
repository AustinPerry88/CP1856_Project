# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:15 2024

@author: shang
"""

from ReadWrite import get_all_videos, save_all_videos

def add_video():
    videos = get_all_videos()
    title = input("Enter video title: ")
    director = input("Enter director: ")
    release_year = input("Enter release year: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration (in minutes): ")

    video = [title, director, release_year, genre, duration]
    videos.append(video)
    save_all_videos(videos)
    print("Video added successfully!")
