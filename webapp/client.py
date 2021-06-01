from flask import Flask, redirect, url_for, render_template, request
from Class.LyricsTopic import *
from Class.Lyrics import *
from Class.MusicBrainzSearch import *
from Class.MusicBrainz import *
app = Flask(__name__)


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

    table = []
    total_words = 0
    for song in songs:
        lyrics = Lyrics(music_artist.get_artist_name(), song)
        total_words +=lyrics.number_of_word()
        table.append(
            {
                'song': song,
                'word_count': lyrics.number_of_word()
            }
        )
    average = float(total_words) / float(len(songs))

    print(table)

    # print(total_words)
    # print(len(songs))
    # print(average)
    return render_template('average.html',artist=music_artist.get_artist_name(), id=id, average=average, table=table)



if __name__ == '__main__':
    app.run(debug=True)    