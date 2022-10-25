from moviepy.editor import *


def cut_video(start_seconds, final_seconds):  # using moviepy, we cut the video
    clip = VideoFileClip("bbb.mp4")
    clip = clip.subclip(start_seconds, final_seconds)
    clip.write_videofile("BBB/bbb_cut.mp4")

