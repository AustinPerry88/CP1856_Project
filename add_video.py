# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:15 2024

@author: shang
"""

import ReadWrite

def add_video():
    """
   Adds a video from the video list based on the inputted index.

   """
    video_list = ReadWrite.read_file()
    title = input("Enter video title: ")
    director = input("Enter director: ")
    release_year = input("Enter release year: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration (in minutes): ")

    video = [title, director, release_year, genre, duration]
    video_list.append(video)
    ReadWrite.write_file(video_list)
    print("Video added successfully!")
