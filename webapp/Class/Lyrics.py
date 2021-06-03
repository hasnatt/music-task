import requests, redis, json, re, nltk, csv
from datetime import timedelta
nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

redis_client = redis.Redis(host='localhost', port=6379,db=0)


"""
A Class to interact with the lyrics API and preform NLP
"""
class Lyrics:
    def __init__(self, artist, song):
        self.artist = artist.lower()
        self.song = song.lower()
        # add = CsvController(self.artist,self.song,self.remove_stop_words())

    def get_raw_lyrics(self):

        l = redis_client.get(redis_key(self.artist, self.song))

        if l != 'null':
            if l is None:
                url = f'https://api.lyrics.ovh/v1/{self.artist}/{self.song}'
                print(f'retrieving {self.song} by {self.artist}')
                try:
                    response = requests.request("GET", url)
                    body = json.loads(response.content)
                    # print(f'retrived lyrcis for {self.song} from API')
                    redis_client.set(redis_key(self.artist, self.song), json.dumps(body))
                    redis_client.expire(redis_key(self.artist, self.song), timedelta(days=7))
                    return(body)

                except Exception:
                    redis_client.set(redis_key(self.artist, self.song), 'null')
                    print(f'Error request for record: {self.song} by {self.artist}' )
            else:
                if l == 'null':
                    print('do nothing because blank')
                else:
                    return(json.loads(l))

        # with open('ec.json') as fp:
        #     body = json.load(fp)

    def string_lyrics(self):
        return(self.get_raw_lyrics()['lyrics'])


    def clean_lyrics(self):
        removed_control_char = re.sub(re.compile(r'[\n\r\t]'),' ', self.get_raw_lyrics()['lyrics'])
        cleaned = re.sub("[!,*)@#%(&$_?.^']",'', removed_control_char)
        cleaned = re.sub(r'\b\w{1,3}\b', '', cleaned)
        cleaned = cleaned.lower()
        return(cleaned)


    def remove_stop_words(self):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(self.clean_lyrics())
        stop_words = stopwords.words("english")
        filtered_lyrics = [
        w for w in tokens
        if not w in stop_words]

        return(filtered_lyrics)

def redis_key(artist, song):
    a = artist.replace(" ", "_")
    s = song.replace(" ", "_")
    return(f'{a}-{s}')



def add_to_csv(artist, song, bagofwords):
    with open('lyric_words.csv', 'a') as f:
        fieldnames = ['id', 'artist', 'song', 'lyrics_bow']
        writer = csv.DictWriter(f, fieldnames)
        writer.writerow({
            'id': f'{artist}+{song}',
            'artist': artist,
            'song': song,
            'lyrics_bow': bagofwords})

# def clean_csv(self):
#     self.add_to_csv()
#     df = pd.read_csv('lyric_words.csv', delimiter=',')