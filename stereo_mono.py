import os


def stereo2mono(input_video):  # conversion stereo 2 mono
    os.system("ffmpeg -i {input_video} -ac 1 BBB/bbb_mono.mp4".format(input_video=input_video))


def mono2stereo(input_video):  # conversion mono 2 stereo
    os.system("ffmpeg -i {input_video} -ac 2 BBB/bbb_stereo.mp4".format(input_video=input_video))


def mono_question(answer, video):  # if the user wants the video back into stereo format
    if answer == "y":
        mono2stereo(video)
    if answer == "n":
        return
    else:
        print("Please, write a valid answer! \n")


