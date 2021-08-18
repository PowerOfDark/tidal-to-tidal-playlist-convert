import tidalapi

# import os, ssl


def get_playlist_tag(dst: tidalapi.Session, playlist_id):
    ret = dst.request("GET", f"playlists/{playlist_id}")
    return ret.headers["Etag"].strip(' "')


def add_playlist_items(dst: tidalapi.Session, playlist_id, items: list, position=0):
    ret = dst.request(
        "POST",
        f"playlists/{playlist_id}/items",
        data=dict(trackIds=",".join(items), toIndex=position),
        headers={"If-None-Match": get_playlist_tag(dst, playlist_id)},
    )
    return ret


def create_playlist(dst: tidalapi.Session, name):
    ret = dst.request(
        "POST",
        f"users/{dst.user.id}/playlists",
        data=dict(title=name, description=""),
    )
    my_playlists = dst.get_user_playlists(dst.user.id)
    dst_playlist = next((p for p in my_playlists if p.name == name), None)
    return dst_playlist


def copy_playlist(dst: tidalapi.Session, playlist):
    print(f"Copying playlist {playlist.name}")
    my_playlists = dst.get_user_playlists(dst.user.id)
    dst_playlist = next((p for p in my_playlists if p.name == playlist.name), None)
    if dst_playlist:
        print("\tAlready exists!")
        return
    dst_playlist = create_playlist(dst, playlist.name)
    tracks = dst.get_playlist_tracks(playlist.id)
    for track in tracks:
        print(f"\t{track.name}")
    trackIds = [str(t.id) for t in tracks]
    return add_playlist_items(dst, dst_playlist.id, trackIds)


session = tidalapi.Session()
session.login_oauth_simple()
session2 = tidalapi.Session()
session2.login_oauth_simple()
id1 = session.user.id
id2 = session2.user.id
fav = tidalapi.Favorites(session, id1)
fav2 = tidalapi.Favorites(session2, id2)
playlists = session.get_user_playlists(id1)
for playlist in playlists:
    print(playlist.id + " // " + playlist.name)
    copy_playlist(session2, playlist)
