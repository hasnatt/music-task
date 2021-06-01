import json
import musicbrainzngs


class MusicBrainz:
    
    musicbrainzngs.set_useragent("Example music app", "0.1", "http://hasnat.io")

    def __init__(self, id):
        self.id = id

    def get_artist_data(self):
        artist = musicbrainzngs.get_artist_by_id(id=self.id)
        return(artist)

    def get_song_list(self):
        releases = musicbrainzngs.browse_releases(artist=self.id)  
        releases = releases['release-list']
        songs_list = []
        for song in releases:
            songs_list.append(song['title'].lower())
        return(list(dict.fromkeys(songs_list)))  

    def get_artist_name(self):
        return(self.get_artist_data()['artist']['name'])    