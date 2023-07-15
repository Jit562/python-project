from pytube import YouTube, Playlist

link = "https://www.youtube.com/watch?v=8HF8ONn9S1U"


res = YouTube(link)

# print(res.title)

# print(res.thumbnail_url)


"""
downl = res.streams.all()
downl = res.streams.filter(only_audio=True)
downl = res.streams.filter(only_video=True)

vid = list(enumerate(downl))

for i in vid:
    print(i)

print()

user = int(input("enter: "))

downl[user].download()

print("Successfully")

"""

".................................download playlist video......................................."

py = Playlist("https://www.youtube.com/watch?v=76H-8-mi1Cc&list=PLjVLYmrlmjGdEE2jFpL71LsVH5QjDP5s4")

print(py.title)

for video in py.videos:

    video.streams.first().download()


