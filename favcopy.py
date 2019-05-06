import tidalapi
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
tracks = fav.tracks()
for track in tracks:
    print(track.id)
    fav2.add_track(track.id)
