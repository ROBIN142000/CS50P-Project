from project import add_song, edit_list, edit_artist, edit_song, compile_csv, clear_list, delete_song
import csv



def test_add_song():
    list = [ ["Id", "Song", "Artist"] ]
    assert add_song(1, list, "Animals", "Martin Garrix" ) == 2
    assert add_song(1, list, "1", "2" ) == 2

def test_compile_csv():
    existing_list = [ ["Id", "Song", "Artist"], ["1", "Animals", "Martin Garrix"] ]
    new_list = []
    compile_csv(existing_list)

    with open("playlist.csv") as existing_playlist:
        reader = csv.reader(existing_playlist)
        for iD, song, artist in reader:
            new_list.append( [iD, song, artist] )

    assert existing_list == new_list

def test_edit_song():
    list = [ ["Id", "Song", "Artist"], ["1", "Animals", "Martin Garrix"] ]
    assert edit_song(list, "1", "so far away") == [ ["Id", "Song", "Artist"], ["1", "so far away", "Martin Garrix"] ]
    assert edit_song(list, "2", "SO FAR AWAY") == list
    

def test_edit_artist():
    list = [ ["Id", "Song", "Artist"], ["1", "Animals", "Martin Garrix"], ["2", "so far away", "Martin Garrix"] ]
    assert edit_artist(list, "1", "Justin Beiber") == [ ["Id", "Song", "Artist"], ["1", "Animals", "Justin Beiber"], ["2", "so far away", "Martin Garrix"] ]
    assert edit_artist(list, "3", "Justin Beiber") == list

def test_clear_list():
    list = [ ["Id", "Song", "Artist"], ["1", "Animals", "Martin Garrix"], ["2", "so far away", "Martin Garrix"] ]
    assert clear_list(list) == ([ ["Id", "Song", "Artist"] ], 1)

def test_delete_song():
    list = [ 

        ["Id", "Song", "Artist"],
        ["1", "Animals", "Martin Garrix"],
        ["2", "so far away", "Martin Garrix"],
        ["3", "Decadence", "Disturbed"]

          ]
    
    assert delete_song(list, 2) == ([['Id', 'Song', 'Artist'], ['1', 'Animals', 'Martin Garrix'], [2, 'Decadence', 'Disturbed']], 2)
    assert delete_song([ ["Id", "Song", "Artist"] ], 1) == ([ ["Id", "Song", "Artist"] ], 1)
    