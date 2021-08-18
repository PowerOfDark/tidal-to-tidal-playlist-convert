import tidalapi
session = tidalapi.Session()
session.login_oauth_simple()
session2 = tidalapi.Session()
session2.login_oauth_simple()
id1 = session.user.id
id2 = session2.user.id
fav = tidalapi.Favorites(session, id1)
fav2 = tidalapi.Favorites(session2, id2)
tracks = fav.tracks()
a = []
i = 0
b = 0
for track in tracks:
    try:
        print(track.name)
        fav2.add_track(track.id)
        i += 1
    except Exception as e:
        print(e)
        a.append((track.id) + " // " + (track.name))
        b += 1
print(i)
print(a)
print(b)
fav3 = tidalapi.Favorites(session2, id2)
tracks3 = fav3.tracks()
count = 0
for track in tracks:
    count += 1
print(str(count) + " on 2nd acc")
