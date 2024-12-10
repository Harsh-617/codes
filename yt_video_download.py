# from pytube import YouTube
# from sys import argv           #sys.argv: This is used to get command-line arguments passed to the script.
#
# # Get the link from the command line arguments
# link = argv[1]
#
# # Create a YouTube object
# YT = YouTube(link)
#
# # Print video details
# print("Title: ", YT.title)
# print("Views: ", YT.views)
#
# # Get the highest resolution stream
# YD = YT.streams.get_highest_resolution()    #<< there are many other options as well
#
# # Download the video to the specified directory
# YD.download('/Users/LENOVO-PC/demo_expm')
#---------------------------------------------------------------------------------
# from pytube import YouTube
# from sys import argv, exit
#
# if len(argv) < 2:
#     print("Error: Please provide a YouTube video link.")
#     exit(1)
#
# link = argv[1]
#
# try:
#     YT = YouTube(link)
#     print("Title: ", YT.title)
#     print("Views: ", YT.views)
#
#     # Get the first stream with progressive download (video + audio)
#     YD = YT.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#
#     if YD:
#         YD.download('/Users/LENOVO-PC/demo_expm')
#         print("Download completed successfully!")
#     else:
#         print("No suitable stream found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
#----------------------------------------------------------------------------------------------------------------------------
import yt_dlp

video_url = input("Enter the link")   #list

#specified options for downloading video
ydl_opts = {                                                      #ydl_opts is a dictionary that specifies options for the download.
    'outtmpl': '/Users/LENOVO-PC/demo_expm/%(title)s.%(ext)s',    #The 'outtmpl' key defines the output template for the downloaded file.
}                                                                 #In this case, the video will be saved in the /Users/LENOVO-PC/demo_expm/ directory with the video’s title as the filename and the appropriate file extension.

with yt_dlp.YoutubeDL(ydl_opts) as ydl:      #YoutubeDL is a class
    ydl.download([video_url])                #This block of code creates an instance(object created from class) of yt_dlp.YoutubeDL with the specified options (ydl_opts).
#----------------------------------------------------------------------------------------------------------------------------------
# import yt_dlp
#
# video_url = input("Enter the link")
#
# # Create an instance of YoutubeDL
# ydl = yt_dlp.YoutubeDL()
#
# # Set options directly
# ydl.params['outtmpl'] = '/Users/LENOVO-PC/demo_expm/%(title)s.%(ext)s'
# ydl.params['format'] = 'best'
#
# # Download the video
# ydl.download([video_url])