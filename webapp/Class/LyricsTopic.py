import json
import requests 


class LyricsTopic:
    def __init__(self,artist,song,amount):
        self.artist = artist
        self.song = song
        self.amount = amount


    def get_reccommendations(self):
        # return(f'Blah {self.artist} {self.song}')
        url = f'https://kxk44df7n2.execute-api.eu-west-2.amazonaws.com/test/transactions?artist={self.artist}&song={self.song}&amount={self.amount}'
        try:
            response = requests.get(url)
            body = json.loads(response.content)
            
        except Exception:
            print(f'Error request for record: {self.song} by {self.artist}' )

        # with open('ec.json') as fp:
        #     body = json.load(fp)
        return(body)