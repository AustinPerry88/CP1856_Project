import csv

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
    with open("movielist.csv", 'w') as file:
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
        with open("movielist.csv", 'r') as file:
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



