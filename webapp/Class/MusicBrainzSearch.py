import musicbrainzngs
import json

class MusicBrainzSearch:
    
    musicbrainzngs.set_useragent("Example music app", "0.1", "http://hasnat.io")

    def __init__(self, artist):
        self.artist = artist
    

    def get_artists(self):
        results = musicbrainzngs.search_artists(artist = self.artist, limit = 4)

        # for artist in results['artist-list']:
        #     print(f"Name: {artist['name']} - ID :{artist['id']}")
        return(results['artist-list'])
       


# x = musicbrainzngs.get_artist_by_id(id='9fff2f8a-21e6-47de-a2b8-7f449929d43f')
# print(x)

# releases = musicbrainzngs.browse_releases(artist='9fff2f8a-21e6-47de-a2b8-7f449929d43f')

# for release in releases['release-list']:
#     print(release['title'])


# with open('release_data.json', 'w') as fp:
#     json.dump(releases, fp)