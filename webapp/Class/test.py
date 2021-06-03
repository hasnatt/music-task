# from MusicBrainz import *
# from Lyrics import *
from LdaController import *

from CsvController import *
import redis, json
# search = MusicBrainz('Kid Cudi')
# search.get_artists()

# redis_client = redis.Redis(host='localhost', port=6379,db=0)
#
# test = redis_client.get('myname')
#
# redis_client.set('msft',json.dumps({"pe":33}))
#
# print(test)

# x= Lyrics('coldplay', 'Yellow')
# x.get_raw_lyrics()

x = LdaController(5)


# z = CsvController('hasnat', 'a song', '[1,23]')