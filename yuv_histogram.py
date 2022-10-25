import os
import cv2
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from moviepy.editor import VideoFileClip, clips_array
import glob
import re


def delete_files(folder):  # deletes all files in a folder
    for filename in folder:
        os.remove(filename)


def numerical_sort(value):  # it sorts the files in order (in this case the histograms)
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def yuv_histogram(image, count):  # we generate the 3 YUV plots

    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    y, u, v = cv2.split(yuv_image)

    gs = gridspec.GridSpec(3, 1)

    plt.figure()
    plt.subplot(gs[0, 0])
    plt.hist(y.ravel(), 256, [0, 256])
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gca().axes.yaxis.set_ticklabels([])
    plt.title("Y histogram (Luminance)")  # we generate the Y plot

    plt.subplot(gs[1, 0])
    plt.hist(u.ravel(), 256, [0, 256])
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gca().axes.yaxis.set_ticklabels([])
    plt.title("U histogram (Cb)")  # we generate the U plot

    plt.subplot(gs[2, 0])
    plt.hist(v.ravel(), 256, [0, 256])
    plt.gca().axes.xaxis.set_ticklabels([])
    plt.gca().axes.yaxis.set_ticklabels([])
    plt.title("V histogram (Cr)")  # we generate the V plot

    plt.savefig("histograms/histogram%d.jpg" % count)  # we save all the histograms .jpg in a folder


def extract_frames(video):  # we extract all the frames from the cut video
    vidcap = cv2.VideoCapture(video)
    success, frame = vidcap.read()
    frames = []
    while success:
        success, frame = vidcap.read()
        frames.append(frame)
    return frames


def extract_histograms(frames):  # we create an histogram for every 30 frames because the video has 30 fps
    count = 0                       # so we create an histogram per second
    for i in range(0, len(frames), 30):
        yuv_histogram(frames[i], count)
        count += 1


def create_histogram_video():  # we use all the histogram like frames to create a 1fps histogram video that can
    histograms = []             # match the original video duration
    for filename in sorted(glob.glob("histograms/*.jpg"), key=numerical_sort):
        hist = cv2.imread(filename)
        height, width, layers = hist.shape
        size = (width, height)
        histograms.append(hist)

    out = cv2.VideoWriter('BBB/histograms.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 1, size)

    for i in range(len(histograms)):
        out.write(histograms[i])
    out.release()


def create_final_video(video):  # once we have both videos, we define the same exact duration and we create a new
    og_video = VideoFileClip(video)     # video that shows both of them side to side
    duration = og_video.duration
    final_hist = VideoFileClip("BBB/histograms.mp4").subclip(0, duration)
    og_video = og_video.subclip(0, duration)
    combined = clips_array([[og_video, final_hist]])

    combined.write_videofile("BBB/final_histogram_video.mp4")

    histograms_path = glob.glob('histograms/*')
    delete_files(histograms_path)  # finally, we delete all the histogram video frames
