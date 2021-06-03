import csv
import pandas as pd


class CsvController:
    def __init__(self, artist, song, bagofwords):
        self.artist = artist
        self.song = song
        self.bagofwords = bagofwords
        self.clean_csv()

    def add_to_csv(self):
        with open('lyric_words.csv', 'a') as f:
            fieldnames = ['id', 'artist', 'song', 'lyrics_bow']
            writer = csv.DictWriter(f, fieldnames)
            writer.writerow({
                'id': f'{self.artist}+{self.song}',
                'artist': self.artist,
                'song': self.song,
                'lyrics_bow': self.bagofwords})

    def clean_csv(self):
        self.add_to_csv()
        df = pd.read_csv('lyric_words.csv', delimiter=',')



        # dropping ALL duplicte values
        df =df.drop_duplicates()
        df.to_csv('lyric_words.csv', index=False)

