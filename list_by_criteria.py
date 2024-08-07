# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:39:52 2024

@author: shang
"""


import ReadWrite

def list_by_criteria():
    criteria = {
        "1": "director",
        "2": "release year",
        "3": "genre",
        "4": "duration"
    }

    print("The following criteria is available:")
    print("1. Director")
    print("2. Release Year")
    print("3. Genre")
    print("4. Duration")
    print()
    choice = input("Enter criteria: ")

    if choice in criteria:
        video_list = ReadWrite.read_file()
        unique_values = sorted(set(video[int(choice)].lower() for video in video_list))
        
        print()
        print(f"You selected {criteria[choice]}. The list of available {criteria[choice]}s is below:")
        for i, unique_value in enumerate(unique_values, start=1):
           print(f"{i}. {unique_value}")

        print()
        selection = int(input("Enter selection: ")) - 1

        if 0 <= selection < len(unique_values):
           selected_value = unique_values[selection]
           results = [video for video in video_list if video[int(choice)].lower() == selected_value]

           if results:
               for result in results:
                   print(f"{result[0]}")
           else:
               print("No videos found.")
        else:
           print("Invalid selection.")
    else:
       print("Invalid criteria.")
