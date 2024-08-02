# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:19:36 2024

@author: shang
"""

import csv
FILENAME = "movielist.csv"


def display_menu():
    print("Welcome to the Video Library Management System!")
    print("Choose from the options below:\n")
    print("1. Add new video.")
    print("2. Edit video.")
    print("3. Delete video.")
    print("4. Display all videos by name.")
    print("5. Display detailed video information.")
    print("6. List videos by criteria.")
    print("7. Exit.\n")

def save_all_videos(videos):
    with open(FILENAME, 'w') as file:
        for video in videos:
            title = video[0]
            director = video[1]
            release_year = video[2]
            genre = video[3]
            duration = video[4]
            file.write(f"{title}#{director}#{release_year}#{genre}#{duration}\n")


def get_all_videos():
    videos = []
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                s = line.split("#")
                title = s[0]
                director = s[1]
                release_year = int(s[2])
                genre = s[3]
                duration = int(s[4])
                videos.append([title, director, release_year, genre, duration])
        return videos
    except FileNotFoundError:
        return videos
    
def add_video():
    videos = get_all_videos()
    title = input("Enter video title: ")
    director = input("Enter director: ")
    release_year = int(input("Enter release year: "))
    genre = input("Enter genre: ")
    duration = int(input("Enter duration (in minutes): "))

    video = [title, director, release_year, genre, duration]
    videos.append(video)
    save_all_videos(videos)
    print("Video added successfully!")
    
def edit_video():
    videos = get_all_videos()
    display_videos()
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
        
def display_videos():
    videos = get_all_videos()
    if not videos:
        print("No videos in the library.")
    else:
        for i, video in enumerate(videos, start=1):
            print(f"{i}. {video[0]}")
            

