from tabulate import tabulate
import csv, os


def view_playlist(list):
    print("\n Your Playlist")
    try:
        print(tabulate(list[1:], headers=list[0], tablefmt="fancy_grid"))
    except IndexError:
        print("\nNo song added")

def add_song(id, list, song, artist):

    list.append( [f"{id}", f"{song}", f"{artist}"] )
    compile_csv(list)
    return int(id)+1

def compile_csv(list):
    with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            for i in range(0, len(list)):
                writer.writerow([f"{list[i][0]}", f"{list[i][1]}", f"{list[i][2]}"])

def edit_song(list, edit_id, new_song):
    try:
        list[int(edit_id)][1] = new_song
    except IndexError:
        print("\nInvalid Id")
        return list
    
    return list

def edit_artist(list, edit_id, new_artist):
    try:
        list[int(edit_id)][2] = new_artist
    except IndexError:
        print("\nInvalid Id")
        return list
    
    return list

def edit_list(list, choice):
    match choice:
        case "1":
            try:
                edit_id = int(input("Enter id of song which you want to edit: ").strip())
            except ValueError:
                print("\nId must be integer")
                return list
            new_song = input("Type new song: ")
            return edit_song(list, edit_id, new_song)

        case "2":
            try:
                edit_id = int(input("Enter id of artist which you want to edit: ").strip())
            except ValueError:
                print("\nId must be integer")
                return list
            new_artist = input("Type new artist: ").strip()
            return edit_artist(list, edit_id, new_artist)
        
        case "3":
            try:
                edit_id = int(input("Enter id of song which you want to edit: ").strip())
            except ValueError:
                print("\nId must be integer")
                return list
            new_song = input("Type new song: ")
            list = edit_song(list, edit_id, new_song)
            try:
                edit_id = int(input("Enter id of artist which you want to edit: ").strip())
            except ValueError:
                print("\nId must be integer")
                return list
            new_artist = input("Type new artist: ").strip()
            return edit_artist(list, edit_id, new_artist)

        case "4":
            return list

        case _:
            print("Invalid Input")
            return list

def delete_song(list, delete_song_id):
    id = 0
    try:
        list.pop(delete_song_id)
    except IndexError:
        print("\nList is Empty or Invalid Id")
        return list, 1

    for iteration in range(delete_song_id, len(list)):
        new_id = int(list[iteration][0]) - 1 
        list[iteration][0] = new_id
        id = new_id

    compile_csv(list)
    return list, id

def clear_list(list):
    del list[1:len(list)]
    compile_csv(list)

    return list, 1

def main():
    list = []
    id = 0

    if not os.path.isfile("playlist.csv"):
        with open("playlist.csv", 'w', newline='') as playlist:
            writer = csv.writer(playlist)
            writer.writerow(["Id", "Song", "Artist"])


    with open("playlist.csv") as existing_playlist:
        reader = csv.reader(existing_playlist)
        for iD, song, artist in reader:
            id+=1
            list.append(
                [iD, song, artist]
            )
        
    while True:
        
        home = [["Key", "Action"], ["1", "View Playlist"], ["2", "Add Song"], ["3", "Edit list"], ["4", "Delete Song"], ["5", "Clear List"], ["6", "Exit Program"]]

        print("\nMain Menu")
        print(tabulate(home[1:], headers=home[0], tablefmt= "heavy_grid"))

        inp = input("Input: ").strip()

        match inp:
            case "1":
                view_playlist(list)
                input("Press any Enter to go to Menu: ")

            case "2":
                song = input("song: ").strip()
                artist = input("Artist (Click enter if you don't want to specify): ").strip()
                id = add_song(id, list, song, artist)

            case "3":
                print("\n Edit List")
                choice_table = [ ["Key", "Action"], ["1", "Edit Song"], ["2", "Add Artist"], ["3", "Edit Song and Artist both"], ["4", "Go back"] ]
                print(tabulate(choice_table[1:], headers=choice_table[0], tablefmt= "rounded_grid"))
                choice = input("What do you want to edit ? : ").strip()
                list = edit_list(list, choice)
                compile_csv(list)

            case "4":
                try:
                    delete_song_id = int(input("Enter id of song you want to delete: ").strip())
                    list, id = delete_song(list, delete_song_id)
                except ValueError:
                    print("\nId must be integer")

            case "5":
                confirm = input("Are you sure ?\nPress y for Yes and n for No: ").strip()
                try:
                    list, id = clear_list(list) if confirm.lower() == "y" else confirm
                except ValueError:
                    pass
                    
            case "6":
                print("Exited")
                break

            case _:
                input("Invalid input\nPress any key to go to Menu")

if __name__ == "__main__":
    main()