# PLAYLIST IN PYTHON
## Video Demo: 
## Description: 
This is a playlist application for your songs which is made using python programming language. The users can persistently store their favourite songs using this playlist. This playlist provides features to view your stored songs, add a song to your playlist, edit song name or artist name or both, delete a song in the playlist or clear list which deletes all songs in the user's playlist.
## Project Directory
### **playlist.csv**
This playlist uses a `.csv` file named `playlist.csv` to store the playlist data which is used by programe to view, add, edit, delete and clear songs in playlist
### **project.py**
The `project.py` file is the main programe and it contains the all the code of the playlist and features. Below is the description and explaination for all the function in `project.py file.

1. **main:** The main function contains a list variable named `list` and an int variable named `id` initialized to 0. The programme edits or maipulates this `list` variable according to user's input and then writes or rewrites `playlist.csv` file with the data of the list variable to persistently store the playlist data. The `id` variable is the id of the song in the playlist and the programme references this id which is associated with songs to manipulate songs.

    The main function creates the `playlist.csv` file if it is not present in the project's directory else it just store data in `playlist.csv` file to the `list` variable.

    The main function runs the programme in an infinite loop and the loop breaks when the user enters the exit key. Starting of this loop there is **Playlist Menu** which asks user for their input and shows menu in form of tables using `tabulate` library, apart from this, the infinite loop calls the functions to perform the task directed by the user.

2. **view_playlist:** The `view_playlist` function displays the songs in the `list` variable in the form of tables using `tabulate` library.

3. **add_song:** The `add_song()` function add a new song to the playlist. It takes `list` and `id` variable along with user entered song and artist and returns an incremented value of `id` variable by 1.

4. **compile_csv:** The `compile_csv()` function takes the `list` variable and rewrites `playlist.csv` file with the data of `list` variable.

5. **edit_song:** The `edit_song()` function takes `list` variable, an `edit_id` and a `new_song` both provided by the user. It then replaces the song in the `list` variable whose id matches with the `edit_id` with the `new_song`. It returns the edited `list` variable.

    Throws error if there is no song whose id matches with `edit_id` .

6. **edit_artist:** The `edit_artist()` function takes `list` variable, an `edit_id` and a `new_artist` both provided by the user. It then replaces the artist in the `list` variable whose id matches with the `edit_id` with the `new_artist`. It returns the edited `list` variable.
    
    Throws error if there is no artist whose id matches with `edit_id.`

7. **edit_list:** The `edit_list()` function takes `list` variable and `choice` provided by the user and calls `edit_song`, `edit_artist` or both according the `choice` provided by the user and returns the value returned by these functions. It also returns an unchanged `list` variable if user cancels edit or if the value of `choice` is invalid.

    Throws error if `edit_id` does not match id of the song or artist on the `list` variable.

8. **delete_song:** `The delete_song()` function takes `list` variable and `delete_song_id` which is provided by the user and then deletes the song whose id matches with `delete_song_id` in the `list` variable and then decrement id of all the songs below the deleted song by 1. Then it calls the `compile_csv()` function to update the playlist. Throws error if there is no song whose id matches with `delete_song_id`.

9. **clear_list:** The `clear_list()` function takes the `list` variable and deletes elements from second index or second element to the end index. It then calls `compile_csv` function and returns this edited list and an int whose value is 1.

### **test_project.py**
This file contains functions which tests all function in `project.py` file except `edit_list` and `main` function.

### **requirements.txt**
Contains dependencies for the project to run.


   

