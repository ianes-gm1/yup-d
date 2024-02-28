
""" 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ #Yup-d ver. 1.2                                                          │
  └──────────────────────────────────────────────────────────────────────────┘
 """

from pytube import *
import logging
import subprocess
import argparse

#lllllog format
logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

#arguments, arguments ohh arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest='URL', help="URL to the youtube playlist e.g.https://www.youtube.com/playlist?list=PLU1WuLg45SiyrXahjvFahDuA060P487pV")
parser.add_argument(dest='Output_location', help=r"Output location e.g.C:\Users\Default\Music")
parser.add_argument(dest='Format', help="Formats -type of format for your download / Formats available- MP3;MP4 ")
args = parser.parse_args()

#gets rid off all the bad stuff
def title_swap(title):
     new_title = title.translate(str.maketrans('', '', "|\?/_:,#*()[]{}'"))
     return new_title

#believe this is self explanatory
def Download_Process(URL, O_D, TYPE) :
     
     logging.warning("The download process is starting\n")

     if(URL == "" or O_D == "" or TYPE == ""):
          logging.error("The required values were not given 'URL, O_D, TYPE'\n")
          return

     p = Playlist(URL)
     
     try :
          for video in p.videos:
               pass
     except (RuntimeError, TypeError, NameError, KeyError):
          logging.error("URL not recognize - might not be a playlist\n")
          

     for video in p.videos:
          
          title = video.title

          print("")
          print("Title: " + video.title)
          print("Author: " + video.author)
          print(video.thumbnail_url)
          print("")

          logging.warning("Downloading\n")
          video.streams.get_highest_resolution().download()

          if(TYPE != "mp4"):
               logging.warning(video.title + TYPE + " is done\n")
               subprocess.call("ffmpeg -i " + '"' + title_swap(video.title) + ".mp4" + '"' +" -vn out.mp3" + '"', shell=True)
               subprocess.call("del " + '"' + video.title + ".mp4" + '"', shell=True)
               
               subprocess.call("ffmpeg -i out.mp3 -i " + '"' + video.thumbnail_url + '"' + " -c copy -map 0 -map 1 in.mp3" ,shell=True)
               subprocess.call("del out.mp3", shell=True)

               subprocess.call("ffmpeg -i in.mp3 -i " + video.thumbnail_url + " -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="" -metadata:s:v comment="" out.mp3" ,shell=True)
               subprocess.call("del in.mp3", shell=True)

               subprocess.call("ren out.mp3 " + '"' + video.title + ".mp3" + '"' ,shell=True)
               print("move " + '"' + video.title + ".mp3" + '" ' + O_D)
               subprocess.call("move " + '"' + video.title + ".mp3" + '" ' + O_D ,shell=True)

          logging.warning("The process is done\n")

Download_Process(args.URL, args.Output_location, args.Format)
#fin          
