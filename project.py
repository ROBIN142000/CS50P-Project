from tabulate import tabulate
import csv, sys, os

def view_playlist(list):
    try:
        print(tabulate(list[1:], headers=list[0], tablefmt="fancy_grid"))
    except IndexError:
        print("\nNo song added")

def add_song(id):
    song = input("song: ")
    artist = input("Artist (optional): ")
    
    with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            writer.writerow([id+1, song, artist])
    

def main():
    list = []
    id = 0

    if not os.path.isfile("playlist.csv"):
        with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            writer.writerow(["Id", "Song", "Artist"])
        
    while True:
        
        home = [["Key", "Action"], ["1", "View Playlist"], ["2", "Add Song"], ["3", "Edit list"], ["4", "Delete Song"], ["5", "Exit Program"]]

        print(tabulate(home[1:], headers=home[0], tablefmt= "grid"))

        inp = input("Input: ")

        sys.exit("\nExited") if inp == "5" else inp
        view_playlist(list) if inp == "1" else inp
        add_song(id) if inp == 2 else inp

if __name__ == "__main__":
    main()