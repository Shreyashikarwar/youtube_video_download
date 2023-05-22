from pytube import YouTube

def yt_download_link(link):
    youtube_1 = YouTube(link)
    print(youtube_1.title)

    # for all the format
    video = youtube_1.streams.all()

    #for audio only
    # video = youtube_1.streams.filter(only_audio=True)

    #for specific type of video
    video = youtube_1.streams.filter(progressive=True, file_extension='mp4')

    vid_list = list(enumerate(video))

    for i in vid_list:
        print(i)

    strm = int(input("enter : "))
    video[strm].download()
    print("successfully")

yt_download_link(link = "https://www.youtube.com/watch?v=XnNzck5-HdQ&list=PLu0W_9lII9ahwLNzab_rVfZ06ZCZYEcNs")