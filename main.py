import cut_video
import yuv_histogram
import resize_video
import stereo_mono
import glob


def menu():  # we print the main menu of the program
    print("WELCOME TO THE MAIN MENU")
    print("IMPORTANT: In order to use the other options, you need to cut the video first!!!")  # all these operations
    print("[1] Cut video")  # are used with the cut video, so before selecting any other option we need to generate
    print("[2] Create a YUV histogram video")  # it first
    print("[3] Resize video")
    print("[4] Convert to mono and back to stereo")
    print("[5] Delete all videos in the BBB folder")
    print("[0] Exit \n")


menu()

option = ""

while option != "0":
    option = input("Option: ")
    if option == "0":
        print("Program finished :)")
        break
    if option == "1":  # cut video
        print("Select the part of the video you want to cut")
        print("Please consider that the longer the cut, the longer the renders are going to be!")
        start_seconds = int(input("Enter the starting value (in seconds): "))  # asks for starting point (s)
        final_seconds = int(input("Enter the ending value (in seconds): "))  # asks for final point (s)
        cut_video.cut_video(start_seconds, final_seconds)  # we cut the video
        print("\n")
        menu()
    if option == "2":  # create yuv histogram video
        video = "BBB/bbb_cut.mp4"
        frames = yuv_histogram.extract_frames(video)
        yuv_histogram.extract_histograms(frames)
        yuv_histogram.create_histogram_video()
        yuv_histogram.create_final_video(video)
        print("\n")
        menu()
    if option == "3":  # resize videos
        video = "BBB/bbb_cut.mp4"
        width, height = resize_video.get_dimensions(video)
        resize_video.options_resize(video, width, height)  # opens the resize menu
        print("\n")
        menu()
    if option == "4":  # stereo2mono & mono2stereo
        video = "BBB/bbb_cut.mp4"
        stereo_mono.stereo2mono(video)
        mono2stereo = input("Want to transform back into stereo audio? [y/n]")  # if the user wants to convert it back,
        stereo_mono.mono_question(mono2stereo, video)  # since the cut original video has already stereo format
        print("\n")
        menu()
    if option == "5":
        BBB_path = glob.glob('BBB/*')
        yuv_histogram.delete_files(BBB_path)  # using the function we used in the yuv_histogram to delete the histogram
        print("Videos deleted :( \n")  # frames, we delete all the files from the BBB folder
        menu()
    else:
        print("Please select a valid option")
