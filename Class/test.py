from lyrics import *
# from ldacontroller import *

# df = pd.read_csv ('grammySongs_1999-2019.csv')

# for index, row in df.iterrows():
#     try:
#         Lyrics(row['Artist'], row['Name'])
#         print(f"added {row['Artist']} {row['Name']}")
        
#     except:
#         pass    


song_lyrics = Lyrics('Kid Cudi', 'Sad People')
print(song_lyrics.number_of_word())

# runLDA = Ldacontroller(5)

