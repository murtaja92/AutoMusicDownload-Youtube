
from youtube_search import YoutubeSearch
import os
import iGetMusic as iGet
import subprocess
import time
SearchQ = input("Enter Search:")
search = SearchQ + " lyric music" 
country = "US"
cmd = './yt-dlp_linux -x -o "sounds/%(title)s.%(ext)s" --audio-format mp3 --no-keep-fragments https://www.youtube.com'
artist = iGet.getArtist(term=search,  explicit=False) #country="US",
song = iGet.get(term=search,  explicit=True)
import json
def download(url):
    os.system(url)
    time.sleep(20.5)
def itube(fname):
  results = YoutubeSearch(fname + ' lyric', max_results=20).to_json()
  data = json.loads(results)
  for element in data['videos']:
      download(cmd+element['url_suffix'])
for val in song:
     latr = val.getName() + " " + val.getArtistName()
     print(latr)
     itube(latr)