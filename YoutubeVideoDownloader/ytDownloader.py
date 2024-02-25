# Importing the YouTube class from the pytube library and argv from sys module to handle command-line arguments
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/ea02a/Downloads/Youtube Download Links')
