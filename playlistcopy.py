import tidalapi
#import os, ssl

session = tidalapi.Session()
u1 = raw_input("Enter username of account you are copying from.")
p1 = raw_input("Enter password of account you are copying from.")
session.login(u1,p1)
u2 = raw_input("Enter username of account you are copying to.")
p2 = raw_input("Enter password of account you are copying to.")
session2 = tidalapi.Session()
session2.login(u2,p2)
id1 = session.user.id
id2 = session2.user.id
fav = tidalapi.Favorites(session, id1)
fav2 = tidalapi.Favorites(session2, id2)
playlists = session.get_user_playlists(id1)
for playlist in playlists:
    print(playlist.id + ' // ' + playlist.name)
play1 = raw_input('input playlist id that you want to copy: ')

tracks = session.get_playlist_tracks(play1)

playlists2 = session.get_user_playlists(id2)
for playlist2 in playlists2:
    print(playlist2.id + ' // ' + playlist2.name)
play2 = raw_input('input playlist id that you want to copy to: ')

tracks = fav.tracks()
for track in tracks:
    print(track.id)
    fav2.add_to_playlist(track.id, play2) # https://github.com/SimDoes/python-tidal
