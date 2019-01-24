import tidalapi
session = tidalapi.Session()
u1 = input("Enter username of account you are copying from.")
p1 = input("Enter password of account you are copying from.")
session.login(u1,p1)
u2 = input("Enter username of account you are copying to.")
p2 = input("Enter password of account you are copying to.")
session2 = tidalapi.Session()
session2.login(u2,p2)
id1 = input("Enter the user.id of the 1st account.") # Found by using Fiddler or somewhere in inspect element.
id2 = input("Enter the user.id of the 2nd account.") # Found by using Fiddler or somewhere in inspect element.
fav = tidalapi.Favorites(session, id1)
fav2 = tidalapi.Favorites(session2, id2)
tracks = fav.tracks()
for track in tracks:
    print(track.id)
    fav2.add_track(track.id)
