# My very own youtube converter based on Python3. Woho!

from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(url=link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

#Getting the highest resolution possible
ys = yt.streams.get_audio_only()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")