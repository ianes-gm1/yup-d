
#Yup-d ver. 1.0

from pytube import *
import subprocess
import os

def Download_Process(URL, O_D) :
     
     p = Playlist(URL)
     
     for video in p.videos:
          
          title = video.title

          print("")
          print("Title: " + video.title)
          print("Author: " + video.author)
          print(video.thumbnail_url)

          video.streams.get_highest_resolution().download()


          subprocess.call("ffmpeg -i " + '"' + video.title + ".mp4" + '"' +" -vn out.mp3" + '"', shell=True)
          subprocess.call("del " + '"' + video.title + ".mp4" + '"', shell=True)
          
          subprocess.call("ffmpeg -i out.mp3 -i " + '"' + video.thumbnail_url + '"' + " -c copy -map 0 -map 1 in.mp3" ,shell=True)
          subprocess.call("del out.mp3", shell=True)

          

          subprocess.call("ffmpeg -i in.mp3 -i " + video.thumbnail_url + " -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title="" -metadata:s:v comment="" out.mp3" ,shell=True)
          subprocess.call("del in.mp3", shell=True)

          subprocess.call("ren out.mp3 " + '"' + video.title + ".mp3" + '"' ,shell=True)
          print("move " + '"' + video.title + ".mp3" + '" ' + O_D)
          subprocess.call("move " + '"' + video.title + ".mp3" + '" ' + O_D ,shell=True)


          


if __name__ == "__main__":
     Output_location = input(r"output location : ")
     URL = input(r"URL : ")
     Download_Process(URL, Output_location)
     
