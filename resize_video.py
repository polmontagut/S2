import os
import cv2


def menu_resize():  # shows the resize options
    print("To what resolution you want the video to be resize?")
    print("[1] 720p")
    print("[2] 480p")
    print("[3] 360x240p")
    print("[4] 160x120p")
    print("[0] Exit \n")


def get_width(width, height, new_height):  # if our resulting width results to be odd, can causes problems with the
                                            # resize operation
    new_width = int(width * new_height / height)
    if new_width % 2 == 0:
        return new_width
    else:
        new_width = int(width * 480 / height) + 1
        return new_width


def resize_video(input_video, height, width):  # resize the video and creates an mp4 in the BBB folder
    os.system("ffmpeg -i {input_video} -vf scale={width}:{height} BBB/bbb_resize_{height}.mp4".format(
        input_video=input_video,
        height=height,
        width=width))


def options_resize(video, width, height):
    option = ""
    menu_resize()
    while option != "0":
        option = input("Enter your option: ")
        if option == "0":
            print("Thanks for using this resizing program! :) \n")
            break
        if option == "1":  # creates a 720p video
            new_height = 720
            new_width = get_width(width, height, new_height)
            resize_video(video, new_height, new_width)
            print("Video created in the BBB folder")
            menu_resize()
        if option == "2":  # creates a 480p video
            new_height = 480
            new_width = get_width(width, height, new_height)
            resize_video(video, new_height, new_width)
            print("Video created in the BBB folder")
            menu_resize()
        if option == "3":  # creates a 360x240p video
            new_height = 240
            new_width = 360
            resize_video(video, new_height, new_width)
            print("Video created in the BBB folder")
            menu_resize()
        if option == "4":  # creates a 160x120p video
            new_height = 120
            new_width = 160
            resize_video(video, new_height, new_width)
            print("Video created in the BBB folder")
            menu_resize()
        else:  # wrong selection
            print("Please, select a valid option")


def get_dimensions(video):
    vid = cv2.VideoCapture(video)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)  # gets the video width
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  # gets the video height
    return width, height



