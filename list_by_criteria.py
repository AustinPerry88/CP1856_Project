# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:52 2024

@author: shang
"""

from ReadWrite import get_all_videos

def list_videos_by_criteria():
    criteria = {
        "1": "director",
        "2": "release_year",
        "3": "genre",
        "4": "duration"
    }

    print("The following criteria is available:")
    print("1. Director")
    print("2. Release Year")
    print("3. Genre")
    print("4. Duration")
    choice = input("Enter criteria: ")

    if choice in criteria:
        value = input(f"You selected {criteria[choice]}. Enter the value to search: ")
        videos = get_all_videos()
        results = [video for video in videos if video[int(choice) - 1].lower() == value.lower()]

        if results:
            for video in results:
                print(f"{video[0]}")
        else:
            print("No videos found.")
    else:
        print("Invalid criteria.")
