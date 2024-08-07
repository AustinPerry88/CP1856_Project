# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:19:36 2024

@author: shang
"""
import add_video
import edit_video
# import delete_video
import display_videos
# import display_detailed_video
import list_by_criteria


def display_menu():
    print("Welcome to the Video Library Management System!")
    print("Choose from the options below:\n")
    print("1. Add new video.")
    print("2. Edit video.")
    print("3. Delete video.")
    print("4. Display all videos by name.")
    print("5. Display detailed video information.")
    print("6. List videos by criteria.")
    print("7. Exit.")


def main():
    display_menu()
    while True:
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_video.add_video()
        elif choice == '2':
            edit_video.edit_video()
        elif choice == '3':
            delete_video.delete_video()
        elif choice == '4':
            display_videos.display_videos()
        elif choice == '5':
            display_detailed_video.display_detailed_video()
        elif choice == '6':
            list_by_criteria.list_by_criteria()
        elif choice == '7':
            print("Thank you for using the Video Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            

