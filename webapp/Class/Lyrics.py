import requests
import re 
import json
import nltk
nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
# from csvcontroller import *

"""
A Class to interact with the lyrics API and preform NLP
"""
class Lyrics:
    def __init__(self, artist, song):
        self.artist = artist.lower()
        self.song = song.lower()
        # add_csv = Csvcontroller(self.artist,self.song,self.remove_stop_words())

    def get_raw_lyrics(self):
        
        # url = f'https://api.lyrics.ovh/v1/{self.artist}/{self.song}'
        # try:
        #     response = requests.request("GET", url)
        #     body = json.loads(response.content)
            
        # except Exception:
        #     print(f'Error request for record: {self.song} by {self.artist}' )

        with open('ec.json') as fp:
            body = json.load(fp)
        return(body)

    def clean_lyrics(self):
        removed_control_char = re.sub(re.compile(r'[\n\r\t]'),' ', self.get_raw_lyrics()['lyrics'])
        cleaned = re.sub("[!,*)@#%(&$_?.^']",'', removed_control_char)
        cleaned = re.sub(r'\b\w{1,2}\b', '', cleaned)
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


    def number_of_word(self):
        removed_control_char = re.sub(re.compile(r'[\n\r\t]'),' ', self.get_raw_lyrics()['lyrics'])
        words = len(removed_control_char.split())
        return(words)

