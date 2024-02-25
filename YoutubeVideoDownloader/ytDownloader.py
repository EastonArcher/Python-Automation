# Importing the YouTube class from the pytube library and argv from sys module to handle command-line arguments
from pytube import YouTube
from sys import argv

# Fetching the video link from the command-line arguments
link = argv[1]
# Creating an object instance with the provided link
yt = YouTube(link)

# Print the title and views of the video
print("Title:", yt.title)
print("Views:", yt.views)

# Getting the highest resolution stream available for the video
yd = yt.streams.get_highest_resolution()

yd.download('/Users/ea02a/Downloads/Youtube Download Links')
