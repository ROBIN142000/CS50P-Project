from tabulate import tabulate
import csv, sys, os

def view_playlist(list, playlist_present):
    try:
        if not playlist_present:
            print(tabulate(list[2:], headers=list[0], tablefmt="fancy_grid"))
        else:
            print(tabulate(list[1:], headers=list[0], tablefmt="fancy_grid"))
    except IndexError:
        print("\nNo song added")

def add_song(id, list):
    song = "Baby" #input("song: ")
    artist = "Justin Beiber" #input("Artist (optional): ")

    list.append( [f"{id}", f"{song}", f"{artist}"] )
    compile_csv(list)
    return int(id)+1

def compile_csv(list):
    with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            for i in range(1, len(list)):
                writer.writerow([f"{list[i][0]}", f"{list[i][1]}", f"{list[i][2]}"])

def edit_song(list):
    edit_id = int(input("Enter id of song which you want to edit "))
    new_song = input("Type new song ")
    list[edit_id+1][1] = new_song
    return list

def edit_artist(list):
    edit_id = int(input("Enter id of artist which you want to edit "))
    new_artist = input("Type new artist ")
    list[edit_id+1][2] = new_artist
    return list

def edit_list(list):
    choice_table = [ ["Key", "Action"], ["1", "Edit Song"], ["2", "Add Artist"], ["3", "Edit Song and Artist both"], ["4", "Go back"] ]
    print(tabulate(choice_table[1:], headers=choice_table[0], tablefmt= "rounded_grid"))
    choice = input("What do you want to edit ? ")

    match choice:
        case "1":
            return edit_song(list)

        case "2":
            return edit_artist(list)
        
        case "3":
            list = edit_song(list)
            return edit_artist(list)

        case "4":
            return list

        case _:
            print("Invalid Input")
            return list


def main():
    list = []
    id = 0
    playlist_present = True

    if not os.path.isfile("playlist.csv"):
        with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            writer.writerow(["Id", "Song", "Artist"])
            list.append( ["Id", "Song", "Artist"] )

        playlist_present = False

    with open("playlist.csv") as existing_playlist:
        reader = csv.reader(existing_playlist)
        if playlist_present:
            num = -1
        else:
            num = 0
        for iD, song, artist in reader:
            num+=1
            list.append(
                [iD, song, artist]
            )
        id = num
        print(list)
        
    while True:
        
        home = [["Key", "Action"], ["1", "View Playlist"], ["2", "Add Song"], ["3", "Edit list"], ["4", "Delete Song"], ["5", "Exit Program"]]

        print(tabulate(home[1:], headers=home[0], tablefmt= "heavy_grid"))

        inp = input("Input: ")

        if inp == "5":
            sys.exit("\nExited")
        elif inp == "1":
            view_playlist(list, playlist_present)
        elif inp == "2":
            id = add_song(id, list)
        elif inp == "3":
            list = edit_list(list)
            compile_csv(list)

if __name__ == "__main__":
    main()