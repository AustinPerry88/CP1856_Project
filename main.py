# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:19:36 2024

@author: shang
"""
import add_video
import edit_video
import DeleteVideo
import DisplayVideos
import VideoInfo
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
        print()
  
        if choice == '1':
            add_video.add_video()
        elif choice == '2':
            edit_video.edit_video()
        elif choice == '3':
            DeleteVideo.delete_video()
        elif choice == '4':
            DisplayVideos.display_videos()
        elif choice == '5':
            VideoInfo.video_info()
        elif choice == '6':
            list_by_criteria.list_by_criteria()
        elif choice == '7':
            print("Thank you for using the Video Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            

