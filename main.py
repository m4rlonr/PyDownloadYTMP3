# Import from libraries
from pytube import YouTube, Playlist
import os
import subprocess


# Get link
link = input("Cole aqui o link da PlayList: ")

# p = Playlist
p = Playlist(link)
print('Na PlayList tem {0} videos.'.format(len(p.video_urls)))
print(f'Downloading: {p.title}')
for video in p.videos:
    print(f'Downloading: {video.title}')
    video.streams.first().download(output_path=p.title)

# begin download
# for i in range(len(p.video_urls)):
#     yt = YouTube(p.video_urls[i])
#     video.streams.first().download()
#     video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path='%HOMEPATH%\Downloads', filename=yt.title)
#     video.download()


# vids= yt.streams.all()
# for i in range(len(vids)):
#     print(i,'. ',vids[i])

# vnum = int(input("Enter vid num: "))


# vids[vnum].download(parent_dir)

# new_filename = input("Enter filename (including extension): "))  # e.g. new_filename.mp3

# default_filename = vids[vnum].default_filename  # get default name using pytube API
# subprocess.run([
#     'ffmpeg',
#     '-i', os.path.join(parent_dir, default_filename),
#     os.path.join(parent_dir, new_filename)
# ])https://youtube.com/playlist?list=PLO0UWxRwURap95yHs4K1y-fmMbJnJA9QZ&si=fwcu9X52JzOR77Wx

print('done')
