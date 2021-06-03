from flask import Flask, redirect, url_for, render_template, request
from Class.LyricsTopic import *
from Class.Lyrics import *
from Class.MusicBrainzSearch import *
from Class.MusicBrainz import *
import pandas as pd
import os
app = Flask(__name__)


@app.route('/lda_output')
def lda_output():

    return render_template('lda_output.html')

@app.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        artist = request.form['artist']
        mb = MusicBrainzSearch(artist)
        search_query = mb.get_artists()

        # print(search_query)

    else:
        return render_template('index.html')
    return render_template('index.html', artists=search_query)

@app.route('/lyrics', methods = ['GET','POST'])
def lyrics():
    if request.method == 'POST':
        artist = request.form['artist']
        song = request.form['song']
        amount = request.form['amount']

        song_request = LyricsTopic(artist, song, amount)
        reccommened_songs = song_request.get_reccommendations()

    else:
        return render_template('lyrics.html')

    return render_template('lyrics.html', topic=reccommened_songs['queried_topic'], songs=reccommened_songs['recommended_songs'])


@app.route('/avg/<id>', methods = ['GET','POST'])
def avg_words(id):

    music_artist = MusicBrainz(id)
    songs = music_artist.get_song_list()
    print(songs)

    table = []
    total_words = 0
    for song in songs:
        print(song)
        try:
            lyrics = Lyrics(music_artist.get_artist_name(), song)
            total_words +=number_of_word(lyrics.get_raw_lyrics()['lyrics'])
            add_to_csv(music_artist.get_artist_name(), song, lyrics.remove_stop_words())
            table.append(
                {
                    'song': song,
                    'word_count': number_of_word(lyrics.get_raw_lyrics()['lyrics'])
                })

            print(table)
        except Exception as e:
            print('Error', e)


    average = 0
    if (len(songs) == 0):
        average ==0
    else:
        average = float(total_words) / float(len(table))

    print(table)

    # print(total_words)
    # print(len(songs))
    # print(average)
    return render_template('average.html',artist=music_artist.get_artist_name(), id=id, average=average, table=table)


def number_of_word(lyrics):
    # removed_control_char = re.sub(re.compile(r'[\n\r\t]'),' ', self.get_raw_lyrics()['lyrics'])
    words = len(lyrics.split())
    return(words)

def add_to_csv(artist, song, bagofwords):
    with open('lyric_words.csv', 'a') as f:
        fieldnames = ['id', 'artist', 'song', 'lyrics_bow']
        writer = csv.DictWriter(f, fieldnames)
        writer.writerow({
            'id': f'{artist.lower()}+{song.lower()}',
            'artist': artist.lower(),
            'song': song.lower(),
            'lyrics_bow': bagofwords})
    df = pd.read_csv('lyric_words.csv', delimiter=',')
    df = df.drop_duplicates()
    df.to_csv('lyric_words.csv', index=False)

if __name__ == '__main__':
    app.run(debug=True)