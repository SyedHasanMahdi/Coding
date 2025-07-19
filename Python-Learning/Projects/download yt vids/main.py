# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:\Coding\Python-Learning\Projects\download yt vids\ " #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension


#to set the name of the file


# get the video with the extension and
# resolution passed in the get() function
d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
